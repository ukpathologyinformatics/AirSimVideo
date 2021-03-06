import cv2
import numpy as np
import glob


video_length = 100
video_frames = []
video_folder = "videos"
image_folder = "images"

"""
 Example of building a video from these frames. 

 Capturing individual frames is helpful for debugging. This could be moved to
 the main loop, but would require some more futzing with the data before passing
 it to VideoWriter
"""   

filenames = sorted(glob.glob(image_folder+"/*.png"))
for filename in filenames:
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    video_frames.append(img)

# Creating a video from all the images. This is separate from main loop for debugging
out = cv2.VideoWriter(video_folder + "/drone_video.mp4", cv2.VideoWriter_fourcc(*'MP4V'), 15, size)
for frame in video_frames:
    out.write(frame)
out.release()
