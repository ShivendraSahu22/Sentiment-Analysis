import pickle
import torch
import torch.nn.functional as F

from models.rnn import RNN


# ==================================
# Configuration
# ==================================

INPUT_SIZE = 5000      # training ke time jo use kiya tha
HIDDEN_SIZE = 128
OUTPUT_SIZE = 2

MODEL_VERSION = "1.0"


# ==================================
# Load Vectorizer
# ==================================

with open("model/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)


# ==================================
# Load Model
# ==================================

model = RNN(
    input_size=INPUT_SIZE,
    hidden_size=HIDDEN_SIZE,
    output_size=OUTPUT_SIZE
)

model.load_state_dict(
    torch.load(
        "model/rnn_model.pth",
        map_location=torch.device("cpu")
    )
)

model.eval()


# ==================================
# Prediction Function
# ==================================

def predict_sentiment(user_input):

    text = user_input.text

    # TF-IDF transform
    features = vectorizer.transform([text])

    # Sparse -> Dense
    features = features.toarray()

    # Convert to Tensor
    tensor_input = torch.tensor(
        features,
        dtype=torch.float32
    )

    # RNN expects 3D tensor
    tensor_input = tensor_input.unsqueeze(1)

    with torch.no_grad():

        output = model(tensor_input)

        probabilities = F.softmax(
            output,
            dim=1
        )

        confidence = torch.max(
            probabilities
        ).item()

        prediction = torch.argmax(
            probabilities,
            dim=1
        ).item()

    sentiment_map = {
        0: "Negative 😔",
        1: "Positive 😊"
    }

    return {
        "sentiment":
            sentiment_map[prediction],

        "sentiment_score":
            round(confidence, 4)
    }