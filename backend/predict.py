import pickle
import torch
import torch.nn as nn


# ==========================
# RNN Model
# ==========================

class RNN(nn.Module):

    def __init__(self, input_size, hidden_size=128, num_layers=1):

        super().__init__()

        self.hidden_size = hidden_size
        self.num_layers = num_layers

        self.rnn = nn.RNN(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True
        )

        self.fc = nn.Linear(hidden_size, 1)

    def forward(self, x):

        h0 = torch.zeros(
            self.num_layers,
            x.size(0),
            self.hidden_size,
            device=x.device
        )

        out, _ = self.rnn(x, h0)

        out = self.fc(out[:, -1, :])

        return out


# ==========================
# Load Vectorizer
# ==========================

with open("model/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)


# ==========================
# Config
# ==========================

INPUT_SIZE = 5000
HIDDEN_SIZE = 128

MODEL_VERSION = "1.0"


# ==========================
# Load Model
# ==========================

model = RNN(
    input_size=INPUT_SIZE,
    hidden_size=HIDDEN_SIZE
)

checkpoint = torch.load(
    "model/modelRNN.pth",
    map_location="cpu"
)

model.load_state_dict(checkpoint)

model.eval()


# ==========================
# Prediction
# ==========================

def predict_sentiment(user_input):

    text = user_input.text

    features = vectorizer.transform([text])

    features = features.toarray()

    tensor_input = torch.tensor(
        features,
        dtype=torch.float32
    )

    tensor_input = tensor_input.unsqueeze(1)

    with torch.no_grad():

        output = model(tensor_input)

        probability = torch.sigmoid(output)

        confidence = float(probability.item())

        prediction = 1 if confidence >= 0.5 else 0

    sentiment_map = {
        0: "Negative 😔",
        1: "Positive 😊"
    }

    return {
        "predicted_sentiment": sentiment_map[prediction],
        "predicted_sentiment_score": round(confidence, 4)
    }