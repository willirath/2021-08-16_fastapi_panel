from fastapi import FastAPI

import pandas as pd

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "This is the compute part."}


@app.get("/pi")
async def calc_pi(length: int = 100):
    x = pd.read_json(f"http://data/rs/?length={length}", typ="series")
    y = pd.read_json(f"http://data/rs/?length={length}", typ="series")
    r2 = x ** 2 + y ** 2
    pi = 4 * (r2 < 1).mean()
    return {"pi": pi}
