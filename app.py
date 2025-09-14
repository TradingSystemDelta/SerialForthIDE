import sys

from PySide6.QtWidgets import QApplication

from simple_forth_gui.mainwindow import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())