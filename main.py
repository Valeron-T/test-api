import asyncio
from fastapi import FastAPI
from pydantic import BaseModel
import requests


class CardInfo(BaseModel):
    name: str
    number: int
    cvv: int
    exp: str


app = FastAPI()


@app.get("/")
async def root():
    # await asyncio.sleep(2)
    return {"message": "API is running"}


@app.post("/checkout")
async def checkout(card: CardInfo):
    # Some processing logic - Check inventory, Validate address etc.
    # Assume everything is valid and pass info to payment gateway
    furl = f"https://mockservicecustomapi340180.mock.blazemeter.com/api/validate?name={card.name}&cvv={card.cvv}&exp={card.exp}&cardnumber={card.number}"
    response = requests.get(furl)
    return {"status": response.json()}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
