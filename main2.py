import numpy as np
from PIL import ImageGrab
import time
import os
from datetime import datetime
import cv2
import pyautogui
import random

x1, y1, x2, y2 = 658, 686, 1152, 737

save_folder = "images"

if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# Hàm phát hiện màu
def detect_color():
    # COLOR FOR DETECT ALL ISLAND 
    target_colors = [
        
        (22, 42, 219),  # Chuyển sang RGB: (219, 42, 22)
        (19, 45, 221),  # Chuyển sang RGB: (221, 45, 19)
        (23, 45, 221),  # Chuyển sang RGB: (221, 45, 23)
        (15, 38, 222),  # Chuyển sang RGB: (222, 38, 15)
        (15, 38, 222),  # Chuyển sang RGB: (222, 38, 15)
        (12, 48, 212),  # Chuyển sang RGB: (212, 48, 12)
        (23, 44, 216)   # Chuyển sang RGB: (216, 44, 23)
    ]
    
   
    screenshot = np.array(ImageGrab.grab(bbox=(x1, y1, x2, y2)))
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d-%H%M%S-%f")[:-3]
    image_path = os.path.join(save_folder, f"{timestamp}.png")
   
    bgr_image = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    
    for target_color in target_colors:
        
        lower_color = np.array(target_color, dtype="uint8")
        upper_color = np.array(target_color, dtype="uint8")

        mask = cv2.inRange(bgr_image, lower_color, upper_color)

        count = cv2.countNonZero(mask)

        if count > 0:
           
            with open("./log.txt", "a") as log_file:
                log_file.write("Detected\n")
            print("Detected")
            return True
    
    return False


def perform_action():
    # Tạo ra một số thời gian ngẫu nhiên cho mỗi hành động
    click_delay = random.uniform(0.08, 0.15)
    action_delay = random.uniform(0, 0.15)
    retry_delay = random.uniform(7, 9)

    # Di chuyển chuột đến vị trí cụ thể và thực hiện click
    x = random.uniform(1235, 1245)
    y = random.uniform(695, 715)
    pyautogui.click(x, y, duration=click_delay)
    time.sleep(action_delay)
    action_delay = random.uniform(0.3, 0.5)
    x = random.uniform(950, 980)
    y = random.uniform(695, 715)
    click_delay = random.uniform(0.7, 2.5)
    pyautogui.click(x, y, duration=click_delay)
    time.sleep(retry_delay)

counter = 0

while True:
    ok = detect_color()
    
    if ok:
        perform_action()
        counter = 0

    else:
        if(counter > 100):
            
            pyautogui.click(x=925, y=689)
            counter = 0
            
        else:
            counter += 1