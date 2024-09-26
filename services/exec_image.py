import os.path
import subprocess

import cv2
import numpy as np


def getlocation_image(image_direct, image_original):
    try:
        print(image_direct)
        if not os.path.exists(image_direct):
            return {
                "result": "error",
                "message": "no file path image"
            }
        image_detect = cv2.imread(image_direct)
        original_gray = cv2.cvtColor(image_original, cv2.COLOR_BGR2GRAY)
        detect_gray = cv2.cvtColor(image_detect, cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(original_gray, detect_gray, cv2.TM_CCOEFF_NORMED)
        threshold = 0.80
        locations = np.where(result >= threshold)
        return {
            "result": "success",
            "locations": locations,
            "image_original": image_original,
            "image_detect": image_detect,
        }
    except Exception as ex:
        return {
            "result": "error",
            "message": str(ex)
        }


def detect_image(image_direct, device_connect):
    try:
        subprocess.run(f'adb -s {device_connect} shell screencap /sdcard/{device_connect.replace("-", "")}.png')
        subprocess.run(f'adb -s {device_connect} pull /sdcard/{device_connect.replace("-", "")}.png')
        image_original = cv2.imread(f"./{device_connect.replace("-", "")}.png")
        result = []
        for index, img in enumerate(image_direct):
            result_check_image = getlocation_image(img, image_original)
            if result_check_image['result'] == "error":
                return {
                    "result": "error",
                    "message": result_check_image['message']
                }
            locations = result_check_image['locations']
            image_detect = result_check_image['image_detect']
            image_original = result_check_image['image_original']
            for pt in zip(*locations[::-1]):
                print(pt)
                point_a = (int(pt[0] + (image_detect.shape[1]) / 2), int(pt[1] + (image_detect.shape[0] / 2)))
                result.append(point_a)
        return {
            "result": result,
        }
    except Exception as ex:
        return {
            "result": "error",
        }
