from fastapi import FastAPI 
#This is the core FastAPI class to create your API application.
from fastapi.middleware.cors import CORSMiddleware
#Without this, your frontend won’t be able to talk to your FastAPI backend during development.
from fastapi.responses import JSONResponse
"""To send a response with JSON data back to the client (frontend).
I want to send the audio base64 string wrapped in JSON."""
from app.tts_module import tts_module
import base64
"""To encode the audio bytes back into base64
   string before sending to frontend,so it can be easily
   transferred over HTTP (which is text-based)."""
from pydantic import BaseModel
# defines shape of model which type of requests it will recieve validate and parse data easily

import asyncio
#TTS function is asynchronous (async), so asyncio helps manage async calls smoothly.
app=FastAPI()
app.add.middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for production
    allow_methods=["*"],
    allow_headers=["*"],
)
tts = tts_module()


class  TextRequest(BaseModel):
    text:str
    #Call its method in your API endpoint:
    @app.post("/tts/")
    async def tts_api(request: TextRequest):
        audio_bytes = await tts.text_to_speech(request.text)
        audio_b64 = base64.b64encode(audio_bytes).decode("utf-8")
        return JSONResponse(content={"audio": audio_b64})

