import cv2

class Config:
    def __init__(self):
        self.templates = {
            'mario' :'images/templates/mario.png',
            'enemy1':'images/templates/enemy1.png',
            'obs1'  :'images/templates/obs1.png',
            'obs2'  :'images/templates/obs2.png',
            'brick' :'images/templates/brick.png'
        }

        self.colors = {
            'mario': (245, 93, 66),
            'obs1': (123, 66, 245),
            'obs2': (123, 66, 245),
            'brick': (123, 66, 245),
            'enemy1': (105, 245, 66)
        }

        self.methods = {
            'CCOEFF':cv2.TM_CCOEFF, 
            'CCOEFF_NORMED':cv2.TM_CCOEFF_NORMED, 
            'CCORR':cv2.TM_CCORR,
            'CCORR_NORMED':cv2.TM_CCORR_NORMED, 
            'SQDIFF':cv2.TM_SQDIFF, 
            'SQDIFF_NORMED':cv2.TM_SQDIFF_NORMED
        }

        self.method = self.methods['CCOEFF_NORMED']
    
    def get_templates(self):
        return self.templates
    
    def get_colors(self):
        return self.colors
    
    def get_method(self):
        return self.method