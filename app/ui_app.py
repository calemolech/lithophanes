import pyvista as pv
from PyQt5 import Qt, QtGui
from PyQt5.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsPixmapItem, \
    QMessageBox, QFileDialog, QDialog
from pyvistaqt import QtInteractor
from app.config import Config
from app.constants import DEFAULT_OUTPUT_NAME, DEBUG_MODE
from app.lithophane import *
from resources.ui.main_window import *
from stl import Mode


class UIApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UiMainWindow()
        self.ui.setupUi(self)
        self.image2d = None
        self.is_show_color = False
        self.model = None

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
        self.ui.curveSpinBox.setDisabled(True)
        self.ui.curveSlider.setDisabled(True)

        # Init output view
        self.frame = Qt.QFrame()
        self.plotter = QtInteractor(self.frame)
        self.ui.outputLayout.addWidget(self.plotter.interactor)
        self.plotter.show_axes_all()
        self.plotter.set_background("dimgray")
        # self.plotter.show_grid()
        # self.plotter.enable_zoom_style()
        # self.plotter.view_xy()
        self.ui.graphicsViewInput.setStyleSheet("background:dimgray;")

        # Init Dialogs
        self.load_dialog = QFileDialog()
        self.load_dialog.setFilter(self.load_dialog.filter())
        self.load_dialog.setAcceptMode(QFileDialog.AcceptOpen)
        self.load_dialog.setNameFilters(["Images (*.png *.jpg)"])
        self.load_dialog.setDirectory(Qt.QDir.currentPath())
        # self.load_dialog.setOption(QFileDialog.DontUseNativeDialog)

        self.save_dialog = QFileDialog()
        self.save_dialog.setFilter(self.save_dialog.filter())
        self.save_dialog.setDefaultSuffix('stl')
        self.save_dialog.setAcceptMode(QFileDialog.AcceptSave)
        self.save_dialog.setNameFilters(['STL (*.stl)'])
        self.save_dialog.setDirectory(Qt.QDir.currentPath())
        # self.save_dialog.setOption(QFileDialog.DontUseNativeDialog)

        # Menubar trigger
        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionExit.triggered.connect(self.close)

        # Button trigger
        self.ui.shapeComboBox.currentTextChanged.connect(
            self.update_config_by_shape)
        self.ui.selectImageButton.clicked.connect(self.open_file)
        self.ui.renderButton.clicked.connect(self.render_file)
        self.ui.downloadButton.clicked.connect(self.download_file)
        self.ui.showColorButton.clicked.connect(self.show_color)

        # Load default config
        self.config = Config()

    def open_file(self):
        """
        Dialog for open file
        """
        if self.load_dialog.exec_() == QDialog.Accepted:
            file_name = self.load_dialog.selectedFiles()[0]
            if DEBUG_MODE:
                print(file_name)
                file_name = "/Users/cale/Desktop/M1-IEI/Project/04_Code" \
                            "/lithophanes/tests/test_images/a.jpg"

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

                self.image2d = Lithophane(file_name)

    def render_file(self):
        """
        Get config. Convert 2D image to cloud point and make mesh
        """
        if self.image2d is None or self.ui.lineImagePath.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Please select image before render!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setWindowFlag(QtCore.Qt.Drawer)
            retval = msg.exec_()
            return
        else:
            self.config = self.get_ui_config()

            x, y, z = self.image2d.image2points(self.config.size,
                                                self.config.max_thickness,
                                                self.config.min_thickness,
                                                self.config.use_border,
                                                self.config.border_thickness)

            x2, y2, z2 = self.image2d.make_shape(x, y, z, self.config.curve,
                                                 self.config.shape)

            model = self.image2d.make_mesh(x2, y2, z2)
            self.model = model

            model.save(filename=DEFAULT_OUTPUT_NAME, mode=Mode.BINARY)
            sphere = pv.read(DEFAULT_OUTPUT_NAME)
            self.plotter.clear()
            if self.is_show_color:
                self.ui.showColorButton.setText("Hide Color")
                sphere["Elevation"] = model.vectors[:, :, 2][:, 1].ravel(
                    order="F")
            else:
                self.ui.showColorButton.setText("Show Color")
            self.plotter.add_mesh(sphere)
            self.plotter.camera_position = [(0, 0, z.shape[1] * 3.5),
                                            sphere.center, (0, 1, 0)]

    def get_ui_config(self):
        """
        Get config from UI and cast to class Config
        """
        use_border = True if self.ui.borderYesRadioButton.isChecked() else False
        stl_format = "Binary" if self.ui.binaryFormatRadioButton.isChecked() else "ASCII"

        current_config = Config(
            shape=self.ui.shapeComboBox.currentText(),
            size=self.ui.sizeSlider.value(),
            min_thick=self.ui.minThickDoubleSpinBox.value(),
            max_thick=self.ui.maxThickDoubleSpinBox.value(),
            curve=self.ui.curveSpinBox.value(),
            use_border=use_border,
            border_thick=self.ui.borderThicknessSlider.value(),
            stl_format=stl_format
        )

        if DEBUG_MODE:
            attrs = vars(current_config)
            for (k, v) in attrs.items():
                print(k, v)

        return current_config

    def update_config_by_shape(self):
        """
        Set default config when shape changed.
        """
        shape = self.ui.shapeComboBox.currentText()
        if shape == 'Flat':
            self.ui.curveSpinBox.setValue(0)
            self.ui.curveSpinBox.setDisabled(True)
            self.ui.curveSlider.setDisabled(True)
        elif shape == 'Cylinder':
            self.ui.curveSpinBox.setValue(360)
            self.ui.curveSpinBox.setDisabled(True)
            self.ui.curveSlider.setDisabled(True)
        elif shape == 'Curve':
            self.ui.curveSpinBox.setValue(90)
            self.ui.curveSpinBox.setEnabled(True)
            self.ui.curveSlider.setEnabled(True)
        elif shape == 'Heart':
            self.ui.curveSpinBox.setValue(360)
            self.ui.curveSpinBox.setDisabled(True)
            self.ui.curveSlider.setDisabled(True)

    def update_input_size(self, event):
        """
        Update size of Graphics View of input when windows resized.
        """
        if self.pixmap is not None:
            pixmap = self.pixmap
            pixmap = pixmap.scaled(self.ui.graphicsViewInput.size(),
                                   QtCore.Qt.KeepAspectRatio,
                                   QtCore.Qt.SmoothTransformation)
            self.input_scene.clear()
            self.input_scene.setSceneRect(self.ui.graphicsViewInput.sceneRect())
            self.input_scene.addItem(QGraphicsPixmapItem(pixmap))

    def download_file(self):
        """
        Dialog to save file
        """
        if self.model is None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Please render image before download!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setWindowFlag(QtCore.Qt.Drawer)
            retval = msg.exec_()
            return
        if self.save_dialog.exec_() == QDialog.Accepted:
            out_file_name = self.save_dialog.selectedFiles()[0]
            self.model.save(filename=out_file_name,  mode=Mode.BINARY if
                self.config.format == "Binary" else Mode.ASCII)

    def show_color(self):
        """
        Dialog to save file
        """
        self.is_show_color = not self.is_show_color
        self.render_file()
