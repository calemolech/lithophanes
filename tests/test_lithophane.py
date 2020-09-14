import os
import sys
import unittest
import copy

import HtmlTestRunner
import cv2
import numpy as np
from app.lithophane import Lithophane


class TestLithophane(unittest.TestCase):
    """Test Lithophane class"""
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = os.path.split(curPath)[0]
    sys.path.append(rootPath)

    @classmethod
    def setUp(self):
        """Init class with default image"""
        test_image_path = "test_images/a.jpg"
        self.litho = Lithophane(test_image_path)

    def test_scale_image(self):
        """Test scale image"""
        expect_width = 400
        image = copy.copy(self.litho.image)
        actual = self.litho.scale_image(image, expect_width)
        self.assertEqual(expect_width, actual.shape[1])

    def test_rgb_to_gray(self):
        """Test convert rgb to gray"""
        expected_channel = 2
        actual = self.litho.rgb_to_gray(self.litho.image)
        self.assertEqual(expected_channel, actual.ndim)

    def test_flip(self):
        """Test flip image vertical"""
        expected = cv2.flip(self.litho.image, 1)
        actual = self.litho.flip_image(self.litho.image)
        np.testing.assert_array_equal(expected, actual)

    def test_add_border(self):
        """Test add border to original image"""
        border_thickness = 10
        expected = cv2.copyMakeBorder(
            self.litho.image,
            border_thickness,
            border_thickness,
            border_thickness,
            border_thickness,
            cv2.BORDER_CONSTANT,
            value=[0, 0, 0]
        )
        actual = self.litho.add_border(self.litho.image, border_thickness)
        np.testing.assert_array_equal(expected, actual)
        self.assertEqual(actual.shape[0], self.litho.image.shape[0] +
                         2 * border_thickness)
        self.assertEqual(actual.shape[1], self.litho.image.shape[1] +
                         2 * border_thickness)
        self.assertEqual(actual.shape[2], self.litho.image.shape[2])

    def test_image_to_points(self):
        """Test convert image to points cloud"""
        actual = self.litho.image2points()
        expected_shape = np.add(self.litho.image.shape[:2], (2, 2))
        np.testing.assert_array_equal(actual[0].shape, expected_shape)
        np.testing.assert_array_equal(actual[1].shape, expected_shape)
        np.testing.assert_array_equal(actual[2].shape, expected_shape)


if __name__ == "__main__":
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestLithophane)
    # ColourTextTestRunner(verbosity=2).run(suite)

    # HTML Report
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        verbosity=2,
        combine_reports=True,
        output="test_results",
        report_title="Report Unittest Lithophane",
        report_name="Report_Unittest_Lithophane",
        add_timestamp=False))
