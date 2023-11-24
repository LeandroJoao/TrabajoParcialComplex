import sys
from PySide6.QtWidgets import QApplication
from Widget import Widget


app = QApplication(sys.argv)

button = Widget()

button.show()
app.exec()