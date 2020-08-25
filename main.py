import pyvista as pv
from PyQt5 import Qt, QtGui
from PyQt5.QtWidgets import QMainWindow, QGraphicsScene, QFileDialog, \
    QGraphicsPixmapItem
from pyvistaqt import QtInteractor
import sys
from config import Config
from lithophane import *
from resources.ui.main_window import *
from stl import Mode
import copy


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UiMainWindow()
        self.ui.setupUi(self)

        # Menubar trigger
        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionExit.triggered.connect(app.quit)

        # Button trigger
        self.ui.shapeComboBox.currentTextChanged.connect(
            self.update_config_by_shape)
        self.ui.selectImageButton.clicked.connect(self.open_file)
        self.ui.renderButton.clicked.connect(self.render_file)

        # Init default for UI
        self.ui.shapeComboBox.addItems(["Flat", "Cylinder", "Curve", "Heart"])
        self.ui.graphicsViewInput.resizeEvent = self.update_input_size
        self.ui.graphicsViewInput.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.ui.graphicsViewInput.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.ui.graphicsViewInput.setMinimumSize(300, 300)
        self.input_scene = QGraphicsScene(self)
        self.pixmap = None

        # Load default config
        self.config = Config()

        # Init output view
        self.frame = Qt.QFrame()
        self.plotter = QtInteractor(self.frame)
        self.ui.outputLayout.addWidget(self.plotter.interactor)
        self.plotter.show_axes_all()
        # self.plotter.show_grid()
        # self.plotter.enable_zoom_style()
        # self.plotter.view_xy()

    def open_file(self):
        # file_name, _ = QFileDialog.getOpenFileName(self, "Open Image",
        #                                            QtCore.QDir.currentPath(),
        #                                            "Images (*.png *.jpg)")
        file_name = "/Users/cale/Desktop/M1-IEI/Project/04_Code/lithophanes/a.jpg"
        if file_name:
            # Qt Graphics
            self.ui.lineImagePath.setText(file_name)
            self.input_scene.clear()
            self.pixmap = QtGui.QPixmap(file_name)
            pixmap = self.pixmap
            pixmap = pixmap.scaled(self.ui.graphicsViewInput.size(),
                                   QtCore.Qt.KeepAspectRatio)
            self.input_scene.addItem(QGraphicsPixmapItem(pixmap))
            self.ui.graphicsViewInput.setScene(self.input_scene)


            self.image2d = ImageMap(file_name)

    def render_file(self):
        self.config = self.get_ui_config()

        x, y, z = self.image2d.image2points(self.config.size,
                                            self.config.max_thickness,
                                            self.config.min_thickness)
        # x2,y2,z2 = image2d.makeCylinder(x, y, z)
        x2, y2, z2 = self.image2d.make_cylinder2(x, y, z,
                                                 self.ui.curveSpinBox.value(),
                                                 self.ui.shapeComboBox.currentText())
        # model = self.image2d.make_mesh(x2, y2, z2)
        model = self.image2d.make_mesh_speed(x2, y2, z2)
        print("render ok")

        # sphere = pv.StructuredGrid(x2,y2,z2)

        import time
        t1 = time.time()
        model.save(filename="temp.stl", mode=Mode.BINARY)
        sphere = pv.read("temp.stl")
        print(time.time() - t1)

        self.plotter.clear()
        self.plotter.add_mesh(sphere)
        self.plotter.camera_position = [(0, 0, z.shape[1] * 3.5),
                                        sphere.center, (0, 1, 0)]

    def get_ui_config(self):
        shape_index = self.ui.shapeComboBox.currentIndex()
        use_border = True if self.ui.borderYesRadioButton.isChecked() else False

        current_config = Config(
            shape=self.ui.shapeComboBox.currentData(shape_index),
            size=self.ui.sizeSlider.value(),
            min_thick=self.ui.minThickDoubleSpinBox.value(),
            max_thick=self.ui.maxThickDoubleSpinBox.value(),
            curve=self.ui.curveSpinBox.value(),
            use_border=use_border,
            border_thick=self.ui.borderThicknessSlider.value()
        )
        return current_config

    def update_config_by_shape(self):
        shape = self.ui.shapeComboBox.currentText()
        if shape == 'Heart':
            self.ui.curveSpinBox.setValue(360)
            self.ui.curveSpinBox.setDisabled(True)
            self.ui.curveSlider.setDisabled(True)
        elif shape == 'Cylinder':
            self.ui.curveSpinBox.setValue(360)

    def update_input_size(self, event):
        if self.pixmap is not None:
            pixmap = self.pixmap
            pixmap = pixmap.scaled(self.ui.graphicsViewInput.size(),
                                   QtCore.Qt.KeepAspectRatio,
                                   QtCore.Qt.SmoothTransformation)
            self.input_scene.clear()
            self.input_scene.setSceneRect(self.ui.graphicsViewInput.sceneRect())
            self.input_scene.addItem(QGraphicsPixmapItem(pixmap))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationDisplayName("3D Lithophanes")
    # app.setStyle("Fusion")
    TestMainWindow = MainWindow()
    TestMainWindow.show()
    sys.exit(app.exec_())
