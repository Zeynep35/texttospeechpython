from gtts import gTTS

def yaziyi_sese_donustur(text):
    tts = gTTS(text=text, lang="en")
    tts.save("mp3")