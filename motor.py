import RPi.GPIO as GPIO
import time

# Pines definidos en la tabla
DIR = 20     # Dirección del giro
STEP = 21    # Pulso de paso
MS1 = 14     # Resolución del microstepping
MS2 = 15
MS3 = 18

# Configuración de GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(MS1, GPIO.OUT)
GPIO.setup(MS2, GPIO.OUT)
GPIO.setup(MS3, GPIO.OUT)

# Configurar microstepping a full-step (MS1=0, MS2=0, MS3=0)
GPIO.output(MS1, GPIO.LOW)
GPIO.output(MS2, GPIO.LOW)
GPIO.output(MS3, GPIO.LOW)

# Dirección del motor (1 = una dirección, 0 = la opuesta)
GPIO.output(DIR, GPIO.HIGH)

# Número de pasos a realizar
steps = 200  # 200 pasos para una vuelta completa en full-step

try:
    for _ in range(steps):
        GPIO.output(STEP, GPIO.HIGH)
        time.sleep(0.002)  # 2 ms = 500 pasos por segundo
        GPIO.output(STEP, GPIO.LOW)
        time.sleep(0.002)
    print("Movimiento completado.")

except KeyboardInterrupt:
    print("Interrumpido por el usuario.")

finally:
    GPIO.cleanup()
