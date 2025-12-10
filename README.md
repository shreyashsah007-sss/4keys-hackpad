# 4-Key Hackpad Project

## 1. Overall Hackpad
Here is the finished design of my custom macro pad.
<img width="1920" height="724" alt="overall png" src="https://github.com/user-attachments/assets/13647515-e96b-4c6e-8f02-507445ffb2f3" />


## 2. Bill of Materials (BOM)
| Part | Qty | Description |
| :--- | :--- | :--- |
| **Hackpad Kit** | 1 | Standard kit provided for the project |
| ↳ *Microcontroller* | 1 | Seeed XIAO RP2040 (Included in kit) |
| ↳ *Switches* | 4 | Mechanical Switches (Included in kit) |
| ↳ *Keycaps* | 4 | 1u Keycaps (Included in kit) |
| **Case** | 1 | Custom 3D Printed PLA Case |
| **Wiring** | - | Stranded Hookup Wire |

## 3. CAD Assembly (How it fits)
The case consists of a top and bottom shell, snap-fitted (or screwed) together.
<img width="409" height="520" alt="assembly png" src="https://github.com/user-attachments/assets/b473a8a0-5e4b-4136-8112-bd853d0897fa" />



## 4. Electronics
### Schematic
The wiring logic for the switches and microcontroller.
<img width="666" height="495" alt="schematic png" src="https://github.com/user-attachments/assets/cdcca0a7-02e6-49cd-86b0-123c34dc5659" />

### PCB Design
The physical board layout designed in KiCad.
<img width="1700" height="907" alt="pcb png" src="https://github.com/user-attachments/assets/866b22a5-6a4b-4578-8ca0-e60183cf4f47" />

## 5. Firmware
This project uses **CircuitPython** with **KMK**.
* **File:** [main.py](https://github.com/user-attachments/files/24086007/main.py)
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

* **Microcontroller:** Seeed XIAO RP2040
