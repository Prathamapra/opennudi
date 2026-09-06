import keyboard as key
import speech_recognition as sr
class funcs:
    def keywrite(words):
        key.write(words)
        return 0
    def listenhere():
        rec=sr.Recognizer()
        with sr.Microphone() as source:
            rec.adjust_for_ambient_noise(source, duration=1)
            aud=rec.listen(source)
        try:
            words=rec.recognize_google(aud,language="kn-IN")
            funcs.keywrite(words)
        except sr.UnknownValueError:
            return "E"
    

        
    
