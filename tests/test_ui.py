import unittest
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication
from colour_runner.runner import ColourTextTestRunner

from app.lithophane_app import LithophaneApp

app = QApplication(sys.argv)


class Test_UI(unittest.TestCase):
    """Test the GUI"""

    def setUp(self):
        """Create the GUI"""
        self.form = LithophaneApp()

    # region Test init
    def test_init_ui(self):
        """Test init buttons and labels"""
        self.assertEqual(self.form.ui.selectImageButton.text(), "Select Image")
        self.assertEqual(self.form.ui.renderButton.text(), "Render")
        self.assertEqual(self.form.ui.showColorButton.text(), "Show Color")
        self.assertEqual(self.form.ui.downloadButton.text(), "Download")
        self.assertEqual(self.form.ui.lblShape.text(), "Shape")
        self.assertEqual(self.form.ui.lblSize.text(), "Size")
        self.assertEqual(self.form.ui.lblMinThick.text(), "Min Thickness")
        self.assertEqual(self.form.ui.lblMaxThick.text(), "Max Thickness")
        self.assertEqual(self.form.ui.lblBorder.text(), "Border")
        self.assertEqual(self.form.ui.borderYesRadioButton.text(), "Yes")
        self.assertEqual(self.form.ui.borderNoRadioButton.text(), "No")
        self.assertEqual(self.form.ui.lblBorderThickness.text(),
                         "Border Thickness")
        self.assertEqual(self.form.ui.lblCurve.text(), "Curve")
        self.assertEqual(self.form.ui.lblFormat.text(), "STL Format")
        self.assertEqual(self.form.ui.binaryFormatRadioButton.text(), "Binary")
        self.assertEqual(self.form.ui.asciiFormatRadioButton.text(), "ASCII")

    def test_init_value(self):
        """Test init default values"""
        self.assertEqual("Flat", self.form.ui.shapeComboBox.currentText())
        self.assertEqual(300, self.form.ui.sizeSlider.value())
        self.assertEqual(300, self.form.ui.sizeSpinBox.value())
        self.assertEqual(1.0, round(self.form.ui.minThickSlider.value(), 1))
        self.assertEqual(1.0, round(self.form.ui.minThickDoubleSpinBox.value(),
                                    1))
        self.assertEqual(5.0, round(self.form.ui.maxThickSlider.value()))
        self.assertEqual(5.0, round(self.form.ui.maxThickDoubleSpinBox.value()))
        self.assertEqual(False, self.form.ui.borderYesRadioButton.isChecked())
        self.assertEqual(True, self.form.ui.borderNoRadioButton.isChecked())
        self.assertEqual(False, self.form.ui.borderThicknessSlider.isEnabled())
        self.assertEqual(False,
                         self.form.ui.borderThicknessDoubleSpinBox.isEnabled())
        self.assertEqual(0, self.form.ui.curveSlider.value())
        self.assertEqual(0, self.form.ui.curveSpinBox.value())
        self.assertEqual(True, self.form.ui.binaryFormatRadioButton.isChecked())
        self.assertEqual(False, self.form.ui.asciiFormatRadioButton.isChecked())

    # endregion

    # region Test Config
    def test_shape_change(self):
        """Test change shape comboBox"""
        shape_combo_box = self.form.ui.shapeComboBox
        QTest.keyClick(shape_combo_box,Qt.Key_PageUp)
        all_items = [self.form.ui.shapeComboBox.itemText(i)
                     for i in range(self.form.ui.shapeComboBox.count())]
        for i in range(shape_combo_box.count() - 2):
            shape_combo_box.setCurrentIndex(i)
            current_shape = self.form.ui.shapeComboBox.currentText()
            self.assertEqual(all_items[i], current_shape)

    def test_size_out_range(self):
        """Test change size out of range (Slider and Spinbox)"""
        self.form.ui.sizeSlider.setValue(-1)
        self.assertEqual(1, self.form.ui.sizeSlider.value())
        self.assertEqual(1, self.form.ui.sizeSpinBox.value())
        self.form.ui.sizeSpinBox.setValue(600)
        self.assertEqual(500, self.form.ui.sizeSlider.value())
        self.assertEqual(500, self.form.ui.sizeSpinBox.value())

    def test_size_change(self):
        """Test change size (Slider and Spinbox)"""
        self.form.ui.sizeSlider.setValue(100)
        self.assertEqual(self.form.ui.sizeSlider.value(),
                         self.form.ui.sizeSpinBox.value())
        self.form.ui.sizeSpinBox.setValue(30)
        self.assertEqual(self.form.ui.sizeSlider.value(),
                         self.form.ui.sizeSpinBox.value())

    def test_min_thick_out_range(self):
        """Test change minimum thickness out of range (Slider and Spinbox)"""
        self.form.ui.minThickSlider.setValue(0)
        self.assertEqual(0.1, self.form.ui.minThickSlider.value())
        self.assertEqual(0.1, self.form.ui.minThickDoubleSpinBox.value())
        self.form.ui.minThickDoubleSpinBox.setValue(11.0)
        self.assertEqual(10.0, self.form.ui.minThickSlider.value())
        self.assertEqual(10.0, self.form.ui.minThickDoubleSpinBox.value())

    def test_min_thick_change(self):
        """Test change minimum thickness (Slider and Spinbox)"""
        self.form.ui.minThickSlider.setValue(0.5)
        self.assertEqual(round(self.form.ui.minThickSlider.value()),
                         round(self.form.ui.minThickDoubleSpinBox.value()))
        self.form.ui.minThickDoubleSpinBox.setValue(9.0)
        self.assertEqual(round(self.form.ui.minThickSlider.value()),
                         round(self.form.ui.minThickDoubleSpinBox.value()))

    def test_max_thick_out_range(self):
        """Test change maximum thickness out of range (Slider and Spinbox)"""
        self.form.ui.maxThickSlider.setValue(0)
        self.assertEqual(0.1, self.form.ui.maxThickSlider.value())
        self.assertEqual(0.1, self.form.ui.maxThickDoubleSpinBox.value())
        self.form.ui.maxThickDoubleSpinBox.setValue(16.0)
        self.assertEqual(15.0, self.form.ui.maxThickSlider.value())
        self.assertEqual(15.0, self.form.ui.maxThickDoubleSpinBox.value())

    def test_max_thick_change(self):
        """Test change maximum thickness (Slider and Spinbox)"""
        self.form.ui.maxThickSlider.setValue(0.5)
        self.assertEqual(round(self.form.ui.maxThickSlider.value()),
                         round(self.form.ui.maxThickDoubleSpinBox.value()))
        self.form.ui.maxThickDoubleSpinBox.setValue(9.0)
        self.assertEqual(round(self.form.ui.maxThickSlider.value()),
                         round(self.form.ui.maxThickDoubleSpinBox.value()))

    def test_border_thick_out_range(self):
        """Test change border thickness out of range (Slider and Spinbox)"""
        self.form.ui.borderThicknessSlider.setValue(-1)
        self.assertEqual(0, self.form.ui.borderThicknessSlider.value())
        self.assertEqual(0, self.form.ui.borderThicknessDoubleSpinBox.value())
        self.form.ui.borderThicknessDoubleSpinBox.setValue(100.0)
        self.assertEqual(50.0, self.form.ui.borderThicknessSlider.value())
        self.assertEqual(50.0,
                         self.form.ui.borderThicknessDoubleSpinBox.value())

    def test_border_thick_change(self):
        """Test change border thickness (Slider and Spinbox)"""
        self.form.ui.borderThicknessSlider.setValue(0.5)
        self.assertEqual(round(self.form.ui.borderThicknessSlider.value()),
                         round(
                             self.form.ui.borderThicknessDoubleSpinBox.value()))
        self.form.ui.borderThicknessDoubleSpinBox.setValue(49.5)
        self.assertEqual(round(self.form.ui.borderThicknessSlider.value()),
                         round(
                             self.form.ui.borderThicknessDoubleSpinBox.value()))

    def test_curve_out_range(self):
        """Test change curve out of range (Slider and Spinbox)"""
        self.form.ui.curveSlider.setValue(-1)
        self.assertEqual(0, self.form.ui.curveSlider.value())
        self.assertEqual(0, self.form.ui.curveSpinBox.value())
        self.form.ui.curveSpinBox.setValue(370)
        self.assertEqual(360, self.form.ui.curveSlider.value())
        self.assertEqual(360, self.form.ui.curveSpinBox.value())

    def test_curve_change(self):
        """Test change curve (Slider and Spinbox)"""
        self.form.ui.curveSlider.setValue(1)
        self.assertEqual(round(self.form.ui.curveSlider.value()),
                         round(self.form.ui.curveSpinBox.value()))
        self.form.ui.curveSpinBox.setValue(300)
        self.assertEqual(round(self.form.ui.curveSlider.value()),
                         round(self.form.ui.curveSpinBox.value()))

    def test_border_radio(self):
        """Test border radio button"""
        self.form.ui.borderYesRadioButton.setChecked(True)
        self.assertEqual(False, self.form.ui.borderNoRadioButton.isChecked())

        self.form.ui.borderNoRadioButton.setChecked(True)
        self.assertEqual(False, self.form.ui.borderYesRadioButton.isChecked())

    def test_format_radio(self):
        """Test border radio button"""
        self.form.ui.binaryFormatRadioButton.setChecked(True)
        self.assertEqual(False, self.form.ui.asciiFormatRadioButton.isChecked())

        self.form.ui.asciiFormatRadioButton.setChecked(True)
        self.assertEqual(False,
                         self.form.ui.binaryFormatRadioButton.isChecked())
    # endregion


if __name__ == "__main__":
    # unittest.TextTestRunner(verbosity=2)

    suite = unittest.TestLoader().loadTestsFromTestCase(Test_UI)
    ColourTextTestRunner(verbosity=2).run(suite)
