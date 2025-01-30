from mss import mss
import numpy as np
import cv2


class ScreenCapturer:
    def __init__(self, region=None):
        self.sct = mss()
        self.region = region or {"top": 0, "left": 0, "width": 1920, "height": 1080}

    def capture_frame(self):
        """Capture screen frame as numpy array"""
        frame = np.array(self.sct.grab(self.region))
        return cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
