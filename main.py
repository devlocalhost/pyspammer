import time
import os
from pynput.keyboard import Key, Controller

keyboard = Controller()

tx = input("  Enter the text that you want to spam: ")

nm = input('  Enter the amount of times that you want to spam "{}": '.format(tx))

print('   Now focus on a apps textbox and hold your pointer there\n   5')
time.sleep(1)
os.system('clear')
time.sleep(1)
print("  4")
time.sleep(1)
os.system('clear')
print("  3")
time.sleep(1)
os.system('clear')
print("  2")
time.sleep(1)
os.system('clear')
print("  1")
time.sleep(1)
os.system('clear')
print('  Spamming "{}" {} times...'.format(tx, nm))
time.sleep(1)

for num in range(int(nm)):
    for letter in tx:
        keyboard.press(letter)
        keyboard.release(letter)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.3) # you can modify the time and make even slower
    
print("  Done")
