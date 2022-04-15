import random
import string
import time, sys

chars = list(string.digits + string.ascii_uppercase)

def gen1():
    random.shuffle(chars)
    serial1 = []
    for i in range(4):
        serial1.append(random.choice(chars))
    random.shuffle(serial1)
    serial2 = []
    for i in range(4):
        serial2.append(random.choice(chars))
    random.shuffle(serial2)
    serial3 = []
    for i in range(4):
        serial3.append(random.choice(chars))
    random.shuffle(serial3)
    serial4 = []
    for i in range(4):
        serial4.append(random.choice(chars))
    random.shuffle(serial4)
    print("".join(serial1) + "-" + "".join(serial2) + "-" + "".join(serial3) + "-" + "".join(serial4))

generating = 'Generating serial keys...\n'
for char in generating:
    sys.stdout.write(char)
    time.sleep(0.1)
    sys.stdout.flush()
serial_count = int(input('How many serial keys? '))


for i in range(serial_count):
    gen1()
