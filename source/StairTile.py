class StairTile(BasicTile):
	def __init__(self, *args, **kwargs):
		super(StairTile, self).__init__(*args, **kwargs)
		self.direction = direction
	
	# Way complicated because stairs are directional, mostly same code over and over
	def canEnter(self, direction, entity):
		if self.direction = "up":
			if direction == "down":
				if entity.getLayer() == self.layer + 1:
					return True # Can enter if going down stairs
				else:
					return False # But not if you're not on the right layer
			if direction == "left" or direction == "right" or direction == "up":
				if entity.getLayer() == self.layer:
					return True # Can enter if moving along wide stairs or going up stairs
				else:
					return False # Unless you're on the wrong layer
		elif self.direction = "down":
			if direction == "up":
				if entity.getLayer() == self.layer + 1:
					return True
				else:
					return False
			if direction == "left" or direction == "right" or direction == "down":
				if entity.getLayer() == self.layer:
					return True
				else:
					return False
		elif self.direction = "left":
			if direction == "right":
				if entity.getLayer() == self.layer + 1:
					return True
				else:
					return False
			if direction == "left" or direction == "down" or direction == "up":
				if entity.getLayer() == self.layer:
					return True
				else:
					return False
		elif self.direction = "right":
			if direction == "left":
				if entity.getLayer() == self.layer + 1:
					return True
				else:
					return False
			if direction == "down" or direction == "right" or direction == "up":
				if entity.getLayer() == self.layer:
					return True
				else:
					return False
	
	# Also complicated due to directionality
	def enterAction(self, entity):
		if entity.getDirection() == self.direction:
			entity.increaseLayer()
		elif self.direction = "left":
			if entity.getDirection() == "up" or entity.getDirection() == "down":
				pass # Don't change layer if moving along stairs
			else:
				entity.decreaseLayer() # Decrease is moving down stairs
		elif self.direction = "up":
			if entity.getDirection() == "left" or entity.getDirection() == "right":
				pass
			else:
				entity.decreaseLayer()
		elif self.direction = "right":
			if entity.getDirection() == "up" or entity.getDirection() == "down":
				pass
			else:
				entity.decreaseLayer()
		elif self.direction = "down":
			if entity.getDirection() == "left" or entity.getDirection() == "right":
				pass
			else:
				entity.decreaseLayer()