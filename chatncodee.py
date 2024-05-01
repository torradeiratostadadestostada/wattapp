import pyautogui
import keyboard
import time
a = 902
waggg = time.time()
contatos = 16730
contatos_restantes = contatos - a
quantos = 0

for i in range(round(contatos_restantes / 5)):
    tempo_inicial=time.time()
    pyautogui.moveTo(x=895, y=761)
    time.sleep(1)
    pyautogui.mouseDown(button="left", x=895, y=761)
    time.sleep(1)
    pyautogui.mouseUp(button="left")
    for i in range(40):
        branco = pyautogui.pixel(966, 124)
        if branco == (249, 249, 249):
            time.sleep(0.5)
        else:
            break
    pyautogui.moveTo(x=1089, y=125)
    time.sleep(0.1)
    pyautogui.click(x=1089, y=125)
    time.sleep(1)
    pyautogui.moveTo(799, 179)
    for i in range(9999999999):
        x,y = pyautogui.position()
        r,g,b = pyautogui.pixel(x,y)
        if r == 14 and g == 187 and b == 131:
            time.sleep(0.5)
            break
        time.sleep(0.2)
    for i in range(a):
        pyautogui.press("down")
    for i in range(5):
        pyautogui.press("down")
        a = a + 1
        time.sleep(0.2)
        keyboard.press("enter")
        keyboard.release("enter")
        time.sleep(0.5)
        r,g,b = pyautogui.pixel(984, 134)
        quantos = quantos + 1
        time.sleep(0.2)
        if not r == 61 and not g == 87 and not b == 98:
            print("Grupo...")
            pyautogui.moveTo(1075, 568)
            time.sleep(0.3)
            pyautogui.click(x=1075, y=568)
            break
    pyautogui.moveTo(x=1136, y=896)
    time.sleep(0.2)
    pyautogui.click(x=1136, y=896)
    print(f"Nessa Sessão:{quantos}")
    print(f"Total:{a}")
    print(f"Tempo sendo executado:{waggg}")
    print(f"Tempo desde o ultimo contato: {time.time() - tempo_inicial}")
    print("--------------------------------")
    time.sleep(3)

