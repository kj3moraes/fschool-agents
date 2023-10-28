
# import module
from pdf2image import convert_from_path
import time
import pyautogui
 

def convert_pdf_to_imgs():
    import os
    if not os.path.exists('output'):
        os.makedirs('output')
    # Store Pdf with convert_from_path function
    images = convert_from_path('ps3.pdf')
    
    for i in range(len(images)):
    
        # Save pages as images in the pdf
        images[i].save('output/scrapepage'+ str(i) +'.jpg', 'JPEG')
    return len(images)

def upload_imgs_to_chatgpt(num_imgs: int):
    pyautogui.keyDown('command')
    pyautogui.press('space')
    pyautogui.keyUp('command')
    pyautogui.typewrite("https://chat.openai.com/?model=gpt-4")
    time.sleep(1)
    pyautogui.press('enter')

    time.sleep(3) # wait for hte page to load

    # get to the img button
    pyautogui.press('tab')
    searchFile()
    selectFile(0)
    for i in range(1, num_imgs):
        pyautogui.press('enter')  # press upload img
        selectFile(i)

def searchFile():
    pyautogui.press('enter')  # press upload img
    time.sleep(1)
    pyautogui.keyDown('command')
    pyautogui.press('f')
    pyautogui.keyUp('command')
    time.sleep(1)
    filename = 'scrapepage'
    pyautogui.typewrite(filename)
    pyautogui.press('enter')
    pyautogui.press('tab') # move the selection to the img
    pyautogui.press('tab') # move the selection to the img

def selectFile(ith_file:str):
    time.sleep(1)

    # pyautogui.keyDown('command')
    # pyautogui.press('f')
    # pyautogui.keyUp('command')
    # time.sleep(1)
    # filename = 'scrapepage'+ str(ith_file) +'.jpg'
    # pyautogui.typewrite(filename, interval=0.2, _pause=True)
    
    # time.sleep(2)
    # pyautogui.press('enter')
    # pyautogui.press('tab') # move the selection to the img
    # pyautogui.press('tab') # move the selection to the img
    pyautogui.press('down', presses=ith_file + 1)
    pyautogui.press('enter')  # upload the img

def main():
    num_imgs = convert_pdf_to_imgs()
    upload_imgs_to_chatgpt(num_imgs)
    # time.sleep(1)
    # selectFile(1)
main()