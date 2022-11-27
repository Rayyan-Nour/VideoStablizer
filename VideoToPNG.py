import cv2
KPS = 60# Target Keyframes Per Second
VIDEO_PATH = "D:/AIM_GAN_Model/PersonalTest/stable/0.avi"#"path/to/video/folder" # Change this
IMAGE_PATH = "D:/AIM_GAN_Model/PersonalTest/FrameStable/Video0/"#"path/to/image/folder" # ...and this 
EXTENSION = ".png"
cap = cv2.VideoCapture(VIDEO_PATH)
fps = round(cap.get(cv2.CAP_PROP_FPS))
print(fps)
# exit()
hop = round(fps / KPS)
curr_frame = 0
while(True):
    ret, frame = cap.read()
    if not ret: 
        break
    if curr_frame % hop == 0:
        name = IMAGE_PATH + "_" + str(curr_frame) + EXTENSION
        cv2.imwrite(name, frame)
        curr_frame += 1
cap.release()