from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QSplashScreen


class MovieSplashScreen(QSplashScreen):

    def __init__(self, movie, parent=None):
        movie.jumpToFrame(0)
        QSplashScreen.__init__(self, QPixmap(movie.frameRect().size()))
        self.movie = movie
        self.movie.setSpeed(200)
        self.movie.frameChanged.connect(self.repaint)

    def showEvent(self, event):
        self.movie.start()

    def hideEvent(self, event):
        self.movie.stop()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap_ = self.movie.currentPixmap()
        self.setMask(pixmap_.mask())
        painter.drawPixmap(0, 0, pixmap_)

    def sizeHint(self):
        return self.movie.scaledSize()
