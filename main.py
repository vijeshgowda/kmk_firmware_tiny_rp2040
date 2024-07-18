# main.py
from kmk.extensions.rgb import RGB, AnimationModes
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
import board
print("Starting")


keyboard = KMKKeyboard()

keyboard.modules.append(Layers())

# Using drive names (REDOXL, REDOXR) to recognize sides; use split_side arg if you're not doing it
split = Split(split_type=SplitType.UART, split_side=SplitSide.LEFT,
              data_pin=board.GP0, data_pin2=board.GP1, use_pio=True, uart_flip=True)
# split = Split(split_type=SplitType.UART, split_side=SplitSide.RIGHT, data_pin=board.GP0, data_pin2=board.GP1, use_pio=True, uart_flip = True)
keyboard.modules.append(split)

keyboard.row_pins = (board.GP9, board.GP8, board.GP7, board.GP6)
keyboard.col_pins = (board.GP27, board.GP26, board.GP22,
                     board.GP21, board.GP20, board.GP19)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

FnKey = KC.MO(1)

keyboard.keymap = keymap = [
    # Layer 0 (default layer)
    [
        KC.ESCAPE, KC.Q, KC.W, KC.E, KC.R, KC.T,       KC.Y, KC.U, KC.I, KC.O, KC.P, KC.BSPC,
        KC.LCTL, KC.A, KC.S, KC.D, KC.F, KC.G,      KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT,
        KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B,      KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.ESC,
        KC.LGUI, KC.MO(1), KC.SPC,      KC.ENT, KC.MO(2),   KC.RALT
    ],
    # Layer 1 (activated by pressing FN)
    [
        KC.TAB, KC.ONE, KC.TWO, KC.THREE, KC.FOUR, KC.FIVE,         KC.SIX, KC.SEVEN, KC.EIGHT, KC.NINE, KC.ZERO, KC.BSPC,
        KC.LCTL, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,       KC.LEFT, KC.DOWN, KC.UP, KC.RIGHT, XXXXXXX, XXXXXXX,
        KC.LSFT, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,       XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        KC.LGUI, _______, KC.SPC,       KC.ENT, KC.MO(3), KC.RALT
    ],
    # Layer 2 (activated by another FN key)
    [
        KC.TAB, KC.EXLM, KC.AT, KC.HASH, KC.DLR, KC.PERC,           KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN, KC.BSPC,
        KC.LCTL, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,       KC.MINS, KC.EQL, KC.LBRC, KC.RBRC, KC.BSLS, KC.GRV,
        KC.LSFT, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,       KC.UNDS, KC.PLUS, KC.LCBR, KC.RCBR, KC.PIPE, KC.TILD,
        KC.LGUI, KC.MO(3), KC.SPC,      KC.ENT, _______, KC.RALT
    ]
]


if __name__ == '__main__':
    keyboard.go()
