from PyQt5.QtCore import QTimer
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QLabel


@pyqtSlot()
def gif_display(par, file, speed, length):
    disable_list = [element for element in par.btn_list if element.isEnabled()]
    par.dice_label.setHidden(True)
    for each in disable_list:
        each.setDisabled(True)

    class QMovieLabel(QLabel):
        def __init__(self, file_name, parent):
            super().__init__(parent)
            movie = QMovie(file_name)
            super().setMovie(movie)
            movie.setSpeed(speed)
            self.move(81, 727)
            movie.start()

    gif = QMovieLabel(file, par)
    gif.adjustSize()
    gif.show()

    QTimer.singleShot(length * 1000, gif.close)

    par.dice_label.setHidden(False)
    for each in disable_list:
        each.setDisabled(False)
