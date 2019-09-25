# import cv2
from config import *
import numpy as np
from matplotlib import pyplot as plt

class TemplateMatching:
    def __init__(self, *args, **kwargs):
        '''
        Load templates which will be used for multiple frames.
        Templates defined in config file
        '''
        self.templates = dict()
        self.template_dims = dict()
        self.config = Config()
        self.load_templates()

    def load_templates(self):
        for name, loc in self.config.get_templates().items():
            img = cv2.imread(loc, 0) #0:Grayscale, 1:RGB without trasparency, -1:without alpha channel

            if img is not None:
                self.templates[name] = img 

        self.template_dims = {name: template.shape[::-1] for name, template in self.templates.items()}

    def match_templates(self, frame):
        img_rgb = cv2.imread('images/frame.png')
        img_rgb = img_rgb.copy() #Dont modify frame inplace
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        colors = self.config.get_colors()

        for name, template in self.templates.items():
            res = cv2.matchTemplate(img_gray, template, self.config.get_method())
            threshold = 0.8#TODO Move to config
            loc = np.where(res >= threshold)

            w,h = self.template_dims[name]
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), colors[name], cv2.FILLED)

        return img_rgb

    def process_results(self, img):
        cv2.imwrite('images/res.png',img)

if __name__=='__main__':
    tm = TemplateMatching()
    res_img = tm.match_templates('test')
    tm.process_results(res_img)
