from fastapi import FastAPI
from pydantic import BaseModel
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import pygame
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],  # You can specify specific HTTP methods if needed
    allow_headers=["*"],  # You can specify specific headers if needed
)


@app.get("/speak")
async def speak():
    # Your code to handle the GET request for /speak goes here
    return {"message": "Hello from /speak GET endpoint"}

recognizer = sr.Recognizer()

class TextRequest(BaseModel):
    text: str
    lang: Optional[str] = "en"

def translate_text(text, lang):
        translator = Translator()
        translated_text = translator.translate(text, dest="hi")
        return translated_text.text

def say(text, lang="en"):
    translated_text = translate_text(text, lang)
    tts = gTTS(text=translated_text, lang="hi", slow=False)
    filename = "voice.mp3"
    tts.save(filename)
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.quit()

@app.post("/speak")
def speak_text(text_request: TextRequest):
    say(text_request.text, lang=text_request.lang)
    return {"message": "Text has been spoken"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)