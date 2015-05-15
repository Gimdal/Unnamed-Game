class BasicTile():
	def __init__(self, layer, graphic, **kwargs):
		self.layer = layer
		self.graphic = graphic
		self.occupant = None
	
	# Returns layer tile is on
	def getLayer(self):
		return self.layer
	
	# Returns occupant of tile
	def getOccupant(self):
		return self.occupant
	
	# Sets the occupant of a tile
	def setOccupant(self, occupant):
		self.occupant = occupant
	
	# Is this tile a block?  
	def isBlock(self):
		return False
	
	# Entity can enter as long as tile isn't already occupied, and entity is on same layer
	def canEnter(self, direction, entity):
		if self.occupant is None && entity.getLayer() == self.layer:
			return True
		return False
	
	def enterAction(self, entity):
		pass