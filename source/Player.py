class Player():
	def __init__(self, tile, layer):
		self.currentTile = tile
		tile.setOccupant(self)
		self.x = tile.x
		self.y = tile.y
	
	def move(self, direction):
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
		self.currentTile.setOccupant(None)
		self.currentTile = self.currentTile.map.getTile(newX, newY)
		self.x = newX
		self.y = newY
		self.currentTile.setOccupant(self)
		self.currentTile.enterAction(self)
	
	def setCurrentTile(self, tile):
		self.currentTile.setOccupant(None)
		self.currentTile = tile
		tile.setOccupant(self)
	
	def getLayer(self):
		return self.layer
	
	def decreaseLayer(self):
		self.layer -= 1
	
	def increaseLayer(self):
		self.layer += 1