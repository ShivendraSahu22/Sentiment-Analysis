from fastapi import FastAPI, HTTPException
from schema.user_input import UserInput
from schema.prediction_response import PredictionResponse
from predict import predict_sentiment
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# human readable       
@app.get('/')
def home():
    return {'message':'Sentiment Analysis API'}

@app.get('/health')
def health_check():
    return {
        'status': 'OK',
        'version': MODEL_VERSION,
        'model_loaded': model is not None
    }


@app.post('/predict', response_model=PredictionResponse)
def predict(data: UserInput):

    try:

        prediction = predict_sentiment(data)

        return {'predicted_sentiment': prediction}
    
    except Exception as e:

        raise HTTPException(status_code=500, detail=str(e)) from e