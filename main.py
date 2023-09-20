from fastapi import FastAPI
from pydantic import BaseModel
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import pygame
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
import time
from fastapi.responses import JSONResponse
import pyttsx3


class TextRequest(BaseModel):
    text: str
    lang: Optional[str] = "en"

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)


@app.get("/speak")
async def speak():
    response = JSONResponse(content={"message": "Hello from /speak GET endpoint at " + str(time.time())})
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

@app.get("/")
async def welcome():
    return "Welcome to the Translator API"

recognizer = sr.Recognizer()


def translate_text(text, lang):
        translator = Translator()
        translated_text = translator.translate(text, dest="hi")
        return translated_text.text

def say(text,lang):
    print(f"Before Translation: {text}")
    text = translate_text(text,lang)
    print(f"After Translation: {text}")
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 160)
    engine.say(text)
    engine.runAndWait()

@app.post("/speak")
def speak_text(text_request: TextRequest):
    say(text_request.text, lang=text_request.lang)
    return {"message": "Text has been spoken"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)