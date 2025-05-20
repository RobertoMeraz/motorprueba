import RPi.GPIO as GPIO
import time

# Configura los pines
DIR = 27    # Dirección (GPIO27, pin 13)
STEP = 17   # Paso (GPIO17, pin 11)

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)

# Establece la dirección
GPIO.output(DIR, GPIO.HIGH)

# Gira el motor
try:
    for i in range(200):  # 200 pasos = 1 vuelta (si es de 1.8°/paso)
        GPIO.output(STEP, GPIO.HIGH)
        time.sleep(0.001)  # Velocidad (más bajo = más rápido)
        GPIO.output(STEP, GPIO.LOW)
        time.sleep(0.001)

finally:
    GPIO.cleanup()
