class SliderTile(BasicTile):
	# SliderTile forces player in a certain direction (if possible) upon entering
	def __init__(self, *args, **kwargs):
		super(SliderTile, self).__init__(*args, **kwargs)
		self.direction = direction
	
	def enterAction(self, entity):
		entity.tryMove(self.direction)