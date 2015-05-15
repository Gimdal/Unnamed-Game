class LedgeTile(SliderTile):
	def canEnter(self, direction, entity):
		if direction == self.direction and entity.getLayer() == self.layer:
			return True
		return False
	
	def enter(self, direction, entity):
		entity.move(direction)
		entity.move(direction)
		entity.decreaseLayer()