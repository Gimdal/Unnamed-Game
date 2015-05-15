class SliderTile(BasicTile):
	def __init__(self, map, xCoord, yCoord, layer, graphic, direction=0, **kwargs):
		super().__init__(map, xCoord, yCoord, layer, graphic)
		self.direction = direction
	
	def enterAction(self, entity):
		newX = self.x
		newY = self.y
		if self.direction == 0:
			newX -= 1
		elif self.direction == 1:
			newY += 1
		elif self.direction == 2:
			newX += 1
		elif self.irection == 3:
			newY -= 1
		if self.map.getTile(newX, newY).canEnter(direction, entity):
			entity.move(direction)