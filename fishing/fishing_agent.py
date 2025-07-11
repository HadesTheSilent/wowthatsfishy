import cv2 as cv
import numpy as np
import pyautogui
import time

class FishingAgent:
    def __init__(self, main_agent) -> None:
        self.main_agent = main_agent
        self.fishing_target = cv.imread("fishing/assets/fishing_target.png")
        self.fishing_thread = None

    def cast_lure(self):
        print("Pescando...")
        pyautogui.press('1')
        time.sleep(2)
        self.find_lure()

    def find_lure(self):
        while self.main_agent.cur_img is None or not isinstance(self.main_agent.cur_img, np.ndarray):
            print("Aguardando captura de tela...")
            time.sleep(0.1)
        cur_img = self.main_agent.cur_img
        lure_location = cv.matchTemplate(
            cur_img, 
            self.fishing_target,
            cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(lure_location)
        print(max_loc)
        self.move_to_lure(max_loc)
        # cv.imshow("Match Template", lure_location)
        # cv.waitKey(0)

    def move_to_lure(self, max_loc):
        pyautogui.moveTo(max_loc[0], max_loc[1], 1, pyautogui.easeOutQuad)
        self.watch_lure(max_loc)

    def watch_lure(self, max_loc):
        watch_time = time.time()
        while True:
            pixel = self.main_agent.cur_imgHSV[max_loc[1], max_loc[0]]
            print(pixel)

            if self.main_agent.zone == "Darkmoon Faire" and self.main_agent.time == "night":
                if pixel[0] >= 60:
                    print("Peixe detectado!")
                    break

            if time.time() - watch_time >= 20:
                break
        self.pull_line()

    def pull_line(self):
        print("Puxando a linha...")
        pyautogui.keyDown('shift')
        time.sleep(0.005)
        pyautogui.click(button='right')
        time.sleep(0.010)
        

    def run(self):
        while True:
            self.cast_lure()
            time.sleep(5)