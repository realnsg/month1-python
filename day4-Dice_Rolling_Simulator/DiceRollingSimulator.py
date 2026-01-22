import random
from pynput import keyboard

print("Welcome to the dice rolling simulator. Press 'enter' to roll or 'esc' to exit.")

def roll():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print(f"You rolled {die1} and {die2} for a total of {die1 + die2}")

def onPress(key):
    try:
        if key == keyboard.Key.enter:
            roll()
        elif key == keyboard.Key.esc:
            print("Exiting...")
            return False
    except AttributeError:
        pass

with keyboard.Listener(on_press=onPress) as listener:
    listener.join()