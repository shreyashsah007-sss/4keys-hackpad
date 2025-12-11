[trying.csv](https://github.com/user-attachments/files/24104382/trying.csv)# 4-Key Hackpad Project

## 1. Overall Hackpad
Here is the finished design of my custom macro pad.
<img width="583" height="627" alt="Screenshot 2025-12-11 191650" src="https://github.com/user-attachments/assets/e81f0365-d1f4-462f-95b3-44273758d8b5" />



Component,Quantity,Description
Microcontroller,1,Seeed XIAO RP2040
Diodes,2,Through-hole 1N4148
Switches,16,MX-Style switches
Keycaps,16,Blank DSA keycaps (White)
Rotary Encoders,1,EC11 Rotary encoders
LEDs,2,SK6812 MINI-E LEDs
Screws,-,M3x16mm screws
Inserts,-,M3x5mmx4mm heatset inserts
Case,1,3D Printed Case

## 3. CAD Assembly (How it fits)
The case consists of a top and bottom shell, screwed together.
<img width="307" height="502" alt="Screenshot 2025-12-11 192406" src="https://github.com/user-attachments/assets/3909f3e3-d119-41f0-a1f0-6891f0fcab2a" />



## 4. Electronics
### Schematic
The wiring logic for the switches and microcontroller.
<img width="3507" height="2480" alt="image" src="https://github.com/user-attachments/assets/39ad36b5-b3c4-4996-b57e-4bd03bf0be31" />

### PCB Design
<img width="1700" height="907" alt="trying" src="https://github.com/user-attachments/assets/a55685b3-4c18-4388-b6aa-3fb9c6c27bd0" />
The physical board layout designed in KiCad.


## 5. Firmware
[main.py](https://github.com/user-attachments/files/24104359/main.py)
"""
Hackpad Firmware (KMK on Seeed XIAO RP2040)
Hardware: Seeed XIAO RP2040
Firmware: KMK (CircuitPython)
"""

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

# -------------------------------------------------------------------------
# SETUP
# -------------------------------------------------------------------------
keyboard = KMKKeyboard()

# Enable Media Keys (Required for Volume Control)
keyboard.extensions.append(MediaKeys())

# -------------------------------------------------------------------------
# PINS & WIRING
# -------------------------------------------------------------------------
# MATRIX PINS (Switches)
# Change these pins to match your PCB traces if different
keyboard.col_pins = (board.D0, board.D1)
keyboard.row_pins = (board.D2, board.D3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# ROTARY ENCODER PINS
# Common Hackpad pinout: A=D10, B=D9
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((board.D10, board.D9, None, False),)

# -------------------------------------------------------------------------
# KEYMAPPING
# -------------------------------------------------------------------------

# Encoder Map: [ (Counter-Clockwise, Clockwise, Button_Press) ]
# Currently set to Volume Down (Left) and Volume Up (Right)
encoder_handler.map = [ ((KC.VOLD, KC.VOLU),) ]

# Button Map: 2x2 Grid
# Current Layout: Copy, Paste, Cut, Save
keyboard.keymap = [
    [
        KC.LCTL(KC.C),  # Top Left
        KC.LCTL(KC.V),  # Top Right
        KC.LCTL(KC.X),  # Bottom Left
        KC.LCTL(KC.S)   # Bottom Right
    ]
]

if __name__ == '__main__':
    keyboard.go()
