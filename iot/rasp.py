from machine import Pin, ADC
import utime

# sensor interno do RP2040
sensor_temperatura = ADC(ADC.CORE_TEMP)

conversor = 3.3 / 65535

# LED compatível com Pico / Pico W
try:
    led = Pin("LED", Pin.OUT)
except:
    led = Pin(25, Pin.OUT)


def media_adc(n=32, us=50):
    s = 0
    for _ in range(n):
        s += sensor_temperatura.read_u16()
        utime.sleep_us(us)
    return s // n


while True:
    raw = media_adc()
    v = raw * conversor
    temperatura = 27 - (v - 0.706) / 0.001721
    fahrenheit = temperatura * 9 / 5 + 32
    led.toggle()
    print(f"{temperatura:.2f}ºC | {fahrenheit:.2f}ºF  (raw={raw}, V={v:.3f} V)")
    utime.sleep(2)
