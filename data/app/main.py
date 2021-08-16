from fastapi import FastAPI

import pandas as pd
import numpy as np

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "This is the data part."}


@app.get("/rs")
async def random_series(length: int = 100):
    return pd.Series(
        np.random.uniform(0, 1, size=(length,)),
        index=np.arange(length),
    )