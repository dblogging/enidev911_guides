import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
for voice in voices:
    print("Voice: %s" % voice.name)
    print(" - ID: %s" % voice.id)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
    print("\n")



engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)
engine.setProperty('voice', 'spanish')
engine.setProperty('volume', 1)

engine.say('Hola me llamo marco')
engine.save_to_file('How do you do?', 'output.mp3')

engine.runAndWait()