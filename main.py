import sys
import cv2
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsPixmapItem, QFileDialog

from matplotlib import cm
from matplotlib.pyplot import figure
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from mpl_toolkits.mplot3d import Axes3D

from resources.ui.main_window import *
from lithophane import ImageMap
from stl import mesh
import numpy as np


class ThreeDSurfaceGraphWindow(FigureCanvas):  # Class for 3D window
    def __init__(self):
        self.plot_colorbar = None
        self.plot_figure = figure(figsize=(7, 7))
        FigureCanvas.__init__(self, self.plot_figure)  # creating FigureCanvas
        self.axes = self.plot_figure.gca(projection='3d')  # generates 3D Axes object
        self.setWindowTitle("figure")  # sets Window title

    def draw_graph(self, x, y, z):  # Function for graph plotting
        self.axes.clear()
        if self.plot_colorbar is not None:  # avoids adding one more colorbar at each draw operation
            self.plot_colorbar.remove()
        # plots the 3D surface plot
        plot_stuff = self.axes.plot_surface(x, y, z,
                                            cmap=cm.coolwarm, linewidth=0, antialiased=False)
        self.axes.zaxis.set_major_locator(LinearLocator(10))
        self.axes.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
        # Add a color bar which maps values to colors.
        self.plot_colorbar = self.plot_figure.colorbar(plot_stuff, shrink=0.5, aspect=5)
        # draw plot
        self.draw()


def f(x, y):  # For Generating Z coordinates
    return np.sin(np.sqrt(x ** 2 + y ** 2))


def g(x, y):  # For Generating Z coordinates (alternative)
    return np.sin(x) + np.cos(y)


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

        self.plot_container = ThreeDSurfaceGraphWindow()
        self.ui.outputLayout.addWidget(self.plot_container)
        self.plot_status = u'a'
        self.X_plot_val = None
        self.Y_plot_val = None
        self.Z_plot_val = None
        self.test_std_out()

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

            # CV2
            # image2d = ImageMap(file_name)
            # image = image2d.image
            # gray = image2d.rgb_to_gray(image)
            # scaled = image2d.scale_image(gray, 40)

            # cv2.namedWindow('image', cv2.WINDOW_NORMAL)
            # cv2.imshow('image', scaled)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()

    @pyqtSlot()
    def test_std_out(self):
        # Make plot data
        if self.plot_status == u'a':
            self.X_plot_val = np.arange(-10, 10, 0.25)  # X coordinates
            self.Y_plot_val = np.arange(-10, 10, 0.25)  # Y coordinates
            # Forming MeshGrid
            self.X_plot_val, self.Y_plot_val = np.meshgrid(self.X_plot_val, self.Y_plot_val)
            self.Z_plot_val = g(self.X_plot_val, self.Y_plot_val)
            self.plot_status = u'b'
        else:
            self.X_plot_val = np.arange(-5, 5, 0.25)  # X coordinates
            self.Y_plot_val = np.arange(-5, 5, 0.25)  # Y coordinates
            # Forming MeshGrid
            self.X_plot_val, self.Y_plot_val = np.meshgrid(self.X_plot_val, self.Y_plot_val)
            self.Z_plot_val = f(self.X_plot_val, self.Y_plot_val)
            self.plot_status = u'a'
        # call plot for tests
        self.plot_container.draw_graph(self.X_plot_val, self.Y_plot_val, self.Z_plot_val)

    def render_file(self):
        config = self.get_config();

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
