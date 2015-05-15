class TrapTile(BasicTile):
	def __init__(self, *args, **kwargs):
		super(TrapTile, self).__init__(*args, **kwargs)
		self.trapType = trapType
	
	# Change action depending on trap type
	def enterAction(self, entity):
		if self.trapType == "spikes":
			pass
		elif self.trapType == "poison":
			pass