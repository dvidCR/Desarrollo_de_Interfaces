import speech_recognition as sp
import os
import sys

def recognitionCommand(text):
    text = text.lower()
    fraseListada = text.split(" ")
    
    for comando in fraseListada:
        if comando == "abrir" or comando == "abreme":
            for ejecutar in fraseListada:
                if ejecutar == "notas":
                    os.startfile("notepad.exe")
                elif ejecutar == "chrome":
                    os.startfile("chrome.exe")
                elif ejecutar == "calculadora":
                    os.startfile("calc.exe")
        elif comando == "salir":
            sys.exit()
                
def quitarTildes(text):
    text = text.replace("á", "a"),
    text = text.replace("é", "e"),
    text = text.replace("í", "i"),
    text = text.replace("ó", "o"),
    text = text.replace("ú", "u"),

r = sp.Recognizer()
while True:
    with sp.Microphone() as source:
        print("Hola, soy tu asistente de voz: ")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language = 'es-ES')
            quitarTildes(text)
            print("Has dicho: {}".format(text))
        except:
            print("No te ha entendido")
            
        recognitionCommand(text)