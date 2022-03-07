import tkinter
import tkinter.messagebox
import threading
import subprocess
from selenium import webdriver

root = tkinter.Tk()
root.title('Session de travail - FSEG')
root.geometry("400x430")
logo = tkinter.PhotoImage(file = "/Users/Filippo/Desktop/LOGO-FSEG.png")

canvas = tkinter.Canvas(root, width = 410, height = 230, relief = 'raised', bg = 'white')
canvas.pack(fill = "both")

label = tkinter.Label(root, text = 'Combien de minutes souhaitez-vous travailler ?', relief = 'flat', bg = 'white')
label.config(font=('futura', 14))
canvas.create_window(200, 180, window=label)

entry = tkinter.Entry(root) 
canvas.create_window(200, 210, window=entry)

canvas.create_image(0, 0, image=logo, anchor = "nw")

###############################################################################

driverTP = []
driverEAII = []
driverEAIIP = []
driverEGC = []

###############################################################################

def TP():
    
    time = int(entry.get()) * 60
    start_time = threading.Timer(time,endTP)
    start_time.start()
    
    time2 = float(time) - 30
    start_time2 = threading.Timer(time2,endmsg)
    start_time2.start()
    
    subprocess.Popen(['open', '/Applications/RStudio.app'])
    subprocess.Popen(['open', '/Applications/Anaconda-Navigator.app'])
        
    global driverTP
    
    if not driverTP: 
       
        driverTP = webdriver.Chrome(executable_path = '/Users/Filippo/Desktop/FSEG/TP/chromedriver.exe')
        driverTP.get('https://master-ds2e.github.io/M1-Programming/')
        driverTP.execute_script("window.open('https://stackoverflow.com')") 
        driverTP.execute_script("window.open('https://www.ecosia.org')")
        driverTP.switch_to.window(driverTP.window_handles[0])
    
def endTP():
    
    subprocess.call(['osascript', '-e', 'tell application "RStudio" to quit'])
    subprocess.call(['osascript', '-e', 'tell application "Anaconda-Navigator" to quit'])
    
    global driverTP 
    
    if driverTP:
        driverTP.close()
        driverTP = []
    
    choice = tkinter.messagebox.askquestion(title  = "Fin de la session", message = "C'est l'heure de la pause ! Souhaitez-vous continuer ?")
    if choice == "yes" : TP()
    if choice == "no" : tkinter.messagebox.showinfo("Fin de la session", "A la prochaine !")
    
###############################################################################

def EAII():
    
    time = int(entry.get()) * 60
    start_time = threading.Timer(time,endEAII)
    start_time.start()
    
    time2 = float(time) - 30
    start_time2 = threading.Timer(time2,endmsg)
    start_time2.start()
    
    subprocess.Popen(['open', '/Applications/RStudio.app'])
    subprocess.Popen(['open', '/Users/Filippo/Desktop/FSEG/ECONOMETRIE APPLIQUEE I/EAII - FICHE TECHNIQUE.pages'])
        
    global driverEAII
    
    if not driverEAII: 
       
        driverEAII = webdriver.Chrome(executable_path = '/Users/Filippo/Desktop/FSEG/TP/chromedriver.exe')
        driverEAII.get('https://ernest.unistra.fr')
        driverEAII.execute_script("window.open('https://bu.unistra.fr')") 
        driverEAII.execute_script("window.open('https://www.ecosia.org')")
        driverEAII.switch_to.window(driverEAII.window_handles[0])
    
def endEAII():
    
    subprocess.call(['osascript', '-e', 'tell application "RStudio" to quit'])
    subprocess.call(['osascript', '-e', 'tell application "Pages" to quit'])
    
    global driverEAII 
    
    if driverEAII:
        driverEAII.close()
        driverEAII = []
    
    choice = tkinter.messagebox.askquestion(title  = "Fin de la session", message = "C'est l'heure de la pause ! Souhaitez-vous continuer ?")
    if choice == "yes" : EAII()
    if choice == "no" : tkinter.messagebox.showinfo("Fin de la session", "A la prochaine !")
    
###############################################################################

def EAIIP():
    
    time = int(entry.get()) * 60
    start_time = threading.Timer(time,endEAIIP)
    start_time.start()
    
    time2 = float(time) - 30
    start_time2 = threading.Timer(time2,endmsg)
    start_time2.start()
    
    subprocess.Popen(['open', '/Applications/RStudio.app'])
    subprocess.Popen(['open', '/Users/Filippo/Desktop/FSEG/ECONOMETRIE APPLIQUEE I/EAIIP - FICHE TECHNIQUE.pages'])
        
    global driverEAIIP
    
    if not driverEAIIP: 
       
        driverEAIIP = webdriver.Chrome(executable_path = '/Users/Filippo/Desktop/FSEG/TP/chromedriver.exe')
        driverEAIIP.get('https://ernest.unistra.fr')
        driverEAIIP.execute_script("window.open('https://bu.unistra.fr')") 
        driverEAIIP.execute_script("window.open('https://www.ecosia.org')")
        driverEAIIP.switch_to.window(driverEAII.window_handles[0])
    
def endEAIIP():
    
    subprocess.call(['osascript', '-e', 'tell application "RStudio" to quit'])
    subprocess.call(['osascript', '-e', 'tell application "Pages" to quit'])
    
    global driverEAIIP
    
    if driverEAIIP:
        driverEAIIP.close()
        driverEAIIP = []
    
    choice = tkinter.messagebox.askquestion(title  = "Fin de la session", message = "C'est l'heure de la pause ! Souhaitez-vous continuer ?")
    if choice == "yes" : EAIIP()
    if choice == "no" : tkinter.messagebox.showinfo("Fin de la session", "A la prochaine !")
    
###############################################################################

def EGC():
    
    time = int(entry.get()) * 60
    start_time = threading.Timer(time,endEGC)
    start_time.start()
    
    time2 = float(time) - 30
    start_time2 = threading.Timer(time2,endmsg)
    start_time2.start()
    
    subprocess.Popen(['open', '/Users/Filippo/Desktop/FSEG/EGC/PROJETS - EGC - MANDAT 21-22-3.numbers'])
    
    global driverEGC
    
    if not driverEGC: 
       
        driverEGC = webdriver.Chrome(executable_path = '/Users/Filippo/Desktop/FSEG/TP/chromedriver.exe')
        driverEGC.get('https://docs.google.com/spreadsheets/d/1085rGitkNpYCkH084R1oIvfM7ASbqYgtZHA5egexyHw/edit?usp=sharing')
        
def endEGC():
    
    subprocess.call(['osascript', '-e', 'tell application "Keynote" to quit'])
    
    global driverEGC
    
    if driverEGC:
        driverEGC.close()
        driverEGC = []
    
    choice = tkinter.messagebox.askquestion(title  = "Fin de la session", message = "C'est l'heure de la pause ! Souhaitez-vous continuer ?")
    if choice == "yes" : EGC()
    if choice == "no" : tkinter.messagebox.showinfo("Fin de la session", "A la prochaine !")
    
###############################################################################
    
def endmsg():
    tkinter.messagebox.showinfo("La session se termine", "Il reste 30s avant la fin de la session, courage !")
    
###############################################################################

ButtonTP = tkinter.Button(root, text='Techniques de Programmation', command=TP, pady=10)
ButtonEAII = tkinter.Button(root, text='Econométrie Appliquée II', command=EAII, pady=10)
ButtonEAIIP = tkinter.Button(root, text='Econométrie Appliquée II - Panel', command=EAIIP, pady=10)
ButtonEGC = tkinter.Button(root, text='Eco-Gestion Conseil', command=EGC, pady=10)

###############################################################################

ButtonTP.pack()
ButtonEAII.pack()
ButtonEAIIP.pack()
ButtonEGC.pack()

###############################################################################

root.lift()
root.attributes('-topmost',True)
root.after_idle(root.attributes,'-topmost',False)

###############################################################################

root.mainloop()