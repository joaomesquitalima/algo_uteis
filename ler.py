import easyocr
import pyautogui
import cv2
import numpy as np
import time

# cria leitor
reader = easyocr.Reader(['en'])

while True:

    
    screenshot = pyautogui.screenshot(region=(400, 250, 600, 300))

    # converte pra OpenCV
    img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # OCR
    resultados = reader.readtext(img)

    texto_total = ""

    for resultado in resultados:
        texto = resultado[1]
        texto_total += texto.upper() + " "

    print(texto_total)

    if "DOWN" in texto_total:
        print("CAIU!")

    if "UP" in texto_total:
        print("VOLTOU!")

    time.sleep(1)
