import os
from tkinter import *
from PIL import ImageTk,Image
from imageai.Detection import ObjectDetection
import os
import cv2
import matplotlib.pyplot as plt
execution_path=os.getcwd()
#object Detection part
detector=ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath("resnet50_coco_best_v2.0.1.h5")
detector.loadModel()
custom=detector.CustomObjects(person=True,motorcycle=True)
detection=detector.detectCustomObjectsFromImage(custom_objects=custom, input_image=os.path.join(execution_path,"both.jpg")
,output_image_path=os.path.join(execution_path,"output.jpg"),minimum_percentage_probability=50)
def object_detection():
img=cv2.imread('output.jpg')
inn=cv2.imread("both.jpg")
person=[]
for eachObject in detection:
print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
p=eachObject["box_points"]
#plt.imshow(inn[p[1]:p[0],p[3]:p[2]])
point=eachObject["name"]
if point=="person":
person.append(inn[p[1]:p[0],p[3]:p[2]])
