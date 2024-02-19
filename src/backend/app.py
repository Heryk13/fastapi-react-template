from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
import sys


if getattr(sys, "frozen", False):
    ROOT = sys._MEIPASS # type: ignore
else:
    ROOT = os.path.dirname(__file__)

app = FastAPI()

app.mount("/", StaticFiles(directory=os.path.join(ROOT, "backend", "static"),html = True), name="static")

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
