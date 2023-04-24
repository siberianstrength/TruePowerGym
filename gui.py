# C:\Users\komme\Desktop\Study\Андрианова 3_2
import arcade
import arcade.gui
import numpy as np
from functions import Buttons
from registration import Registration
from functions import box
from edit import Edit


class GuiWindow(arcade.View):
    def __init__(self, my_window: arcade.Window, fullscreen = True):
        super().__init__(my_window)
        self.set_location = (0, 0)
        self.width = 1920
        self.height = 1080
        self.buttons_array = []
        self.buttons_array_insys = []
        self.insys = True
        self.background = wenge
        self.sw_2 = self.width//2
        self.sh_2 = self.height//2

        self.name = 'yakov'
        self.surname = 'goncharov'
        self.fathername = 'yevg'
        self.gender = 'male'
        self.DOB = '06.06.2002'
        self.user_password = 'deadashell'
        
        self.ui_manager = arcade.gui.UIManager(self.window)
        self.setup_not_insys()
        for each in self.buttons_array:
            self.ui_manager.add(each)

        self.ui_manager_insys = arcade.gui.UIManager(self.window)
        self.main_manager = arcade.gui.UIManager(self.window)
        self.editBtn_manager = arcade.gui.UIManager(self.window)
        self.setup_insys()
        for each in self.buttons_array_insys:
            self.ui_manager_insys.add(each)
        for each in self.main_page_container:
            self.main_manager.add(each)
        for each in self.edit_container:
            self.editBtn_manager.add(each)


    def on_draw(self):
        arcade.start_render()
        if not self.insys:
            self.background = arcade.load_texture(f'resources/bg_files/back{self.i}.png')
            arcade.draw_texture_rectangle(self.sw_2, self.sh_2, 1920, 1080, self.background)
            self.i += self.di
            if self.i == 478 or self.i == 0:
                self.di = -self.di
            arcade.draw_lrtb_rectangle_filled(self.xpos1, self.xpos2, self.ypos1, self.ypos2, white)
            arcade.draw_lrtb_rectangle_outline(self.xpos1, self.xpos2, self.ypos1, self.ypos2, grey, border_width= 3)
            arcade.draw_lrtb_rectangle_filled(self.xpos3, self.xpos4, self.ypos1, self.ypos2, white)
            arcade.draw_lrtb_rectangle_outline(self.xpos3, self.xpos4, self.ypos1, self.ypos2, grey, border_width= 3)
            self.ui_manager.draw()
            if not self.isValid:
                arcade.draw_text("Invalid data, try again",
                 self.sw_2-100,
                 self.buttony-20,
                 font_size = 14,
                 color = arcade.color.RED)
        else:
            arcade.start_render()
            arcade.set_background_color(self.background)
            if self.page == 'main':
                self.background = grey
                arcade.draw_lrtb_rectangle_filled(0,self.width,self.height, self.height-200, black)
                self.main_manager.draw()
                self.editBtn_manager.draw()
                self.main_manager.enable()
                self.editBtn_manager.enable()
                if self.underpage == 'info':
                    self.underscore(self.sidebar_visibility_range + 10, self.height - 200 - self.main_dy, 100)
                    self.underscore(self.sidebar_visibility_range + 10, self.height - 200 - 2*self.main_dy, 145)
                    self.underscore(self.sidebar_visibility_range + 10, self.height - 200 - 3*self.main_dy, 190)
                    self.underscore(self.sidebar_visibility_range + 10, self.height - 200 - 4*self.main_dy, 120)
                    self.underscore(self.sidebar_visibility_range + 10, self.height - 200 - 5*self.main_dy, 195)
                    self.underscore(self.sidebar_visibility_range + 10, self.height - 200 - 6*self.main_dy, 155)
                    self.underscore(self.width//2+40, self.height//2-360, 440)
                    arcade.draw_text(f"Name:  {self.name}", self.sidebar_visibility_range+10, self.height - 200 - self.main_dy, font_size=25, color=arcade.color.BLACK)
                    arcade.draw_text(f"Surname:  {self.surname}", self.sidebar_visibility_range+10, self.height - 200 - 2*self.main_dy, font_size=25, color=arcade.color.BLACK)
                    arcade.draw_text(f"Fathername:  {self.fathername}", self.sidebar_visibility_range+10, self.height - 200 - 3*self.main_dy, font_size=25, color=arcade.color.BLACK)
                    arcade.draw_text(f"Gender:  {self.gender}", self.sidebar_visibility_range+10, self.height - 200 - 4*self.main_dy, font_size=25, color=arcade.color.BLACK)
                    arcade.draw_text(f"Date of birth:  {self.DOB}", self.sidebar_visibility_range+10, self.height - 200 - 5*self.main_dy, font_size=25, color=arcade.color.BLACK)
                    arcade.draw_text(f"Password:  {self.user_password}", self.sidebar_visibility_range+10, self.height - 200 - 6*self.main_dy, font_size=25, color=arcade.color.BLACK)

            elif self.page == 'qr':
                arcade.draw_texture_rectangle(self.sw_2, self.sh_2, self.qr_code_image.size[0], self.qr_code_image.size[1], self.qr_code_image)
            if self.insys_sidebar_visible:
                arcade.draw_lrtb_rectangle_filled(0, self.sidebar_visibility_range, self.height, 0, black)
                self.ui_manager_insys.enable()
                self.ui_manager_insys.draw()

    
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
            for each in self.login.text:
                if not ((ord(each) >= 97 and ord(each) <= 122) or (ord(each) >= 65 and ord(each) <= 90)):
                    self.isValid = False
                    return
        self.check_data(self.login.text, self.password.text)
        
    def check_data(self, login, password):
        with open('customers_id.txt', 'r') as file:
            data = np.array([line.split() for line in file.readlines()])
            for each in data:
                if login == each[0]:
                    if password == each[1]:
                        self.background = grey
                        self.insys = True
                        self.login.text = 'Login'
                        self.password.text = 'Password'
                        self.ui_manager.disable()
                        self.isValid = True
                        self.user_id = each[2]

        with open(f'customers_login_info/customer{self.user_id}.txt', 'r') as file:
            data = np.array(list(line.split() for line in file.readlines()))
            self.name = data[0][0]
            self.surname = data[0][1]
            self.fathername = data[0][2]
            self.gender = data[0][3]
            self.DOB = data[0][4]
            self.user_password = data[0][5]
            self.isValid = False
                        
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
    
    def registration_on_click(self, *_):
        self.registration_window.enabled = True

    def logopic_on_click(self, *_):
        self.underpage = 'info'

    def health_formBtn_on_click(self, *_):
        self.underpage = 'form'

    def underscore(self, x, y, length):
        arcade.draw_line(x, y-5, x+length, y-5, black, line_width=3)

    def editBtn_on_click(self, *_):
        self.edit_window.enabled = True

    def get_info(self, *_):
        with open(f'customers_login_info/customer{self.user_id}.txt', 'r') as file:
            data = np.array(list(line.split() for line in file.readlines()))
            self.name = data[0][0]
            self.surname = data[0][1]
            self.fathername = data[0][2]
            self.gender = data[0][3]
            self.DOB = data[0][4]
            self.user_password = data[0][5]

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
        self.isValid = True
        
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
        
        self.registration_button = Buttons.add_texture_button('resources/registration_1.jpg',
                                                              'resources/registration_1.jpg',
                                                              'resources/registration_1.jpg',
                                                              _x = self.xpos3+self.passwidth+30,
                                                              _y = self.ypos2,
                                                              _scale = .04)
        self.buttons_array.append(self.registration_button)
        self.registration_button.on_click = self.registration_on_click
        self.registration_window = Registration(0, 0, self.width, self.height)
        self.section_manager.add_section(self.registration_window)

        
        
    def setup_insys(self, *_):
        # insys
        self.page = 'main'
        self.underpage = 'info'
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
        self.qr_code_image = arcade.load_texture('resources/qr_code.png')
        self.buttons_array_insys.append(self.qrBtn)
        self.qrBtn.on_click = self.set_page_as_qr
        
        self.trainingsy = self.height*1//2
        self.trainingsBtn = arcade.gui.UIFlatButton(
            x = self.btnsx,
            y = self.trainingsy,
            width = self.buttonwidth,
            text='Trainings')
        self.buttons_array_insys.append(self.trainingsBtn)
        self.trainingsBtn.on_click = self.set_page_as_trs
        
        self.exity = self.height*1//8
        self.exitBtn = arcade.gui.UIFlatButton(
            x = self.btnsx,
            y = self.exity,
            width = self.buttonwidth,
            text='Exit')
        self.buttons_array_insys.append(self.exitBtn)
        self.exitBtn.on_click = self.sys_exit

        self.main_page_container = []
        self.logopic = Buttons.add_texture_button('resources/logo.png',
                                                       'resources/logo.png',
                                                       'resources/logo.png',
                                                       _x = self.width//2-50,
                                                       _y = self.height-180,
                                                       _scale = .08
        )
        self.main_page_container.append(self.logopic)
        self.logopic.on_click = self.logopic_on_click

        self.galaxypic = Buttons.add_texture_button('resources/galaxy_main.png',
                                                       'resources/galaxy_main.png',
                                                       'resources/galaxy_main.png',
                                                       _x = self.width//2-300,
                                                       _y = self.height-200,
                                                       _scale = .2
        )
        self.main_page_container.append(self.galaxypic)

        self.health_formBtn = Buttons.add_texture_button('resources/health_form.png',
                                                       'resources/health_form.png',
                                                       'resources/health_form.png',
                                                       _x = self.width//2+180,
                                                       _y = self.height-180,
                                                       _scale = .3
        )
        self.main_page_container.append(self.health_formBtn)
        self.health_formBtn.on_click = self.health_formBtn_on_click

        self.main_dy = self.height//10
        self.edit_container = []
        self.editBtn = Buttons.add_texture_button('resources/edit.png',
                                                       'resources/edit.png',
                                                       'resources/edit.png',
                                                       _x = self.sidebar_visibility_range+10,
                                                       _y = self.height - 200 - self.main_dy*7,
                                                       _scale = .1
        )
        self.editBtn.on_click = self.editBtn_on_click
        self.edit_container.append(self.editBtn)
        self.edit_window = Edit(0, 0, self.width, self.height, [self.name, self.surname, self.fathername, self.gender, self.DOB, self.user_password, 4])
        self.section_manager.add_section(self.edit_window)

        self.renew = Buttons.add_texture_button('resources/renew.png',
                                                       'resources/renew.png',
                                                       'resources/renew.png',
                                                       _x = self.sidebar_visibility_range+10,
                                                       _y = self.height - 200 - self.main_dy*8,
                                                       _scale = .03
        )
        self.edit_container.append(self.renew)
        self.renew.on_click = self.get_info

        self.member_red = Buttons.add_texture_button('resources/member_black.png',
                                                       'resources/member_black.png',
                                                       'resources/member_black.png',
                                                       _x = self.width//2,
                                                       _y = self.height//2,
                                                       _scale = .07
        )
        self.edit_container.append(self.member_red)

        self.member_yellow = Buttons.add_texture_button('resources/member_yellow.png',
                                                       'resources/member_yellow.png',
                                                       'resources/member_yellow.png',
                                                       _x = self.width//2+300,
                                                       _y = self.height//2,
                                                       _scale = .07
        )
        self.edit_container.append(self.member_yellow)

        self.member_blue = Buttons.add_texture_button('resources/member_blue.png',
                                                       'resources/member_blue.png',
                                                       'resources/member_blue.png',
                                                       _x = self.width//2,
                                                       _y = self.height//2-250,
                                                       _scale = .07
        )
        self.edit_container.append(self.member_blue)

        self.member_red = Buttons.add_texture_button('resources/member_red.png',
                                                       'resources/member_red.png',
                                                       'resources/member_red.png',
                                                       _x = self.width//2+300,
                                                       _y = self.height//2-250,
                                                       _scale = .07
        )
        self.edit_container.append(self.member_red)

        self.membership_card = 'member_black'
        self.small_card = Buttons.add_texture_button(f'resources/{self.membership_card}.png',
                                                     f'resources/{self.membership_card}.png',
                                                     f'resources/{self.membership_card}.png',
                                                     _x=self.width // 2 + 500,
                                                     _y=self.height // 2 - 400,
                                                     _scale=.03
                                                     )
        self.edit_container.append(self.small_card)

        self.membership_text = arcade.gui.UIInputText(
            x=self.width//2+40,
            y = self.height*.25-100,
            text_color=black,
            font_name=('Yu Gothic'),
            font_size=30,
            width = 500,
            text='Your membership card: ')
        self.edit_container.append(self.membership_text)





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


