mport cv2
import numpy as np
import time
from PIL import Image, ImageDraw
from luma.core.interface.serial import spi
from luma.oled.device import ssd1351
from collections import deque

# ---- GLOBAL QUEUE TO STORE LAST 5 ELLIPSE CENTERS ----
ellipse_queue = deque(maxlen=5)

# ---- OLED SETUP ----
serial = spi(port=0, device=0, gpio_DC=23, gpio_RST=22, bus_speed_hz=32000000)
oled = ssd1351(serial_interface=serial, width=128, height=128)

# Global pixel shifts for display rendering
x_shift = 0
y_shift = 20
y_scale = 0.75  # Set to <1.0 to squash vertically, >1.0 to stretch

# ---- IMAGE PROCESSING UTILS ----
def crop_to_aspect_ratio(image, width=640, height=480):
    current_height, current_width = image.shape[:2]
    desired_ratio = width / height
    current_ratio = current_width / current_height

    if current_ratio > desired_ratio:
        new_width = int(desired_ratio * current_height)
        offset = (current_width - new_width) // 2
        cropped_img = image[:, offset:offset + new_width]
    else:
        new_height = int(current_width / desired_ratio)
        offset = (current_height - new_height) // 2
        cropped_img = image[offset:offset + new_height, :]

    return cv2.resize(cropped_img, (width, height))

def apply_binary_threshold(image, darkestPixelValue, addedThreshold):
    threshold = darkestPixelValue + addedThreshold
    _, thresholded_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY_INV)
    return thresholded_image

def get_darkest_area(image):
    ignoreBounds = 20
    imageSkipSize = 20
    searchArea = 20
    internalSkipSize = 10

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    min_sum = float('inf')
    darkest_point = None

    for y in range(ignoreBounds, gray.shape[0] - ignoreBounds, imageSkipSize):
        for x in range(ignoreBounds, gray.shape[1] - ignoreBounds, imageSkipSize):
            current_sum = 0
            num_pixels = 0
            for dy in range(0, searchArea, internalSkipSize):
                if y + dy >= gray.shape[0]:
                    break
                for dx in range(0, searchArea, internalSkipSize):
                    if x + dx >= gray.shape[1]:
                        break
                    current_sum += gray[y + dy][x + dx]
                    num_pixels += 1

            if current_sum < min_sum and num_pixels > 0:
                min_sum = current_sum
                darkest_point = (x + searchArea // 2, y + searchArea // 2)

    return darkest_point
    
mport cv2
import numpy as np
import time
from PIL import Image, ImageDraw
from luma.core.interface.serial import spi
from luma.oled.device import ssd1351
from collections import deque

# ---- GLOBAL QUEUE TO STORE LAST 5 ELLIPSE CENTERS ----
ellipse_queue = deque(maxlen=5)

# ---- OLED SETUP ----
serial = spi(port=0, device=0, gpio_DC=23, gpio_RST=22, bus_speed_hz=32000000)
oled = ssd1351(serial_interface=serial, width=128, height=128)

# Global pixel shifts for display rendering
x_shift = 0
y_shift = 20
y_scale = 0.75  # Set to <1.0 to squash vertically, >1.0 to stretch

# ---- IMAGE PROCESSING UTILS ----
def crop_to_aspect_ratio(image, width=640, height=480):
    current_height, current_width = image.shape[:2]
    desired_ratio = width / height
    current_ratio = current_width / current_height

    if current_ratio > desired_ratio:
        new_width = int(desired_ratio * current_height)
        offset = (current_width - new_width) // 2
        cropped_img = image[:, offset:offset + new_width]
    else:
        new_height = int(current_width / desired_ratio)
        offset = (current_height - new_height) // 2
        cropped_img = image[offset:offset + new_height, :]

    return cv2.resize(cropped_img, (width, height))

def apply_binary_threshold(image, darkestPixelValue, addedThreshold):
    threshold = darkestPixelValue + addedThreshold
    _, thresholded_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY_INV)
    return thresholded_image

def get_darkest_area(image):
    ignoreBounds = 20
    imageSkipSize = 20
    searchArea = 20
    internalSkipSize = 10

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    min_sum = float('inf')
    darkest_point = None

    for y in range(ignoreBounds, gray.shape[0] - ignoreBounds, imageSkipSize):
        for x in range(ignoreBounds, gray.shape[1] - ignoreBounds, imageSkipSize):
            current_sum = 0
            num_pixels = 0
            for dy in range(0, searchArea, internalSkipSize):
                if y + dy >= gray.shape[0]:
                    break
                for dx in range(0, searchArea, internalSkipSize):
                    if x + dx >= gray.shape[1]:
                        break
                    current_sum += gray[y + dy][x + dx]
                    num_pixels += 1

            if current_sum < min_sum and num_pixels > 0:
                min_sum = current_sum
                darkest_point = (x + searchArea // 2, y + searchArea // 2)

    return darkest_point
    
mport cv2
import numpy as np
import time
from PIL import Image, ImageDraw
from luma.core.interface.serial import spi
from luma.oled.device import ssd1351
from collections import deque

# ---- GLOBAL QUEUE TO STORE LAST 5 ELLIPSE CENTERS ----
ellipse_queue = deque(maxlen=5)

# ---- OLED SETUP ----
serial = spi(port=0, device=0, gpio_DC=23, gpio_RST=22, bus_speed_hz=32000000)
oled = ssd1351(serial_interface=serial, width=128, height=128)

# Global pixel shifts for display rendering
x_shift = 0
y_shift = 20
y_scale = 0.75  # Set to <1.0 to squash vertically, >1.0 to stretch

# ---- IMAGE PROCESSING UTILS ----
def crop_to_aspect_ratio(image, width=640, height=480):
    current_height, current_width = image.shape[:2]
    desired_ratio = width / height
    current_ratio = current_width / current_height

    if current_ratio > desired_ratio:
        new_width = int(desired_ratio * current_height)
        offset = (current_width - new_width) // 2
        cropped_img = image[:, offset:offset + new_width]
    else:
        new_height = int(current_width / desired_ratio)
        offset = (current_height - new_height) // 2
        cropped_img = image[offset:offset + new_height, :]

    return cv2.resize(cropped_img, (width, height))

def apply_binary_threshold(image, darkestPixelValue, addedThreshold):
    threshold = darkestPixelValue + addedThreshold
    _, thresholded_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY_INV)
    return thresholded_image

def get_darkest_area(image):
    ignoreBounds = 20
    imageSkipSize = 20
    searchArea = 20
    internalSkipSize = 10

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    min_sum = float('inf')
    darkest_point = None

    for y in range(ignoreBounds, gray.shape[0] - ignoreBounds, imageSkipSize):
        for x in range(ignoreBounds, gray.shape[1] - ignoreBounds, imageSkipSize):
            current_sum = 0
            num_pixels = 0
            for dy in range(0, searchArea, internalSkipSize):
                if y + dy >= gray.shape[0]:
                    break
                for dx in range(0, searchArea, internalSkipSize):
                    if x + dx >= gray.shape[1]:
                        break
                    current_sum += gray[y + dy][x + dx]
                    num_pixels += 1

            if current_sum < min_sum and num_pixels > 0:
                min_sum = current_sum
                darkest_point = (x + searchArea // 2, y + searchArea // 2)

    return darkest_point