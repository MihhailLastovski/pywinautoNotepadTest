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

    open_dialog = None
    timeout = 20
    while open_dialog is None and timeout > 0:
        open_dialog = app.window(title='Ava')
        timeout -= 1
        time.sleep(1)

    

    main_window.Edit.type_keys("!!!!!")

    main_window.menu_item("Fail->Salvesta").click_input()

    main_window.menu_item("Fail->Välju").click_input()

    app.kill()

except Exception as e:
    print("Произошла ошибка:", str(e))
