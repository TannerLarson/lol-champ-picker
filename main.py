import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtQuick import QQuickView
from PySide6.QtCore import QUrl

app = QApplication(sys.argv)
view = QQuickView()
url = QUrl("view.qml")

print("hello")
view.setSource(url)
view.show()
print("hello")
app.exec_()
print("hello")