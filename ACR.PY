import cv2
import numpy as np
import pyautogui


class AutoClickerR:
    def __init__(self):
        pass

    def get_coords(self, img, threshold=0.8):
        img_rgb = np.array(pyautogui.screenshot())
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(img, 0)
        w, h = template.shape[::-1]

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        coords = list()
        for pt in zip(*loc[::-1]):
            x, y = pt[0] + w // 2, pt[1] + h // 2
            coords.append((x, y))
        print(coords)
        return coords[:2]

    def click(self, img, button='left', click_num=1, interval=0, id=0, duration=2, threshold=0.8):
        coords = self.get_coords(img, threshold)
        print(coords)
        pyautogui.moveTo(coords[id], duration=duration)
        pyautogui.click(clicks=click_num, button=button, interval=interval)

    def dragTo(self, img, button='left', id=0, duration=2, threshold=0.8):
        coords = self.get_coords(img, threshold)
        pyautogui.dragTo(coords[id], button=button, duration=duration)

    def scroll(self, num):
        pyautogui.scroll(num)

    def write(self, text, interval):
        pyautogui.typewrite(text, interval)

    def hotkey(self, keys):
        pyautogui.hotkey(keys)

