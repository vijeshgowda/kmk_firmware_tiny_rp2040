from kmk.extensions.rgb import RGB, AnimationModes
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
import board
import time

print("Starting")

keyboard = KMKKeyboard()

keyboard.modules.append(Layers())

# Debugging: Print initialization status
print("Initializing Split Module")

split = Split(
    split_type=SplitType.UART,
    data_pin=board.GP12,
    data_pin2=board.GP13,
    use_pio=True,
    uart_flip=True
)
keyboard.modules.append(split)

print("Split Module Initialized")

keyboard.row_pins = (board.GP6, board.GP7, board.GP8, board.GP9)
keyboard.col_pins = (board.GP27, board.GP26, board.GP22,
                     board.GP21, board.GP20, board.GP19)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Debugging: Confirm pin setup
print(f"Row Pins: {keyboard.row_pins}")
print(f"Column Pins: {keyboard.col_pins}")

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

FnKey = KC.MO(1)

keyboard.keymap = keymap = [
    # Layer 0 (default layer)
    [
        KC.ESCAPE,  KC.Q,       KC.W,       KC.E,      KC.R,       KC.T,      KC.Y,     KC.U,       KC.I,       KC.O,       KC.P,       KC.BSPACE,
        KC.LCTL,    KC.A,       KC.S,       KC.D,      KC.F,       KC.G,      KC.H,     KC.J,       KC.K,       KC.L,       KC.SCOLON,	KC.QUOTE,
        KC.LSHIFT,  KC.Z,       KC.X,       KC.C,      KC.V,       KC.B,      KC.N,     KC.M,       KC.COMMA,	KC.DOT,		KC.SLASH,	KC.RSHIFT,
        XXXXXXX,    XXXXXXX,    XXXXXXX,    KC.LCTRL,  KC.MO(
            1),   KC.SPACE,  KC.ENTER, KC.MO(2),   KC.RALT
    ],
    # Layer 1 (activated by pressing FN)
    [
        KC.TAB, KC.KP_1, KC.KP_2, KC.KP_3, KC.KP_4, KC.KP_5,         KC.KP_6, KC.KP_7, KC.KP_8, KC.KP_9, KC.KP_0, KC.BSPC,
        KC.LCTL, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,       KC.LEFT, KC.DOWN, KC.UP, KC.RIGHT, XXXXXXX, XXXXXXX,
        KC.LSFT, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,       XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX, XXXXXXX, XXXXXXX, KC.LGUI, _______, KC.SPC,       KC.ENT, KC.MO(
            3), KC.RALT
    ],
    # Layer 2 (activated by another FN key)
    [
        KC.TAB, KC.EXLM, KC.AT, KC.HASH, KC.DLR, KC.PERC,           KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN, KC.BSPC,
        KC.LCTL, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,       KC.MINS, KC.EQL, KC.LBRC, KC.RBRC, KC.BSLS, KC.GRV,
        KC.LSFT, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,       KC.UNDS, KC.PLUS, KC.LCBR, KC.RCBR, KC.PIPE, KC.TILD,
        XXXXXXX, XXXXXXX, XXXXXXX, KC.LGUI, KC.MO(
            3), KC.SPC,      KC.ENT, _______, KC.RALT
    ]
]

if __name__ == '__main__':
    print("Starting Keyboard Loop")
    keyboard.go()
