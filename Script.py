
#from selenium import webdriver
import pyautogui
#from selenium.webdriver.common.keys import Keys
import time
import threading
from pynput import keyboard
import sys

class MainThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.stop_flag = threading.Event()
        
    def run(self):
        print("Programa iniciado")
        while not self.stop_flag.is_set():
            pyautogui.moveTo(563, 1079, 0.5)
            time.sleep(2)
            pyautogui.click()
            time.sleep(2)
            pyautogui.write('Python 3', interval=0.25)
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.click(x=358, y=52)
            time.sleep(2)
            pyautogui.click(x=592, y=51)
            time.sleep(2)
            pyautogui.click(x=827, y=51)
            time.sleep(2)
            pyautogui.click(x=28, y=47)
            pass
        print("Programa encerrando")
        sys.exit()

class ControlThread(threading.Thread):
    def __init__(self, main_thread):
        super().__init__()
        self.main_thread = main_thread
        
    def on_press(self, key):
        if key == keyboard.Key.f8:
            self.main_thread.stop_flag.set()
            return False
        
    def run(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

main_thread = MainThread()
control_thread = ControlThread(main_thread)

main_thread.start()
control_thread.start()

main_thread.join()
control_thread.join()
