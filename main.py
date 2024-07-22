from kmk.extensions.display.builtin import BuiltInDisplay
from kmk.extensions.rgb import RGB, AnimationModes
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
import board
import time

import busio

from kmk.extensions.display import Display, TextEntry, ImageEntry

# For SSD1306
from kmk.extensions.display.ssd1306 import SSD1306

print("Starting")

keyboard = KMKKeyboard()

keyboard.modules.append(Layers())


# Start display bit
i2c_bus = busio.I2C(scl=board.GP5, sda=board.GP4)

driver = SSD1306(
    i2c=i2c_bus,

)

display = Display(
    # Mandatory:
    display=driver,
    # Optional:
    width=128,  # screen size
    height=32,  # screen size
    flip=False,  # flips your display content
    flip_left=False,  # flips your display content on left side split
    flip_right=False,  # flips your display content on right side split
    brightness=0.8,  # initial screen brightness level
    brightness_step=0.1,  # used for brightness increase/decrease keycodes
    dim_time=20,  # time in seconds to reduce screen brightness
    dim_target=0.1,  # set level for brightness decrease
    off_time=60,  # time in seconds to turn off screen
    powersave_dim_time=10,  # time in seconds to reduce screen brightness
    powersave_dim_target=0.1,  # set level for brightness decrease
    powersave_off_time=30,  # time in seconds to turn off screen
)

display.entries = [
    TextEntry(text="Hi :)", x=128, y=0, x_anchor="R", y_anchor="T"),
    TextEntry(text='Layer: ', x=0, y=32, y_anchor='B'),
    TextEntry(text='BASE', x=40, y=32, y_anchor='B', layer=0),
    TextEntry(text='NUM', x=40, y=32, y_anchor='B', layer=1),
    TextEntry(text='NAV', x=40, y=32, y_anchor='B', layer=2),
    TextEntry(text='0 1 2', x=0, y=4),
    TextEntry(text='0', x=0, y=4, inverted=True, layer=0),
    TextEntry(text='1', x=12, y=4, inverted=True, layer=1),
    TextEntry(text='2', x=24, y=4, inverted=True, layer=2),
]
keyboard.extensions.append(display)
# End diplay bit

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
            1),   KC.ENTER,  KC.MO(2), KC.SPACE,  KC.RALT
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
