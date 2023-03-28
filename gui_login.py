# C:\Users\komme\Desktop\Study\Андрианова 3_2
import arcade
import arcade.gui
from time import sleep
import numpy as np
from gui_main import MainWindow
# import imgenerator


class GuiWindow(arcade.View):
    def __init__(self, my_window: arcade.Window, fullscreen = True):
        super().__init__(my_window)
        self.set_location = (0, 0)
        self.width = 1920
        self.height = 1080
        self.ui_manager = arcade.gui.UIManager(self.window)
        self.ui_manager.enable()
        self.buttons_array = []
        self.i = 0
        self.di = 1
        self.xpos1 = self.width//2.25-self.width//8
        self.xpos2 = self.width//1.65-self.width//8
        self.ypos1 = self.height//2.5-self.height//5
        self.ypos2 = self.height//2.5-self.height//24-self.height//5
        self.xpos3 = self.width//2.25+self.width//16
        self.xpos4 = self.width//1.65+self.width//16
        self.passwidth = self.logwidth = self.width//1.65-self.width//2.25
        self.passheight = self.logheight =self.height//2.5-self.height//5
        
        self.insys = False
        
        
        self.login = arcade.gui.UIInputText(
            x = self.xpos1,
            text_color= black,
            font_name = ('Yu Gothic'), # Control Panel\All Control Panel Items\Fonts, 
            font_size = 24,
            width = self.logwidth,
            height = self.logheight,
            text='Login')
        self.buttons_array.append(self.login)
 
        
        self.password = arcade.gui.UIInputText(
            x = self.xpos3,
            text_color = black,
            font_name = ('Yu Gothic'), # Control Panel\All Control Panel Items\Fonts, 
            font_size = 24,
            width = self.passwidth,
            height = self.passheight,
            text='Password')
        self.buttons_array.append(self.password)
       
        
        self.buttonx = self.width//2.25+self.width//68
        self.buttony = self.height//11
        self.buttonwidth = self.width//15
        self.submit_button = arcade.gui.UIFlatButton(
            x = self.buttonx,
            y = self.buttony,
            width = self.buttonwidth,
            text='Submit')
        self.buttons_array.append(self.submit_button)
        self.submit_button.on_click = self.submit_data
        
        for each in self.buttons_array:
            self.ui_manager.add(each)


    def on_draw(self):
        if not self.insys:
            sleep(.02)
            arcade.start_render()
            self.background = arcade.load_texture(f'back{self.i}.png')
            arcade.draw_texture_rectangle(self.width//2, self.height//2, 1920, 1080, self.background)
            self.i += self.di
            if self.i == 239 or self.i == 0:
                self.di = -self.di
            arcade.draw_lrtb_rectangle_filled(self.xpos1, self.xpos2, self.ypos1, self.ypos2, white)
            arcade.draw_lrtb_rectangle_outline(self.xpos1, self.xpos2, self.ypos1, self.ypos2, grey, border_width= 3)
            arcade.draw_lrtb_rectangle_filled(self.xpos3, self.xpos4, self.ypos1, self.ypos2, white)
            arcade.draw_lrtb_rectangle_outline(self.xpos3, self.xpos4, self.ypos1, self.ypos2, grey, border_width= 3)
            self.ui_manager.draw()
        else:
            arcade.start_render()
            self.background = arcade.set_background_color(grey)

            
    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            if not self.insys:
                if y < self.ypos1 and y > self.ypos2:
                    if x > self.xpos1 and x < self.xpos2:
                        self.login.text = ''
                    elif x > self.xpos3 and x < self.xpos4:
                        self.password.text = ''    
                    
    def submit_data(self, *_):
        if self.login.text != 'Login' and self.password.text != 'Password':
            self.isValid = True
            for each in self.login.text:
                if not ((ord(each) >= 97 and ord(each) <= 122) or (ord(each) >= 65 and ord(each) <= 90)):
                    self.isValid = False
                    print("data is invalid")
                    break
            if self.isValid:
                print('data is valid')
                self.check_data(self.login.text, self.password.text)
        
    def check_data(self, login, password):
        with open('C:/Users/komme/Desktop/Study/Андрианова 3_2/customers_login_info.txt', 'r') as file:
            data = np.array([line.split() for line in file.readlines()])
            for each in data:
                if login == each[0]:
                    if password == each[1]:
                        print('in')
                        self.insys = True
                        self.username = each[0]
                        self.surname = each[1]
                        self.ui_manager.disable()
                        

        
if __name__ == "__main__":
    # generate_images()
    white = arcade.color.WHITE
    grey = arcade.color.ASH_GREY
    black = arcade.color.BLACK
    window = arcade.Window(1920, 1080, title="Deam", fullscreen = True)
    window.show_view(GuiWindow(window))
    arcade.run()
    arcade.close_window()

