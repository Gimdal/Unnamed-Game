class DoorTile(BasicTile):
	def __init__(self, *args, **kwargs):
		super(DoorTile, self).__init__(*args, **kwargs)
		self.newMap = newMap
		self.newTile = newTile
	
	# Transport player to new map and/or new tile
	def enterAction(self, entity):
		entity.setMap(self.newMap)
		entity.setTile(self.newTile)