import json

import board
import busio
import digitalio
import usb_cdc
from kmk.extensions import Extension
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.rgb import RGB
from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules.encoder import EncoderHandler
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import MatrixScanner
from kmk.scanners.mcp230xx import MCP23017


API_VERSION = "1.0"


keyboard = KMKKeyboard()
serial = usb_cdc.data


# I2C
i2c = busio.I2C(board.GP5, board.GP4)


# Matrix (MCP23017)
mcp = MCP23017(i2c=i2c, address=0x20)
ROWS = [board.GP26, board.GP27]
COLS = [mcp.get_pin(i) for i in range(9)]


keyboard.matrix = MatrixScanner(
    columns=COLS,
    rows=ROWS,
    diode_orientation=DiodeOrientation.COL2ROW,
)


keyboard.keymap = [[None] * 18]


# Status LEDs
status_leds = []
for pin in [board.GP17, board.GP18, board.GP19]:
    led = digitalio.DigitalInOut(pin)
    led.direction = digitalio.Direction.OUTPUT
    status_leds.append(led)


# RGB
rgb = RGB(pixel_pin=board.GP16, num_pixels=16, val_limit=120)
keyboard.extensions.append(rgb)


# OLED
display = Display(
    display=SSD1306(i2c=i2c),
    entries=[
        TextEntry(text="MacroPad", x=0, y=0),
        TextEntry(text="Ready", x=0, y=10),
    ],
)
keyboard.extensions.append(display)


# Encoder
encoder = EncoderHandler()
encoder.pins = ((board.GP10, board.GP11, board.GP12),)
keyboard.modules.append(encoder)


class JsonAPI(Extension):
    def send(self, obj):
        serial.write(json.dumps(obj).encode() + b"\n")

    def before_matrix_scan(self, keyboard):
        if serial.in_waiting:
            try:
                msg = json.loads(serial.readline())
                self.handle_cmd(msg)
            except Exception:
                self.send({"type": "err", "cmd": "unknown", "reason": "json"})

    def handle_cmd(self, msg):
        t = msg.get("type")
        if t == "led":
            status_leds[msg["index"]].value = bool(msg["value"])
        elif t == "rgb":
            rgb.set_pixel(msg["index"], (msg["r"], msg["g"], msg["b"]))
            rgb.show()
        elif t == "rgb_all":
            for i in range(16):
                rgb.set_pixel(i, (msg["r"], msg["g"], msg["b"]))
            rgb.show()
        elif t == "oled":
            display.entries[msg["line"]].text = msg["text"]


keyboard.go()
