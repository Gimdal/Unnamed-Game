class LadderTile(BasicTile):
	def canEnter(self, direction, entity):
		if direction == "left" or direction == "right":
			if entity.getLayer() == self.layer:
				# Entering from the side on same layer, allowed
				return True
			else:
				# Entering from side on different layer, not allowed
				return False
		if direction == "up":
			if entity.getLayer() == self.layer:
				# Entering from below on same layer, allowed
				return True
			else:
				# Entering from below on any other layer, not allowed
				return False
		if entity.getLayer() == self.layer + 1:
			# Entering from above one layer up, allowed
			return True
		# Entering from above on any other layer, now allowed
		return False
	
	# Forces player to move completely up or down the ladder
	def enterAction(self, entity):
		if entity.getLayer() > self.layer:
			entity.decreaseLayer()
			entity.move("down")
		else:
			entity.increaseLayer()
			entity.move("up")