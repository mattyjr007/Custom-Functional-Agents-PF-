import time
import gunicorn
from fastapi import FastAPI
from typing import Any
from pydantic import BaseModel
import uvicorn
import os
from model import Model

app = FastAPI()

model = Model()


# home page
@app.get("/")
def root():
    return {"message": "Hello World, please head over to /docs"}



# Langchain chat Model
@app.post("/api/")
async def langModel(user_input:str) -> dict:

    # pass message to model
    
    response_msg = model.chatBot(msg=user_input)
    # store response in dictionary
    reponse_out = {"response":response_msg}

    return reponse_out




    # pass message to model
    
    try:
        response_msg = model.chatLlama2(message=user_input)
    except Exception as e:
        print("Exception caught: ", e)
        response_msg = "Heyy!, there seems to be an issue please try again in a few secs!"

    # store response in dictionary
    reponse_out = {"AI_out":response_msg}

    return reponse_out