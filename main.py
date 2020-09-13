import sys
from PyQt5 import QtGui, QtWidgets
from app.ui_app import UIApp

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationDisplayName("3D Lithophanes")
    app.setWindowIcon(QtGui.QIcon('resources/icons/3D-icon.png'))
    # app.setStyle("Fusion")
    TestMainWindow = UIApp()
    TestMainWindow.show()
    sys.exit(app.exec_())
