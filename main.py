import sys
import cv2
from PyQt5.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsPixmapItem, QFileDialog

from resources.ui.main_window import *
from lithophane import ImageMap



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.shapeComboBox.addItems(["Flat", "Cylinder", "Curve", "Heart"])

        # Image Default
        self.input_scene = QGraphicsScene(self)
        self.output_scene = QGraphicsScene(self)

        # Open File
        self.ui.selectImageButton.clicked.connect(self.openFile)

    def openFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", QtCore.QDir.currentPath(),
                                                   "Images (*.png *.jpg)", options=options)
        if file_name:
            # Qt Graphics
            self.ui.lineImagePath.setText(file_name)
            self.input_scene.clear()
            pixmap = QtGui.QPixmap(file_name)
            pixmap = pixmap.scaled(self.ui.graphicsViewInput.size(), QtCore.Qt.KeepAspectRatio)
            item = QGraphicsPixmapItem(pixmap)
            self.input_scene.addItem(item)
            self.ui.graphicsViewInput.setScene(self.input_scene)


            # CV2
            image2d = ImageMap(file_name)
            image = image2d.image
            gray = image2d.rgb_to_gray(image)
            scaled = image2d.scale_image(gray, 40)

            cv2.namedWindow('image', cv2.WINDOW_NORMAL)
            cv2.imshow('image', scaled)
            cv2.waitKey(0)
            cv2.destroyAllWindows()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    TestMainWindow = MainWindow()
    TestMainWindow.show()
    sys.exit(app.exec_())
