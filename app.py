from gtts import gTTS
text = "how are you today?"
tts = gTTS(text=text, lang="en")
tts.save("mp3")