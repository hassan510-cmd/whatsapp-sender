from selenium import webdriver
import time
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
import pandas
from pynput import mouse , keyboard
from pynput.keyboard import Key, Controller , Listener
import win32gui
import win32con

The_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(The_program_to_hide, win32con.SW_HIDE)
keyboards=keyboard.Controller()

ui, _ = loadUiType("D:/backup/Desktop/DeskFiles/python/main.ui")


def testData(path):
    data=pandas.read_csv(path)
    # print("data here :" , data)
    nums=data["PhoneNumber"]
    return nums

def table(text):
    s=[text]
    listOfMsg=s[0].split('\n')

    return listOfMsg

class mainApp(QMainWindow, ui):
    
    def __init__(self, parent=None ):
        super(mainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handelButtons()
        self.placholder()
        self.radio1.toggled.connect(lambda:self.placholder(self.radio1))
        self.radio2.toggled.connect(lambda:self.placholder(self.radio2))

    def saveBrowes(self):
        saveLocation = QFileDialog.getOpenFileName(
            self, caption="save as", directory=".", filter="all files(*.*)")
        self.saveLocation.setText(str(saveLocation[0]))
        self.phoneList.clear()
        list=testData(self.saveLocation.text())
        print(list)
        self.phoneList.addItems(["0"+str(i) for i in list])

    def handelButtons(self):
        self.sendbutton.clicked.connect(self.sendMSG)
        self.openlink.clicked.connect(self.openLink)
        self.browse.clicked.connect(self.saveBrowes)

    def sendMSG(self):
        count=0
        x=''
        site='https://web.WhatsApp.com/send?phone=+20'
        # same message for all numbers
        if self.radio1.isChecked() :
            msg=self.msgarea.toPlainText()
            for i in testData(self.saveLocation.text()) :
                url2=site+str(i)
                try :
                    web.get(url2)
                    time.sleep(6)
                    web.find_element_by_class_name("_3uMse").send_keys(msg)
                    time.sleep(3)
                    web.find_element_by_class_name("_1U1xa").click()
                    time.sleep(3)
                except Exception :
                    # count+=1
                    # print(i , count)
                    time.sleep(2)
                    keyboards.press(Key.enter)
          # each number has it's owen message
        elif self.radio2.isChecked():
            for i,j in zip(testData(self.saveLocation.text()),table(self.msgarea.toPlainText())) :
                url2=site+str(i)
                try :
                    web.get(url2)
                    time.sleep(6)
                    web.find_element_by_class_name("_3uMse").send_keys(msg)
                    time.sleep(1)
                    web.find_element_by_class_name("_1U1xa").click()
                    time.sleep(3)
                except Exception :
                    time.sleep(2)
                    keyboards.press(Key.enter)
            
    def openLink(self):
        global web
        web=webdriver.Chrome("D:/backup/Desktop/DeskFiles/python/chromedriver.exe")
        url=self.link.text()
        web.get(url)
    
    def placholder(self,*a):
        if self.radio2.isChecked():
            # self.msgarea.clear()
            self.msgarea.setPlaceholderText("Enter your messages separeted by 'ENTER'")
        if self.radio1.isChecked():
            self.msgarea.setPlaceholderText("Type your message")
    
def main():
    
    app = QApplication(sys.argv)
    window = mainApp()
    window.show()
    app.exec_()
    The_program_to_hide = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(The_program_to_hide, win32con.SW_HIDE)



if __name__ == "__main__":
    main()