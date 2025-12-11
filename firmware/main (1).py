import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((board.D10, board.D9, None, False),)
encoder_handler.map = [ ((KC.VOLD, KC.VOLU),) ]

keyboard.col_pins = (board.D0, board.D1)
keyboard.row_pins = (board.D2, board.D3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.LCTL(KC.C),
        KC.LCTL(KC.V),
        KC.LCTL(KC.X),
        KC.LCTL(KC.S)
    ]
]

if __name__ == '__main__':
    keyboard.go()