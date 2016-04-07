


def gen_html_for_instruction(examples):
	content_list = []
	
	no_examples = len(examples)

	for i in range(0, no_examples):
		content_list.append('<b>\n')
		content_list.append('Example')
		content_list.append(str(i))
		content_list.append(":</b>\n")
		content_list.append("<p>")
		content_list.append(examples[i])
		content_list.append("\n</p>\n")

	content = ' '.join(content_list)
	#print content

	return content


def gen_html_for_question(str1, str2):
	content_list = []
	content_list.append('<HTMLQuestion xmlns="http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2011-11-11/HTMLQuestion.xsd">\n')
  	#content_list.append('<HTMLContent><![CDATA[\n')
	content_list.append('<!DOCTYPE html>\n')
	content_list.append('<html>\n')
	content_list.append('<body>\n')
	content_list.append('<form name="mturk_form" method="post" id="mturk_form" action="https:////www.mturk.com//mturk//externalSubmit>"\n')
	content_list.append('<h2> Question: Do the strings ' + str1 + ' ' + str2 + ' match? </h2>\n')

	content_list.append('</body>\n')
	content_list.append('</html>\n')

	content = ' '.join(content_list)
	#print content

	return content

def generate_qualification(location='US', tot_approved_hits = 100, approval_rate = 10):
	qualification = {}
	qualification[location] = location
	qualification[tot_approved_hits] = x
	qualification[approval_rate] = y
	return qualification

	
