# terminatorglasses
DIY project for eye tracked terminator sunglasses. This project captures real-time video from a webcam, processes it to identify the darkest region of the eye (typically the pupil), and visualizes the detected ellipse on a 128x128 RGB OLED display (SSD1351). The output ellipse is stabilized using median filtering and displayed with configurable positioning and scaling. A video tutorial can be found here: https://youtu.be/xjmwgky0e2Q.

To help support this software and other open-source projects, please consider subscribing to my YouTube channel: https://www.youtube.com/@jeoresearch

## 📷 Features

- Real-time webcam-based eye tracking using OpenCV
- Pupil detection with brightness thresholding and contour filtering
- Smoothed ellipse rendering using a rolling median of the last 5 frames
- Visualization on a 128x128 SSD1351 OLED via SPI
- Adjustable:
  - X/Y position shifts (`x_shift`, `y_shift`)
  - Vertical scaling of the ellipse (`y_scale`)
  - Optional horizontal flip for mirrored display

---

## 🛠 Hardware Requirements

- Raspberry Pi 3/4/5 with SPI enabled
- Waveshare or equivalent 1.5" 128x128 SSD1351 RGB OLED (SPI)
- GC0308 infrared webcam

## Links to parts
- GC0308 Eye Tracking Camera ($17): https://amzn.to/41x8p2W
- USB extension cables ($10): https://amzn.to/43SznVl
- Raspberry Pi 4B ($60): https://amzn.to/3YlQnzV
- RBG OLED Panel ($24): https://amzn.to/3ElpkxC
- Pi cable set ($6): https://amzn.to/43TeSYC

Affiliate links on this page help support the channel at no extra cost to you. As an Amazon Associate, I earn from qualifying purchases. All earnings support the development of open-source software and projects like this! 


### OLED Wiring Reference

| OLED Pin | Function     | Raspberry Pi Pin | GPIO         |
|----------|--------------|------------------|--------------|
| VCC      | 3.3V         | Pin 1            |              |
| GND      | Ground       | Pin 6            |              |
| DIN      | SPI MOSI     | Pin 19           | GPIO10       |
| CLK      | SPI Clock    | Pin 23           | GPIO11       |
| CS       | Chip Select  | Pin 24           | GPIO8        |
| DC       | Data/Command | Pin 16           | GPIO23       |
| RST      | Reset        | Pin 15           | GPIO22       |

---

## 📦 Dependencies

Install dependencies using pip:

```bash
pip3 install opencv-python pillow luma.oled
