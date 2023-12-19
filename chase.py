import sys
import random

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("RUN")
        self.setMinimumSize(800, 600)
        self.setMaximumSize(1200, 900)

        button_width = 150
        button_height = 45
        button_x = (self.width() - button_width) // 2
        button_y = (self.height() - button_height) // 2

        self.my_button = QPushButton("YES", self)
        self.my_button.setGeometry(button_x, button_y - 50, button_width, button_height)
        self.my_button.enterEvent = lambda event: self.move_button_random_my()

        self.ny_button = QPushButton("NO", self)
        self.ny_button.setGeometry(button_x, button_y - 150, button_width, button_height)
        self.ny_button.enterEvent = lambda event: self.move_button_random_ny()

        self.demo_button = QPushButton("MAYBE", self)
        self.demo_button.setGeometry(button_x, button_y - 250, button_width, button_height)
        self.demo_button.enterEvent = lambda event: self.move_button_random()

    def change_button_color(self):
        # Generate a random color
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.demo_button.setStyleSheet("background-color: %s;" % color.name())

    def move_button_random(self):
        # Get random coordinates within the window size
        window_width = self.width() - self.demo_button.width()
        window_height = self.height() - self.demo_button.height()

        random_x = random.randint(0, window_width)
        random_y = random.randint(0, window_height)

        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        self.demo_button.setStyleSheet("background-color: %s;" % color.name())
        self.demo_button.move(random_x, random_y)

    def move_button_random_my(self):
        # Get random coordinates within the window size
        window_width = self.width() - self.demo_button.width()
        window_height = self.height() - self.demo_button.height()

        random_x = random.randint(0, window_width)
        random_y = random.randint(0, window_height)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        self.my_button.setStyleSheet("background-color: %s;" % color.name())
        self.my_button.move(random_x, random_y)

    def move_button_random_ny(self):
        # Get random coordinates within the window size
        window_width = self.width() - self.demo_button.width()
        window_height = self.height() - self.demo_button.height()

        random_x = random.randint(0, window_width)
        random_y = random.randint(0, window_height)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        self.ny_button.setStyleSheet("background-color: %s;" % color.name())
        self.ny_button.move(random_x, random_y)

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self,
            'Confirmation',
            'Are you sure you want to exit?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
