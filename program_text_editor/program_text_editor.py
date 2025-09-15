from PySide6.QtWidgets import QTextEdit

from pygments.formatters import HtmlFormatter
from pygments.lexers.forth import ForthLexer
from pygments import highlight


class ProgramTextEditor:
    def __init__(self, qt_text_edit_obj: QTextEdit) -> None:
        """Initialize the ProgramTextEditor with optional initial text.
        """
        self._qt_text_edit_obj = qt_text_edit_obj
        self._program_text = self._qt_text_edit_obj.toPlainText()

        self._qt_text_edit_obj.textChanged.connect(self._on_text_changed)

        self._formatter = HtmlFormatter(linenos=False, cssclass="source", style='default')
        self.css_format = self._formatter.get_style_defs('.source') + ".source { background: transparent !important; }"

    def _on_text_changed(self):
        self.program_text = self._qt_text_edit_obj.toPlainText()

    def load_file(self, file_path: str) -> None:
        """Load program text from a file into the editor.
        """
        with open(file_path, 'r') as file:
            text = file.read()
        self.program_text = text

    @property
    def program_text(self) -> str:
        """Get the program text.
        """
        return self._program_text

    @program_text.setter
    def program_text(self, new_text: str) -> None:
        """Set the raw program text. and update the text edit widget.
        """
        self._program_text = new_text
        html_result = highlight(new_text, ForthLexer(), self._formatter)
        html_result = f"<style>{self.css_format}</style>\n{html_result}"
        self.update_html(html_result)
    
    @program_text.deleter
    def program_text(self) -> None:
        """Delete the program text, Replacing it with an empty string.
        """
        del self._program_text
        self._program_text = ""
        raise NotImplementedError("LineNumber widget update is not implemented yet.")
    
    def update_html(self, html: str) -> None:
        """Update the text edit widget with the given HTML content. Also
        disables the signal to avoid recursive calls, and moves the cursor to
        the correct position.
        """
        cursor_position = self._qt_text_edit_obj.textCursor().position()

        # Update the text edit content
        self._qt_text_edit_obj.blockSignals(True)
        self._qt_text_edit_obj.setHtml(html)
        self._qt_text_edit_obj.blockSignals(False)

        # Restore the cursor position
        cursor = self._qt_text_edit_obj.textCursor()
        cursor.setPosition(cursor_position)
        self._qt_text_edit_obj.setTextCursor(cursor)
    
    @property
    def program_text_lines(self) -> list[str]:
        """Get the program text as a list of lines.
        """
        return self.get_program_text.splitlines()


