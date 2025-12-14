# Hi

Hey, I’m a young student from Germany who found out about the Hack Club a few hours ago XD. Since then, I have been using every second to start building a project I’ve had in mind forever.

# The Project

In a very similar fashion to the "Hackpad" guide, I have been dreaming of a hardware interface on my desk for the projects I build (and to check if my backup is live, just to calm some nerves…). As I have discovered, I have not been able to fit my plans into the constraints of the Hackpad guide. But if you look at the plan, it becomes clear that it has provided some inspiration. Despite this, the original idea is already a few weeks old. In these weeks, I have already built an Arduino-based prototype to test some of the functionality.

As I developed the idea today, I made a simple analog draft of the layout:

![WhatsApp Bild 2025-12-06 um 00.24.01_b16f0518](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTk0NTAsInB1ciI6ImJsb2JfaWQifX0=--37e2e399011b1b5180a64b8cb51b9df19c8af8f1/WhatsApp%20Bild%202025-12-06%20um%2000.24.01_b16f0518.jpg)

I have come as far as to start learning KiCad, which I, as a programmer and developer in software, have never touched before. In this process, I have started to lay out the components: 

![grafik](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTk0NTIsInB1ciI6ImJsb2JfaWQifX0=--ec1a45b2c6825646fb1788e0f19310250e0fca1d/grafik.png)

---

The last few hours I’ve been working on the schematic without a relay, having no idea what I was doing… XD

With the information from the provided guides and a bit of research, I was able to put together a version that 🤞 should work. To verify this, I’ve put a post up in Slack.

![grafik](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MjAxMDAsInB1ciI6ImJsb2JfaWQifX0=--b97ded5fb2289ef8e1c3e5233a620bdb8fbbb82f/grafik.png)

This schematic implements every part that I thought of in the drawing yesterday. To make this work, I had to use an IO expander, even though I didn’t really know how to do that. The next step toward completion will be to verify the correct implementation of this...

---

Today I started by finishing the schematic. Most of the work ended up being a fight with the libraries to get the right OLED and a matching footprint…

This change came from the message that was sent in Slack yesterday.

![WhatsApp Bild 2025-12-07 um 17.29.00_7e5e3bc0](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MjA2ODIsInB1ciI6ImJsb2JfaWQifX0=--8b51eb754e5cf974be81aabca4782a5e286b6b8f/WhatsApp%20Bild%202025-12-07%20um%2017.29.00_7e5e3bc0.jpg)


After finally completing the schematic, I moved on to the PCB.

The layout wasn’t much of a challenge. I had already done most of the thinking while sketching the first layout by hand (as shown in the entries below), so cleaning up the automatic placement only took a few minutes.

With that done, I started routing the PCB, taking extra care to make the traces look nice and to leave enough room for the silkscreen in the areas where the board will be visible in the end.

Even though I’ve never done anything like this before, I didn’t really run into problems and got everything done in a reasonable amount of time once I figured out the controls.

(And then I played around with the silkscreen…)

![WhatsApp Bild 2025-12-07 um 17.28.47_4aa92623](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MjA2ODEsInB1ciI6ImJsb2JfaWQifX0=--eb00cb8a6a32142d56cfb55b3a7257bb18c726e3/WhatsApp%20Bild%202025-12-07%20um%2017.28.47_4aa92623.jpg)


Just to be sure, I posted the result on Slack to check if I messed anything up.

---

## There is a Case!?

![DPDIM V1_FrontRight](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MjM5MTYsInB1ciI6ImJsb2JfaWQifX0=--7a394545360b6a1921878a77d5d1a89178d2b9a6/DPDIM%20V1_FrontRight.png)

In the time since the last journal, I have finished the hardware. On the PCB there were a few small errors, which the slack helped me correct, and I also spent some time cleaning up the routing while adding pins for future expansion. I also took the time to get 3D models for all the components to make designing the case easier.

![KiCad-Diynamic-Project-Display-Module](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MjM5MTcsInB1ciI6ImJsb2JfaWQifX0=--7eb2d985cc81f25a8124513ea1d53cab56abb2d4/KiCad-Diynamic-Project-Display-Module.png)

I started designing the case in the Onshape cloud. This, as it turned out, wasn’t my brightest idea, as it took an eternity to even rotate the part, which was especially irritating while learning the controls on the fly. This caused me to give up on the program entirely and forced me to wait a few hours to get my Fusion 360 license.

After getting back to work with the processing power of my local machine, I didn’t have many problems creating a usable case, as I have prior experience with (very) simple CAD design.

My design is fairly simple, including only two “unconventional” features. The first is a large cutout that provides a view of the LED array, and the second is a cutout in the back that gives access to the expansion pins.

After getting a usable design, I added a few simple artistic elements to pimp it up and build something I actually want to have on my desk all the time. These come in the form of a few small channels in the top plate that will be filled with colored inlays after printing (they are colored in the renders).

![DPDIM V1_Inside](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MjM5MjMsInB1ciI6ImJsb2JfaWQifX0=--907fc38323987068e10fbf2db019d02a49235599/DPDIM%20V1_Inside.png)

![DPDIM_V1_FrontLeft](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MjM5MjQsInB1ciI6ImJsb2JfaWQifX0=--88b4b56fc934c598c50568fdeb74093b9ae6c32c/DPDIM_V1_FrontLeft.png)

![DPDIM_V1_FrontTop](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MjM5MjUsInB1ciI6ImJsb2JfaWQifX0=--07194f1179cc9a3efd0b07d9e593408e194d54e4/DPDIM_V1_FrontTop.png)


In the next step, I will create the README and check if there is anything else to do before submitting.

---

In the last few hours I have been able to produce 171 lines of code, that in theory should get my board up and running.

The software architecture of my design incorporates two parts, that are working in sync. The first one is the firmware, which is based on KMK. It implements a JSON API on the serial bus which enables me to send inputs to the PC and receive status updates for the various display options. On the side of the PC there is a program, that is on auto start. It acts on the inputs and queries various sources of information locally, like my ActivityWatch localhost and the server and website. This information is sent to the pad to be displayed.

The exact API layout:

### 1. LED Control

Control individual status LEDs.

**Command:**
```json
{
  "type": "led",
  "index": 0,
  "value": true
}
```

**Parameters:**
- `type` (string): `"led"`
- `index` (integer): LED index
- `value` (boolean): `true` = ON, `false` = OFF



### 2. RGB Pixel Control (Single)

**Command:**
```json
{
  "type": "rgb",
  "index": 5,
  "r": 255,
  "g": 128,
  "b": 0
}
```

**Parameters:**
- `type` (string): `"rgb"`
- `index` (integer): Pixel index
- `r` (integer)
- `g` (integer)
- `b` (integer)



### 3. RGB Pixel Control (All)

**Command:**
```json
{
  "type": "rgb_all",
  "r": 255,
  "g": 0,
  "b": 0
}
```

**Parameters:**
- `type` (string): `"rgb_all"`
- `r` (integer)
- `g` (integer)
- `b` (integer)



### 4. OLED Display - Set Text

**Command:**
```json
{
  "type": "oled",
  "line": 0,
  "text": "Hello World"
}
```

**Parameters:**
- `type` (string): `"oled"`
- `line` (integer): Line index
- `text` (string)




### 5. OLED Display - Clear All

**Command:**
```json
{
  "type": "oled_clear"
}
```

**Parameters:**
- `type` (string): `"oled_clear"`



## Events (Device → Host)

### 1. Key Press/Release

**Message:**
```json
{
  "type": "key",
  "row": 0,
  "col": 5,
  "state": "press"
}
```

**Fields:**
- `type` (string): `"key"`
- `row` (integer): Row index (0-1)
- `col` (integer): Column index (0-8)
- `state` (string): `"press"` or `"release"`

---

### 2. Encoder Rotation

**Message:**
```json
{
  "type": "encoder",
  "id": 0,
  "delta": 1
}
```

**Fields:**
- `type` (string): `"encoder"`
- `id` (integer)
- `delta` (integer): Direction: `1` = clockwise, `-1` = counter-clockwise


### 3. Encoder Button

**Message:**
```json
{
  "type": "encoder_btn",
  "id": 0,
  "state": "press"
}
```

**Fields:**
- `type` (string): `"encoder_btn"`
- `id` (integer)
- `state` (string): `"press"` or `"release"`



## Response Types

### Acknowledgment (ACK)

Sent when a command is successfully executed.

**Format:**
```json
{
  "type": "ack",
  "cmd": "led"
}
```

**Fields:**
- `type` (string): `"ack"`
- `cmd` (string): The command type that was executed



### Error

Sent when a command fails.

**Format:**
```json
{
  "type": "err",
  "cmd": "rgb",
  "reason": "bad_args"
}
```

**Fields:**
- `type` (string): `"err"`
- `cmd` (string): The command type that failed
- `reason` (string): Error reason:
  - `"json"` - JSON parsing error
  - `"bad_args"` - Invalid arguments or out-of-range values
  - `"unknown_cmd"` - Unknown command type

As I don’t have my board yet, my only option is to pray this works...

(the same render als last time: I like it as the profile pic!)
![DPDIM V1_FrontRight](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MjQ0NDUsInB1ciI6ImJsb2JfaWQifX0=--758ea7fa2879281a545dce1340fcf5cb2c75b873/DPDIM%20V1_FrontRight.png)

---