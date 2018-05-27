import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

try:
    print(r.recognize_google(audio,show_all=True))
except:
    print('error happend :(')
    