
# import module
from pdf2image import convert_from_path
import time
import pyautogui
import pyperclip  # handy cross-platform clipboard text handler
 

def convert_pdf_to_imgs(pdf_name):
    import os
    if os.path.exists('output'):
        os.system('rm -rf output')
        os.makedirs('output')
    # Store Pdf with convert_from_path function
    images = convert_from_path(pdf_name)
    
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
    # searchFile()
    # selectFile(0)
    for i in range(0, num_imgs):
        pyautogui.press('enter')  # press upload img
        selectFile(i)
    send_prompt()

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
    pyautogui.keyDown('command')
    pyautogui.press('f')
    pyautogui.keyUp('command')
    time.sleep(0.1)
    filename = 'scrapepage'+ str(ith_file) +'.jpg'
    pyautogui.keyUp('Fn') # so we don't press the emoji bar
    pyautogui.typewrite(filename)
    
    time.sleep(1)
    pyautogui.press('enter')
    pyautogui.press('tab') # move the selection to the img
    pyautogui.press('tab') # move the selection to the img
    pyautogui.press('down', presses=ith_file + 1)
    pyautogui.press('enter')  # upload the img
    time.sleep(1)

def send_prompt():
    pyautogui.keyDown('shiftleft')
    pyautogui.press('tab')
    pyautogui.keyUp('shiftleft')
    time.sleep(3) # so the iamges finish uploading
    pyautogui.keyUp('Fn') # so we don't press the emoji bar
    pyautogui.typewrite("extract the text from this pdf")
    pyautogui.press('enter')

def copy_text():
    pyautogui.keyDown('command')
    pyautogui.press('f')
    pyautogui.keyUp('command')
    time.sleep(0.1)
    pyautogui.keyUp('Fn') # so we don't press the emoji bar
    pyautogui.typewrite("copy code")
    pyautogui.press('enter')
    pyautogui.press('escape')
    pyautogui.press('enter')
    return pyperclip.paste()

def extract_text_from_pdf(pdf_name):
    num_imgs = convert_pdf_to_imgs(pdf_name)
    upload_imgs_to_chatgpt(num_imgs)

    # every 10 seconds, try to copy the text. if the text between the
    # last time we copied is the same as the current text copied, then
    # return the final copied text
    last_copied_text = ""
    while True:
        time.sleep(10)
        current_copied_text = copy_text()
        if current_copied_text == last_copied_text:
            break
        last_copied_text = current_copied_text
    return last_copied_text
# extract_text_from_pdf("ps3.pdf")