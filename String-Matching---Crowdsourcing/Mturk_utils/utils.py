#coding=utf-8

def gen_html_for_instruction(examples):
	"""
	Generates HTML for Instructions

	Args: 
		examples (tuple) : Input examples for which HTML is to be generated

	Returns:
		HTML content generated (str)

	Examples:
		>>> gen_html_for_instruction(("(abc, aabc) - not match", "(abc, abc) - match"))
		<b>
		Example 1:
		</b>
		<p>
		(abc, aabc) - not match
		</p>
		<b>
		Example 2:
		</b>
		<p>
		(abc, abc) - match
		</p>

	"""
	content_list = []
	
	no_examples = len(examples)

	for i in range(0, no_examples):
		content_list.append('<b>\n')
		content_list.append('Example')
		content_list.append(str(i))
		content_list.append(":\n</b>\n")
		content_list.append("<p>")
		content_list.append(examples[i])
		content_list.append("\n</p>\n")

	content = ' '.join(content_list)
	#print content

	return content

def generate_qualification(location='US', tot_approved_hits = 100, approval_rate = 10):
	"""
	Generates a qualification for workers from input arguments

	Args:
		location (str) :  Location of workers
		tot_approved_hits (int) : Total number of hits approved for the workers
		approval_rate (int) : Approval rate for the workers

	Returns:
		Dictionary with location, tot_approved_hits and approval_rate populated
	"""
	qualification = {}
	qualification[location] = location
	qualification[tot_approved_hits] = x
	qualification[approval_rate] = y
	return qualification

	
