import serial
import time

device = '/dev/ttyAMA0'
baudrate = 115200
ser = serial.Serial(device, baudrate, timeout=1)
f = None
ticks = time.time()

try:
    while True:
        linestr = ser.readlins()
        total = ticks, linestr
        print (total)

        if linestr:
            f = open('home/pi/Desk/the_com1.txt','wt')
            f.write(str(total))
            break

except keyboardInterrupt:
    print ('keyboardInterrupt:')

finally:
    if ser is not None:
        ser.close()
    if f is not None:
        f.close()
