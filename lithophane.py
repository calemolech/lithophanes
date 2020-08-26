import cv2
import numpy as np
from stl import mesh


class ImageMap:
    def __init__(self, image_path, positive=True, mirror=False, flip=False):
        self.image = cv2.imread(image_path)
        self.gray = None
        self.positive = positive
        self.mirror = mirror
        self.flip = flip

    @staticmethod
    def process_image(self):
        return 1

    # TODO: 1. Load image with opencv

    # TODO: 2. Scale image
    @staticmethod
    def scale_image(image, width_mm=400):
        """Scale image to 0.1 pixel width

        Will make an image with 1000 pixels wide.
        The height will be scale proportionally
        """
        height = image.shape[0]
        width = image.shape[1]
        scale = (width_mm / width)
        new_size = (int(width * scale), int(height * scale))
        output = cv2.resize(image, new_size, interpolation=cv2.INTER_CUBIC)
        return output

    # TODO: 3. Convert to gray
    @staticmethod
    def rgb_to_gray(image):
        """
        Convert rgb image to grayscale image in range 0-1
        """
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray

    # TODO: 4. Flip image (optional)
    def flip_image(self):
        if self.flip:
            self.image = cv2.flip(self.image, 1)
        return self

    # TODO: 5. Convert2D image to CloudPoint
    def image2points(self, width='', max_thickness=3.0, min_thickness=0.5):
        depth = max_thickness
        offset = min_thickness

        if width == '':
            width = self.image.shape[1]

        # TODO: Width is actually height
        self.image = self.scale_image(self.image, width_mm=width)

        # Convert to grayscale
        if len(self.image.shape) == 3:
            self.gray = self.rgb_to_gray(self.image)
        else:
            self.gray = self.image

        self.gray = self.gray / 255.0

        # g = np.fliplr(g)
        # if (show):
        #     cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        #     cv2.imshow('image', self.gray)
        #     cv2.waitKey(0)
        #     cv2.destroyAllWindows()

        # print(np.max(g))
        # print(g.shape)

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

    @staticmethod
    def make_mesh(x, y, z):
        """ Convert point cloud grid to mesh """
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

    @staticmethod
    def make_shape(x, y, z, curve, shape):
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
            deg2Rad = (np.pi / 180)
            angle = abs(curve)
            arc_radius = (width / curve) * (180 / np.pi)
            y_arc_radius = (height / curve) * (180 / np.pi)
            distance_from_flat = np.sin(angle * (360 / np.pi)) * arc_radius
            if (angle >= 180):
                distance_from_flat = 0
            start_angle = (0 - angle / 2)

            if (curve < 0):
                distance_from_flat = 0 - distance_from_flat

        for i in range(0, height):
            for j in range(0, width):
                jpos = j
                ipos = i

                # if j == 1:
                #     jpos -= 1
                # elif j == (width - 1):
                #     jpos += 1
                # if i == 1:
                #     ipos -= 1
                # elif i == (height - 1):
                #     ipos += 1

                degrees_rotated = start_angle + (
                        jpos / (width - overlap_offset) * angle)
                rotation = degrees_rotated * deg2Rad
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


class Lithophane:
    def __index__(self):
        self.thickness = 1
