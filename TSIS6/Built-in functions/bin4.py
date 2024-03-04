import math
import time

def calc(number, milliseconds):
    time.sleep(milliseconds / 1000)
    return math.sqrt(number)


number = int(input())
milliseconds = int(input())

result = calc(number, milliseconds)
print(f"Square root of {number} after {milliseconds} milliseconds is {result}")