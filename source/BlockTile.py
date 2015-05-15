class BlockTile(BarrierTile):
	# Blocks you from entering tile on layer below this one
	def isBlock(self):
		return True