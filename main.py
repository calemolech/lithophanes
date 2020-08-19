import sys
import cv2
from PyQt5 import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsPixmapItem, QFileDialog

from matplotlib import cm
from matplotlib.pyplot import figure
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from mpl_toolkits.mplot3d import Axes3D

from resources.ui.main_window import *
from lithophane import *
from stl import mesh
import numpy as np
import pyvista as pv
from pyvistaqt import BackgroundPlotter, QtInteractor
from pyvista import examples

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

        # Render test
        self.ui.renderButton.clicked.connect(self.render_file)

        self.frame = Qt.QFrame()
        self.plotter = QtInteractor(self.frame)
        self.ui.outputLayout.addWidget(self.plotter.interactor)

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
            pixmap = pixmap.scaled(0.95 * self.ui.graphicsViewInput.size(), QtCore.Qt.KeepAspectRatio)
            item = QGraphicsPixmapItem(pixmap)
            self.input_scene.addItem(item)
            self.ui.graphicsViewInput.setScene(self.input_scene)


            image2d = ImageMap(file_name)
            image = image2d.image
            x,y,z = image2d.jpg2stl(width=40, h=3, d=0.5, show=False)
            model = image2d.makemesh(x, y,z )
            model.save("temp.stl")
            print("ok")
            sphere = pv.read("temp.stl")
            self.plotter.add_mesh(sphere)



    def render_file(self):
        config = self.get_config();

        sphere = pv.read("/Users/cale/Desktop/M1-IEI/Project/04_Code/lithophanes/out_stl/c.stl")
        sphere = pv.read("/Users/cale/Desktop/M1-IEI/Project/04_Code/lithophanes/out_stl/a_Cylinder.stl")
        sphere = pv.read("/Users/cale/Desktop/M1-IEI/Project/04_Code/lithophanes/out_stl/a_Flat.stl")
        self.plotter.add_mesh(sphere)

    def get_config(self):
        shape = self.ui.shapeComboBox.currentData(self.ui.shapeComboBox.currentIndex())
        size = self.ui.sizeSlider.value()
        border = True if self.ui.borderYesRadioButton.isChecked() else False
        thickness = self.ui.minThickSlider.value()
        border_thickness = self.ui.borderThicknessSlider.value()
        return shape, size, border, thickness, border_thickness


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    TestMainWindow = MainWindow()
    TestMainWindow.show()
    sys.exit(app.exec_())
