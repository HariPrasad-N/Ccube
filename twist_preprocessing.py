import cv2
import numpy as np
import os

def twist(img):
	return cv2.flip(img,1)

def showImage(img):
	cv2.imshow('',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def readImg(path):
	img = cv2.imread(str(path))
	return img

def destination(outputFile,img):
	cv2.imwrite(outputFile, img)

if __name__ == '__main__':
	
	img_path = '/home/shivsj/CCC/twist'
	dest_path = "/home/shivsj/CCC/normal/"
	for i in os.listdir(img_path):
		a = readImg(img_path+'/'+i)		
		a = twist(a)
		#print(dest_path+i)
		destination(dest_path+i,a)
	