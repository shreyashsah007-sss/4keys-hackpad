This project runs on **CircuitPython** using the **KMK Library**.

```python
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# Initialize Keyboard
keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)

# Pin Definitions (Seeed XIAO RP2040)
# Wired to D0, D1, D2, D3
PINS = [board.D0, board.D1, board.D2, board.D3]

# Matrix Setup
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Key Mapping
# Button 1: Copy  (Ctrl + C)
# Button 2: Paste (Ctrl + V)
# Button 3: Undo  (Ctrl + Z)
# Button 4: Enter
keyboard.keymap = [
    [
        KC.MACRO(Press(KC.LCTRL), Tap(KC.C), Release(KC.LCTRL)),
        KC.MACRO(Press(KC.LCTRL), Tap(KC.V), Release(KC.LCTRL)),
        KC.MACRO(Press(KC.LCTRL), Tap(KC.Z), Release(KC.LCTRL)),
        KC.ENTER,
    ]
]

if __name__ == '__main__':
    keyboard.go()
