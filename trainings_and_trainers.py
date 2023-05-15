import arcade
from functions import box
import os, os.path


class Trainings(arcade.Section):
    def __init__(self, left, bottom, width, height, id, abo_type):
        super().__init__(left, bottom, width, height, modal = True)
        self.enabled = False
        self.width = self.w = 1920
        self.height = self.h = 1080
        self.w2 = self.width//2
        self.h2 = self.height//2
        self.id = id
        self.abo_type = abo_type
        self.container = []
        self.manager = arcade.gui.UIManager(self.window)
        self.buttonwidth = self.width//15
        self.trainer_ = None
        self.training_ = 'Strength'
        self.get_info()
        self.dx_ = 200
        self.dy_ = 150
        self.enroll_manager = arcade.gui.UIManager(self.window)
        
        self.date_text = arcade.gui.UIInputText(x = self.width//2+700, y = self.h2-1*self.dy_-20, text = 'Дата', font_size = 21)
        self.time_text = arcade.gui.UIInputText(x = self.width//2+700, y = self.h2-2*self.dy_-20, text = 'Время', font_size = 21)
        self.enrolllist = [self.date_text, self.time_text]
        for each in self.enrolllist:
            self.enroll_manager.add(each)
        
        
        self.trainersx = self.width//2+200
        self.trainer1Btn = arcade.gui.UIFlatButton(
            x=self.trainersx,
            y=self.height-200,
            width=self.buttonwidth,
            text='Trainer1')
        self.container.append(self.trainer1Btn)
        self.trainer1Btn.on_click = self.tr1_on_click
        
        self.trainer2Btn = arcade.gui.UIFlatButton(
            x=self.trainersx,
            y=self.height-300,
            width=self.buttonwidth,
            text='Trainer2')
        self.container.append(self.trainer2Btn)
        self.trainer2Btn.on_click = self.tr2_on_click
        
        self.trainer3Btn = arcade.gui.UIFlatButton(
            x=self.trainersx,
            y=self.height-400,
            width=self.buttonwidth,
            text='Trainer3')
        self.container.append(self.trainer3Btn)
        self.trainer3Btn.on_click = self.tr3_on_click
        self.trainers = [self.trainer1Btn.text, self.trainer2Btn.text, self.trainer3Btn.text]
        
        self.trainingsx = self.width//2+500
        self.cardioB = arcade.gui.UIFlatButton(
            x=self.trainingsx,
            y=self.height-400,
            width=self.buttonwidth,
            text='Cardio')
        self.container.append(self.cardioB)
        self.cardioB.on_click = self.cardioB_on_click
        
        
        self.strengthB = arcade.gui.UIFlatButton(
            x=self.trainingsx,
            y=self.height-300,
            width=self.buttonwidth,
            text='Strength')
        self.container.append(self.strengthB)
        self.strengthB.on_click = self.strengthB_on_click
        
        self.poolB = arcade.gui.UIFlatButton(
            x=self.trainingsx,
            y=self.height-200,
            width=self.buttonwidth,
            text='Pool')
        a = [self.poolB]
        self.pool_manager = arcade.gui.UIManager(self.window)
        for each in a:
            self.pool_manager.add(each)
        self.poolB.on_click = self.poolB_on_click
        
        self.signUp = arcade.gui.UIFlatButton(
            x=self.w2+700,
            y=self.h2-3*self.dy_-20,
            width=self.buttonwidth,
            text='Sing up')
        self.container.append(self.signUp)
        self.signUp.on_click = self.check_info
        
        for each in self.container:
            self.manager.add(each)
        
    def on_draw(self):
        arcade.draw_text(text = f'Ваша ближайшая тренировка запланирована на: {self.date_month} ', start_x= self.width//2-500, start_y= self.height-150, font_size = 21, color = arcade.color.BLACK, width = 500,  multiline=True)
        arcade.draw_text(text = f'В: {self.time}', start_x= self.width//2-500, start_y= self.height-225, font_size = 21, color = arcade.color.BLACK, width = 500,  multiline=True)
        arcade.draw_text(text = f'С тренером: {self.trainer}', start_x= self.width//2-500, start_y= self.height-275, font_size = 21, color = arcade.color.BLACK, width = 500,  multiline=True)
        arcade.draw_text(text = f'Вид тренировки: {self.type}', start_x= self.width//2-500, start_y= self.height-325, font_size = 21, color = arcade.color.BLACK, width = 500,  multiline=True)
        self.manager.enable()
        self.manager.draw()
        if self.trainer_ is not None:
            self.draw_timetable()
            self.enroll_manager.enable()
            box(self.w2+700, self.h2-.65*self.dy_-20)
            box(self.w2+700, self.h2-1.65*self.dy_-20)
            self.enroll_manager.draw()
        if self.abo_type == 'member_black' or self.abo_type == 'member_yellow':
            self.pool_manager.draw()
            self.pool_manager.enable()
        
    def get_info(self):
        path = 'trainings'
        for (dirpath, dirnames, filenames) in os.walk(path):
            for filename in filenames:
                if filename == f'customer{self.id}.txt':
                    with open(os.path.join(dirpath, filename), 'r') as f:
                        self.data = f.readlines()[0].split()
                        break
        self.date_month = self.data[0]+' '+self.data[1]
        self.time = self.data[2]
        self.type = self.data[3]
        self.trainer = ' '.join(i for i in self.data[4:])
        
        
    def get_trainer_time(self):
        path = 'trainers'
        for (dirpath, dirnames, filenames) in os.walk(path):
            for filename in filenames:
                if filename == f'trainer{self.trainer_}.txt':
                    with open(os.path.join(dirpath, filename), 'r') as f:
                        data = f.readlines()
        self.trainertimes = [data[i].split() for i in range(len(data))] 
        
    def draw_timetable(self):
        arcade.draw_text(self.date_month.split()[-1], start_x=self.w2-3*self.dx_, start_y=self.h2-.5*self.dy_, font_size = 21, color = arcade.color.BLACK)
        for j in range(len(self.trainertimes)):
            arcade.draw_text(self.trainertimes[j][0], start_x=self.w2-3*self.dx_, start_y=self.h2-(3-j)*self.dy_, font_size = 21, color = arcade.color.BLACK)
            for i in range(1, len(self.trainertimes[j])):
                arcade.draw_text(self.trainertimes[j][i], start_x=self.w2-(3-i)*self.dx_, start_y=self.h2-(3-j)*self.dy_, font_size = 21, color = arcade.color.BLACK)
                
    def check_info(self, *_):
        with open('trainers/trainer2.txt', 'r') as f:
            data = f.readlines()
        num = None
        available_dates = [self.trainertimes[i][0] for i in range(len(self.trainertimes))]
        if not self.date_text.text in available_dates:
            return 
        else:   
            for i in range(len(self.trainertimes)):
                if self.date_text.text in self.trainertimes[i]:
                    num = i
                    available_times = self.trainertimes[num][1:]
                    break
        if self.time_text.text not in available_times:
            return
        else:
            available_times.remove(self.time_text.text)
            available_times.insert(0, self.date_text.text)
            final_array = []
            for i in range(len(self.trainertimes)):
                if i != num:
                    final_array.append(self.trainertimes[i])
                else:   
                    final_array.append(available_times)
        strs = [None for i in range(len(final_array))]
        for j in range(len(final_array)):
            val = ''
            for i in range(len(final_array[j])):
                val += ' '+final_array[j][i]
            val += '\n'
            strs[j] = val
        strs[-1] = strs[-1][:-1]
        for i in range(len(strs)):
            strs[i] = strs[i][1:]
        res = ''.join(strs[i] for i in range(len(strs)))
        with open(f'trainers/trainer{self.trainer_}.txt', 'w') as f:
            f.write(res)
            f.close()
        with open(f'trainings/customer{self.id}.txt', 'a') as f:
            res_ = '\n' + self.date_month + ' ' + self.time_text.text + ' ' + self.training_ + ' ' + f'Trainer{self.trainer_}'
            f.write(res_)
        self.get_trainer_time()
        self.get_info()
        
    def tr1_on_click(self, *_):
        self.trainer_ = 1
        self.get_trainer_time()
        
    def tr2_on_click(self, *_):
        self.trainer_ = 2   
        self.get_trainer_time()

    def tr3_on_click(self, *_):
        self.trainer_ = 3
        self.get_trainer_time()

    def poolB_on_click(self, *_):
        self.training_ = 'Pool'
        
    def cardioB_on_click(self, *_):
        self.training_ = 'Cardio'
        
    def strengthB_on_click(self, *_):
        self.training_ = 'Strength'
        