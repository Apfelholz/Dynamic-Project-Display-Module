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
                # serial.readline() returns bytes; decode before json parsing
                raw = serial.readline()
                msg = json.loads(raw.decode())
                self.handle_cmd(msg)
            except Exception:
                self.send({"type": "err", "cmd": "unknown", "reason": "json"})

    def handle_cmd(self, msg):
        t = msg.get("type")
        try:
            if t == "led":
                idx = int(msg.get("index", -1))
                val = bool(msg.get("value", False))
                if 0 <= idx < len(status_leds):
                    status_leds[idx].value = val
                else:
                    raise ValueError("bad_led_index")
            elif t == "rgb":
                idx = int(msg.get("index", -1))
                r = int(msg.get("r", 0))
                g = int(msg.get("g", 0))
                b = int(msg.get("b", 0))
                if 0 <= idx < rgb.num_pixels:
                    rgb.set_pixel(idx, (r, g, b))
                    rgb.show()
                else:
                    raise ValueError("bad_rgb_index")
            elif t == "rgb_all":
                r = int(msg.get("r", 0))
                g = int(msg.get("g", 0))
                b = int(msg.get("b", 0))
                for i in range(rgb.num_pixels):
                    rgb.set_pixel(i, (r, g, b))
                rgb.show()
            elif t == "oled":
                line = int(msg.get("line", -1))
                text = str(msg.get("text", ""))
                if 0 <= line < len(display.entries):
                    display.entries[line].text = text
                else:
                    raise ValueError("bad_oled_line")
            elif t == "oled_clear":
                for e in display.entries:
                    e.text = ""
            else:
                raise ValueError("unknown_cmd")


            self.send({"type": "ack", "cmd": t})


        except Exception:
            self.send({"type": "err", "cmd": t, "reason": "bad_args"})

    def on_key_event(self, keyboard, key, is_pressed):
        if key:
            self.send({
                "type": "key",
                "row": key.row,
                "col": key.col,
                "state": "press" if is_pressed else "release",
            })


    def on_encoder_turn(self, keyboard, encoder_id, direction):
        self.send({
            "type": "encoder",
            "id": encoder_id,
            "delta": direction,
        })


    def on_encoder_press(self, keyboard, encoder_id, is_pressed):
        self.send({
            "type": "encoder_btn",
            "id": encoder_id,
            "state": "press" if is_pressed else "release",
        })


keyboard.extensions.append(JsonAPI())


serial.write(json.dumps({
    "type": "boot",
    "api": API_VERSION,
    "status": "ready",
}).encode() + b"\n")

keyboard.go()