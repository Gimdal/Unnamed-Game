import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.core.image import Image
from kivy.core.window import Window
from kivy.config import Config
from kivy.graphics import Color, Rectangle
from kivy.graphics.texture import Texture
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput


Config.set('input', 'mouse', 'mouse,disable_multitouch')
Window.size = (1024, 768)
tileRes = 64

class RootWidget(GridLayout):
	def __init__(self, **kwargs):
		super(RootWidget, self).__init__(**kwargs)
		self.width = kwargs["rootWidth"]
		self.height = kwargs["rootHeight"]
		
		self.topLayout = GridLayout(cols = 4, size_hint_y = None, height = 50)
		self.add_widget(self.topLayout)
		
		self.bottomLayout = GridLayout(cols = 3)
		self.add_widget(self.bottomLayout)
		
		self.leftOptions = GridLayout(cols = 1, size_hint_x = None, width = 4*tileRes + 5)
		self.bottomLayout.add_widget(self.leftOptions)
		
		self.mapArea = ScrollView(scroll_type = ["bars"], 
									bar_width = 8, 
									bar_color = [0, 0, 0, 1], 
									bar_inactive_color = [0, 0, 0, .1])
		self.bottomLayout.add_widget(self.mapArea)
		
		self.rightOptions = GridLayout(size_hint_x = None, width = 150)
		self.bottomLayout.add_widget(self.rightOptions)
		
		### TOP BAR ###
		# BUTTONS:
		newBtn = Button(text = "New Map", size_hint = (None, None), size = (100, 30))
		saveBtn = Button(text = "Save Map", size_hint = (None, None), size = (100, 30))
		loadBtn = Button(text = "Load Map", size_hint = (None, None), size = (100, 30))
		optionsBtn = Button(text = "Options", size_hint = (None, None), size = (100, 30))
		
		self.topLayout.add_widget(newBtn)
		self.topLayout.add_widget(saveBtn)
		self.topLayout.add_widget(loadBtn)
		self.topLayout.add_widget(optionsBtn)
		
		
		
		
		### LEFT SIDEBAR ###
		# LABELS:
		MP = Label(text = "Map Properties", color = [0, 0, 0, 1], size_hint_y = None, height = 20)
		ID = Label(text = "ID:", color = [0, 0, 0, 1], size_hint = (None, None), size = (60, 20))
		NM = Label(text = "Name:", color = [0, 0, 0, 1], size_hint = (None, None), size = (60, 20))
		WD = Label(text = "Width:", color = [0, 0, 0, 1], size_hint = (None, None), size = (60, 20))
		HT = Label(text = "Height:", color = [0, 0, 0, 1], size_hint = (None, None), size = (60, 20))
		
		# TEXT INPUTS:
		self.IDTB = TextInput(multiline = False, size_hint = (None, None), size = (100, 20), padding = [3, 3, 3, 3])
		self.NMTB = TextInput(multiline = False, size_hint = (None, None), size = (100, 20), padding = [3, 3, 3, 3])
		self.WDTB = TextInput(text = str(self.width), multiline = False, size_hint = (None, None), size = (100, 20), padding = [3, 3, 3, 3])
		self.HTTB = TextInput(text = str(self.height), multiline = False, size_hint = (None, None), size = (100, 20), padding = [3, 3, 3, 3])
		
		self.leftOptions.add_widget(MP)
		self.leftLayoutTop = GridLayout(cols = 2, padding = [5, 5, 5, 5], size_hint_y = None, height = 90)
		self.leftOptions.add_widget(self.leftLayoutTop)
		
		self.leftLayoutTop.add_widget(ID)
		self.leftLayoutTop.add_widget(self.IDTB)
		self.leftLayoutTop.add_widget(NM)
		self.leftLayoutTop.add_widget(self.NMTB)
		self.leftLayoutTop.add_widget(WD)
		self.leftLayoutTop.add_widget(self.WDTB)
		self.leftLayoutTop.add_widget(HT)
		self.leftLayoutTop.add_widget(self.HTTB)

		self.paletteHeight = 20
		self.leftLayoutBottom = GridLayout(cols = 1)
		self.leftOptions.add_widget(self.leftLayoutBottom)
		self.paletteWindow = ScrollView(scroll_type = ["bars"], 
									bar_width = 8, 
									bar_color = [0, 0, 0, 1], 
									bar_inactive_color = [0, 0, 0, .1],
									size_hint_y = 1)
		self.leftLayoutBottom.add_widget(self.paletteWindow)
		self.palette = FloatLayout(size_hint = (None, None), size = (4*tileRes + 5, self.paletteHeight*tileRes + self.paletteHeight + 1))
		self.paletteWindow.add_widget(self.palette)
		with self.palette.canvas.before:
			Color(0, 0, 0, 1)
			Rectangle(size = self.palette.size, pos = self.palette.pos)
			Color(1, 1, 0.5, 1)
			for i in range(4):
				for j in range(self.paletteHeight):
					Rectangle(size = (tileRes, tileRes), pos = (tileRes * i + i + 1, tileRes * j + j + 1))
		self.leftLayoutBottom.add_widget(Button(size_hint_y = None, height = 25))
		
		
		### MAP AREA ###
		self.actualMap = FloatLayout(size_hint = (None, None), size = (tileRes * self.width + self.width + 1, tileRes * self.height + self.height + 1))
		self.mapArea.add_widget(self.actualMap)
		with self.actualMap.canvas.before:
			Color(0, 0, 0, 1)
			Rectangle(size = self.actualMap.size, pos = self.actualMap.pos)
			Color(.9, .9, .9, .9)
			for i in range(self.width):
				for j in range(self.height):
					Rectangle(size = (tileRes, tileRes), pos = (tileRes * i + i + 1, tileRes * j + j + 1))
	
	def updateMap(self, x, y, layer, graphic):
		pass
	#texture = Image("C:\\Users\\Daryl\\Desktop\\Unnamed-Game\\graphics\\textures.png").texture
	#topLeft = texture.get_region(0, tileRes, tileRes, 0)
	#with actualMap.canvas.before:
	#	Rectangle(texture = topLeft, pos = (200, 350), size = (tileRes, tileRes))
	
	
	### RIGHT BAR ###
	#Todo

class MainWindow(App):
	def build(self):
		width = 36
		height = 25
		self.root = root = RootWidget(cols = 1, rootWidth = width, rootHeight = height)
		# listen to size and position changes
		root.bind(pos = self.update_rect, size = self.update_rect)
		
		with root.canvas.before:
			Color(1, 1, 1, 1)
			self.rect = Rectangle(size = root.size, pos = root.pos)
		
		return root
		
	def update_rect(self, instance, value):
		self.rect.pos = instance.pos
		self.rect.size = instance.size


if __name__ == "__main__":
	MainWindow().run()