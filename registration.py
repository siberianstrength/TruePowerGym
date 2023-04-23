import arcade
from tkinter.filedialog import askopenfilename
from functions import Buttons

class Registration(arcade.Section):
    def __init__(self, left, botttom, width, height):
        super().__init__(left, botttom, width, height, modal = True)
        self.l = self.width // 4
        self.r = self.width*.75
        self.b = self.height*.25
        self.t = self.height*.75
        self.enabled = False
        self.manager = arcade.gui.UIManager(self.window)
        
        self.xleft = self.l+20
        self.yfirst = self.t-80
        self.dy = self.height//10
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
        
        self.upload_photo = Buttons.add_texture_button('resources/upload.png',
                                                       'resources/upload.png', 
                                                       'resources/upload.png',
                                                       _x = self.r - 350,
                                                       _y = self.t  - 60,
                                                       _scale = .05                                       
                                                       )
        self.container.append(self.upload_photo)
        self.upload_photo.on_click = self.upload_photo_on_click
        
        for each in self.container:
            self.manager.add(each)
        
        self.box1 = [self.xleft, self.yfirst+50]
        self.box2 = [self.xleft, self.yfirst+50-self.dy]
        self.box3 = [self.xleft, self.yfirst+50-2*self.dy]
        self.box4 = [self.xleft, self.yfirst+50-3*self.dy]
        self.box5 = [self.xleft, self.yfirst+50-4*self.dy]
        
    def on_draw(self):
        self.manager.enable()
        arcade.draw_lrtb_rectangle_filled(self.l, self.r, self.t, self.b, arcade.color.GRAY)
        self.box(*self.box1)
        self.box(*self.box2)
        self.box(*self.box3)
        self.box(*self.box4)
        self.box(*self.box5)
        self.manager.draw()

    def box(self, x, y):
        arcade.draw_lrtb_rectangle_filled(x, x+250, y, y-40, arcade.color.WHITE)
        arcade.draw_lrtb_rectangle_outline(x, x+250, y, y-40, arcade.color.BLACK, border_width= 3)
        
    def upload_photo_on_click(self, *_):
        self.filename = askopenfilename()
        print(self.filename)
        # if self.filename[-4:] == '.png':
            