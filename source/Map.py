class Map():
	def __init__(self, rowCount, columnCount):
		self.width = columnCount
		self.height = rowCount
		self.matrix = [[None for i in range(columnCount)] for j in range(rowCount)]
	
	def changeWidthTo(self, newWidth):
		for subMatrix in self.matrix:
			subMatrix = subMatrix[:newWidth]
		self.width = newWidth
	
	def changeHeightTo(self, newHeight):
		self.matrix = self.matrix[:newHeight]
		self.height = newHeight
	
	def addTile(self, x, y, tile):
		self.matrix[self.height - y - 1][x] = tile
	
	def getTile(self, x, y):
		return self.matrix[self.height - y - 1][x]
	
	def swapLayers(self, layerOne, layerTwo):
		for row in self.matrix:
			for tile in row:
				tile.swapLayers(layerOne, layerTwo)