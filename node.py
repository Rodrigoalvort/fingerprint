import glob 
import cv2

class  node:

    def __init__(self,path):

        self.position = path
        self.subnodes  =[]





"""import os
cnt = 0
for root, dirs, files in os.walk("C:\Users", topdown=True):
   for name in files:
      cnt +=1
   for name in dirs:
      cnt +=1
print(cnt)
"""

import pyscreenshot as ImageGrab
import time
if __name__ == '__main__':

    # grab fullscreen
    time.sleep(3)
    im = ImageGrab.grab()

    # save image file
    im.save('screenshot1.png')

    # show image in a window
    im.show()