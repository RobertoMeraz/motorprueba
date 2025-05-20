import RPi.GPIO as GPIO
import time

STEP_PIN = 17
DIR_PIN = 27
ENABLE_PIN = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(ENABLE_PIN, GPIO.OUT)
GPIO.output(ENABLE_PIN, GPIO.LOW)  # Habilita el motor

# Gira en un sentido
GPIO.output(DIR_PIN, GPIO.HIGH)
for _ in range(200):  # 200 pasos = 1 vuelta en un motor de 200 pasos/rev
    GPIO.output(STEP_PIN, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(STEP_PIN, GPIO.LOW)
    time.sleep(0.001)

# Gira en el sentido contrario
GPIO.output(DIR_PIN, GPIO.LOW)
for _ in range(200):
    GPIO.output(STEP_PIN, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(STEP_PIN, GPIO.LOW)
    time.sleep(0.001)

GPIO.cleanup()