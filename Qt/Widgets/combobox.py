#!/usr/bin/python
# -*- coding: utf-8 -*-

# ZetCode PyQt4 tutorial
#
# In this example, we show how to 
# use the QComboBox widget.
# 
# author: Jan Bodnar
# website: zetcode.com
# last edited: December 2010


from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):
  
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()


    def initUI(self):

        self.label = QtGui.QLabel("Ubuntu", self)

        combo = QtGui.QComboBox(self)
        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem("Red Hat")
        combo.addItem("Gentoo")

        combo.move(50, 50)
        self.label.move(50, 150)

        self.connect(combo, QtCore.SIGNAL('activated(QString)'), 
            self.onActivated)

        self.setGeometry(250, 200, 350, 250)
        self.setWindowTitle('QComboBox')

    def onActivated(self, text):
      
        self.label.setText(text)
        self.label.adjustSize()


def main():
  
    app = QtGui.QApplication([])
    ex = Example()
    ex.show()
    app.exec_()    


if __name__ == '__main__':
    main()