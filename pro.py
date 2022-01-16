from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class FirstScr(Screen):
	def __init__(self, name='first'):
		super().__init__(name=name) 
		vl = BoxLayout(orientation='vertical')
		self.lbl = Label()
		vl.add_widget(self.lbl) 
		#####################
		hl1 = BoxLayout()
		btn1 = Button(text='1')
		btn1.on_press = lambda : self.AddSymbol('1')
		btn2 = Button(text='2')
		btn2.on_press = lambda : self.AddSymbol('2')
		btn3 = Button(text='3')
		btn3.on_press = lambda : self.AddSymbol('3')
		btnPlus = Button(text='+')
		btnPlus.on_press = lambda : self.AddSymbol('+')
		hl1.add_widget(btn1)
		hl1.add_widget(btn2)
		hl1.add_widget(btn3)
		hl1.add_widget(btnPlus)
		vl.add_widget(hl1)
		######################
		hl2 = BoxLayout()
		btn4 = Button(text='4')
		btn4.on_press = lambda : self.AddSymbol('4')
		btn5 = Button(text='5')
		btn5.on_press = lambda : self.AddSymbol('5')
		btn6 = Button(text='6')
		btn6.on_press = lambda : self.AddSymbol('6')
		btnMinus = Button(text='-')
		btnMinus.on_press = lambda : self.AddSymbol('-')
		hl2.add_widget(btn4)
		hl2.add_widget(btn5)
		hl2.add_widget(btn6)
		hl2.add_widget(btnMinus)
		vl.add_widget(hl2)
		######################
		hl3 = BoxLayout()
		btn7 = Button(text='7')
		btn7.on_press = lambda : self.AddSymbol('7')
		btn8 = Button(text='8')
		btn8.on_press = lambda : self.AddSymbol('8')
		btn9 = Button(text='9')
		btn9.on_press = lambda : self.AddSymbol('9')
		btnMult = Button(text='-')
		btnMult.on_press = lambda : self.AddSymbol('-')
		hl3.add_widget(btn7)
		hl3.add_widget(btn8)
		hl3.add_widget(btn9)
		hl3.add_widget(btnMult)
		vl.add_widget(hl3)
		######################
		hl4 = BoxLayout()
		btnClear = Button(text='C')
		btnClear.on_press = self.Clear
		btn0 = Button(text='0')
		btn0.on_press = lambda : self.AddSymbol('0')
		btnEqual = Button(text='=')
		btnEqual.on_press = self.Equal
		btnDiv = Button(text='/')
		btnDiv.on_press = lambda : self.AddSymbol('/')
		hl4.add_widget(btnClear)
		hl4.add_widget(btn0)
		hl4.add_widget(btnEqual)
		hl4.add_widget(btnDiv)
		vl.add_widget(hl4)
		######################
		self.add_widget(vl) 
	def AddSymbol(self,s):
		self.lbl.text = self.lbl.text+s
	def Equal(self):
		self.lbl.text = str( eval(self.lbl.text) )
		#Запихиваем в eval()
		#результат работы eval() снова пихаем на лейбл
	def Clear(self):
		self.lbl.text = self.lbl.text[0:-1]
	def next(self):
		self.manager.transition.direction = 'left' 								   
		self.manager.current = 'second'


class SecondScr(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)
        pass
    def next(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'first'

class MyApp(App):
	def build(self):
		sm = ScreenManager()
		sm.add_widget(FirstScr())
		sm.add_widget(SecondScr())
		return sm

app = MyApp()
app.run()