import unittest

import HtmlTestRunner

from app.config import Config
from app.constants import *


class TestConfig(unittest.TestCase):
    """Test Config"""
    def setUp(self):
        self.config = Config()

    def test_default_config(self):
        """Test init default config"""
        self.assertEqual(DEFAULT_CONFIG_SHAPE, self.config.shape)
        self.assertEqual(DEFAULT_CONFIG_SIZE, self.config.size)
        self.assertEqual(MAXIMUM_CONFIG_THICKNESS, self.config.max_thickness)
        self.assertEqual(MINIMUM_CONFIG_THICKNESS, self.config.min_thickness)
        self.assertEqual(DEFAULT_CONFIG_BORDER, self.config.use_border)
        self.assertEqual(DEFAULT_CONFIG_BORDER_THICKNESS,
                         self.config.border_thickness)
        self.assertEqual(DEFAULT_CONFIG_CURVE, self.config.curve)
        self.assertEqual(DEFAULT_CONFIG_FORMAT, self.config.format)

    def test_get_config(self):
        actual_config = self.config.get_config()
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


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestConfig)
    # ColourTextTestRunner(verbosity=2).run(suite)

    # HTML Report
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        verbosity=2,
        combine_reports=True,
        output="test_results",
        report_title="Report Unittest Config",
        report_name="Report_Unittest_Config",
        add_timestamp=False))