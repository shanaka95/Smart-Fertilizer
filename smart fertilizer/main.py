import sys

from PyQt4.QtGui import *
from PyQt4 import QtGui, uic

class MyWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('untitled.ui', self)
        self.show()
        self.comboBox.currentIndexChanged.connect(self.selectCrop)
        self.pushButton.clicked.connect(self.submit)
        self.pushButton_2.clicked.connect(self.resetfields)
        
        self.chilly={'u':{"Basal Dressing":0,'2':62.5,'4':62.5,'8':62.5,'12':62.5},'tsp':{"Basal Dressing":100},'mop':{"Basal Dressing":50,'8':50}}
        self.paddy4={'u':{"Basal Dressing":15,'3':20,'9':55,'6':20},'tsp':{"Basal Dressing":25},'mop':{"Basal Dressing":15}}
        self.paddy42={'u':{"Basal Dressing":15,'3':20,'10':55,'6':20},'tsp':{"Basal Dressing":25},'mop':{"Basal Dressing":15}}
        self.paddy3={'u':{"Basal Dressing":15,'3':20,'6':55},'tsp':{"Basal Dressing":25},'mop':{"Basal Dressing":15}}
        self.paddy32={'u':{"Basal Dressing":15,'3':20,'7':55},'tsp':{"Basal Dressing":25},'mop':{"Basal Dressing":15}}
        #self.label_14.setOpacity(50)



    def selectCrop(self):
        if str(self.comboBox.currentText())=='Paddy':
            self.comboBox_4.setEnabled(True)
        else:
            self.comboBox_4.setEnabled(False)
    def submit(self):
        if self.setUrea():
            if self.setTSP():
                if self.setMOP():
                    if self.setLand():
                        self.setDefault()
    def resetfields(self):
        self.lineEdit_14.setText('')
        self.lineEdit_15.setText('')
        self.lineEdit_16.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        self.lineEdit_4.setText('')
        self.lineEdit_8.setText('')
        self.lineEdit_9.setText('')
        self.lineEdit_21.setText('')
        self.lineEdit.setText('')
        self.lineEdit_18.setText('')
        self.lineEdit_19.setText('')
        self.lineEdit_20.setText('')

    def calcRequired(self):
        ur=float(self.lineEdit_14.text())-float(self.lineEdit.text())
        tsp=float(self.lineEdit_15.text())-float(self.lineEdit_2.text())
        mop=float(self.lineEdit_16.text())-float(self.lineEdit_3.text())
        size=float(self.lineEdit_4.text())
        
        if str(self.comboBox_2.currentText())=='Hectare':
            size=size*2.471
        elif str(self.comboBox_2.currentText())=='Sqr Mtr.':
            size=size*0.00024711
        print self.comboBox_2.currentText()
        self.lineEdit_18.setText(str(size*ur))
        self.lineEdit_19.setText(str(size*tsp))
        self.lineEdit_20.setText(str(size*mop))
    def setDefault(self):
        if str(self.comboBox.currentText())=='Paddy':
            if str(self.comboBox_4.currentText())=='3 Months':
                try:
                    self.lineEdit_14.setText(str(self.paddy3['u'][str(self.comboBox_3.currentText())]))
                except Exception as e:
                    self.lineEdit_14.setText('0')
                try:
                    self.lineEdit_15.setText(str(self.paddy3['tsp'][str(self.comboBox_3.currentText())]))
                except Exception as e:
                    
                    self.lineEdit_15.setText('0')
                try:
                    self.lineEdit_16.setText(str(self.paddy3['mop'][str(self.comboBox_3.currentText())]))
                except Exception as e:
                    self.lineEdit_16.setText('0')
            elif str(self.comboBox_4.currentText())=='3 1/2 Months':
                try:
                    self.lineEdit_14.setText(str(self.paddy32['u'][str(self.comboBox_3.currentText())]))
                except Exception as e:
                    self.lineEdit_14.setText('0')
                try:
                    self.lineEdit_15.setText(str(self.paddy32['tsp'][str(self.comboBox_3.currentText())]))
                except Exception as e:
                    
                    self.lineEdit_15.setText('0')
                try:
                    self.lineEdit_16.setText(str(self.paddy32['mop'][str(self.comboBox_3.currentText())]))
                except Exception as e:
                    self.lineEdit_16.setText('0')               
            elif str(self.comboBox_4.currentText())=='4 Months':
                try:
                    self.lineEdit_14.setText(str(self.paddy4['u'][str(self.comboBox_3.currentText())]))
                except Exception as e:
                    self.lineEdit_14.setText('0')
                try:
                    self.lineEdit_15.setText(str(self.paddy4['tsp'][str(self.comboBox_3.currentText())]))
                except Exception as e:
                    
                    self.lineEdit_15.setText('0')
                try:
                    self.lineEdit_16.setText(str(self.paddy4['mop'][str(self.comboBox_3.currentText())]))
                except Exception as e:
                    self.lineEdit_16.setText('0')                  
            elif str(self.comboBox_4.currentText())=='4 1/2 Months':
                try:
                    self.lineEdit_14.setText(str(self.paddy42['u'][str(self.comboBox_3.currentText())]))
                except Exception as e:
                    self.lineEdit_14.setText('0')
                try:
                    self.lineEdit_15.setText(str(self.paddy42['tsp'][str(self.comboBox_3.currentText())]))
                except Exception as e:
                    
                    self.lineEdit_15.setText('0')
                try:
                    self.lineEdit_16.setText(str(self.paddy42['mop'][str(self.comboBox_3.currentText())]))
                except Exception as e:
                    self.lineEdit_16.setText('0')                  
                
        elif str(self.comboBox.currentText())=='Chilly':
            try:
                self.lineEdit_14.setText(str(self.chilly['u'][str(self.comboBox_3.currentText())]))
            except Exception as e:
                self.lineEdit_14.setText('0')
            try:
                self.lineEdit_15.setText(str(self.chilly['tsp'][str(self.comboBox_3.currentText())]))
            except Exception as e:
                
                self.lineEdit_15.setText('0')
            try:
                self.lineEdit_16.setText(str(self.chilly['mop'][str(self.comboBox_3.currentText())]))
            except Exception as e:
                self.lineEdit_16.setText('0')
        self.calcRequired()
    def setUrea(self):
        inp=str(self.lineEdit.text())
        if inp=='' or inp==' ' or not inp.isdigit():
            QMessageBox.critical(self, "Input Error!", "Enter correct value for Urea.")
        else:
                               
            return True

    def setTSP(self):
        inp=str(self.lineEdit_2.text())
        if inp=='' or inp==' ' or not inp.isdigit():
            QMessageBox.critical(self, "Input Error!", "Enter correct value for TSP.")
        else:
            return True

    def setMOP(self):
        inp=str(self.lineEdit_3.text())
        if inp=='' or inp==' ' or not inp.isdigit():
            QMessageBox.critical(self, "Input Error!", "Enter correct value for MOP.")
        else:
            return True
            
    def setLand(self):
        inp=str(self.lineEdit_4.text())
        if inp=='' or inp==' ' or not inp.isdigit():
            QMessageBox.critical(self, "Input Error!", "Enter correct value for Land Size.")
        else:
            return True
            

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
