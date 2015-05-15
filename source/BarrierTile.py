class BarrierTile(BasicTile):
	# Can't enter a barrier tile
	def canEnter(self, direction, entity):
		return False