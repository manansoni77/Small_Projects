import cv2
from threading import Thread

class Vidget:
    def __init__(self, src=0):
        self.stream = cv2.VideoCapture(src)
        self.grab, self.frame = self.stream.read()
        self.stop = False
    
    def start(self):
        Thread(target=self.get, args=()).start()
        return self
    
    def get(self):
        while not self.stop:
            if not self.grab:
                self.stop()
            else:
                self.grab, self.frame = self.stream.read()
    
    def stop(self):
        self.stop = True
