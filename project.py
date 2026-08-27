import time
import pyautogui as pag
import keyboard 
import easyocr 
import numpy as np


def main():
    print("Ready")
    keyboard.wait('w')
    pag.click(x=956, y=731)
    pag.click(x=964, y=785)
    time.sleep(3)
    while True:
        type(listWords(findWords()))
def findWords():
    img = np.array(pag.screenshot(region=(720, 190, 480, 270)))
    result = reader.readtext(img, detail=0)
    return result


def listWords(inputList):
    outputList = []
    for x in inputList:
        if len(outputList) > 0:
            for y in outputList:
                if x in y:
                    break
                else:
                    outputList.append(x)
        else:
            outputList.append(x)

    outputList = list(dict.fromkeys(outputList))
    inputList.clear()
    return outputList


def type(wordsToType):
    for x in wordsToType:
        pag.write(x)
    wordsToType.clear()

if __name__ == "__main__":
    reader = easyocr.Reader(['en'])
    main()
