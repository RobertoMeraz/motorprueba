import RPi.GPIO as GPIO
import time

# Configuración de pines (según tu tabla)
STEP_PIN = 21    # GPIO 21 (Pin 40) conectado a STP del A4988
DIR_PIN = 20     # GPIO 20 (Pin 38) conectado a DIR del A4988
ENABLE_PIN = None  # Si no usas ENABLE, déjalo como None (o conéctalo a GND en el A4988)

# Inicialización
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)  # Evita advertencias si los pines ya están en uso

GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(DIR_PIN, GPIO.OUT)

if ENABLE_PIN is not None:
    GPIO.setup(ENABLE_PIN, GPIO.OUT)
    GPIO.output(ENABLE_PIN, GPIO.LOW)  # Habilita el motor (LOW = activo)

try:
    print("Girando en sentido horario (1 vuelta)...")
    GPIO.output(DIR_PIN, GPIO.HIGH)  # Sentido horario
    for _ in range(200):  # 200 pasos = 1 vuelta en motor NEMA17 (200 pasos/rev)
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(0.001)  # Ajusta este valor para cambiar la velocidad
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(0.001)

    print("Girando en sentido antihorario (1 vuelta)...")
    GPIO.output(DIR_PIN, GPIO.LOW)  # Sentido antihorario
    for _ in range(200):
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(0.001)

finally:
    GPIO.cleanup()  # Limpia los pines al terminar
    print("Prueba finalizada. Pines GPIO liberados.")