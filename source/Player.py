class Player():
	def __init__(self, map, tile, layer, direction):
		self.map = map
		self.tile = tile
		tile.setOccupant(self)
		self.layer = layer
		self.direction = direction
	
	# Returns direction player is facing
	def getDirection(self):
		return self.direction
	
	# Sets direction player is facing
	def setDirection(self, direction):
		self.direction = direction
	
	# Returns map the player is in
	def getMap(self):
		return self.map
	
	# Sets map the player is in
	def setMap(self, map):
		self.map = map
	
	# Returns tile the player is on
	def getTile(self):
		return self.tile
	
	# Sets tile the player is on
	def setTile(self, tile):
		self.tile.setOccupant(None)
		self.tile = tile
		tile.setOccupant(self)
	
	# Returns layer of the player
	def getLayer(self):
		return self.layer
	
	# Sets layer of the player
	def setLayer(self, layer):
		self.layer = layer
	
	# Decreases current layer by 1
	def decreaseLayer(self):
		self.layer -= 1
	
	# Increases current layer by 1
	def increaseLayer(self):
		self.layer += 1
	
	# Moves only if possible
	def tryMove(self, *args):
		if len(args) == 1:
			newX = self.tile.getX()
			newY = self.tile.getY()
			if direction == "left":
				newX -= 1
			elif direction == "up":
				newY += 1
			elif direction == "right":
				newX += 1
			elif direction == "down":
				newY -= 1
		else:
			newX = args[0]
			newY = args[1]
		if self.map.getTile(newX, newY).canEnter():
			self.move(newX, newY)
	
	# Moves
	def move(self, *args):
		if len(args) == 1:
			direction = args[0]
			self.direction = direction
			newX = self.tile.getX()
			newY = self.tile.getY()
			if direction == "left":
				newX -= 1
			elif direction == "up":
				newY += 1
			elif direction == "right":
				newX += 1
			elif direction == "down":
				newY -= 1
		else:
			newX = args[0]
			newY = args[1]
			if newX < self.tile.getX():
				self.direction = "left"
			elif newX > self.tile.getX():
				self.direction = "right"
			elif newY < self.tile.getY():
				self.direction = "down"
			else:
				self.direction = "up"
		self.tile.setOccupant(None)
		self.tile = self.map.getTile(newX, newY)
		self.tile.setOccupant(self)
		self.tile.enterAction(self)