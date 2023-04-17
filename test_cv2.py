import numpy as np
import cv2
import matplotlib.pyplot as plt 
from matplotlib.image import imsave 

cap = cv2.VideoCapture('C:/Users/komme/Desktop/Study/Андрианова 3_2/mixkit-rendering-of-a-black-hole-rotating-in-the-darkness-of-45020-medium.mp4')

# def f():
#     while(cap.isOpened()):
#         ret, frame = cap.read()
#         try:
#             gray = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
#             cv2.imshow('frame',gray)
#             if cv2.waitKey(25) & 0xFF == ord('q'):
#                 break
#         except:
#             break
#     cap.release()
#     cv2.destroyAllWindows()

# a = np.zeros((1920, 1080)) 
# b = np.zeros((1920,1080))

# value = np.in1d(a,b)
# if False in value:
#     print("F")
def gen():
    while(cap.isOpened()):
        ret, frame = cap.read()
        try:
            a = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            yield a
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        except:
            break
i = 0
for j in gen():
    try:
        imsave(f'back{i}.png', j)
        i+=1
    except AttributeError:
        print(1)

cap.release()
cv2.destroyAllWindows()
