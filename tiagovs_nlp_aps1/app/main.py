from fastapi import FastAPI, Query
import os
import uvicorn
import scripts

import scripts.get_data

class DummyModel:
    def predict(self, X):
        return "dummy prediction"

def load_model():
    predictor = DummyModel()
    return predictor

app = FastAPI()
app.predictor = load_model()

@app.get("/hello")
def read_hello():
    return {"message": "hello life"}

@app.get("/predict")
def predict(X: str = Query(..., description="Input text for prediction")):
    result = app.predictor.predict(X)
    return {"input_value": X, "predicted_value": result, "message": "prediction successful"}

@app.get("/query")
def query_route(query: str = Query(..., description="Search query")):
    # TODO: write your code here, keeping the return format
    return scripts.get_data.get_name(query)

def run():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    run()