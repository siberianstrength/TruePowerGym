from matplotlib.image import imsave  
import cv2
import numpy as np

def gen(cap):
    while(cap.isOpened()):
        ret, frame = cap.read()
        try:
            a = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            yield a
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        except:
            break
def generate_images():
    with open('C:/Users/komme/Desktop/Study/Андрианова 3_2/back0.png') as back:
        if back:
            print("Already exists")
            return 
    cap = cv2.VideoCapture('C:/Users/komme/Desktop/Study/Андрианова 3_2/mixkit-rendering-of-a-black-hole-rotating-in-the-darkness-of-45020-medium.mp4')
    i = 0
    for j in gen(cap):
        try:
            imsave(f'back{i}.png', j)
            i+=1
        except AttributeError:
            print(1)
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    generate_images()