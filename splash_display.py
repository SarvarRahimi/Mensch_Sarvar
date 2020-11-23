from time import sleep

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QSplashScreen


def flashSplash(parent, file_name, t):
    splash = QSplashScreen(parent, QPixmap(file_name))
    splash.show()
    QTimer.singleShot(t, splash.close)
    sleep(t / 1000)
