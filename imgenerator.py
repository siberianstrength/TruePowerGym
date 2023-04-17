from matplotlib.image import imsave  
import cv2
import numpy as np

def gen(cap):
    while(cap.isOpened()):
        ret, frame = cap.read()
        try:
            a = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            yield a
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        except:
            break
def generate_images():
    try:
        with open('bg_files/back0.png') as back:
            if back:
                print("Already exists")
                return 
    except FileNotFoundError:
        ...
    cap = cv2.VideoCapture('bg_files/black_hole.mp4')
    i = 0
    for j in gen(cap):
        try:
            imsave(f'bg_files/back{i}.png', j)
            i+=1
        except AttributeError:
            ...
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    generate_images()