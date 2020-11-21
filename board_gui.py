# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'board_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Mensch(object):
    def setupUi(self, Mensch):
        Mensch.setObjectName("Mensch")
        Mensch.setEnabled(True)
        Mensch.resize(900, 743)
        Mensch.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Mensch)
        self.centralwidget.setObjectName("centralwidget")
        self.pieces_board = QtWidgets.QWidget(self.centralwidget)
        self.pieces_board.setGeometry(QtCore.QRect(219, 0, 671, 701))
        self.pieces_board.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid gray;\n"
"border-radius: 12px;")
        self.pieces_board.setObjectName("pieces_board")
        self.label9 = QtWidgets.QLabel(self.pieces_board)
        self.label9.setGeometry(QtCore.QRect(10, 400, 50, 50))
        self.label9.setToolTipDuration(-3)
        self.label9.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label9.setText("")
        self.label9.setObjectName("label9")
        self.label11 = QtWidgets.QLabel(self.pieces_board)
        self.label11.setGeometry(QtCore.QRect(10, 280, 50, 50))
        self.label11.setToolTipDuration(-3)
        self.label11.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label11.setText("")
        self.label11.setObjectName("label11")
        self.label10 = QtWidgets.QLabel(self.pieces_board)
        self.label10.setGeometry(QtCore.QRect(10, 340, 50, 50))
        self.label10.setToolTipDuration(-3)
        self.label10.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label10.setText("")
        self.label10.setObjectName("label10")
        self.label30 = QtWidgets.QLabel(self.pieces_board)
        self.label30.setGeometry(QtCore.QRect(610, 340, 50, 50))
        self.label30.setToolTipDuration(-3)
        self.label30.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label30.setText("")
        self.label30.setObjectName("label30")
        self.label29 = QtWidgets.QLabel(self.pieces_board)
        self.label29.setGeometry(QtCore.QRect(610, 280, 50, 50))
        self.label29.setToolTipDuration(-3)
        self.label29.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label29.setText("")
        self.label29.setObjectName("label29")
        self.label31 = QtWidgets.QLabel(self.pieces_board)
        self.label31.setGeometry(QtCore.QRect(610, 400, 50, 50))
        self.label31.setToolTipDuration(-3)
        self.label31.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label31.setText("")
        self.label31.setObjectName("label31")
        self.label40 = QtWidgets.QLabel(self.pieces_board)
        self.label40.setGeometry(QtCore.QRect(310, 640, 50, 50))
        self.label40.setToolTipDuration(-3)
        self.label40.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label40.setText("")
        self.label40.setObjectName("label40")
        self.label1 = QtWidgets.QLabel(self.pieces_board)
        self.label1.setGeometry(QtCore.QRect(250, 640, 50, 50))
        self.label1.setToolTipDuration(-3)
        self.label1.setStyleSheet("background-color: rgb(2, 133, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label1.setText("")
        self.label1.setObjectName("label1")
        self.label39 = QtWidgets.QLabel(self.pieces_board)
        self.label39.setGeometry(QtCore.QRect(370, 640, 50, 50))
        self.label39.setToolTipDuration(-3)
        self.label39.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label39.setText("")
        self.label39.setObjectName("label39")
        self.label4 = QtWidgets.QLabel(self.pieces_board)
        self.label4.setGeometry(QtCore.QRect(250, 460, 50, 50))
        self.label4.setToolTipDuration(-3)
        self.label4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label4.setText("")
        self.label4.setObjectName("label4")
        self.label2 = QtWidgets.QLabel(self.pieces_board)
        self.label2.setGeometry(QtCore.QRect(250, 580, 50, 50))
        self.label2.setToolTipDuration(-3)
        self.label2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label2.setText("")
        self.label2.setScaledContents(True)
        self.label2.setObjectName("label2")
        self.label6 = QtWidgets.QLabel(self.pieces_board)
        self.label6.setGeometry(QtCore.QRect(190, 400, 50, 50))
        self.label6.setToolTipDuration(-3)
        self.label6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label6.setText("")
        self.label6.setObjectName("label6")
        self.label5 = QtWidgets.QLabel(self.pieces_board)
        self.label5.setGeometry(QtCore.QRect(250, 400, 50, 50))
        self.label5.setToolTipDuration(-3)
        self.label5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label5.setText("")
        self.label5.setObjectName("label5")
        self.label8 = QtWidgets.QLabel(self.pieces_board)
        self.label8.setGeometry(QtCore.QRect(70, 400, 50, 50))
        self.label8.setToolTipDuration(-3)
        self.label8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label8.setText("")
        self.label8.setObjectName("label8")
        self.label7 = QtWidgets.QLabel(self.pieces_board)
        self.label7.setGeometry(QtCore.QRect(130, 400, 50, 50))
        self.label7.setToolTipDuration(-3)
        self.label7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label7.setText("")
        self.label7.setObjectName("label7")
        self.label14 = QtWidgets.QLabel(self.pieces_board)
        self.label14.setGeometry(QtCore.QRect(190, 280, 50, 50))
        self.label14.setToolTipDuration(-3)
        self.label14.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label14.setText("")
        self.label14.setObjectName("label14")
        self.label13 = QtWidgets.QLabel(self.pieces_board)
        self.label13.setGeometry(QtCore.QRect(130, 280, 50, 50))
        self.label13.setToolTipDuration(-3)
        self.label13.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label13.setText("")
        self.label13.setObjectName("label13")
        self.label12 = QtWidgets.QLabel(self.pieces_board)
        self.label12.setGeometry(QtCore.QRect(70, 280, 50, 50))
        self.label12.setToolTipDuration(-3)
        self.label12.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label12.setText("")
        self.label12.setObjectName("label12")
        self.label16 = QtWidgets.QLabel(self.pieces_board)
        self.label16.setGeometry(QtCore.QRect(250, 220, 50, 50))
        self.label16.setToolTipDuration(-3)
        self.label16.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label16.setText("")
        self.label16.setObjectName("label16")
        self.label18 = QtWidgets.QLabel(self.pieces_board)
        self.label18.setGeometry(QtCore.QRect(250, 100, 50, 50))
        self.label18.setToolTipDuration(-3)
        self.label18.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label18.setText("")
        self.label18.setObjectName("label18")
        self.label17 = QtWidgets.QLabel(self.pieces_board)
        self.label17.setGeometry(QtCore.QRect(250, 160, 50, 50))
        self.label17.setToolTipDuration(-3)
        self.label17.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label17.setText("")
        self.label17.setObjectName("label17")
        self.label20 = QtWidgets.QLabel(self.pieces_board)
        self.label20.setGeometry(QtCore.QRect(310, 40, 50, 50))
        self.label20.setToolTipDuration(-3)
        self.label20.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label20.setText("")
        self.label20.setObjectName("label20")
        self.label21 = QtWidgets.QLabel(self.pieces_board)
        self.label21.setGeometry(QtCore.QRect(370, 40, 50, 50))
        self.label21.setToolTipDuration(-3)
        self.label21.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label21.setText("")
        self.label21.setObjectName("label21")
        self.label19 = QtWidgets.QLabel(self.pieces_board)
        self.label19.setGeometry(QtCore.QRect(250, 40, 50, 50))
        self.label19.setToolTipDuration(-3)
        self.label19.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label19.setText("")
        self.label19.setObjectName("label19")
        self.label22 = QtWidgets.QLabel(self.pieces_board)
        self.label22.setGeometry(QtCore.QRect(370, 100, 50, 50))
        self.label22.setToolTipDuration(-3)
        self.label22.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label22.setText("")
        self.label22.setObjectName("label22")
        self.label24 = QtWidgets.QLabel(self.pieces_board)
        self.label24.setGeometry(QtCore.QRect(370, 220, 50, 50))
        self.label24.setToolTipDuration(-3)
        self.label24.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label24.setText("")
        self.label24.setObjectName("label24")
        self.label23 = QtWidgets.QLabel(self.pieces_board)
        self.label23.setGeometry(QtCore.QRect(370, 160, 50, 50))
        self.label23.setToolTipDuration(-3)
        self.label23.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label23.setText("")
        self.label23.setObjectName("label23")
        self.label28 = QtWidgets.QLabel(self.pieces_board)
        self.label28.setGeometry(QtCore.QRect(550, 280, 50, 50))
        self.label28.setToolTipDuration(-3)
        self.label28.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label28.setText("")
        self.label28.setObjectName("label28")
        self.label26 = QtWidgets.QLabel(self.pieces_board)
        self.label26.setGeometry(QtCore.QRect(430, 280, 50, 50))
        self.label26.setToolTipDuration(-3)
        self.label26.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label26.setText("")
        self.label26.setObjectName("label26")
        self.label27 = QtWidgets.QLabel(self.pieces_board)
        self.label27.setGeometry(QtCore.QRect(490, 280, 50, 50))
        self.label27.setToolTipDuration(-3)
        self.label27.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label27.setText("")
        self.label27.setObjectName("label27")
        self.label33 = QtWidgets.QLabel(self.pieces_board)
        self.label33.setGeometry(QtCore.QRect(490, 400, 50, 51))
        self.label33.setToolTipDuration(-3)
        self.label33.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label33.setText("")
        self.label33.setObjectName("label33")
        self.label34 = QtWidgets.QLabel(self.pieces_board)
        self.label34.setGeometry(QtCore.QRect(430, 400, 50, 50))
        self.label34.setToolTipDuration(-3)
        self.label34.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label34.setText("")
        self.label34.setObjectName("label34")
        self.label35 = QtWidgets.QLabel(self.pieces_board)
        self.label35.setGeometry(QtCore.QRect(370, 400, 50, 50))
        self.label35.setToolTipDuration(-3)
        self.label35.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label35.setText("")
        self.label35.setObjectName("label35")
        self.label32 = QtWidgets.QLabel(self.pieces_board)
        self.label32.setGeometry(QtCore.QRect(550, 400, 50, 50))
        self.label32.setToolTipDuration(-3)
        self.label32.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label32.setText("")
        self.label32.setObjectName("label32")
        self.label36 = QtWidgets.QLabel(self.pieces_board)
        self.label36.setGeometry(QtCore.QRect(370, 460, 50, 50))
        self.label36.setToolTipDuration(-3)
        self.label36.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label36.setText("")
        self.label36.setObjectName("label36")
        self.label38 = QtWidgets.QLabel(self.pieces_board)
        self.label38.setGeometry(QtCore.QRect(370, 580, 50, 50))
        self.label38.setToolTipDuration(-3)
        self.label38.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label38.setText("")
        self.label38.setObjectName("label38")
        self.label25 = QtWidgets.QLabel(self.pieces_board)
        self.label25.setGeometry(QtCore.QRect(370, 280, 50, 50))
        self.label25.setToolTipDuration(-3)
        self.label25.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label25.setText("")
        self.label25.setObjectName("label25")
        self.label15 = QtWidgets.QLabel(self.pieces_board)
        self.label15.setGeometry(QtCore.QRect(250, 280, 50, 50))
        self.label15.setToolTipDuration(-3)
        self.label15.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label15.setText("")
        self.label15.setObjectName("label15")
        self.label3 = QtWidgets.QLabel(self.pieces_board)
        self.label3.setGeometry(QtCore.QRect(250, 520, 50, 50))
        self.label3.setToolTipDuration(-3)
        self.label3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label3.setText("")
        self.label3.setObjectName("label3")
        self.label37 = QtWidgets.QLabel(self.pieces_board)
        self.label37.setGeometry(QtCore.QRect(370, 520, 50, 50))
        self.label37.setToolTipDuration(-3)
        self.label37.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.label37.setText("")
        self.label37.setObjectName("label37")
        self.blue_win_1 = QtWidgets.QLabel(self.pieces_board)
        self.blue_win_1.setGeometry(QtCore.QRect(310, 580, 50, 50))
        self.blue_win_1.setToolTipDuration(-3)
        self.blue_win_1.setStyleSheet("background-color: rgb(2, 133, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.blue_win_1.setText("")
        self.blue_win_1.setObjectName("blue_win_1")
        self.yellow_win_1 = QtWidgets.QLabel(self.pieces_board)
        self.yellow_win_1.setGeometry(QtCore.QRect(550, 340, 50, 50))
        self.yellow_win_1.setToolTipDuration(-3)
        self.yellow_win_1.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.yellow_win_1.setText("")
        self.yellow_win_1.setObjectName("yellow_win_1")
        self.green_win_1 = QtWidgets.QLabel(self.pieces_board)
        self.green_win_1.setGeometry(QtCore.QRect(310, 100, 50, 50))
        self.green_win_1.setToolTipDuration(-3)
        self.green_win_1.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.green_win_1.setText("")
        self.green_win_1.setObjectName("green_win_1")
        self.red_win_1 = QtWidgets.QLabel(self.pieces_board)
        self.red_win_1.setGeometry(QtCore.QRect(70, 340, 50, 50))
        self.red_win_1.setToolTipDuration(-3)
        self.red_win_1.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.red_win_1.setText("")
        self.red_win_1.setObjectName("red_win_1")
        self.blue_win_2 = QtWidgets.QLabel(self.pieces_board)
        self.blue_win_2.setGeometry(QtCore.QRect(310, 520, 50, 50))
        self.blue_win_2.setToolTipDuration(-3)
        self.blue_win_2.setStyleSheet("background-color: rgb(2, 133, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.blue_win_2.setText("")
        self.blue_win_2.setObjectName("blue_win_2")
        self.blue_win_3 = QtWidgets.QLabel(self.pieces_board)
        self.blue_win_3.setGeometry(QtCore.QRect(310, 460, 50, 50))
        self.blue_win_3.setToolTipDuration(-3)
        self.blue_win_3.setStyleSheet("background-color: rgb(2, 133, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.blue_win_3.setText("")
        self.blue_win_3.setObjectName("blue_win_3")
        self.blue_win_4 = QtWidgets.QLabel(self.pieces_board)
        self.blue_win_4.setGeometry(QtCore.QRect(310, 400, 50, 50))
        self.blue_win_4.setToolTipDuration(-3)
        self.blue_win_4.setStyleSheet("background-color: rgb(2, 133, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.blue_win_4.setText("")
        self.blue_win_4.setObjectName("blue_win_4")
        self.yellow_win_2 = QtWidgets.QLabel(self.pieces_board)
        self.yellow_win_2.setGeometry(QtCore.QRect(490, 340, 50, 50))
        self.yellow_win_2.setToolTipDuration(-3)
        self.yellow_win_2.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.yellow_win_2.setText("")
        self.yellow_win_2.setObjectName("yellow_win_2")
        self.yellow_win_3 = QtWidgets.QLabel(self.pieces_board)
        self.yellow_win_3.setGeometry(QtCore.QRect(430, 340, 50, 50))
        self.yellow_win_3.setToolTipDuration(-3)
        self.yellow_win_3.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.yellow_win_3.setText("")
        self.yellow_win_3.setObjectName("yellow_win_3")
        self.yellow_win_4 = QtWidgets.QLabel(self.pieces_board)
        self.yellow_win_4.setGeometry(QtCore.QRect(370, 340, 50, 50))
        self.yellow_win_4.setToolTipDuration(-3)
        self.yellow_win_4.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.yellow_win_4.setText("")
        self.yellow_win_4.setObjectName("yellow_win_4")
        self.green_win_2 = QtWidgets.QLabel(self.pieces_board)
        self.green_win_2.setGeometry(QtCore.QRect(310, 160, 50, 50))
        self.green_win_2.setToolTipDuration(-3)
        self.green_win_2.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.green_win_2.setText("")
        self.green_win_2.setObjectName("green_win_2")
        self.green_win_3 = QtWidgets.QLabel(self.pieces_board)
        self.green_win_3.setGeometry(QtCore.QRect(310, 220, 50, 50))
        self.green_win_3.setToolTipDuration(-3)
        self.green_win_3.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.green_win_3.setText("")
        self.green_win_3.setObjectName("green_win_3")
        self.green_win_4 = QtWidgets.QLabel(self.pieces_board)
        self.green_win_4.setGeometry(QtCore.QRect(310, 280, 50, 50))
        self.green_win_4.setToolTipDuration(-3)
        self.green_win_4.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.green_win_4.setText("")
        self.green_win_4.setObjectName("green_win_4")
        self.red_win_2 = QtWidgets.QLabel(self.pieces_board)
        self.red_win_2.setGeometry(QtCore.QRect(130, 340, 50, 50))
        self.red_win_2.setToolTipDuration(-3)
        self.red_win_2.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.red_win_2.setText("")
        self.red_win_2.setObjectName("red_win_2")
        self.red_win_3 = QtWidgets.QLabel(self.pieces_board)
        self.red_win_3.setGeometry(QtCore.QRect(190, 340, 50, 50))
        self.red_win_3.setToolTipDuration(-3)
        self.red_win_3.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.red_win_3.setText("")
        self.red_win_3.setObjectName("red_win_3")
        self.red_win_4 = QtWidgets.QLabel(self.pieces_board)
        self.red_win_4.setGeometry(QtCore.QRect(250, 340, 50, 50))
        self.red_win_4.setToolTipDuration(-3)
        self.red_win_4.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.red_win_4.setText("")
        self.red_win_4.setObjectName("red_win_4")
        self.blue_home_2 = QtWidgets.QLabel(self.pieces_board)
        self.blue_home_2.setGeometry(QtCore.QRect(70, 580, 50, 50))
        self.blue_home_2.setToolTipDuration(-3)
        self.blue_home_2.setStyleSheet("background-color: rgb(2, 133, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.blue_home_2.setText("")
        self.blue_home_2.setObjectName("blue_home_2")
        self.blue_home_1 = QtWidgets.QLabel(self.pieces_board)
        self.blue_home_1.setGeometry(QtCore.QRect(10, 580, 50, 50))
        self.blue_home_1.setToolTipDuration(-3)
        self.blue_home_1.setStyleSheet("background-color: rgb(2, 133, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.blue_home_1.setText("")
        self.blue_home_1.setObjectName("blue_home_1")
        self.blue_home_3 = QtWidgets.QLabel(self.pieces_board)
        self.blue_home_3.setGeometry(QtCore.QRect(70, 640, 50, 50))
        self.blue_home_3.setToolTipDuration(-3)
        self.blue_home_3.setStyleSheet("background-color: rgb(2, 133, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.blue_home_3.setText("")
        self.blue_home_3.setObjectName("blue_home_3")
        self.blue_home_4 = QtWidgets.QLabel(self.pieces_board)
        self.blue_home_4.setGeometry(QtCore.QRect(10, 640, 50, 50))
        self.blue_home_4.setToolTipDuration(-3)
        self.blue_home_4.setStyleSheet("background-color: rgb(2, 133, 255);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.blue_home_4.setText("")
        self.blue_home_4.setObjectName("blue_home_4")
        self.yellow_home_4 = QtWidgets.QLabel(self.pieces_board)
        self.yellow_home_4.setGeometry(QtCore.QRect(550, 640, 50, 50))
        self.yellow_home_4.setToolTipDuration(-3)
        self.yellow_home_4.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.yellow_home_4.setText("")
        self.yellow_home_4.setObjectName("yellow_home_4")
        self.yellow_home_3 = QtWidgets.QLabel(self.pieces_board)
        self.yellow_home_3.setGeometry(QtCore.QRect(610, 640, 50, 50))
        self.yellow_home_3.setToolTipDuration(-3)
        self.yellow_home_3.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.yellow_home_3.setText("")
        self.yellow_home_3.setObjectName("yellow_home_3")
        self.yellow_home_1 = QtWidgets.QLabel(self.pieces_board)
        self.yellow_home_1.setGeometry(QtCore.QRect(550, 580, 50, 50))
        self.yellow_home_1.setToolTipDuration(-3)
        self.yellow_home_1.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.yellow_home_1.setText("")
        self.yellow_home_1.setObjectName("yellow_home_1")
        self.yellow_home_2 = QtWidgets.QLabel(self.pieces_board)
        self.yellow_home_2.setGeometry(QtCore.QRect(610, 580, 50, 50))
        self.yellow_home_2.setToolTipDuration(-3)
        self.yellow_home_2.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.yellow_home_2.setText("")
        self.yellow_home_2.setObjectName("yellow_home_2")
        self.green_home_1 = QtWidgets.QLabel(self.pieces_board)
        self.green_home_1.setGeometry(QtCore.QRect(550, 40, 50, 50))
        self.green_home_1.setToolTipDuration(-3)
        self.green_home_1.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.green_home_1.setText("")
        self.green_home_1.setObjectName("green_home_1")
        self.green_home_3 = QtWidgets.QLabel(self.pieces_board)
        self.green_home_3.setGeometry(QtCore.QRect(610, 100, 50, 50))
        self.green_home_3.setToolTipDuration(-3)
        self.green_home_3.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.green_home_3.setText("")
        self.green_home_3.setObjectName("green_home_3")
        self.green_home_2 = QtWidgets.QLabel(self.pieces_board)
        self.green_home_2.setGeometry(QtCore.QRect(610, 40, 50, 50))
        self.green_home_2.setToolTipDuration(-3)
        self.green_home_2.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.green_home_2.setText("")
        self.green_home_2.setObjectName("green_home_2")
        self.green_home_4 = QtWidgets.QLabel(self.pieces_board)
        self.green_home_4.setGeometry(QtCore.QRect(550, 100, 50, 50))
        self.green_home_4.setToolTipDuration(-3)
        self.green_home_4.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.green_home_4.setText("")
        self.green_home_4.setObjectName("green_home_4")
        self.red_home_1 = QtWidgets.QLabel(self.pieces_board)
        self.red_home_1.setGeometry(QtCore.QRect(10, 40, 50, 50))
        self.red_home_1.setToolTipDuration(-3)
        self.red_home_1.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.red_home_1.setText("")
        self.red_home_1.setObjectName("red_home_1")
        self.red_home_2 = QtWidgets.QLabel(self.pieces_board)
        self.red_home_2.setGeometry(QtCore.QRect(70, 40, 50, 50))
        self.red_home_2.setToolTipDuration(-3)
        self.red_home_2.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.red_home_2.setText("")
        self.red_home_2.setObjectName("red_home_2")
        self.red_home_3 = QtWidgets.QLabel(self.pieces_board)
        self.red_home_3.setGeometry(QtCore.QRect(70, 100, 50, 50))
        self.red_home_3.setToolTipDuration(-3)
        self.red_home_3.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.red_home_3.setText("")
        self.red_home_3.setObjectName("red_home_3")
        self.red_home_4 = QtWidgets.QLabel(self.pieces_board)
        self.red_home_4.setGeometry(QtCore.QRect(10, 100, 50, 50))
        self.red_home_4.setToolTipDuration(-3)
        self.red_home_4.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border: 2px solid black;\n"
"border-radius:25px;")
        self.red_home_4.setText("")
        self.red_home_4.setObjectName("red_home_4")
        self.red_win_1.raise_()
        self.green_win_1.raise_()
        self.yellow_win_1.raise_()
        self.blue_win_1.raise_()
        self.label40.raise_()
        self.label39.raise_()
        self.label38.raise_()
        self.label37.raise_()
        self.label36.raise_()
        self.label35.raise_()
        self.label34.raise_()
        self.label33.raise_()
        self.label32.raise_()
        self.label31.raise_()
        self.label30.raise_()
        self.label29.raise_()
        self.label28.raise_()
        self.label27.raise_()
        self.label26.raise_()
        self.label25.raise_()
        self.label24.raise_()
        self.label23.raise_()
        self.label22.raise_()
        self.label21.raise_()
        self.label20.raise_()
        self.label19.raise_()
        self.label18.raise_()
        self.label17.raise_()
        self.label16.raise_()
        self.label15.raise_()
        self.label14.raise_()
        self.label13.raise_()
        self.label12.raise_()
        self.label11.raise_()
        self.label10.raise_()
        self.label9.raise_()
        self.label8.raise_()
        self.label7.raise_()
        self.label6.raise_()
        self.label5.raise_()
        self.label4.raise_()
        self.label3.raise_()
        self.label2.raise_()
        self.label1.raise_()
        self.blue_win_2.raise_()
        self.blue_win_3.raise_()
        self.blue_win_4.raise_()
        self.yellow_win_2.raise_()
        self.yellow_win_3.raise_()
        self.yellow_win_4.raise_()
        self.green_win_2.raise_()
        self.green_win_3.raise_()
        self.green_win_4.raise_()
        self.red_win_2.raise_()
        self.red_win_3.raise_()
        self.red_win_4.raise_()
        self.blue_home_2.raise_()
        self.blue_home_1.raise_()
        self.blue_home_3.raise_()
        self.blue_home_4.raise_()
        self.yellow_home_4.raise_()
        self.yellow_home_3.raise_()
        self.yellow_home_1.raise_()
        self.yellow_home_2.raise_()
        self.green_home_1.raise_()
        self.green_home_3.raise_()
        self.green_home_2.raise_()
        self.green_home_4.raise_()
        self.red_home_1.raise_()
        self.red_home_2.raise_()
        self.red_home_3.raise_()
        self.red_home_4.raise_()
        self.players_board = QtWidgets.QWidget(self.centralwidget)
        self.players_board.setGeometry(QtCore.QRect(10, 0, 201, 371))
        self.players_board.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid gray;\n"
"border-radius:12px;")
        self.players_board.setObjectName("players_board")
        self.players = QtWidgets.QLabel(self.players_board)
        self.players.setGeometry(QtCore.QRect(10, 10, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(33)
        font.setBold(True)
        font.setWeight(75)
        self.players.setFont(font)
        self.players.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.players.setStyleSheet("border-color: rgb(255, 255, 255, 0);")
        self.players.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.players.setObjectName("players")
        self.player_1 = QtWidgets.QLabel(self.players_board)
        self.player_1.setGeometry(QtCore.QRect(12, 90, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.player_1.setFont(font)
        self.player_1.setStyleSheet("border-color: rgb(255, 255, 255, 0);\n"
"background-color: rgb(255, 255, 255, 0);")
        self.player_1.setText("")
        self.player_1.setObjectName("player_1")
        self.player_2 = QtWidgets.QLabel(self.players_board)
        self.player_2.setGeometry(QtCore.QRect(10, 160, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.player_2.setFont(font)
        self.player_2.setStyleSheet("border-color: rgb(255, 255, 255, 0);\n"
"background-color: rgb(255, 255, 255, 0);")
        self.player_2.setText("")
        self.player_2.setObjectName("player_2")
        self.player_3 = QtWidgets.QLabel(self.players_board)
        self.player_3.setGeometry(QtCore.QRect(10, 230, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.player_3.setFont(font)
        self.player_3.setStyleSheet("border-color: rgb(255, 255, 255, 0);\n"
"background-color: rgb(255, 255, 255, 0);")
        self.player_3.setText("")
        self.player_3.setObjectName("player_3")
        self.player_4 = QtWidgets.QLabel(self.players_board)
        self.player_4.setGeometry(QtCore.QRect(10, 300, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.player_4.setFont(font)
        self.player_4.setStyleSheet("border-color: rgb(255, 255, 255, 0);\n"
"background-color: rgb(255, 255, 255, 0);")
        self.player_4.setText("")
        self.player_4.setObjectName("player_4")
        self.dice_board = QtWidgets.QWidget(self.centralwidget)
        self.dice_board.setGeometry(QtCore.QRect(10, 380, 201, 321))
        self.dice_board.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid gray;\n"
"border-radius: 12px;")
        self.dice_board.setObjectName("dice_board")
        self.Roll_Button = QtWidgets.QPushButton(self.dice_board)
        self.Roll_Button.setGeometry(QtCore.QRect(20, 200, 161, 101))
        self.Roll_Button.setStyleSheet("border-color: rgb(255, 255, 255, 0);")
        self.Roll_Button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icons/six.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Roll_Button.setIcon(icon)
        self.Roll_Button.setIconSize(QtCore.QSize(100, 100))
        self.Roll_Button.setObjectName("Roll_Button")
        self.klick_on_dice = QtWidgets.QLabel(self.dice_board)
        self.klick_on_dice.setGeometry(QtCore.QRect(10, 150, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.klick_on_dice.setFont(font)
        self.klick_on_dice.setStyleSheet("border-color: rgb(255, 255, 255, 0);")
        self.klick_on_dice.setObjectName("klick_on_dice")
        self.turn = QtWidgets.QLabel(self.dice_board)
        self.turn.setGeometry(QtCore.QRect(30, 10, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(29)
        self.turn.setFont(font)
        self.turn.setStyleSheet("border-color: rgb(255, 255, 255, 0);\nbackground-color: rgb(255, 255, 255, 0);")
        self.turn.setObjectName("turn")
        self.player_turn = QtWidgets.QLabel(self.dice_board)
        self.player_turn.setGeometry(QtCore.QRect(10, 70, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.player_turn.setFont(font)
        self.player_turn.setStyleSheet("border-color: rgb(255, 255, 255, 0);\nbackground-color: rgb(255, 255, 255, 0);")
        self.player_turn.setText("")
        self.player_turn.setObjectName("player_turn")
        Mensch.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Mensch)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName("menubar")
        self.menuGAME = QtWidgets.QMenu(self.menubar)
        self.menuGAME.setObjectName("menuGAME")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        Mensch.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Mensch)
        self.statusbar.setObjectName("statusbar")
        Mensch.setStatusBar(self.statusbar)
        self.Add_Player = QtWidgets.QAction(Mensch)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/icons/add_person.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Add_Player.setIcon(icon1)
        self.Add_Player.setObjectName("Add_Player")
        self.Start_Game = QtWidgets.QAction(Mensch)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/icons/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Start_Game.setIcon(icon2)
        self.Start_Game.setObjectName("Start_Game")
        self.New_Game = QtWidgets.QAction(Mensch)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/icons/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.New_Game.setIcon(icon3)
        self.New_Game.setObjectName("New_Game")
        self.Exit = QtWidgets.QAction(Mensch)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/icons/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Exit.setIcon(icon4)
        self.Exit.setObjectName("Exit")
        self.actionAbuot = QtWidgets.QAction(Mensch)
        self.actionAbuot.setObjectName("actionAbuot")
        self.Mensch_Rule = QtWidgets.QAction(Mensch)
        self.Mensch_Rule.setObjectName("Mensch_Rule")
        self.About_Designer = QtWidgets.QAction(Mensch)
        self.About_Designer.setObjectName("About_Designer")
        self.menuGAME.addAction(self.Add_Player)
        self.menuGAME.addSeparator()
        self.menuGAME.addAction(self.Start_Game)
        self.menuGAME.addAction(self.New_Game)
        self.menuGAME.addSeparator()
        self.menuGAME.addAction(self.Exit)
        self.menuHelp.addAction(self.Mensch_Rule)
        self.menuHelp.addAction(self.About_Designer)
        self.menubar.addAction(self.menuGAME.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Mensch)
        QtCore.QMetaObject.connectSlotsByName(Mensch)

    def retranslateUi(self, Mensch):
        _translate = QtCore.QCoreApplication.translate
        Mensch.setWindowTitle(_translate("Mensch", "MainWindow"))
        self.players.setText(_translate("Mensch", "Players"))
        self.klick_on_dice.setText(_translate("Mensch", "Klick On Dice"))
        self.turn.setText(_translate("Mensch", "<html><head/><body><p><span style=\" font-weight:600; color:#55ff00;\">TURN</span></p></body></html>"))
        self.menuGAME.setTitle(_translate("Mensch", "GAME"))
        self.menuHelp.setTitle(_translate("Mensch", "Help"))
        self.Add_Player.setText(_translate("Mensch", "Add Player"))
        self.Start_Game.setText(_translate("Mensch", "Start Game"))
        self.New_Game.setText(_translate("Mensch", "New Game"))
        self.Exit.setText(_translate("Mensch", "Exit"))
        self.actionAbuot.setText(_translate("Mensch", "About"))
        self.Mensch_Rule.setText(_translate("Mensch", "Mensch Rule"))
        self.About_Designer.setText(_translate("Mensch", "About Programer"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Mensch = QtWidgets.QMainWindow()
    ui = Ui_Mensch()
    ui.setupUi(Mensch)
    Mensch.show()
    sys.exit(app.exec_())
