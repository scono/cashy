import pywinauto

def search_visual(query_str):
    pywinauto.mouse.click(button='left', coords=(370, 104))
    pywinauto.keyboard.SendKeys(query_str, pause=0.01, with_spaces=True)
    pywinauto.keyboard.SendKeys('{ENTER}')

if __name__ == "__main__":
    pass
    
    

