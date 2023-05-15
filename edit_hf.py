import arcade
from functions import Buttons
class Edit_hf(arcade.Section):
    def __init__(self, left, bottom, width, height, user_id):
        super().__init__(left, bottom, width, height, modal = True)
        self.enabled = False
        self.user_id = user_id
        self.width = 1920
        self.height = 1080
        self.manager = arcade.gui.UIManager(self.window)
        self.container = []
        self.main_dy = self.height//10
        self.note = arcade.gui.UIInputText(
            x = self.width//2-350,
            y = self.height-250,
            text_color= arcade.color.BLACK,
            font_name = ('Yu Gothic'), # Control Panel\All Control Panel Items\Fonts,
            font_size = 24,
            width = 800,
            text='Add note:')
        self.container.append(self.note)
        self.submit = Buttons.add_texture_button('resources/check.png',
                                                  'resources/check.png',
                                                  'resources/check.png',
                                                  _x = self.width//2,
                                                  _y = self.height-200 - self.main_dy*8,
                                                  _scale = .12)
        self.container.append(self.submit)
        self.submit.on_click = self.submit_on_click
        for each in self.container:
            self.manager.add(each)
    def on_draw(self):
        arcade.draw_lrtb_rectangle_filled(self.width // 2 - 350, self.width // 2 + 450, self.height - 200, 0, arcade.color.WHITE)
        self.manager.draw()
        self.manager.enable()

    def submit_on_click(self, *_):
        text = '\n\n'+self.note.text
        with open(f'customers_login_info/health_forms/customer{self.user_id}_hf.txt', 'a') as file:
            file.write(text)
        self.enabled = False