import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget


class WindowWidget(QWidget):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    app = QApplication([])

    window = WindowWidget()
    window.show()

    sys.exit(app.exec())
