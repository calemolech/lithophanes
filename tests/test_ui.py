import os
import unittest
import sys

import HtmlTestRunner
from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication

from app.ui_app import UIApp
from config import Config
from lithophane import Lithophane

app = QApplication(sys.argv)


class TestUi(unittest.TestCase):
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = os.path.split(curPath)[0]
    sys.path.append(rootPath)
    """Test the GUI"""

    def setUp(self):
        """Create the GUI"""
        self.form = UIApp()

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
        QTest.keyClick(shape_combo_box, Qt.Key_PageUp)
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

    # region Test UI App
    def test_get_ui_config(self):
        actual_config = self.form.get_ui_config()
        expected_config = Config()
        self.assertEqual(expected_config.size, actual_config.size)
        self.assertEqual(expected_config.max_thickness,
                         actual_config.max_thickness)
        self.assertEqual(expected_config.min_thickness,
                         actual_config.min_thickness)
        self.assertEqual(expected_config.use_border, actual_config.use_border)
        self.assertEqual(expected_config.border_thickness,
                         actual_config.border_thickness)
        self.assertEqual(expected_config.curve, actual_config.curve)
        self.assertEqual(expected_config.format, actual_config.format)

    def test_update_config_by_shape_flat(self):
        self.form.ui.shapeComboBox.setCurrentIndex(0)
        self.form.update_config_by_shape()
        self.assertEqual(False, self.form.ui.curveSpinBox.isEnabled())

    def test_update_config_by_shape_cylinder(self):
        self.form.ui.shapeComboBox.setCurrentIndex(1)
        self.form.update_config_by_shape()
        self.assertEqual(360, self.form.ui.curveSpinBox.value())
        self.assertEqual(False, self.form.ui.curveSpinBox.isEnabled())

    def test_update_config_by_shape_curve(self):
        self.form.ui.shapeComboBox.setCurrentIndex(2)
        self.form.update_config_by_shape()
        self.assertEqual(True, self.form.ui.curveSpinBox.isEnabled())

    def test_update_config_by_shape_heart(self):
        self.form.ui.shapeComboBox.setCurrentIndex(3)
        self.form.update_config_by_shape()
        self.assertEqual(360, self.form.ui.curveSpinBox.value())
        self.assertEqual(False, self.form.ui.curveSpinBox.isEnabled())

    def test_full_screen(self):
        self.form.hide()
        self.assertEqual(False, self.form.isFullScreen())
        self.form.full_screen()
        self.form.close()
        self.assertEqual(True, self.form.isFullScreen())

    def test_show_normal(self):
        self.form.hide()
        self.form.show_normal()
        self.form.close()
        self.assertEqual(False, self.form.isFullScreen())

    def test_select_image(self):
        file_name = "test_images/a.jpg"
        self.form.image2d = Lithophane(file_name)
        self.assertNotEqual(None, self.form.image2d)

    def test_render(self):
        file_name = "test_images/a.jpg"
        self.form.ui.lineImagePath.setText(file_name)
        self.form.image2d = Lithophane(file_name)
        self.form.render_file()
        self.assertNotEqual(None, self.form.model)
    # endregion


if __name__ == "__main__":
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestUi)
    # ColourTextTestRunner(verbosity=2).run(suite)

    # HTML Report
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        verbosity=2,
        combine_reports=True,
        output="test_results",
        report_title="Report Unittest UI",
        report_name="Report_Unittest_UI",
        add_timestamp=False))
