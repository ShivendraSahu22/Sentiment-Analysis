import pickle

with open('model/model1.pkl', 'rb') as f:
    model = pickle.load(f)

# MLFlow
MODEL_VERSION = '1.0.0'

def predict_marks(user_input):
    # Convert user input to a format suitable for prediction
    input_data = [[user_input.sentiment]]
    
    # Make prediction using the loaded model
    predicted_marks = model.predict(input_data)
    
    return float(predicted_sentiment[0])