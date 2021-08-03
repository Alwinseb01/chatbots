import selenium
import webbrowser
from selenium import webdriver
from time import sleep
import pyautogui
import pyperclip

pyautogui.FAILSAFE = False

#u_name = '...'
#u_pass = '...'



def WhataBot():
    options = webdriver.ChromeOptions()
    options.add_argument(r"user-data-dir=C:\Users\Alwin\Desktop\webbot")
    driver =webdriver.Chrome(executable_path=r'C:\Users\Alwin\Desktop\webbot\chromedriver.exe',options=options)
    driver.get('https://web.whatsapp.com/')
    pyperclip.copy('https://web.whatsapp.com/')
    pyautogui.hotkey('enter')
    sleep(15)
    pyperclip.copy(u_name)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]').click()
    pyautogui.hotkey('ctrl', 'v', interval=0.15)
    pyautogui.hotkey('enter')
    pyperclip.copy(u_pass)
    sleep(1)
    pyautogui.hotkey('ctrl', 'v', interval=0.15)
    sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]').click()
    pyautogui.hotkey('enter')

def whatsapp(contact,message):
    webbrowser.open('https://web.whatsapp.com')
    pyperclip.copy(contact)
    sleep(10)
    pyautogui.hotkey('tab')
    sleep(1)
    pyautogui.hotkey('ctrl', 'v', interval=0.15)
    sleep(1)
    pyautogui.hotkey('enter')
    pyperclip.copy(message)
    sleep(1)
    pyautogui.hotkey('ctrl', 'v', interval=0.15)
    #sleep(1)
    pyautogui.hotkey('enter')
    
def InstaBot():
    driver.get('https://www.instagram.com/')
    pyperclip.copy(u_name)
    sleep(2)
    driver.find_element_by_name('username').click()
    pyautogui.hotkey('ctrl', 'v', interval=0.15)
    pyperclip.copy(u_pass)
    driver.find_element_by_name('password').click()
    pyautogui.hotkey('ctrl', 'v', interval=0.15)
    driver.find_element_by_class_name('sqdOP.L3NKy.y3zKF').click()


'''
def cursorbot():
    sc_Width, sc_Height = pyautogui.size()  #gets the Screen Resolution
    #pyautogui.moveTo(1400,50)
    #sleep(1)
    #pyautogui.click('search.jpg')
    #pyautogui.click(1400,50)
    #pyautogui.press(['windows'])
    pyautogui.hotkey('win', 's', interval=0.15)
    sleep(1)
    pyperclip.copy('Google Chrome')
    pyautogui.hotkey('ctrl', 'v', interval=0.15)
    pyautogui.hotkey('enter')
    sleep(10)
    pyautogui.hotkey('enter')
    pyperclip.copy('https://web.whatsapp.com/')
    pyautogui.hotkey('ctrl', 'v', interval=0.15)
    pyautogui.hotkey('enter')
    sleep(25)
    pyperclip.copy(u_name)
    pyautogui.hotkey('tab')
    pyautogui.hotkey('ctrl', 'v', interval=0.15)0000
    hi
    
    pyautogui.hotkey('enter')
    pyperclip.copy(u_pass)
    sleep(1)
    pyautogui.hotkey('ctrl', 'v', interval=0.15)
    #sleep(1)
    pyautogui.hotkey('enter')

def buttons():
   # pyautogui.('win')
    pyautogui.hotkey('win')
    sleep(1)
    pyautogui.hotkey('tab')
    sleep(1)
    pyautogui.hotkey('down')
    sleep(1)
    pyautogui.hotkey('enter')
    sleep(1)
    pyautogui.hotkey('down')
    sleep(1)
    pyautogui.hotkey('enter')
    sleep(3)
    pyautogui.hotkey('enter')
    sleep(2)
    pyautogui.hotkey('2')
    sleep(1)
    pyautogui.hotkey('9')
    sleep(1)
    pyautogui.hotkey('0')
    sleep(1)
    pyautogui.hotkey('1')

def note():
    pyautogui.hotkey('win', 's', interval=0.15)
    sleep(1)
    pyperclip.copy('notepad')
    pyautogui.hotkey('ctrl', 'v', interval=0.15)
    pyautogui.hotkey('enter')
    sleep(10)
    pyautogui.hotkey('enter')
    pyautogui.hotkey('2')
    sleep(1)
    pyautogui.hotkey('9')
    sleep(1)
    pyautogui.hotkey('0')
    sleep(1)
    pyautogui.hotkey('1')
    pyautogui.hotkey('enter')

'''

def gui():
    query=pyautogui.prompt('enter query', title='input', default='query')
    if query=='':
        pyautogui.alert('invalid input',title='error')
        gui()
    if query is None:
        exit(1)
    elif query=='message':
        query1=pyautogui.prompt('enter contact name', title='input', default='contact')
        query2=pyautogui.prompt('enter message', title='input', default='message')
        opt=pyautogui.confirm('select your choice of platform', buttons=['whatsapp','instagram'],title='select platform')
        if opt=='whatsapp':
            whatsapp(query1,query2)
    #elif opt=='youtube':
     #   webbrowser.open('https://www.youtube.com/results?search_query='+query)
    else:
        exit(1)

#cursorbot()
#buttons()
#note()
gui()
#C:\Users\Alwin\Downloads\chromedriver_win32\chromedriver.exe
#https://github.com/techwithtim/Face-Recognition
