import sys
from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QPlainTextEdit,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)


class WindowWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        hLayout = QHBoxLayout()
        infoDisplay = QPlainTextEdit()
        vLayout = QVBoxLayout()
        wakeTime = QTimeEdit()
        sleepTime = QTimeEdit()

        vLayout.addWidget(wakeTime)
        vLayout.addWidget(sleepTime)
        hLayout.addWidget(infoDisplay)
        hLayout.addLayout(vLayout)
        self.setLayout(hLayout)

        self.setGeometry(400, 200, 400, 200)
        self.setMinimumSize(400, 200)
        self.setMaximumSize(400, 200)
        self.setWindowTitle("waterlogged")
        self.show()


def main():
    app = QApplication([])

    window = WindowWidget()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
