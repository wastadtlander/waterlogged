import sys
from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QMenu,
    QPlainTextEdit,
    QSystemTrayIcon,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import qDebug


class WindowWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Basic Layout
        hLayout = QHBoxLayout()
        infoDisplay = QPlainTextEdit()
        vLayout = QVBoxLayout()
        wakeTime = QTimeEdit()
        sleepTime = QTimeEdit()

        # Connecting Layouts and Widgets
        vLayout.addWidget(wakeTime)
        vLayout.addWidget(sleepTime)
        hLayout.addWidget(infoDisplay)
        hLayout.addLayout(vLayout)
        self.setLayout(hLayout)

        # Tray Functionality 
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon('assets/drop.png'))
        self.tray_icon.setToolTip('waterlogged')
        self.tray_icon.activated.connect(self.restore)

        self.tray_menu = QMenu()
        self.quit_action = self.tray_menu.addAction('Quit')
        self.tray_icon.setContextMenu(self.tray_menu)

        self.quit_action.triggered.connect(QApplication.quit)

        # Window Basics
        self.setGeometry(400, 200, 400, 200)
        self.setMinimumSize(400, 200)
        self.setMaximumSize(400, 200)
        self.setWindowTitle("waterlogged")
        self.show()

    def closeEvent(self, event):
        event.ignore()
        self.hide()
        self.tray_icon.show()
        qDebug(str(self.tray_icon.isVisible()))
        
    def restore(self, reason):
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            self.showNormal()
            self.activateWindow()
            self.tray_icon.hide()
            qDebug(str(self.tray_icon.isVisible()))

def main():
    app = QApplication([])

    window = WindowWidget()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
