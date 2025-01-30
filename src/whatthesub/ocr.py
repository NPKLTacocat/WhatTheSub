import easyocr
import cv2


class OCRProcessor:
    def __init__(self, languages=["en"]):
        self.reader = easyocr.Reader(languages)

    def extract_text(self, frame):
        """Extract text from image frame"""
        results = self.reader.readtext(frame, paragraph=True)
        return " ".join([res[1] for res in results])
