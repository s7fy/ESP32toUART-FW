from machine import UART
from machine import Pin
import sys
import select

# make instans with UART1
# Tx: GPIO17
# Rx: GPIO16

tx = 17
rx = 16
baundrate = 115200
uart_router = UART(1, 115200)

# communication UART0 to PC (default is serial monitor to UART0)
while True:
    # data sends to PC from router
    if uart_router.any(): # if exists data in buffer
        data = uart_router.read()
        if data:
            sys.stdout.write(data.decode('utf-8', errors='ignore')) # data output to PC
      
    # data sends to router from PC
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        data = sys.stdin.read(1) # read 1 byte
        if data:
            uart_router.write(data)
