# C:\Users\komme\Desktop\Study\Андрианова 3_2
import arcade
import arcade.gui
from time import sleep
import numpy as np
# import imgenerator


class GuiWindow(arcade.View):
    def __init__(self, my_window: arcade.Window, fullscreen = True):
        super().__init__(my_window)
        self.set_location = (0, 0)
        self.width = 1920
        self.height = 1080
        self.buttons_array = []
        self.buttons_array_insys = []
        self.insys = False
        self.background = wenge
        self.sw_2 = self.width//2
        self.sh_2 = self.height//2
        
        self.ui_manager = arcade.gui.UIManager(self.window)
        # self.ui_manager.enable()
        self.setup_not_insys()
        for each in self.buttons_array:
            self.ui_manager.add(each)
        
        self.ui_manager_insys = arcade.gui.UIManager(self.window)
        self.setup_insys()
        for each in self.buttons_array_insys:
            self.ui_manager_insys.add(each)

    def on_draw(self):
        arcade.start_render()
        if not self.insys:
            # sleep(.02)
            self.background = arcade.load_texture(f'bg_files/back{self.i}.png')
            # self.background = arcade.load_animated_gif('black_hole.gif')
            arcade.draw_texture_rectangle(self.sw_2, self.sh_2, 1920, 1080, self.background)
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
            arcade.set_background_color(self.background)
            if self.insys_sidebar_visible:
                self.ui_manager_insys.enable()
                arcade.draw_lrtb_rectangle_filled(0, self.sidebar_visibility_range, self.height, 0, black)
                self.ui_manager_insys.draw()
            if self.page == 'main':
                ...
            elif self.page == 'qr':
                arcade.draw_texture_rectangle(self.sw_2, self.sh_2, self.qr_code_image.size[0], self.qr_code_image.size[1], self.qr_code_image)
                
    
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
                    # print("data is invalid")
                    break
            if self.isValid:
                # print('data is valid')
                self.check_data(self.login.text, self.password.text)
        
    def check_data(self, login, password):
        with open('C:/Users/komme/Desktop/Study/Андрианова 3_2/customers_login_info.txt', 'r') as file:
            data = np.array([line.split() for line in file.readlines()])
            for each in data:
                if login == each[0]:
                    if password == each[1]:
                        self.background = grey
                        self.insys = True
                        self.username = each[0]
                        self.surname = each[1]
                        self.login.text = 'Login'
                        self.password.text = 'Password'
                        self.ui_manager.disable()
                        # print(self.login.text)
                        
    def on_mouse_motion(self, x, y, dx, dy):
        if x < self.sidebar_visibility_range:
            self.insys_sidebar_visible = True
        else:
            self.insys_sidebar_visible = False

    def sys_exit(self, *_): 
        self.insys = False
        self.ui_manager.enable()
        self.login.text = 'Login'
        self.password.text = 'Password'
        return 
    
    def set_page_as_main(self, *_):
        self.page = 'main'
        return
    
    def set_page_as_qr(self, *_):
        self.page = 'qr'
        return
    
    def set_page_as_trs(self, *_):
        self.page = 'trs'
        return
    
    def setup_not_insys(self, *_):
        # !insys
        self.ui_manager.enable()
        self.i = 0
        self.di = 1
        self.xpos1 = self.width//2.25-self.width//8
        self.xpos2 = self.width//1.65-self.width//8
        self.ypos1 = self.height//2.5-self.height//5
        self.ypos2 = self.height//2.5-self.height//24-self.height//5
        self.xpos3 = self.width//2.25+self.width//16
        self.xpos4 = self.width//1.65+self.width//16
        self.passwidth = self.logwidth = self.width//1.65-self.width//2.25
        self.passheight = self.logheight = self.height//2.5-self.height//5
        
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
        
    def setup_insys(self, *_):
        # insys
        self.ui_manager_insys.enable()
        self.sidebar_visibility_range = self.width//7
        self.insys_sidebar_visible = True
        self.page = 'main'        
        
        self.btnsx, self.mainy = self.sidebar_visibility_range//2-self.buttonwidth//2, self.height*7//8
        self.mainBtn = arcade.gui.UIFlatButton(
            x = self.btnsx,
            y = self.mainy,
            width = self.buttonwidth,
            text='Main')
        self.buttons_array_insys.append(self.mainBtn)
        self.mainBtn.on_click = self.set_page_as_main
        
        self.qry = self.height*5//8
        self.qrBtn = arcade.gui.UIFlatButton(
            x = self.btnsx,
            y = self.qry,
            width = self.buttonwidth,
            text='QR')
        self.qr_code_image = arcade.load_texture('qr_code.png')
        self.buttons_array_insys.append(self.qrBtn)
        self.qrBtn.on_click = self.set_page_as_qr
        
        self.trainingsy = self.height*1//2
        self.trainingsBtn = arcade.gui.UIFlatButton(
            x = self.btnsx,
            y = self.trainingsy,
            width = self.buttonwidth,
            text='Trainings')
        self.buttons_array_insys.append(self.trainingsBtn)
        self.mainBtn.on_click = self.set_page_as_trs
        
        self.exity = self.height*1//8
        self.exitBtn = arcade.gui.UIFlatButton(
            x = self.btnsx,
            y = self.exity,
            width = self.buttonwidth,
            text='Exit')
        self.buttons_array_insys.append(self.exitBtn)
        self.exitBtn.on_click = self.sys_exit

        
if __name__ == "__main__":
    # generate_images()
    white = arcade.color.WHITE
    grey = arcade.color.ASH_GREY
    black = arcade.color.BLACK
    wenge = arcade.color.WENGE
    window = arcade.Window(1920, 1080, title="Deam", fullscreen = True)
    window.show_view(GuiWindow(window))
    arcade.run()
    arcade.close_window()


