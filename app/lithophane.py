import cv2
import numpy as np
from stl import mesh


class Lithophane:
    def __init__(self, image_path, positive=True, mirror=False, flip=False):
        self.image = cv2.imread(image_path)
        self.processed_image = None
        self.gray = None
        self.positive = positive
        self.mirror = mirror
        self.flip = flip

    def scale_image(self, image, width_mm=400):
        """Scale image to 0.1 pixel width

        Example: im_scaled = scale_image(image, width_mm = 1000)

        Will make an image with 1000 pixels wide.
        The height will be scale proportionally
        :param image: input image
        :param width_mm: expected width
        :return: resized image
        """

        height = image.shape[0]
        width = image.shape[1]
        scale = (width_mm / width)
        new_size = (int(width * scale), int(height * scale))
        output = cv2.resize(image, new_size, interpolation=cv2.INTER_CUBIC)
        return output

    def rgb_to_gray(self, image):
        """
        Convert rgb image to grayscale image in range 0-1
        :param image: original image
        :return: gray image
        """
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray

    def flip_image(self, image):
        """
        Flip image
        """
        return cv2.flip(image, 1)

    def add_border(self, image, border_thickness):
        border_thickness = int(border_thickness)
        border_image = cv2.copyMakeBorder(
             image,
             border_thickness,
             border_thickness,
             border_thickness,
             border_thickness,
             cv2.BORDER_CONSTANT,
             value=[0, 0, 0]
          )
        return border_image

    def image2points(self, width='', max_thickness=3.0, min_thickness=0.5,
                     use_border=False, border_thickness=0):
        """
        Convert image to point clouds
        :param border_thickness:
        :param use_border:
        :param width: Expected width
        :param max_thickness: maximum thickness
        :param min_thickness: minimum thickness
        :return: Coordinate in 3 dimension x, y, z
        """
        depth = max_thickness
        offset = min_thickness

        if width == '':
            width = self.image.shape[1]

        # TODO: Width is actually height
        self.processed_image = self.scale_image(self.image, width_mm=width)

        if use_border and border_thickness > 0:
            self.processed_image = self.add_border(self.processed_image, border_thickness)

        # Convert to grayscale
        if len(self.processed_image.shape) == 3:
            self.gray = self.rgb_to_gray(self.processed_image)
        else:
            self.gray = self.processed_image

        self.gray = self.gray / 255.0

        # Invert threshold for z matrix
        ngray = 1 - np.double(self.gray)

        # scale z matrix to desired max depth and add base height
        z_middle = ngray * (depth - offset) + offset

        # add border of zeros to help with back.
        z = np.zeros([z_middle.shape[0] + 2, z_middle.shape[1] + 2])
        z[1:-1, 1:-1] = z_middle

        x1 = np.linspace(1, z.shape[1], z.shape[1])
        y1 = np.linspace(1, z.shape[0], z.shape[0])

        x, y = np.meshgrid(x1, y1)

        # x = np.fliplr(x)
        y = np.flipud(y)
        return x, y, z

    def make_mesh(self, x, y, z):
        """
         Convert point cloud grid to mesh
        :param x: Array of x coordinate
        :param y: Array of y coordinate
        :param z: Array of z coordinate
        :return: mesh.Mesh()
        """
        count = 0
        width = z.shape[0] - 1
        height = z.shape[1] - 1
        triangles_count = width * height * 2 + height * 2
        model = mesh.Mesh(np.zeros(triangles_count, dtype=mesh.Mesh.dtype))

        for i in range(z.shape[0] - 1):
            for j in range(z.shape[1] - 1):
                # Triangle 1
                model.vectors[count] = np.array([
                    [x[i][j], y[i][j], z[i][j]],
                    [x[i][j + 1], y[i][j + 1], z[i][j + 1]],
                    [x[i + 1][j], y[i + 1][j], z[i + 1][j]]])

                # Triangle 2
                model.vectors[count + 1] = np.array([
                    [x[i][j + 1], y[i][j + 1], z[i][j + 1]],
                    [x[i + 1][j + 1], y[i + 1][j + 1], z[i + 1][j + 1]],
                    [x[i + 1][j], y[i + 1][j], z[i + 1][j]]])

                count += 2

        # BACK
        for j in range(x.shape[1] - 1):
            bot = x.shape[0] - 1

            model.vectors[count] = np.array([
                [x[bot][j], y[bot][j], z[bot][j]],
                [x[0][j + 1], y[0][j + 1], z[0][j + 1]],
                [x[0][j], y[0][j], z[0][j]]])

            model.vectors[count + 1] = np.array([
                [x[bot][j], y[bot][j], z[bot][j]],
                [x[bot][j + 1], y[bot][j + 1], z[bot][j + 1]],
                [x[0][j + 1], y[0][j + 1], z[0][j + 1]]])

            count += 2
        return model

    def make_shape(self, x, y, z, curve, shape):
        """
        Convert from flat to other shape (Cylinder, Curve, Heart)
        :param x: Array of x coordinate
        :param y: Array of y coordinate
        :param z: Array of z coordinate
        :param curve: Curve in degree (0-360)
        :param shape: Expected shape (Cylinder, Curve, Heart)
        :return: Shape coordinate in xyz coordinate
        """
        newx = x.copy()
        newz = z.copy()

        # If type = cylinder , overlap offset =1
        if shape == 'Cylinder':
            overlap_offset = 2
        else:
            overlap_offset = 0

        width = x.shape[1]
        height = x.shape[0]

        if curve == 0:
            return x, y, z
        if curve != 0:
            deg_2_rad = (np.pi / 180)
            angle = abs(curve)
            arc_radius = (width / curve) * (180 / np.pi)
            y_arc_radius = (height / curve) * (180 / np.pi)
            distance_from_flat = np.sin(angle * (360 / np.pi)) * arc_radius
            if angle >= 180:
                distance_from_flat = 0
            start_angle = (0 - angle / 2)

            if curve < 0:
                distance_from_flat = 0 - distance_from_flat

        for i in range(0, height):
            for j in range(0, width):
                degrees_rotated = start_angle + (
                        j / (width - overlap_offset) * angle)
                rotation = degrees_rotated * deg_2_rad
                magnitude = arc_radius + z[i, j]

                # Cylinder, Curve
                if shape in ['Cylinder', 'Curve']:
                    newx[i, j] = width / 2 + magnitude * np.cos(rotation)
                    newz[i, j] = distance_from_flat + magnitude * np.sin(
                        rotation)

                # Heart
                if shape == 'Heart':
                    newx[i, j] = width / 2 + magnitude * ((16 * np.sin(
                        rotation) * np.sin(rotation) * np.sin(rotation)) / 16)

                    newz[i, j] = distance_from_flat + magnitude * ((13 * np.cos(
                        rotation) - 5 * np.cos(2 * rotation) - 2 * np.cos(
                        3 * rotation) - np.cos(4 * rotation)) / 16)

        return newz, y.copy(), newx