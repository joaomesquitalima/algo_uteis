import easyocr
import pyautogui
import cv2
import numpy as np
import time
import serial

# COM3 é exemplo
arduino = serial.Serial('COM3', 9600)

reader = easyocr.Reader(['en'])

estado_anterior = ""

while True:

    screenshot = pyautogui.screenshot(region=(400, 250, 600, 300))

    img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    resultados = reader.readtext(img)

    textos = [r[1].upper() for r in resultados]

    # print(textos)

    # detecta DOWN
    if "DOWN" in textos and estado_anterior != "DOWN":
        print("CAIU!")

        arduino.write(b'1')
        print("caiuuu")

        estado_anterior = "DOWN"

    # detecta UP
    elif "UP" in textos and estado_anterior != "UP":
        print("VOLTOU!")

        arduino.write(b'0')

        estado_anterior = "UP"

    time.sleep(1)
