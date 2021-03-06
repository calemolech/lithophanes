from PyQt5.QtWidgets import QSlider


class QDoubleSlider(QSlider):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set integer max and min. These stay constant.
        super().setMinimum(0)
        self._max_int = 100
        super().setMaximum(self._max_int)

        # The "actual" min and max values seen by user
        self._min_value = 0.1
        self._max_value = 100.0

    @property
    def _value_range(self):
        return self._max_value - self._min_value

    def value(self):
        return float(super().value()) / self._max_int * self._value_range + self._min_value

    def setValue(self, value):
        super().setValue(((value - self._min_value) / self._value_range * self._max_int))

    def setMinimum(self, value):
        if value > self._max_value:
            raise ValueError("Minimum limit cannot be higher than maximum")

        self._min_value = value
        self.setValue(self.value())

    def setMaximum(self, value):
        if value < self._min_value:
            raise ValueError("Minimum limit cannot be higher than maximum")

        self._max_value = value
        self.setValue(self.value())

    def minimum(self):
        return self._min_value

    def maximum(self):
        return self._max_value

    def setMaxInt(self, maximum):
        super().setMaximum(maximum)

    def setMinInt(self, minimum):
        super().setMinimum(minimum)

    def getMinInt(self):
        return super().minimum()

    def getMaxInt(self):
        return super().maximum()