# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from resources.ui.UserWidgets import QDoubleSlider

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(770, 617)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setObjectName("mainLayout")
        self.visualizeLayout = QtWidgets.QHBoxLayout()
        self.visualizeLayout.setObjectName("visualizeLayout")
        self.inputLayout = QtWidgets.QVBoxLayout()
        self.inputLayout.setObjectName("inputLayout")
        self.buttonInputLayout = QtWidgets.QGridLayout()
        self.buttonInputLayout.setObjectName("buttonInputLayout")
        self.lineImagePath = QtWidgets.QLineEdit(self.centralwidget)
        self.lineImagePath.setObjectName("lineImagePath")
        self.buttonInputLayout.addWidget(self.lineImagePath, 0, 1, 1, 1)
        self.selectImageButton = QtWidgets.QPushButton(self.centralwidget)
        self.selectImageButton.setObjectName("selectImageButton")
        self.buttonInputLayout.addWidget(self.selectImageButton, 0, 0, 1, 1)
        self.inputLayout.addLayout(self.buttonInputLayout)
        self.graphicsViewInput = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsViewInput.setObjectName("graphicsViewInput")
        self.inputLayout.addWidget(self.graphicsViewInput)
        self.visualizeLayout.addLayout(self.inputLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.visualizeLayout.addWidget(self.line)
        self.outputLayout = QtWidgets.QVBoxLayout()
        self.outputLayout.setObjectName("outputLayout")
        self.buttonOutputLayout = QtWidgets.QGridLayout()
        self.buttonOutputLayout.setObjectName("buttonOutputLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonOutputLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonOutputLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.renderButton = QtWidgets.QPushButton(self.centralwidget)
        self.renderButton.setObjectName("renderButton")
        self.buttonOutputLayout.addWidget(self.renderButton, 0, 1, 1, 1)
        self.downloadButton = QtWidgets.QPushButton(self.centralwidget)
        self.downloadButton.setObjectName("downloadButton")
        self.buttonOutputLayout.addWidget(self.downloadButton, 0, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonOutputLayout.addItem(spacerItem2, 0, 4, 1, 1)
        self.outputLayout.addLayout(self.buttonOutputLayout)
        self.graphicsViewOutput = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsViewOutput.setObjectName("graphicsViewOutput")
        self.outputLayout.addWidget(self.graphicsViewOutput)
        self.visualizeLayout.addLayout(self.outputLayout)
        self.visualizeLayout.setStretch(0, 1)
        self.visualizeLayout.setStretch(2, 1)
        self.mainLayout.addLayout(self.visualizeLayout)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.mainLayout.addWidget(self.line_2)
        self.settingGridLayout = QtWidgets.QGridLayout()
        self.settingGridLayout.setObjectName("settingGridLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.otherSetting2Slider = QtWidgets.QSlider(self.centralwidget)
        self.otherSetting2Slider.setOrientation(QtCore.Qt.Horizontal)
        self.otherSetting2Slider.setObjectName("otherSetting2Slider")
        self.gridLayout.addWidget(self.otherSetting2Slider, 2, 5, 1, 1)
        self.otherSetting3Slider = QtWidgets.QSlider(self.centralwidget)
        self.otherSetting3Slider.setOrientation(QtCore.Qt.Horizontal)
        self.otherSetting3Slider.setObjectName("otherSetting3Slider")
        self.gridLayout.addWidget(self.otherSetting3Slider, 3, 5, 1, 1)
        self.minThickDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.minThickDoubleSpinBox.setDecimals(1)
        self.minThickDoubleSpinBox.setMinimum(0.1)
        self.minThickDoubleSpinBox.setMaximum(10.0)
        self.minThickDoubleSpinBox.setSingleStep(0.1)
        self.minThickDoubleSpinBox.setProperty("value", 0.5)
        self.minThickDoubleSpinBox.setObjectName("minThickDoubleSpinBox")
        self.gridLayout.addWidget(self.minThickDoubleSpinBox, 2, 2, 1, 1)
        self.lblBorderThickness = QtWidgets.QLabel(self.centralwidget)
        self.lblBorderThickness.setObjectName("lblBorderThickness")
        self.gridLayout.addWidget(self.lblBorderThickness, 1, 4, 1, 1)
        self.otherSetting2SpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.otherSetting2SpinBox.setObjectName("otherSetting2SpinBox")
        self.gridLayout.addWidget(self.otherSetting2SpinBox, 2, 6, 1, 1)
        self.borderHorizontalLayout = QtWidgets.QHBoxLayout()
        self.borderHorizontalLayout.setObjectName("borderHorizontalLayout")
        self.borderYesRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.borderYesRadioButton.setObjectName("borderYesRadioButton")
        self.borderHorizontalLayout.addWidget(self.borderYesRadioButton)
        self.borderNoRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.borderNoRadioButton.setChecked(True)
        self.borderNoRadioButton.setObjectName("borderNoRadioButton")
        self.borderHorizontalLayout.addWidget(self.borderNoRadioButton)
        self.gridLayout.addLayout(self.borderHorizontalLayout, 0, 5, 1, 2)
        self.otherSetting3SpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.otherSetting3SpinBox.setObjectName("otherSetting3SpinBox")
        self.gridLayout.addWidget(self.otherSetting3SpinBox, 3, 6, 1, 1)
        self.lblMinThick = QtWidgets.QLabel(self.centralwidget)
        self.lblMinThick.setObjectName("lblMinThick")
        self.gridLayout.addWidget(self.lblMinThick, 2, 0, 1, 1)
        self.lblShape = QtWidgets.QLabel(self.centralwidget)
        self.lblShape.setObjectName("lblShape")
        self.gridLayout.addWidget(self.lblShape, 0, 0, 1, 1)
        self.lblSize = QtWidgets.QLabel(self.centralwidget)
        self.lblSize.setObjectName("lblSize")
        self.gridLayout.addWidget(self.lblSize, 1, 0, 1, 1)
        self.lblBorder = QtWidgets.QLabel(self.centralwidget)
        self.lblBorder.setObjectName("lblBorder")
        self.gridLayout.addWidget(self.lblBorder, 0, 4, 1, 1)
        self.shapeComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.shapeComboBox.setEditable(False)
        self.shapeComboBox.setObjectName("shapeComboBox")
        self.gridLayout.addWidget(self.shapeComboBox, 0, 1, 1, 2)
        self.borderThicknessSlider = QtWidgets.QSlider(self.centralwidget)
        self.borderThicknessSlider.setEnabled(True)
        self.borderThicknessSlider.setMaximum(50)
        self.borderThicknessSlider.setOrientation(QtCore.Qt.Horizontal)
        self.borderThicknessSlider.setObjectName("borderThicknessSlider")
        self.gridLayout.addWidget(self.borderThicknessSlider, 1, 5, 1, 1)
        self.sizeSlider = QtWidgets.QSlider(self.centralwidget)
        self.sizeSlider.setMinimum(1)
        self.sizeSlider.setMaximum(1000)
        self.sizeSlider.setProperty("value", 100)
        self.sizeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.sizeSlider.setObjectName("sizeSlider")
        self.gridLayout.addWidget(self.sizeSlider, 1, 1, 1, 1)
        self.sizeSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.sizeSpinBox.setMinimum(1)
        self.sizeSpinBox.setMaximum(1000)
        self.sizeSpinBox.setProperty("value", 100)
        self.sizeSpinBox.setObjectName("sizeSpinBox")
        self.gridLayout.addWidget(self.sizeSpinBox, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 3, 1, 1)
        self.lblMaxThick = QtWidgets.QLabel(self.centralwidget)
        self.lblMaxThick.setObjectName("lblMaxThick")
        self.gridLayout.addWidget(self.lblMaxThick, 3, 0, 1, 1)
        self.lblOtherSetting2 = QtWidgets.QLabel(self.centralwidget)
        self.lblOtherSetting2.setObjectName("lblOtherSetting2")
        self.gridLayout.addWidget(self.lblOtherSetting2, 2, 4, 1, 1)
        self.lblOtherSetting3 = QtWidgets.QLabel(self.centralwidget)
        self.lblOtherSetting3.setObjectName("lblOtherSetting3")
        self.gridLayout.addWidget(self.lblOtherSetting3, 3, 4, 1, 1)
        self.maxThickSlider = QDoubleSlider(self.centralwidget)
        self.maxThickSlider.setMinInt(0)
        self.maxThickSlider.setMaxInt(100)
        self.maxThickSlider.setMinimum(0.1)
        self.maxThickSlider.setMaximum(15.0)
        self.maxThickSlider.setProperty("value", 3.5)
        self.maxThickSlider.setOrientation(QtCore.Qt.Horizontal)
        self.maxThickSlider.setObjectName("maxThickSlider")
        self.gridLayout.addWidget(self.maxThickSlider, 3, 1, 1, 1)
        self.minThickSlider = QDoubleSlider()
        self.minThickSlider.setMinimum(0)
        self.minThickSlider.setMaximum(100)
        self.minThickSlider.setMinimum(0.1)
        self.minThickSlider.setMaximum(10.0)
        self.minThickSlider.setProperty("value", 0.5)
        self.minThickSlider.setOrientation(QtCore.Qt.Horizontal)
        self.minThickSlider.setObjectName("minThickSlider")
        self.gridLayout.addWidget(self.minThickSlider, 2, 1, 1, 1)
        self.borderThicknessDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.borderThicknessDoubleSpinBox.setEnabled(True)
        self.borderThicknessDoubleSpinBox.setDecimals(1)
        self.borderThicknessDoubleSpinBox.setMaximum(15.0)
        self.borderThicknessDoubleSpinBox.setSingleStep(0.1)
        self.borderThicknessDoubleSpinBox.setObjectName("borderThicknessDoubleSpinBox")
        self.gridLayout.addWidget(self.borderThicknessDoubleSpinBox, 1, 6, 1, 1)
        self.maxThickDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.maxThickDoubleSpinBox.setDecimals(1)
        self.maxThickDoubleSpinBox.setMinimum(0.1)
        self.maxThickDoubleSpinBox.setMaximum(15.0)
        self.maxThickDoubleSpinBox.setSingleStep(0.1)
        self.maxThickDoubleSpinBox.setProperty("value", 3.5)
        self.maxThickDoubleSpinBox.setObjectName("maxThickDoubleSpinBox")
        self.gridLayout.addWidget(self.maxThickDoubleSpinBox, 3, 2, 1, 1)
        self.settingGridLayout.addLayout(self.gridLayout, 2, 0, 1, 1)
        self.mainLayout.addLayout(self.settingGridLayout)
        self.mainLayout.setStretch(0, 7)
        self.mainLayout.setStretch(2, 3)
        self.verticalLayout_4.addLayout(self.mainLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 770, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuDownload_Settings = QtWidgets.QMenu(self.menuSettings)
        self.menuDownload_Settings.setObjectName("menuDownload_Settings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionDownloads = QtWidgets.QAction(MainWindow)
        self.actionDownloads.setObjectName("actionDownloads")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionBinary_STL = QtWidgets.QAction(MainWindow)
        self.actionBinary_STL.setObjectName("actionBinary_STL")
        self.actionASCII_STL = QtWidgets.QAction(MainWindow)
        self.actionASCII_STL.setObjectName("actionASCII_STL")
        self.actionModels_Setting = QtWidgets.QAction(MainWindow)
        self.actionModels_Setting.setObjectName("actionModels_Setting")
        self.actionImage_Settings = QtWidgets.QAction(MainWindow)
        self.actionImage_Settings.setObjectName("actionImage_Settings")
        self.actionBinary_STL_2 = QtWidgets.QAction(MainWindow)
        self.actionBinary_STL_2.setObjectName("actionBinary_STL_2")
        self.actionASCII_STL_2 = QtWidgets.QAction(MainWindow)
        self.actionASCII_STL_2.setObjectName("actionASCII_STL_2")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuDownload_Settings.addAction(self.actionBinary_STL_2)
        self.menuDownload_Settings.addAction(self.actionASCII_STL_2)
        self.menuSettings.addAction(self.actionModels_Setting)
        self.menuSettings.addAction(self.actionImage_Settings)
        self.menuSettings.addAction(self.menuDownload_Settings.menuAction())
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.sizeSlider.valueChanged['int'].connect(self.sizeSpinBox.setValue)
        self.sizeSpinBox.valueChanged['int'].connect(self.sizeSlider.setValue)
        self.otherSetting2Slider.valueChanged['int'].connect(self.otherSetting2SpinBox.setValue)
        self.otherSetting2SpinBox.valueChanged['int'].connect(self.otherSetting2Slider.setValue)
        self.otherSetting3SpinBox.valueChanged['int'].connect(self.otherSetting3Slider.setValue)
        self.otherSetting3Slider.valueChanged['int'].connect(self.otherSetting3SpinBox.setValue)
        self.borderYesRadioButton.clicked['bool'].connect(self.borderThicknessSlider.setEnabled)
        self.borderNoRadioButton.clicked['bool'].connect(self.borderThicknessSlider.setDisabled)
        self.maxThickDoubleSpinBox.valueChanged['double'].connect(self.maxThickSlider.setValue)
        self.minThickDoubleSpinBox.valueChanged['double'].connect(self.minThickSlider.setValue)
        self.maxThickSlider.valueChanged.connect(self.handleMaxThickSlider)
        self.minThickSlider.valueChanged.connect(self.handleMinThickSlider)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "3D Lithophanes"))
        self.selectImageButton.setText(_translate("MainWindow", "Select Image"))
        self.renderButton.setText(_translate("MainWindow", "Render"))
        self.downloadButton.setText(_translate("MainWindow", "Download"))
        self.lblBorderThickness.setText(_translate("MainWindow", "Border Thickness"))
        self.borderYesRadioButton.setText(_translate("MainWindow", "Yes"))
        self.borderNoRadioButton.setText(_translate("MainWindow", "No"))
        self.lblMinThick.setText(_translate("MainWindow", "Min Thickness"))
        self.lblShape.setText(_translate("MainWindow", "Shape"))
        self.lblSize.setText(_translate("MainWindow", "Size"))
        self.lblBorder.setText(_translate("MainWindow", "Border"))
        self.lblMaxThick.setText(_translate("MainWindow", "Max Thicknes"))
        self.lblOtherSetting2.setText(_translate("MainWindow", "Other Setting"))
        self.lblOtherSetting3.setText(_translate("MainWindow", "Other Setting"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuDownload_Settings.setTitle(_translate("MainWindow", "Download Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionDownloads.setText(_translate("MainWindow", "Downloads"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As..."))
        self.actionSave_As.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionBinary_STL.setText(_translate("MainWindow", "Binary STL"))
        self.actionASCII_STL.setText(_translate("MainWindow", "ASCII STL"))
        self.actionModels_Setting.setText(_translate("MainWindow", "Models Settings"))
        self.actionImage_Settings.setText(_translate("MainWindow", "Image Settings"))
        self.actionBinary_STL_2.setText(_translate("MainWindow", "Binary STL"))
        self.actionASCII_STL_2.setText(_translate("MainWindow", "ASCII STL"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

    def fit(self, val, old_min, old_max, new_min, new_max):
        scale = (float(val) - old_min) / (old_max - old_min)
        new_range = scale * (new_max - new_min)
        if new_min < new_max:
            return round(new_min + new_range, 1)
        else:
            return round(new_min - new_range, 1)

    def handleMaxThickSlider(self, val):
        self.maxThickDoubleSpinBox.blockSignals(True)
        new_val = self.fit(val,
                           self.maxThickSlider.getMinInt(),
                           self.maxThickSlider.getMaxInt(),
                           self.maxThickSlider.minimum(),
                           self.maxThickSlider.maximum())
        self.maxThickDoubleSpinBox.setValue(new_val)
        print(val, new_val)
        self.maxThickDoubleSpinBox.blockSignals(False)


    def handleMinThickSlider(self, val):
        self.minThickDoubleSpinBox.blockSignals(True)
        new_val = self.fit(val,
                           self.minThickSlider.getMinInt(),
                           self.minThickSlider.getMaxInt(),
                           self.minThickSlider.minimum(),
                           self.minThickSlider.maximum())
        self.minThickDoubleSpinBox.setValue(new_val)
        print(val, new_val)
        self.minThickDoubleSpinBox.blockSignals(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())