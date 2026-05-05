import speech_recognition as sr

recognizer = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("Ouvindo...")
        audio = recognizer.listen(source)

    try:
        texto = recognizer.recognize_google(audio, language="pt-BR")
        print("Você disse:", texto)

        # lógica com if/else
        if "abrir youtube" in texto.lower():
            print("Abrindo YouTube...")
        
        elif "parar" in texto.lower():
            print("Encerrando...")
            break
        
        else:
            print("Comando não reconhecido")

    except sr.UnknownValueError:
        print("Não entendi o que você disse")
    
    except sr.RequestError:
        print("Erro na API de reconhecimento")
