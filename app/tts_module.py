import openai
import base64
# teh api key to link the 
openai.api_key=""
# async as the ftc calls api it might take time 
# instead of waiting it gies no accepting other requests 
# -> as return type hint that this ftn will return the binary data
class tts_module:
   async def text_to_speech(self,text:str)->bytes:
      response=await openai.audio.speech.create(
        model="gpt-4o-mini-tts",# 3 models are there but we are using latest one speed mdeium but accuracy higher
        input=text,
        voice="Coral" #multiple types of voice can be integrated
    )
      audio_base64 = response["audio"]
      audio_bytes = base64.b64decode(audio_base64)
      return audio_bytes
   
tts=tts_module()
tts.text_to_speech("HI i am testing the tts module")
