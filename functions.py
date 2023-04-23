from matplotlib.image import imsave  
import cv2
import numpy as np
import arcade

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



class Buttons(arcade.View):
    def add_texture_button(texture_file_name: str,
                           hover_texture_file_name: str,
                           press_texture_file_name: str,
                           _scale: float = 1,
                           _x: float = 0,
                           _y: float = 0):
        normal_texture = arcade.load_texture(texture_file_name)
    
        hover_texture = arcade.load_texture(hover_texture_file_name)
    
        press_texture = arcade.load_texture(press_texture_file_name)
    
        return arcade.gui.UITextureButton(
            x=_x,
            y=_y,
            texture=normal_texture,
            texture_hovered=hover_texture,
            texture_pressed=press_texture,
            scale=_scale
        )



if __name__ == "__main__":
    pass
    