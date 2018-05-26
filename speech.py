import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone()

print(sr.Microphone.list_microphone_names())
'''
harvard = sr.AudioFile('amy.wav')
with harvard as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)

print(r.recognize_google(audio,show_all=True))
'''