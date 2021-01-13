import sys
from PySide2.QtWidgets import QApplication, QLabel


def main():
    app = QApplication(sys.argv)
    # label = QLabel("Hello world")
    label = QLabel("<font color=red size=40>Hello World!</font>")
    label.show()
    app.exec_()


if __name__ == "__main__":
    main()
