'''
Data Structure for the all Tilemons in the world

	* Each Tilemon keeps track of its own:
		+ age
		+ location
		+ genetic code

	* Society keeps a record of:
		+ all living creatures
		+ all species listings

	* World will use the information in Society to find life statistics, 
	  such as:
	  	+ how much surface area of each species is covered
	  	+ how much space each species has around it

	* WorldEngine will use Society to do large-scale operations, such as:
		+ moving species members closer together
		+ reproduction
		+ killing creatures


'''

class Society():
	def __init__(self):
		self.creatures = []
		self.species = {} # defaultdict?
			# --> maps each species to the creatures classified under it