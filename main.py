import sys
from PyQt5.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsPixmapItem, QFileDialog

from resources.ui.main_window import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.cbbShape.addItems(["Flat", "Cylinder", "Curve", "Heart"])
        self.ui.raidoBtnBorderNo.setChecked(True)

        # Image Default
        self.scene = QGraphicsScene(self)

        # Open File
        self.ui.btnSelectImage.clicked.connect(self.openFile)

    def openFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", QtCore.QDir.currentPath(),
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if file_name:
            self.ui.lineImagePath.setText(file_name)
            self.scene.clear()
            pixmap = QtGui.QPixmap(file_name)
            pixmap = pixmap.scaled(self.ui.graphicsViewInput.size(), QtCore.Qt.KeepAspectRatio)
            item = QGraphicsPixmapItem(pixmap)
            self.scene.addItem(item)
            self.ui.graphicsViewInput.setScene(self.scene)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    TestMainWindow = MainWindow()
    TestMainWindow.show()
    sys.exit(app.exec_())