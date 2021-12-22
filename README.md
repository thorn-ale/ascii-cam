# ascii_cam

ascii_cam is a Python toy to display a camera feed in ascii in the windows terminal

## Installation

Clone the repository, install the requirements and enjoy !

```bash
git@github.com:thorn-ale/ascii-cam.git
cd ascii_cam
pip install -r requirements.txt
```

## Usage

```bash
python ascii_cam.py <renderer_type>
```
*<renderer_type>* : either 16 or 64, selects the number of ascii characters to use as a rendering charset.

## Usage as a virtual camera (tested for Teams, Telegram and Signal)
The ascii video stream is set inside a terminal. To make it a functionnal virtual camera you will need to install [OBS](https://obsproject.com/).

1. Launch the terminal stream (see [Usage](#Usage))
2. Launch OBS
3. in OBS add a new "Window capture" source and select your terminal.
You may need to change the capture method to "Windows Graphic Capture (Windows 10 1903 and up)"
You also may have to adjust the size settings in OBS
4. Then click "Start Virtual Camera"
5. Call your colleagues on Teams & enjoy !

## License
[BEERWARE](https://spdx.org/licenses/Beerware.html)