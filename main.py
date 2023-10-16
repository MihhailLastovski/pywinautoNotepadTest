import time
import pywinauto
from pywinauto.application import Application

app = Application().start("notepad.exe")

main_window = app.top_window()

try:
    main_window.Edit.type_keys("Это тест Notepad.")

    main_window.menu_item("Fail->Nimega salvestamine").click_input()
    timestr = time.strftime("%Y%m%d-%H%M%S")

    filename = rf'C:\Users\opilane\Downloads\test_{timestr}.txt' 
    pywinauto.keyboard.send_keys(filename)

    pywinauto.keyboard.send_keys('{VK_RETURN}')

    main_window.Edit.type_keys("!!!!!")

    main_window.menu_item("Fail->Salvesta").click_input()

    main_window.menu_item("Fail->Välju").click_input()

    app.kill()

except Exception as e:
    print("Error:", str(e))
