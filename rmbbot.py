import pyscreeze
import pyautogui
import time

enterabyss = "enterabyss.png"
chooseabyss = "chooseabys.png"
challenge = "challenge.png"
plusone = "plusone.png"

blessingDmg = "dmg.png"
blessingCrit = "crit.png"

#buttons search
buttons = [enterabyss, chooseabyss, challenge, plusone]
#blessing search
blessing = [blessingDmg]
#run timer to pause the script in seconds while doing the run. choose estimated run time
runtimer = 60

####################dont change anything here#############################
def checkBlessing(resImage,blessing,a):
    if resImage == "challange.png":
        #only loop 5 times to prevent stuck on challange screen
        while a < 6:
            for b in blessing:
                try:
                    x, y = pyautogui.locateCenterOnScreen(b, grayscale=False, confidence=0.8)
                    pyautogui.click(x, y)
                    return 1
                except:
                    a += 1
                    print("image loaded but couldn't find " +b)

def checkForImage(resImage):
    try:
        x, y = pyautogui.locateCenterOnScreen(resImage, grayscale=False, confidence=0.8)
        pyautogui.click(x, y)
        return 1
    except:
        print("image loaded but couldn't find " + resImage)
        return 0

while True:
    for i in buttons:
        a = 0
        checkBlessing(i,blessing,a)
        res = checkForImage(i)
        if res == 1 and i == challenge:
            time.sleep(runtimer)
##########################################################################
