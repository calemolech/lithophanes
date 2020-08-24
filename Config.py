import constants as const


class Config:
    def __init__(self, shape=const.DEFAULT_SHAPE, size=const.DEFAULT_SIZE,
                 max_thick=const.MAXIMUM_THICKNESS,
                 min_thick=const.MINIMUM_THICKNESS,
                 use_border=const.DEFAULT_BORDER,
                 border_thick=const.DEFAULT_BORDER_THICKNESS,
                 curve=const.DEFAULT_CURVE):
        self.shape = shape
        self.size = size
        self.max_thickness = max_thick
        self.min_thickness = min_thick
        self.use_border = use_border
        self.border_thickness = border_thick
        self.curve = curve

    def get_config(self, shape_type):
        return self
