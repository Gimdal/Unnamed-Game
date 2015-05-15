class Map():
	def __init__(self, rowCount, columnCount):
		self.width = columnCount
		self.height = rowCount
		self.map = [[None for i in range(columnCount)] for j in range(rowCount)]
	
	# Returns the highest layer that appears in the map
	def getMaxLayer(self):
		maxLayer = 0
		for row in self.map:
			for tile in row:
				if tile.getMaxLayer() > maxLayer:
					maxLayer = tile.getMaxLayer()
		return maxLayer
	
	# Returns the tile at position (x, y), with (0, 0) the bottom left corner
	def getTile(self, x, y):
		return self.map[self.height - y - 1][x]
	
	# Sets the tile at position (x, y)
	def setTile(self, x, y, tile):
		self.map[self.height - y - 1][x] = tile
	
	# Returns the width of the map
	def getWidth(self):
		return self.width
	
	# Sets the width of the map, deleting tiles if necessary
	def setWidth(self, newWidth):
		for row in self.map:
			row = row[:newWidth]
		self.width = newWidth
	
	# Returns the height of the map
	def getHeight(self):
		return self.height
	
	# Sets the height of the map, deleting tiles if necessary
	def setHeight(self, newHeight):
		self.map = self.map[:newHeight]
		self.height = newHeight
	
	# Swaps two layers in the map
	def swapLayers(self, layerOne, layerTwo):
		for row in self.map:
			for tile in row:
				tile.swapLayers(layerOne, layerTwo)