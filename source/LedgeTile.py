class LedgeTile(SliderTile):
	# Can only be entered from one direction
	def canEnter(self, direction, entity):
		if direction == self.direction and entity.getLayer() == self.layer:
			return True
		return False
	
	# Forces player in a direction and decreases their layer
	def enterAction(self, entity):
		entity.decreaseLayer()
		entity.move(self.direction)