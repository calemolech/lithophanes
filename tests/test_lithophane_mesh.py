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

    def __init__(self, *args, **kwargs):
        super(TestLithophane, self).__init__(*args, **kwargs)
        self.test_image_path = "test_images/a.jpg"
        self.litho = Lithophane(self.test_image_path)
        self.x, self.y, self.z = self.litho.image2points(width=100)

    def test_make_shape_cylinder(self):
        """Test make shape"""
        # Skip because very difficult to check input and output of this function
        nx, ny, nz = self.litho.make_shape(self.x, self.y, self.z, 360, "Cylinder")
        self.assertEqual(self.x.shape, nx.shape)
        self.assertEqual(self.y.shape, ny.shape)
        self.assertEqual(self.z.shape, nz.shape)

    def test_make_shape_heart(self):
        """Test make shape"""
        # Skip because very difficult to check input and output of this function
        nx, ny, nz = self.litho.make_shape(self.x, self.y, self.z, 360, "Heart")
        self.assertEqual(self.x.shape, nx.shape)
        self.assertEqual(self.y.shape, ny.shape)
        self.assertEqual(self.z.shape, nz.shape)

    def test_make_shape_curve(self):
        """Test make shape"""
        # Skip because very difficult to check input and output of this function
        nx, ny, nz = self.litho.make_shape(self.x, self.y, self.z, 0, "Curve")
        self.assertEqual(self.x.shape, nx.shape)
        self.assertEqual(self.y.shape, ny.shape)
        self.assertEqual(self.z.shape, nz.shape)

    def test_make_shape_curve2(self):
        """Test make shape"""
        # Skip because very difficult to check input and output of this function
        nx, ny, nz = self.litho.make_shape(self.x, self.y, self.z, 270, "Curve")
        self.assertEqual(self.x.shape, nx.shape)
        self.assertEqual(self.y.shape, ny.shape)
        self.assertEqual(self.z.shape, nz.shape)

    def test_make_mesh(self):
        """Test make shape"""
        # Skip because very difficult to check input and output of this function
        model = self.litho.make_mesh(self.x, self.y, self.z)
        width = self.z.shape[0] - 1
        height = self.z.shape[1] - 1
        triangles_count = width * height * 2 + height * 2
        expected = (triangles_count, 3, 3)
        np.testing.assert_array_equal(expected, model.vectors.shape)


if __name__ == "__main__":
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestLithophane)
    # ColourTextTestRunner(verbosity=2).run(suite)

    # HTML Report
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        verbosity=2,
        combine_reports=True,
        output="test_results",
        report_title="Report Unittest Lithophane Mesh",
        report_name="Report_Unittest_Lithophane_Mesh",
        add_timestamp=False))
