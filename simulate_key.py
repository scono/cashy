import keyboard
from time import sleep
from pywinauto import application
from pywinauto.findwindows import WindowAmbiguousError, WindowNotFoundError
import pywinauto

def take_screenshot():
    app = application.Application()
    app.connect(title_re=".*ApowerMirror Main.*")
    app_dialog = app.top_window()
    app_dialog.set_focus()
    #sleep(1.5)
    pywinauto.keyboard.SendKeys('^q', pause=0.01)
    
if __name__ == "__main__":
    pass