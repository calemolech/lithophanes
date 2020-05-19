import cv2
from skimage.transform import resize


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
        output = cv2.resize(image, (int(height * scale), int(width * scale)), interpolation=cv2.INTER_CUBIC)
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


class Lithophane:
    def __index__(self):
        self.thickness = 1


