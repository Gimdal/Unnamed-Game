class BasicTile():
	def __init__(self, map, xCoord, yCoord, layer, graphic, **kwargs):
		self.map = map
		self.x = xCoord
		self.y = yCoord
		self.layer = layer
		self.graphic = graphic
		self.occupant = None
	
	def getLayer(self):
		return self.layer
	
	def setLayer(self, layer):
		self.layer = layer
	
	def canEnter(self, direction, entity):
		if self.occupant is None && entity.getLayer() == self.layer:
			return True
		return False
	
	def canExit(self, direction, layer):
		newX = self.x
		newY = self.y
		if direction == 0:
			newX -= 1
		elif direction == 1:
			newY += 1
		elif direction == 2:
			newX += 1
		elif direction == 3:
			newY -= 1
		if self.map.getTile(newX, newY) != False && self.map.getTile(newX, newY).canEnter((direction + 2) % 4):
			return True
		return False
	
	def setOccupant(self, occupant):
		self.occupant = occupant
	
	def enterAction(self, entity):
		pass