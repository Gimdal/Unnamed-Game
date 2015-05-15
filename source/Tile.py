class Tile():
	def __init__(self, map, x, y, tileList=[], **kwargs):
		self.map = map
		self.x = x
		self.y = y
		self.tileList = tileList
		self.tileCount = len(self.tileList)
	
	# Returns x coordinate of Tile
	def getX(self):
		return self.x
	
	# Returns y coordinate of Tile
	def getY(self):
		return self.y
	
	# Returns largest layer in Tile
	def getMaxLayer(self):
		return self.tileList[len(self.tileList)-1].getLayer()
	
	# Add a new layer to this Tile
	# Returns True if successful, False otherwise
	def addTile(self, newTile):
		for tile in enumerate(self.tileList):
			if tile[1].getLayer() < newTile.getLayer():
				pass
			if tile[1].getLayer() == newTile.getLayer():
				return False # Will not add if this Tile already has a tile at this layer
			if tile[1].getLayer() > newTile.getLayer():
				self.tileList.insert(tile[0], newTile) # Adds so tiles are in order of layer
				self.tileCount += 1
				return True
		self.tileList.append(newTile)
		self.tileCount += 1
		return True
	
	# Delete a specific tile from this Tile
	# Returns True if successful, False otherwise
	def deleteTile(self, oldTile):
		for tile in enumerate(self.tileList):
			if tile[1] == oldTile:
				del self.tileList[tile[0]]
				self.tileCount -= 1
				return True
		return False
	
	# Delete a specific layer from this Tile
	# Returns True if successful, False otherwise
	def deleteLayer(self, layer):
		for tile in enumerate(self.tileList):
			if tile[1].getLayer() == layer:
				del self.tileList[tile[0]]
				self.tileCount -= 1
				return True
		return False
	
	# Determines if the entity can enter this Tile from that direction
	# Returns the enter-able tile if yes, returns None if no
	def canEnterTile(self, direction, entity):
		for tile in enumerate(self.tileList):
			if tile[1].canEnter(direction, entity):
				if not self.getLayer(tile[0]+1).isBlock():
					return tile[1]
		return None
	
	# Changes all tile layers that are layerOne to layerTwo, and vice versa
	def swapLayers(self, layerOne, layerTwo):
		i = 0
		for tile in self.tileList:
			if tile.getLayer() == layerOne:
				tile.setLayer(layerTwo)
				i += 1
				if i > 1: break
				continue
			elif tile.getLayer() == layerTwo:
				tile.setLayer(layerOne)
				i += 1
				if i > 1: break
	
	# Returns the tile in this Tile at layer layer, returns None if there aren't any
	def getLayer(self, layer):
		for tile in self.tileList:
			if tile.getLayer() == layer:
				return tile
		return None
	
	# Returns a list of this Tile's tiles, with each paired in a list with their layer
	# Should be useful later on for rendering order
	def enumerate(self):
		return [[self.tileList[i].getLayer(), self.tileList[i]] for i in range(len(self.tileList))]