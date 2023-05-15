import arcade
from functions import box
from functions import Buttons


class Edit(arcade.Section):
    def __init__(self, left, bottom, width, height, params):
        super().__init__(left, bottom, width, height, modal = True)
        self.enabled = False
        self.width = 1920
        self.height = 1080
        self.sidebar_visibility_range = self.width//7
        self.main_dy = self.height // 10
        self.name = params[0]
        self.surname = params[1]
        self.fathername = params[2]
        self.gender = params[3]
        self.DOB = params[4]
        self.user_password = params[5]
        self.email = params[6]
        self.user_id = params[7]
        self.manager = arcade.gui.UIManager(self.window)
        black = arcade.color.BLACK
        self.logwidth = 200
        self.logheight = 50

        self.container = []
        self._name = arcade.gui.UIInputText(
            x = self.sidebar_visibility_range+125,
            y = self.height - 325,
            text_color= black,
            font_name = ('Yu Gothic'),
            font_size = 24,
            width = self.logwidth,
            height = self.logheight,
            text=f'{self.name}')

        self._surname = arcade.gui.UIInputText(
            x = self.sidebar_visibility_range+170,
            y = self.height - 430,
            text_color= black,
            font_name = ('Yu Gothic'), # Control Panel\All Control Panel Items\Fonts,
            font_size = 24,
            width = self.logwidth,
            height = self.logheight,
            text=f'{self.surname}')

        self._fathername = arcade.gui.UIInputText(
            x = self.sidebar_visibility_range+215,
            y = self.height - 540,
            text_color= black,
            font_name = ('Yu Gothic'), # Control Panel\All Control Panel Items\Fonts,
            font_size = 24,
            width = self.logwidth,
            height = self.logheight,
            text=f'{self.fathername}')

        self._gender = arcade.gui.UIInputText(
            x = self.sidebar_visibility_range+145,
            y = self.height - 650,
            text_color= black,
            font_name = ('Yu Gothic'), # Control Panel\All Control Panel Items\Fonts,
            font_size = 24,
            width = self.logwidth,
            height = self.logheight,
            text=f'{self.gender}')

        self._DOB = arcade.gui.UIInputText(
            x = self.sidebar_visibility_range+220,
            y = self.height - 760,
            text_color= black,
            font_name = ('Yu Gothic'), # Control Panel\All Control Panel Items\Fonts,
            font_size = 24,
            width = self.logwidth,
            height = self.logheight,
            text=f'{self.DOB}')

        self._user_password = arcade.gui.UIInputText(
            x = self.sidebar_visibility_range+180,
            y = self.height - 865,
            text_color= black,
            font_name = ('Yu Gothic'), # Control Panel\All Control Panel Items\Fonts,
            font_size = 24,
            width = self.logwidth,
            height = self.logheight,
            text=f'{self.user_password}')
        
        self.container.append(self._name)
        self.container.append(self._surname)
        self.container.append(self._fathername)
        self.container.append(self._gender)
        self.container.append(self._DOB)
        self.container.append(self._user_password)

        self.submit = Buttons.add_texture_button('resources/check.png',
                                                  'resources/check.png',
                                                  'resources/check.png',
                                                  _x = self.sidebar_visibility_range + 200,
                                                  _y = self.height-200 - self.main_dy*7,
                                                  _scale = .12)
        self.container.append(self.submit)
        self.submit.on_click = self.submit_on_click

        for each in self.container:
            self.manager.add(each)



    def on_draw(self):
        box(self.sidebar_visibility_range + 120, self.height - 200 - self.main_dy + 30)
        box(self.sidebar_visibility_range + 165, self.height - 200 - 2 * self.main_dy + 30)
        box(self.sidebar_visibility_range + 210, self.height - 200 - 3 * self.main_dy + 30)
        box(self.sidebar_visibility_range + 140, self.height - 200 - 4 * self.main_dy + 30)
        box(self.sidebar_visibility_range + 215, self.height - 200 - 5 * self.main_dy + 30)
        box(self.sidebar_visibility_range + 175, self.height - 200 - 6 * self.main_dy + 30)
        self.manager.draw()
        self.manager.enable()

    def submit_on_click(self, *_):
        infoarr = [self._name.text, self._surname.text, self._fathername.text, self._gender.text, self._DOB.text, self._user_password.text, self.email, self.user_id]
        info = ' '.join(str(infoarr[i]) for i in range(len(infoarr)))
        with open(f'customers_login_info/login/customer{self.user_id}.txt', 'w') as file:
            file.write(info)
        self.enabled = False


