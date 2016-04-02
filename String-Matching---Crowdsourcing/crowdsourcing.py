import pandas as pd 
import boto.mturk as mturk
from boto.mturk.connection import MTurkConnection

#For dev environment
DEV_HOST = 'mechanicalturk.sandbox.amazonaws.com'

#For production
REAL_HOST = 'mechanicalturk.amazonaws.com'

aws_parameters = {}
mtc = None

class Hit:

	def __init__(self):
		self.keywords = []
		self.description = ''
		self.reward = -1
		self.duration = ''
		self.question = ''
		self.instructions = ''
		self.batch_size = -1 

	'''
	keywords = list
	description = strings
	question = string
	'''

	def create_hit(keywords = '', description = '', reward = '', duration = '', question = '', html_instruction = '', size = ''):
		self.keywords = keywords
		self.description = description
		self.reward = reward
		self.duration = duration
		self.question = question
		self.instructions = html_instruction
		self.batch_size = size 


def generate_qualification(location='US', tot_approved_hits = 100, approval_rate = 10):
	qualification = {}
	qualification[location] = location
	qualification[tot_approved_hits] = x
	qualification[approval_rate] = y
	return qualification

def set_aws_parameters(aws):
	aws_parameters['access_key'] = aws['access_key']
	aws_parameters['secret_key'] = aws['secret_key']

def check_account_balance(num_instances, price):
	mtc = MTurkConnection(aws_access_key_id = aws_parameters['access_key'],
                      aws_secret_access_key = aws_parameters['secret_key'],
                      debug = 2, #prints out all requests
                      host = DEV_HOST)

	if mturk.get_account_balance() < num_instances *  price.amount:
		return -1
	else:
		return 1

def create_batches(l_attr_name, l_attr, r_attr_name, r_attr, batch_size):
	#Create batches with each batch containing hit.batch_size number of instances
	
    # batch_list contains each batch of strings as a data frame
	df_batch_list = []
	num_rows = len(l_attr.axes[0])
	combined_data_frame = l_attr
	combined_data_frame[r_attr_name] = r_attr

	for i in range(0, (int)(num_rows/batch_size) + 1):
		index = i * batch_size
    	#print index
    	batch_df = combined_data_frame[index : index + batch_size]
    	#print batch_df
    	df_batch_list.append(batch_df)


	batch_list = []
	for data_frame in list_df:
		batch_list.append(data_frame.values.flatten())
		#print batch_list


	# for i in range(0, batch_size):
	# 	batch = []
	
	# 	new_l = l_attr[(i * batch_size) : ((i * batch_size) + batch_size)]
	# 	new_r = r_attr[(i * batch_size) : ((i * batch_size) + batch_size)]

	# 	for row1,row2 in new_l.iterrows(), new_r.iterrows():
	#     		string_pair = []
	#         	string_pair.append(row1[l_attr_name])
	#         	string_pair.append(row2[r_attr_name])
	#         	batch.append(string_pair)
	# 	batch_list.append(batch)

	return batch_list


def create_hits(hit):
	question_form  = create_question(hit.question)

	mtc.create_hit(questions = question_form,
               max_assignments = 1,
               title = hit.question,
               description = hit.description,
               keywords = hit.keywords,
               duration = hit.duration,
               reward = hit.reward)


def create_question(question):
	qc1 = QuestionContent()
	qc1.append_field('Title',question)
 
    #selections = ['Match', 'No match']

	fta1 = SelectionAnswer(min = 1, max = 1,style = 'radiobutton',
                      #selections = selections,
                      type = 'text',
                      other = False)
 
	q1 = Question(identifier='design',
              content=qc1,
              answer_spec=AnswerSpecification(fta1),
              is_required=True)

	question_form = QuestionForm()
	question_form.append(q1)
	return question_form


def label_using_crowd(A, l_id, r_id, l_attr_name, r_attr_name, l_attr, r_attr, aws, hit, qualification, num_assignments=3, output_attrs=[]):
	if hit.batch_size <= 0 or batch_size >= len(l_attr.axes[0]):
		print 'Invalid batch size'
		return

	if (check_account_balance(len(l_attr(axes[0]))) == 1):
		#Set the AWS parameters - access key and secret key
		set_aws_parameters(aws)
		
		#Create batches containing strings to match
		batches = create_batches(l_attr_name, l_attr, r_attr_name, r_attr, hit.batch_size)

		#Create hits
		create_hits()
		
	else:
		print 'Not enough balance in account to post hits'
		return


def main():
	aws = {}
	aws['access_key'] = 0
	aws['secret_key'] = 0
	set_aws_parameters(aws)
	#label_using_crowd()

if __name__ == '__main__':
	main()





	
