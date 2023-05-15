import arcade
from functions import box
from functions import Buttons

class Cards(arcade.Section):
    def __init__(self, left, bottom, width, height, textures, params):
        super().__init__(left, bottom, width, height, modal = True)
        self.enabled = False
        self.width = 1920
        self.height = 1080
        self.w2 = self.width//2
        self.h2 = self.height//2
        self.abo_type = params
        self.textures = textures
        self.container = []
        self.manager = arcade.gui.UIManager(self.window)
        self.pool = arcade.load_texture('resources/pool.png')
        self.pool.text = 'Посещение плавательного бассейна, длинна которого составляет 25 метров, а глубина доходит до 3. Для очистки воды исопльзуются лишь самые современные средства.'
        self.cardio = arcade.load_texture('resources/cardio.png')
        self.cardio.text = 'Кардио-зона была переоборудована и дополнена самыми разнообразными и новейшими тренажёрами для комфортной и разнообразной работы, ведь каждому нравится своё, и он точно сможет найти здесь то, что ему понравится'
        self.solarium = arcade.load_texture('resources/solarium.png')
        self.solarium.text = 'Витамин D, которого у нас так недостаёт можно получить в нашем солярии, также как и красивый, ровный загар, который так всем нравится.'
        self.gym = arcade.load_texture('resources/gym.png')
        self.gym.text = 'Неограниченное посещение тренажёрного зала, оснащённого самым современным оборудованием. Наши тренажёры постоянно обновляются, добавляются новые и более современные образцы, ведь мир спорта тоже не стоит на месте.'
        self.massage = arcade.load_texture('resources/massage.png')
        self.massage.text = 'Наши массажисты будут рады предоставить самый разнообразный спектр массажей. Оздаравливающий или расслабляющий ? Всё это присутствует в нашем массажном кабинете.'
 
        self.close = Buttons.add_texture_button('resources/close_ash.png',
                                                       'resources/close_ash.png',
                                                       'resources/close_ash.png',
                                                       _x = self.width-40,
                                                       _y = self.height-40,
                                                       _scale = 1.5
                                                 )
        self.container.append(self.close)
        self.close.on_click = self.close_on_click

        for each in self.container:
            self.manager.add(each)
 


    def on_draw(self):
            arcade.draw_lrtb_rectangle_filled(0, self.width, self.height, 0, arcade.color.ASH_GREY)
            arcade.draw_texture_rectangle(self.w2-140, self.height-140, 50, 50, self.card)
            arcade.draw_text(text = 'включает в себя', start_x= self.w2-110, start_y= self.height-150, font_size = 18, color = arcade.color.BLACK, )
            arcade.draw_texture_rectangle(self.pos, self.height-300, 300, 200, self.gym)
            arcade.draw_text(text = self.gym.text, start_x= self.pos-100, start_y= self.h2+100, font_size = 18, color = arcade.color.BLACK, width = 250,  multiline=True)
            arcade.draw_texture_rectangle(self.pos+self.dx, self.height-300, 300, 200, self.cardio)
            arcade.draw_text(text = self.cardio.text, start_x= self.pos+self.dx-100, start_y= self.h2+100, font_size = 18, color = arcade.color.BLACK, width = 250,  multiline=True)
            self.manager.draw()
            self.manager.enable()
            if self.amount <= 3:
                arcade.draw_text(f'Также по данному абонементу доступны {self.amount-1} тренировки с тренером в неделю', start_x= self.w2-450, start_y= 150, font_size = 18, color = arcade.color.BLACK)
            if self.amount > 3:
                arcade.draw_texture_rectangle(self.pos+2*self.dx, self.height-300, 300, 200, self.solarium)
                arcade.draw_text(text = self.solarium.text, start_x= self.pos+2*self.dx-100, start_y= self.h2+100, font_size = 18, color = arcade.color.BLACK, width = 250,  multiline=True)
                if self.amount == 4:
                     arcade.draw_text(f'Также по данному абонементу доступны {self.amount-1} тренировки с тренером в неделю', start_x= self.w2-450, start_y= 150, font_size = 18, color = arcade.color.BLACK)
            if self.amount > 4:
                arcade.draw_texture_rectangle(self.pos+3*self.dx, self.height-300, 300, 200, self.pool)
                arcade.draw_text(text = self.pool.text, start_x= self.pos+3*self.dx-100, start_y= self.h2+100, font_size = 18, color = arcade.color.BLACK, width = 250,  multiline=True)
                if self.amount == 5:
                    arcade.draw_text(f'Также по данному абонементу доступны {self.amount-1} тренировки с тренером в неделю', start_x= self.w2-450, start_y= 150, font_size = 18, color = arcade.color.BLACK)
            if self.amount > 5:
                arcade.draw_texture_rectangle(self.pos+4*self.dx, self.height-300, 300, 200, self.massage)
                arcade.draw_text(text = self.massage.text, start_x= self.pos+4*self.dx-100, start_y= self.h2+100 , font_size = 18, color = arcade.color.BLACK, width = 250,  multiline=True)
                arcade.draw_text('Также по данному абонементу вы можете заниматься с тренером в любое свободное время', start_x= self.w2-550, start_y= 150, font_size = 18, color = arcade.color.BLACK)

    def get_card(self):
        self.card = arcade.load_texture(self.textures[self.abo_type])
        self.pos = self.width//self.amount
        self.dx = self.width//self.amount
    
    def close_on_click(self, *_):
        self.enabled = False