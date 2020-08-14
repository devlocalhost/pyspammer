import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

print("  Welcome to the python spammer!!")
print("  Make sure you open a app quickly\n  and focus your mouse on the text box,\n  therwise bad things could happen!!!")

tx = input("  Enter the text that you want to spam: ")

nm = input('  Enter the amount of times that you want to spam "{}": '.format(tx))

print("  Starting....")
time.sleep(1)
print("  PLEASE FOCUS ON A APPS\n  TEXTBOX!!! YOU HAVE 5 SECONDS!!")

time.sleep(1)
print("  4")
time.sleep(1)
print("  3")
time.sleep(1)
print("  2")
time.sleep(1)
print("  1")
time.sleep(1)
print('  Spamming "{}" {} times...'.format(tx, nm))
time.sleep(1)

for num in range(int(nm)):
    for letter in tx:
        keyboard.press(letter)
        keyboard.release(letter)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.000000000000000000000000000000000000000000000000001) # you can modify the time and make it slower
    
print("  Done")
