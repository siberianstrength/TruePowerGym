# C:\Users\komme\Desktop\Study\Андрианова 3_2
import arcade
import arcade.gui
import numpy as np
from functions import Buttons
from registration import Registration
from edit import Edit
from edit_hf import Edit_hf
import os
from cards import Cards
from trainings_and_trainers import Trainings

class GuiWindow(arcade.View):
    def __init__(self, my_window: arcade.Window, fullscreen = True):
        super().__init__(my_window)
        self.path = 'customers_login_info/login'
        self.set_location = (0, 0)
        self.width = 1920
        self.height = 1080
        self.buttons_array = []
        self.buttons_array_insys = []
        self.insys = False
        self.background = wenge
        self.sw_2 = self.width//2
        self.sh_2 = self.height//2
        self.sidebar_visibility_range = self.width // 7
        self.edit_container = []
        self.main_dy = self.height//10

        self.preload()
        
        self.ui_manager = arcade.gui.UIManager(self.window)
        self.setup_not_insys()
        for each in self.buttons_array:
            self.ui_manager.add(each)
        self.backgroundpic = arcade.load_texture('resources/back0.png')
            



    def on_draw(self):
        arcade.start_render()
        if not self.insys:
            arcade.draw_texture_rectangle(self.sw_2, self.sh_2, 1920, 1080, self.backgroundpic)
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
            arcade.set_background_color(self.background)
            if self.page == 'main':
                self.background = grey
                arcade.draw_lrtb_rectangle_filled(0,self.width,self.height, self.height-200, black)
                self.main_manager.draw()
                self.main_manager.enable()
                if self.subpage == 'info':
                    self.editBtn_manager.enable()
                    self.editBtn_manager.draw()
                    self.underscore(self.sidebar_visibility_range + 10, self.height - 200 - self.main_dy, 100)
                    self.underscore(self.sidebar_visibility_range + 10, self.height - 200 - 2*self.main_dy, 145)
                    self.underscore(self.sidebar_visibility_range + 10, self.height - 200 - 3*self.main_dy, 190)
                    self.underscore(self.sidebar_visibility_range + 10, self.height - 200 - 4*self.main_dy, 120)
                    self.underscore(self.sidebar_visibility_range + 10, self.height - 200 - 5*self.main_dy, 195)
                    self.underscore(self.sidebar_visibility_range + 10, self.height - 200 - 6*self.main_dy, 155)
                    self.underscore(self.width//2+40, self.height//2-360, 440)
                    arcade.draw_text(f"Name:  {self.username}", self.sidebar_visibility_range+10, self.height - 200 - self.main_dy, font_size=25, color=arcade.color.BLACK)
                    arcade.draw_text(f"Surname:  {self.usersurname}", self.sidebar_visibility_range+10, self.height - 200 - 2*self.main_dy, font_size=25, color=arcade.color.BLACK)
                    arcade.draw_text(f"Fathername:  {self.userfathername}", self.sidebar_visibility_range+10, self.height - 200 - 3*self.main_dy, font_size=25, color=arcade.color.BLACK)
                    arcade.draw_text(f"Gender:  {self.usergender}", self.sidebar_visibility_range+10, self.height - 200 - 4*self.main_dy, font_size=25, color=arcade.color.BLACK)
                    arcade.draw_text(f"Date of birth:  {self.userDOB}", self.sidebar_visibility_range+10, self.height - 200 - 5*self.main_dy, font_size=25, color=arcade.color.BLACK)
                    arcade.draw_text(f"Password:  {self.userpassword}", self.sidebar_visibility_range+10, self.height - 200 - 6*self.main_dy, font_size=25, color=arcade.color.BLACK)
                elif self.subpage == 'form':
                    arcade.draw_lrtb_rectangle_filled(self.width//2-350, self.width//2+450, self.height-200, 0, white)
                    self.form_manager.enable()
                    self.form_manager.draw()
            elif self.page == 'qr':
                arcade.draw_texture_rectangle(self.sw_2, self.sh_2, self.qr_code_image.size[0], self.qr_code_image.size[1], self.qr_code_image)
            elif self.page == 'clubinfo':
                arcade.draw_texture_rectangle(self.width//2, self.height//2, self.height//2, self.height//2, self.place)
                arcade.draw_text(text = 'Мы находимся по адресу:\nГород Казань, улица Кремлёвская 35.', start_x= self.width//2-200, start_y= self.height-200, font_size = 21, color = arcade.color.BLACK, width = 500,  multiline=True)
                arcade.draw_text(text = "Пешая доступность от остановки 'Университет'\n или 'Станция метро им. Тукая'", start_x= self.width//2-200, start_y= 200, font_size = 21, color = arcade.color.BLACK, width = 500,  multiline=True)
                arcade.draw_text(text = "TopGyms:\n'Один из лучших залов, что мы посещали.'\n5/5", start_x= self.width//2+500, start_y= self.height//2+100, font_size = 18, color = arcade.color.BLACK, width = 300,  multiline=True)
                arcade.draw_text(text = "GymRating:\n'Зал оборудован по последнему слову техники, все тренажёры новые, в зале всё чисто и опрятно.'\n10/10", start_x= self.width//2+500, start_y= self.height//2-100, font_size = 18, color = arcade.color.BLACK, width = 300,  multiline=True)
                arcade.draw_texture_rectangle(self.width//2-570, self.height//2+215, 170, 50, self.stars)
                arcade.draw_text(text = "IronRating:", start_x= self.width//2-630, start_y= self.height//2+250, font_size = 18, color = arcade.color.BLACK, width = 300,  multiline=True)
                arcade.draw_text(text = """В зале удовлетворило абсолютно всё. Любая зона, которую мы посетили, была крайне хорошо продумана заранее, что создаёт комфортные условия пребывания и дарит хорошие впечатления. Всё оборудование, в том числе солярий, работали, тренера следили за тренирующимися, за правильностью выполнения, что, безусловно, значительно снижает травмоопасность и риск неправильного выполнения упражнений."""
                                         ,start_x= self.width//2-700, start_y= self.height//2+160, font_size = 18, color = arcade.color.BLACK, width = 300,  multiline=True)

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
        if self.check_data(self.login.text, self.password.text):
            self.insys = True
        
    def check_data(self, login, password):
        for (dirpath, dirnames, filenames) in os.walk(self.path):
            for filename in filenames:
                with open(os.path.join(dirpath, filename), 'r') as f:
                    data = f.read().split()
                    if data[0] == login and data[-3] == password:
                        self.insys = True
                        self.login.text = 'Login'
                        self.password.text = 'Password'
                        self.ui_manager.disable()
                        self.isValid = True
                        self.username = data[0]
                        self.usersurname = data[1]
                        self.userfathername = data[2]
                        self.usergender = data[3]
                        self.userDOB = data[4]
                        self.userpassword = data[5]
                        self.useremail = data[6]
                        self.userid = data[7]
                        
                        self.ui_manager_insys = arcade.gui.UIManager(self.window)
                        self.main_manager = arcade.gui.UIManager(self.window)
                        self.editBtn_manager = arcade.gui.UIManager(self.window)
                        self.form_manager = arcade.gui.UIManager(self.window)
                        self.setup_insys()
                        for each in self.buttons_array_insys:
                            self.ui_manager_insys.add(each)
                        for each in self.main_page_container:
                            self.main_manager.add(each)
                        for each in self.edit_container:
                            self.editBtn_manager.add(each)
                        for each in self.form_container:
                            self.form_manager.add(each)
                        self.background = wenge
                        return True
        return False

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
        self.main_manager.enable()
        self.editBtn_manager.enable()
        self.trainingsmenu.enabled = False
    
    def set_page_as_qr(self, *_):
        self.page = 'qr'
        self.main_manager.disable()
        self.editBtn_manager.disable()
        self.trainingsmenu.enabled = False
    
    def trainings_on_click(self, *_):
        self.main_manager.disable()
        self.editBtn_manager.disable()
        self.trainingsmenu.enabled = True
        self.page = None
    
    def infopage(self, *_):
        self.main_manager.disable()
        self.editBtn_manager.disable()
        self.trainingsmenu.enabled = False
        self.page = 'clubinfo'
        
    def registration_on_click(self, *_):
        self.registration_window.enabled = True

    def logopic_on_click(self, *_):
        self.subpage = 'info'

    def health_formBtn_on_click(self, *_):
        self.subpage = 'form'
        

    def underscore(self, x, y, length):
        arcade.draw_line(x, y-5, x+length, y-5, black, line_width=3)

    def editBtn_on_click(self, *_):
        self.edit_window.enabled = True

    def edit_hf_on_click(self, *_):
        self.edit_window_hf.enabled = True
        
    def member_black_on_click(self, *_):
        self.cards_menu.abo_type = 0
        self.cards_menu.amount = 6
        self.cards_menu.get_card()
        self.cards_menu.enabled = True

    def member_yellow_on_click(self, *_):
        self.cards_menu.abo_type = 1
        self.cards_menu.amount = 5
        self.cards_menu.get_card()
        self.cards_menu.enabled = True

    def member_blue_on_click(self, *_):
        self.cards_menu.abo_type = 2
        self.cards_menu.amount = 4
        self.cards_menu.get_card()
        self.cards_menu.enabled = True

    def member_red_on_click(self, *_):
        self.cards_menu.abo_type = 3
        self.cards_menu.amount = 3
        self.cards_menu.get_card()
        self.cards_menu.enabled = True

    def get_info(self, *_):
        with open(f'customers_login_info/login/customer{self.userid}.txt', 'r') as file:
            data = [line.split() for line in file.readlines()]
            self.username = data[0][0]
            self.usersurname = data[0][1]
            self.userfathername = data[0][2]
            self.usergender = data[0][3]
            self.userDOB = data[0][4]
            self.userpassword = data[0][5]

    def renew_hf_on_click(self, *_):
        with open(f'customers_login_info/health_forms/customer{self.userid}_hf.txt') as file:
            text = file.read()
        self.form_text.text = text

    def setup_not_insys(self, *_):
        # !insys
        self.clublogo = arcade.load_texture('resources/clublogo.png')
        self.place = arcade.load_texture('resources/place.png')
        self.stars = arcade.load_texture('resources/stars_i_guess.png')
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
        self.subpage = 'info'
        self.ui_manager_insys.enable()
        self.insys_sidebar_visible = True

        self.btnsx, self.mainy = self.sidebar_visibility_range // 2 - self.buttonwidth // 2, self.height * 7 // 8
        self.mainBtn = arcade.gui.UIFlatButton(
            x=self.btnsx,
            y=self.mainy,
            width=self.buttonwidth,
            text='Main')
        self.buttons_array_insys.append(self.mainBtn)
        self.mainBtn.on_click = self.set_page_as_main

        self.qry = self.height * 3 // 4
        self.qrBtn = arcade.gui.UIFlatButton(
            x=self.btnsx,
            y=self.qry,
            width=self.buttonwidth,
            text='QR')
        self.qr_code_image = arcade.load_texture('resources/qr_code.png')
        self.buttons_array_insys.append(self.qrBtn)
        self.qrBtn.on_click = self.set_page_as_qr

        self.trainingsy = self.height * 1 // 2
        self.trainingsBtn = arcade.gui.UIFlatButton(
            x=self.btnsx,
            y=self.trainingsy,
            width=self.buttonwidth,
            text='Trainings')
        self.buttons_array_insys.append(self.trainingsBtn)
        self.trainingsmenu = Trainings(0, 0, self.width, self.height, self.userid, self.membership_card)
        self.section_manager.add_section(self.trainingsmenu)
        self.trainingsBtn.on_click = self.trainings_on_click

        self.exity = self.height * 1 // 8
        self.exitBtn = arcade.gui.UIFlatButton(
            x=self.btnsx,
            y=self.exity,
            width=self.buttonwidth,
            text='Exit')
        self.buttons_array_insys.append(self.exitBtn)
        self.exitBtn.on_click = self.sys_exit

        self.clubinfoy = self.height * 5//8
        self.clubinfoBtn = arcade.gui.UIFlatButton(
            x=self.btnsx,
            y=self.clubinfoy,
            width=self.buttonwidth,
            text='Info'
            )
        self.buttons_array_insys.append(self.clubinfoBtn)
        self.clubinfoBtn.on_click = self.infopage
        
        self.main_page_container = []
        self.logopic = Buttons.add_texture_button('resources/logo.png',
                                                  'resources/logo.png',
                                                  'resources/logo.png',
                                                  _x=self.width // 2 - 50,
                                                  _y=self.height - 180,
                                                  _scale=.08
                                                  )
        self.main_page_container.append(self.logopic)
        self.logopic.on_click = self.logopic_on_click

        self.galaxypic = Buttons.add_texture_button('resources/clublogo_black.png',
                                                    'resources/clublogo_black.png',
                                                    'resources/clublogo_black.png',
                                                    _x=self.width // 2 - 250,
                                                    _y=self.height - 175,
                                                    _scale=.3
                                                    )
        self.main_page_container.append(self.galaxypic)

        self.health_formBtn = Buttons.add_texture_button('resources/health_form.png',
                                                         'resources/health_form.png',
                                                         'resources/health_form.png',
                                                         _x=self.width // 2 + 180,
                                                         _y=self.height - 180,
                                                         _scale=.3
                                                         )
        self.main_page_container.append(self.health_formBtn)
        self.health_formBtn.on_click = self.health_formBtn_on_click

        self.main_dy = self.height // 10
        self.editBtn = Buttons.add_texture_button('resources/edit.png',
                                                  'resources/edit.png',
                                                  'resources/edit.png',
                                                  _x=self.sidebar_visibility_range + 10,
                                                  _y=self.height - 200 - self.main_dy * 7,
                                                  _scale=.1
                                                  )
        self.editBtn.on_click = self.editBtn_on_click
        self.edit_container.append(self.editBtn)
        self.edit_window = Edit(0, 0, self.width, self.height,
                                [self.username, self.usersurname, self.userfathername, self.usergender, self.userDOB, self.userpassword,
                                 self.useremail, self.userid])
        self.section_manager.add_section(self.edit_window)

        self.renew = Buttons.add_texture_button('resources/renew.png',
                                                'resources/renew.png',
                                                'resources/renew.png',
                                                _x=self.sidebar_visibility_range + 10,
                                                _y=self.height - 200 - self.main_dy * 8,
                                                _scale=.03
                                                )
        self.edit_container.append(self.renew)
        self.renew.on_click = self.get_info

        self.membership_text = arcade.gui.UIInputText(
            x=self.width//2+40,
            y = self.height*.25-100,
            text_color=black,
            font_name=('Yu Gothic'),
            font_size=30,
            width = 500,
            text='Your membership card: ')
        self.edit_container.append(self.membership_text)

        self.form_container = []
        with open(f'customers_login_info/health_forms/customer{self.userid}_hf.txt', 'r') as f:
            self.hf_text = f.read()
        self.form_text = arcade.gui.UITextArea(
            x=self.width//2 - 350,
            y = self.height-1280,
            text_color = black,
            font_name=('Yu Gothic'),
            font_size=30,
            width = 800,
            height= self.height,
            text=f'{self.hf_text}')
        self.form_container.append(self.form_text)

        self.renew_hf = Buttons.add_texture_button('resources/renew.png',
                                                       'resources/renew.png',
                                                       'resources/renew.png',
                                                       _x = self.width//2-450,
                                                       _y = self.height - 200 - self.main_dy*8,
                                                       _scale = .03
        )
        self.form_container.append(self.renew_hf)
        self.renew_hf.on_click = self.renew_hf_on_click

        self.edit_hf = Buttons.add_texture_button('resources/edit.png',
                                                       'resources/edit.png',
                                                       'resources/edit.png',
                                                       _x = self.width//2-450,
                                                       _y = self.height - 200 - self.main_dy*7,
                                                       _scale = .1
        )
        self.form_container.append(self.edit_hf)
        self.edit_hf.on_click = self.edit_hf_on_click
        self.edit_window_hf = Edit_hf(0, 0, self.width, self.height, self.userid)
        self.section_manager.add_section(self.edit_window_hf)
        
        self.cards_menu = Cards(0, 0, self.width, self.height,
                                        ['resources/member_black.png',
                                         'resources/member_yellow.png',
                                         'resources/member_blue.png',
                                         'resources/member_red.png'],
                                        _)
        self.section_manager.add_section(self.cards_menu)
        
        
    def preload(self):
        self.member_black = Buttons.add_texture_button('resources/member_black.png',
                                                     'resources/member_black.png',
                                                     'resources/member_black.png',
                                                     _x=self.width // 2,
                                                     _y=self.height // 2,
                                                     _scale=.07
                                                     )
        self.edit_container.append(self.member_black)
        self.member_black.on_click = self.member_black_on_click
        
        self.member_yellow = Buttons.add_texture_button('resources/member_yellow.png',
                                                        'resources/member_yellow.png',
                                                        'resources/member_yellow.png',
                                                        _x=self.width // 2 + 300,
                                                        _y=self.height // 2,
                                                        _scale=.07
                                                        )
        self.edit_container.append(self.member_yellow)
        self.member_yellow.on_click = self.member_yellow_on_click


        self.member_blue = Buttons.add_texture_button('resources/member_blue.png',
                                                      'resources/member_blue.png',
                                                      'resources/member_blue.png',
                                                      _x=self.width // 2,
                                                      _y=self.height // 2 - 250,
                                                      _scale=.07
                                                      )
        self.edit_container.append(self.member_blue)
        self.member_blue.on_click = self.member_blue_on_click


        self.member_red = Buttons.add_texture_button('resources/member_red.png',
                                                     'resources/member_red.png',
                                                     'resources/member_red.png',
                                                     _x=self.width // 2 + 300,
                                                     _y=self.height // 2 - 250,
                                                     _scale=.07
                                                     )
        self.edit_container.append(self.member_red)
        self.member_red.on_click = self.member_red_on_click


        self.membership_card = 'member_black'
        self.small_card = Buttons.add_texture_button(f'resources/{self.membership_card}.png',
                                                     f'resources/{self.membership_card}.png',
                                                     f'resources/{self.membership_card}.png',
                                                     _x=self.width // 2 + 500,
                                                     _y=self.height // 2 - 400,
                                                     _scale=.03
                                                     )
        self.edit_container.append(self.small_card)



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


