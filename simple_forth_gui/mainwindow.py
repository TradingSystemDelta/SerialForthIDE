# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWidgets import QPushButton, QTextEdit, QFileDialog

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from simple_forth_gui.ui_form import Ui_MainWindow

from program_text_editor.program_text_editor import ProgramTextEditor

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set up button click handlers
        self.ui.SendAll.clicked.connect(self.on_send_all_clicked)
        self.ui.SendLine.clicked.connect(self.on_send_line_clicked)
        self.ui.actionOpen.triggered.connect(self.open_file_dialog)
        self.ui.actionSave_As.triggered.connect(self.save_as_file_dialog)

        self.program_editor = ProgramTextEditor(self.ui.ProgramEditor)

    def save_as_file_dialog(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File As", "", "All Files (*)")
        if file_path:
            print("Selected file to save as:", file_path)
            raise NotImplementedError("File saving functionality is not implemented yet.")

    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)")
        if file_path:
            print("Selected file:", file_path)
            raise NotImplementedError("File opening functionality is not implemented yet.")

    def on_program_editor_cursor_position_changed(self):
        text_edit = self.ui.ProgramEditor
        cursor = text_edit.textCursor()
        line = cursor.blockNumber() + 1  # blockNumber is zero-based
        column = cursor.columnNumber() + 1  # columnNumber is zero-based
        print(f"Cursor moved to line {line}, column {column}")
        raise NotImplementedError("Cursor position change handling is not implemented yet.")
    
    def on_send_line_clicked(self):
        line_text = self.ui.lineEdit.text()
        self.ui.SerialMonitor.append(line_text)
        print(f"Send LINE clicked. Line: {line_text}")
        raise NotImplementedError("Send LINE functionality is not implemented yet.")

    def on_send_all_clicked(self):
        text = self.program_editor.program_text
        print(f"Send ALL clicked. Text: {text}")
        self.ui.SerialMonitor.setPlainText(text)
        raise NotImplementedError("Send ALL functionality is not implemented yet.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
