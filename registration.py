import arcade
from tkinter.filedialog import askopenfilename
from functions import Buttons
import os, os.path


class Registration(arcade.Section):
    def __init__(self, left, bottom, width, height):
        super().__init__(left, bottom, width, height, modal = True)
        self.id = len([name for name in os.listdir('customers_login_info') if os.path.isfile(os.path.join('customers_login_info', name))])
        self.l = self.width // 4
        self.r = self.width*.75
        self.b = self.height*.25
        self.t = self.height*.75
        self.enabled = False
        self.manager = arcade.gui.UIManager(self.window)
        
        self.xleft = self.l+20
        self.yfirst = self.t-80
        self.dy = self.height//12
        self.color = arcade.color.BLACK
        self.w = 200
        self.h = self.height//20
        self.container = []
        
        self.name = arcade.gui.UIInputText(
            x = self.xleft, 
            y = self.yfirst,
            text_color = arcade.color.BLACK,
            font_name = ('Yu Gothic'), # Control Panel\All Control Panel Items\Fonts, 
            font_size = 30,
            width = 200,
            height = self.h,
            text='Name')
        self.container.append(self.name)
        
        self.surname = arcade.gui.UIInputText(
            x = self.xleft,
            y = self.yfirst - self.dy,
            text_color = arcade.color.BLACK,
            font_name = ('Yu Gothic'), # Control Panel\All Control Panel Items\Fonts, 
            font_size = 30,
            width = 200,
            height = self.h,
            text='Surname')
        self.container.append(self.surname)
        
        self.fathername = arcade.gui.UIInputText(
            x = self.xleft,
            y = self.yfirst - 2*self.dy,
            text_color = arcade.color.BLACK,
            font_name = ('Yu Gothic'), # Control Panel\All Control Panel Items\Fonts, 
            font_size = 30,
            width = 230,
            height = self.h,
            text='Fathername')
        self.container.append(self.fathername)
        
        self.gender = arcade.gui.UIInputText(
            x = self.xleft,
            y = self.yfirst - 3*self.dy,
            text_color = arcade.color.BLACK,
            font_name = ('Yu Gothic'), # Control Panel\All Control Panel Items\Fonts, 
            font_size = 30,
            width = 200,
            height = self.h,
            text='Gender')
        self.container.append(self.gender)
        
        self.DOB = arcade.gui.UIInputText(
            x = self.xleft,
            y = self.yfirst - 4*self.dy,
            text_color = arcade.color.BLACK,
            font_name = ('Yu Gothic'), # Control Panel\All Control Panel Items\Fonts, 
            font_size = 30,
            width = 300,
            height = self.h,
            text='Date of birth')
        self.container.append(self.DOB)

        self.password = arcade.gui.UIInputText(
            x = self.xleft,
            y = self.yfirst - 5*self.dy,
            text_color = arcade.color.BLACK,
            font_name = ('Yu Gothic'), # Control Panel\All Control Panel Items\Fonts,
            font_size = 30,
            width = 300,
            height = self.h,
            text='Password')
        self.container.append(self.password)

        self.upload_photo = Buttons.add_texture_button('resources/upload.png',
                                                       'resources/upload.png', 
                                                       'resources/upload.png',
                                                       _x = self.r - 350,
                                                       _y = self.t  - 60,
                                                       _scale = .05                                       
                                                       )
        self.container.append(self.upload_photo)
        self.upload_photo.on_click = self.upload_photo_on_click

        self.submit = Buttons.add_texture_button('resources/submit.png',
                                                       'resources/submit.png',
                                                       'resources/submit.png',
                                                       _x = self.r - 350,
                                                       _y = self.b + 10,
                                                       _scale = .05
                                                 )
        self.container.append(self.submit)
        self.submit.on_click = self.submit_on_click

        for each in self.container:
            self.manager.add(each)
        
        self.box1 = [self.xleft, self.yfirst+50]
        self.box2 = [self.xleft, self.yfirst+50-self.dy]
        self.box3 = [self.xleft, self.yfirst+50-2*self.dy]
        self.box4 = [self.xleft, self.yfirst+50-3*self.dy]
        self.box5 = [self.xleft, self.yfirst+50-4*self.dy]
        self.box6 = [self.xleft, self.yfirst+50-5*self.dy]
        
    def on_draw(self):
        self.manager.enable()
        arcade.draw_lrtb_rectangle_filled(self.l, self.r, self.t, self.b, arcade.color.GRAY)
        self.box(*self.box1)
        self.box(*self.box2)
        self.box(*self.box3)
        self.box(*self.box4)
        self.box(*self.box5)
        self.box(*self.box6)
        self.manager.draw()
        
    def upload_photo_on_click(self, *_):
        raise NotImplementedError
        filename = askopenfilename()

    def submit_on_click(self, *_):
        reg_data = [self.name.text, self.surname.text, self.fathername.text, self.gender.text, self.DOB.text, self.password.text]
        self.id += 1
        self.reg_data = '\n'+' '.join(str(reg_data[i]) for i in range(len(reg_data)))
        with open(f'customers_login_info/id{self.id}', 'w') as f:
            f.write(self.reg_data)
        self.enabled = False




            