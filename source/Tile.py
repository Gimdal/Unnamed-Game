class Tile():
	def __init__(self, tileList=[], **kwargs):
		self.tileList = tileList
		self.tileCount = len(self.tileList)
	
	# Add a new layer to this Tile
	def addTile(self, newTile):
		for tile in enumerate(self.tileList):
			if tile[1].getLayer() < newTile.getLayer():
				pass
			if tile[1].getLayer() == newTile.getLayer():
				return False # Will not add if this Tile already has a tile at this layer
			if tile[1].getLayer() > newTile.getLayer():
				self.tileList.insert(tile[0], newTile)
				self.tileCount += 1
				return True
		self.tileList.append(newTile)
		self.tileCount += 1
		return True
	
	# Delete a specific tile from this Tile
	def deleteTile(self, oldTile):
		for tile in enumerate(self.tileList):
			if tile[1] == oldTile:
				del self.tileList[tile[0]]
				self.tileCount -= 1
				return True
		return False
	
	# Delete a specific layer from this Tile
	def deleteLayer(self, layer):
		for tile in enumerate(self.tileList):
			if tile[1].getLayer() == layer:
				del self.tileList[tile[0]]
				self.tileCount -= 1
				return True
		return False
	
	# Determines if the entity can enter this Tile from that direction
	# Returns the enterable tile if yes, returns None if no
	def canEnterTile(self, direction, entity):
		for tile in self.tileList:
			if tile.canEnter(direction, entity):
				return tile
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
	
	# True if this Tile has a tile at layer, False otherwise
	def hasLayer(self, layer):
		for tile in self.tileList:
			if tile.getLayer() == layer:
				return True
		return False
	
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