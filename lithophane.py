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


    def process_image(self):
        return 1

    # TODO: 1. Load image with opencv

    # TODO: 2. Scale image
    @staticmethod
    def scale_image(image, width_mm=40):
        """Scale image to 0.1 pixel width

        Will make an image with 1000 pixels wide.
        The height will be scale proportionally
        """
        height = image.shape[0]
        width = image.shape[1]
        scale = (width_mm * 10 / width)
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
    def image2points(self, width='', max_thickness=3.0, min_thickness=0.5, show=True):
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
        if (show):
            cv2.namedWindow('image', cv2.WINDOW_NORMAL)
            cv2.imshow('image', self.gray)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        # print(np.max(g))
        # print(g.shape)

        # Invert threshold for z matrix
        ngray = 1 - np.double(self.gray)

        # scale z matrix to desired max depth and add base height
        z_middle = ngray * depth + offset

        # add border of zeros to help with back.
        z = np.zeros([z_middle.shape[0] + 2, z_middle.shape[1] + 2])
        z[1:-1, 1:-1] = z_middle

        x1 = np.linspace(1, z.shape[1], z.shape[1])
        y1 = np.linspace(1, z.shape[0], z.shape[0])

        x, y = np.meshgrid(x1, y1)

        x = np.fliplr(x)
        return x, y, z

    @staticmethod
    def testmesh(x,y,z):
        point_cloud = np.dstack((x, y, x))
        return point_cloud

    @staticmethod
    def makemesh(x, y, z):
        '''Convert point cloud grid to mesh'''
        count = 0
        points = []
        triangles = []
        for i in range(z.shape[0] - 1):
            for j in range(z.shape[1] - 1):
                # Triangle 1
                points.append([x[i][j], y[i][j], z[i][j]])
                points.append([x[i][j + 1], y[i][j + 1], z[i][j + 1]])
                points.append([x[i + 1][j], y[i + 1][j], z[i + 1][j]])

                triangles.append([count, count + 1, count + 2])

                # Triangle 2
                points.append([x[i][j + 1], y[i][j + 1], z[i][j + 1]])
                points.append([x[i + 1][j + 1], y[i + 1][j + 1], z[i + 1][j + 1]])
                points.append([x[i + 1][j], y[i + 1][j], z[i + 1][j]])

                triangles.append([count + 3, count + 4, count + 5])

                count += 6

        # BACK
        for j in range(x.shape[1] - 1):
            bot = x.shape[0] - 1

            # Back Triangle 1
            points.append([x[bot][j], y[bot][j], z[bot][j]])
            points.append([x[0][j + 1], y[0][j + 1], z[0][j + 1]])
            points.append([x[0][j], y[0][j], z[0][j]])

            triangles.append([count, count + 1, count + 2])

            # Triangle 2
            points.append([x[bot][j], y[bot][j], z[bot][j]])
            points.append([x[bot][j + 1], y[bot][j + 1], z[bot][j + 1]])
            points.append([x[0][j + 1], y[0][j + 1], z[0][j + 1]])

            triangles.append([count + 3, count + 4, count + 5])

            count += 6

        # Create the mesh
        model = mesh.Mesh(np.zeros(len(triangles), dtype=mesh.Mesh.dtype))
        for i, f in enumerate(triangles):
            for j in range(3):
                model.vectors[i][j] = points[f[j]]

        return model

    @staticmethod
    def point_cloud(self, depth):
        """Transform a depth image into a point cloud with one point for each
        pixel in the image, using the camera transform for a camera
        centred at cx, cy with field of view fx, fy.

        depth is a 2-D ndarray with shape (rows, cols) containing
        depths from 1 to 254 inclusive. The result is a 3-D array with
        shape (rows, cols, 3). Pixels with invalid depth in the input have
        NaN for the z-coordinate in the result.

        """
        rows, cols = depth.shape
        c, r = np.meshgrid(np.arange(cols), np.arange(rows), sparse=True)
        valid = (depth > 0) & (depth < 255)
        z = np.where(valid, depth / 256.0, np.nan)
        x = np.where(valid, z * (c - self.cx) / self.fx, 0)
        y = np.where(valid, z * (r - self.cy) / self.fy, 0)
        return np.dstack((x, y, z))

class Lithophane:
    def __index__(self):
        self.thickness = 1


