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


class Config():
    def __init__(self):
        shape = 'Flat'
        size = 800
        max_thickness = 3.5
        min_thickness = 0.5
        border = False
        border_thickness = 0


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.shapeComboBox.addItems(["Flat", "Cylinder", "Curve", "Heart"])

        self.config = Config()

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
        # file_name = "/Users/cale/Desktop/M1-IEI/Project/04_Code/lithophanes/a.jpg"
        if file_name:
            # Qt Graphics
            # self.ui.lineImagePath.setText(file_name)
            # self.input_scene.clear()
            # pixmap = QtGui.QPixmap(file_name)
            # pixmap = pixmap.scaled(0.95 * self.ui.graphicsViewInput.size(), QtCore.Qt.KeepAspectRatio)
            # item = QGraphicsPixmapItem(pixmap)
            # self.input_scene.addItem(item)
            # self.ui.graphicsViewInput.setScene(self.input_scene)


            image2d = ImageMap(file_name)
            image = image2d.image
            config = self.get_config()
            # x,y,z = image2d.image2points(width=40, max_thickness=config.max_thickness, min_thickness=config.min_thickness, show=False)
            x,y,z = image2d.image2points(width=40, max_thickness=20, min_thickness=20, show=False)

            # points = image2d.testmesh(x,y,z)
            # print(points.shape)



            model = image2d.makemesh(x, y,z )
            model.save("temp.stl")
            print("ok")
            sphere = pv.read("temp.stl")
            self.plotter.show_grid()
            self.plotter.show_bounds()
            self.plotter.show_axes()

            self.plotter.add_mesh(sphere)

            # grid = pv.StructuredGrid(x, y, z)

            # self.plotter.add_mesh(grid)

    def render_file(self):
        config = self.get_config();

        sphere = pv.read("/Users/cale/Desktop/M1-IEI/Project/04_Code/lithophanes/out_stl/c.stl")
        sphere = pv.read("/Users/cale/Desktop/M1-IEI/Project/04_Code/lithophanes/out_stl/a_Cylinder.stl")
        sphere = pv.read("/Users/cale/Desktop/M1-IEI/Project/04_Code/lithophanes/out_stl/a_Flat.stl")
        self.plotter.add_mesh(sphere)

    def get_config(self):
        self.config.shape = self.ui.shapeComboBox.currentData(self.ui.shapeComboBox.currentIndex())
        self.config.size = self.ui.sizeSlider.value()
        self.config.border = True if self.ui.borderYesRadioButton.isChecked() else False
        self.config.max_thickness = self.ui.maxThickDoubleSpinBox.value()
        self.config.min_thickness = self.ui.minThickDoubleSpinBox.value()
        self.config.border_thickness = self.ui.borderThicknessSlider.value()
        return self.config


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    TestMainWindow = MainWindow()
    TestMainWindow.show()
    sys.exit(app.exec_())
