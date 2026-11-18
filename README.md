<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:4A0D2E,50:C2185B,100:FF8FC7&height=190&section=header&text=Voice%20Module&fontSize=50&fontColor=FFFFFF&fontAlignY=36&desc=First%20prototype%20of%20a%20plug-in%20voice%20layer%20for%20chatbots&descSize=16&descAlignY=58" width="100%" alt="Voice Module"/>

<p>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/OpenAI%20TTS-412991?style=for-the-badge&logo=openai&logoColor=white" alt="OpenAI TTS"/>
  <img src="https://img.shields.io/badge/Status-Prototype-FF4FA3?style=for-the-badge" alt="Prototype"/>
</p>

</div>

---

## About

This repo is the **first sketch** of a voice layer that any text chatbot could plug into: send text to an API, get speech back. It was the starting point for three cleaner, separate modules that replaced it:

| Module | What it does |
|---|---|
| [STT_module](https://github.com/21Afnan/STT_module) | Speech to text |
| [TTS_module](https://github.com/21Afnan/TTS_module) | Text to speech |
| [STS_module](https://github.com/21Afnan/STS_module) | Speech to speech, a full voice conversation |

If you want working code, use those. This one is kept to show where the design began.

## What is here

- `app/main.py`: a FastAPI app with one endpoint, `POST /tts/`, that takes `{"text": "..."}` and returns the generated audio as a base64 string inside JSON, so a web frontend can play it straight away.
- `app/tts_module.py`: an async wrapper around OpenAI's `gpt-4o-mini-tts` speech model.
- `requirements.txt`: FastAPI, Uvicorn, Pydantic, the OpenAI client and audio helpers (NumPy, soundfile).

The code is heavily commented, because it was written while learning how async API calls, CORS and base64 audio transfer fit together.

## Design ideas carried forward

- **Plug-and-play:** the voice layer is its own service, so the chatbot behind it can change without touching audio code.
- **Browser friendly:** audio travels as base64 in JSON, which any frontend can decode and play.
- **Async calls:** the server keeps accepting requests while it waits for the speech API.

---

<div align="center">

**Afnan Shoukat**

<a href="mailto:afnanshoukat35@gmail.com"><img src="https://img.shields.io/badge/Email-afnanshoukat35%40gmail.com-FF4FA3?style=for-the-badge&logo=gmail&logoColor=white&labelColor=4A0D2E" alt="Email"/></a>
<a href="https://www.linkedin.com/in/afnanshoukat"><img src="https://img.shields.io/badge/LinkedIn-Afnan%20Shoukat-FF4FA3?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=4A0D2E" alt="LinkedIn"/></a>
<a href="https://github.com/21Afnan"><img src="https://img.shields.io/badge/GitHub-21Afnan-FF4FA3?style=for-the-badge&logo=github&logoColor=white&labelColor=4A0D2E" alt="GitHub"/></a>

</div>

