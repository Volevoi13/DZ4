import sys
from PyQt5 import QtWidgets, uic
from mplcanvas import MyCanvas

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)

        self.speed_edit = self.findChild(QtWidgets.QLineEdit)
        self.angle_edit = self.findChild(QtWidgets.QLineEdit)
        self.draw_btn = self.findChild(QtWidgets.QPushButton)
        self.my_canvas = self.findChild(MyCanvas)


        self.draw_btn.clicked.connect(self.draw_plot)

    def draw_plot(self):
        try:
            speed = float(self.speed_edit.text())
            angle = float(self.angle_edit.text())
            if speed <= 0:
                raise ValueError("скорость должна быть больше нуля")
            self.my_canvas.draw_trajectory(speed, angle)
        except ValueError as err:
            QtWidgets.QMessageBox.warning(self, "ошибка вода", str(err))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.resize(800, 800)
    win.show()
    sys.exit(app.exec_())
