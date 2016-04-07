#coding=utf-8
class Hit:

	"""
	Defines the structure of a HIT
	"""
	def __init__(self):
		"""
		Initializes all parameters of a HIT to default values
		"""
		self.keywords = []
		self.description = ''
		self.reward = -1
		self.duration = ''
		self.question = ''
		self.instructions = ''
		self.batch_size = -1 

	def create_hit(keywords = '', description = '', reward = '', duration = '', question = '', html_instruction = '', size = ''):
		"""
		Creates a HIT with passed input arguments

		Args:
			keywords (str): Keywords to be used for the HIT
			description (str) :  Description of the HIT
			reward (float) : Reward in cents for each correct HIT
			duration (int) : Duration for which a HIT should remain active
			question (int) : Question to be posted
			html_instruction : HTML containing instructions
			size (int) : Size of each batch i.e. number of strings to be posted in each batch

		"""
		self.keywords = keywords
		self.description = description
		self.reward = reward
		self.duration = duration
		self.question = question
		self.instructions = html_instruction
		self.batch_size = size 
