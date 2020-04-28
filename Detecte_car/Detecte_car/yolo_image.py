import sys
from yolo_class import YOLO, detect_video
from PIL import Image
import os
import cv2

def detect_img(img,yolo):
    r_image = yolo.detect_image(img)
    return r_image

if __name__ == '__main__':
    # class YOLO defines the default value
    yolo = YOLO()
    FLAG = False
    if FLAG is True:
        for (root, dirs, files) in os.walk('images/test'):
            if files:
                for f in files:
                    print(f)
                    path = os.path.join(root, f)
                    image = Image.open(path)
                    image = detect_img(image, yolo)
                    image.save('images/res/'+f)
        yolo.close_session()
    else:
        # video_path = "./4A.mp4"
        video_path = 0
        # video_path = "rtsp://system:system@192.168.1.4:5504/channel=0;stream=0/ch1-s1?tcp"
        video_save_path = ""
        detect_video(yolo, video_path, video_save_path)
