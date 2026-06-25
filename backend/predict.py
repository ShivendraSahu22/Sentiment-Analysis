import pickle
from rnn_model import RNN

with open('model/model1.pkl', 'rb') as f:
    model = pickle.load(f)

with open('model/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# MLFlow
MODEL_VERSION = '1.0.0'
def predict_sentiment(user_input):

    text = user_input.text

    # Convert text to TF-IDF features
    transformed_text = vectorizer.transform([text])

    # Predict class
    prediction = model.predict(transformed_text)[0]

    # Predict probability
    confidence = model.predict_proba(transformed_text).max()

    sentiment_map = {
        0: "Negative",
        1: "Positive"
    }

    return {
        "sentiment": sentiment_map[prediction],
        "sentiment_score": float(confidence)
    }