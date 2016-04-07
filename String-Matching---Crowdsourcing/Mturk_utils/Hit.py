class Hit:

	def __init__(self):
		self.keywords = []
		self.description = ''
		self.reward = -1
		self.duration = ''
		self.question = ''
		self.instructions = ''
		self.batch_size = -1 

	def create_hit(keywords = '', description = '', reward = '', duration = '', question = '', html_instruction = '', size = ''):
		self.keywords = keywords
		self.description = description
		self.reward = reward
		self.duration = duration
		self.question = question
		self.instructions = html_instruction
		self.batch_size = size 
