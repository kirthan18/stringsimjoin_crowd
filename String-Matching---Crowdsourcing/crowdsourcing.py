import pandas as pd 
import boto.mturk as mturk
from boto.mturk.connection import MTurkConnection
from Mturk_utils import Hit
from Mturk_utils import utils
from boto.mturk.question import QuestionContent,Question,QuestionForm,Overview,AnswerSpecification,SelectionAnswer,FormattedContent,FreeTextAnswer

#For dev environment
DEV_HOST = 'mechanicalturk.sandbox.amazonaws.com'

#For production
REAL_HOST = 'mechanicalturk.amazonaws.com'

aws_parameters = {'access_key' : 'AKIAJVQPL4WDMPIPJLJQ',
				   'secret_key' : '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'}
mtc = None

matches =[('Not a match','0'),
	         ('Match','1'),
	         ('I dont know','-1'),]

title = 'Do the following strings match?'
description = 'Are the two strings listed similar to each other?'
keywords = 'string, matching, string similarity'
duration = 60


def set_aws_parameters(aws):
	aws_parameters['access_key'] = aws['access_key']
	aws_parameters['secret_key'] = aws['secret_key']


def check_account_balance(num_instances, price):

	mtc = MTurkConnection(aws_access_key_id = aws_parameters['access_key'],
                      aws_secret_access_key = aws_parameters['secret_key'],
                      debug = 1, 
                      host = DEV_HOST)

	#print mtc.get_account_balance()

	if mtc.get_account_balance() < num_instances *  price:
		return -1
	else:
		return 1

def create_batches(l_attr_name, l_attr, r_attr_name, r_attr, batch_size):
	#Create batches with each batch containing hit.batch_size number of instances
	
    # batch_list contains each batch of strings as a data frame
	df_batch_list = []
	num_rows = len(l_attr.axes[0])
	#print 'Number of rows in data frame : ' + str(num_rows)
	combined_data_frame = l_attr
	combined_data_frame[r_attr_name] = r_attr

	end_range = (int)((num_rows/batch_size) + 1)

	for i in range(0, end_range):
		start_index = (i * batch_size)
		end_index = start_index + batch_size
		batch_df = combined_data_frame[start_index:end_index]
		#print batch_df.values
		if len(batch_df > 0):
			df_batch_list.append(batch_df)

	batch_list = []
	for data_frame in df_batch_list:
		temp=[]
		for row in data_frame.iterrows():
			index,data = row
   			temp.append(data.tolist())
		batch_list.append(temp)
			
	return batch_list


def create_hits(batch, num_assignments, title, description, keywords, duration, reward, examples):

	#print batch
	question_form  = create_question(batch, title, examples)

	mtc = MTurkConnection(aws_access_key_id = aws_parameters['access_key'],
                      aws_secret_access_key = aws_parameters['secret_key'],
                      debug = 1, 
                      host = DEV_HOST)

	mtc.create_hit(questions = question_form,
           max_assignments = num_assignments,
           title = title,
           description = description,
           keywords = keywords,
           duration = duration,
           reward = reward)


def create_question(batch, title, examples):

	question_id = []
	question_form = QuestionForm()


	overview = Overview()
	overview.append_field('Title', title)
	
	#examples = ("(abc, aabc) - not match", "(abc, abc) - match")
	overview.append(FormattedContent(utils.gen_html_for_instruction(examples)))

	question_form.append(overview)

	for i in range(0,len(batch)):
		#print 'String 1  = ' + batch[i][0]
		#print 'String 2  = ' + batch[i][1]

		question_content = QuestionContent()
		text = 'String 1 = ' + batch[i][0] + '\n'
		text = text + 'String 2 = ' + batch[i][1] + '\n'
		question_content.append_field('Text', text)

		q_id = 'q' + str(i) + str(i+1)
		question_id.append(q_id)
		selection_answer = SelectionAnswer(min=1, max=1,style='radiobutton',
	                      selections=matches,
	                      type='text',
	                      other=False)
	 
		question = Question(identifier=q_id,
	              content=question_content,
	              answer_spec=AnswerSpecification(selection_answer),
	              is_required=True)

		question_form.append(question)

	return question_form

	

def label_using_crowd(A, l_attr_name, r_attr_name, l_attr, r_attr, aws, examples, reward = 0.1, num_assignments=3, batch_size =10):
	if batch_size <= 0 or batch_size >= len(l_attr.axes[0]):
		print 'Invalid batch size'
		return

	#Set the AWS parameters - access key and secret key
	set_aws_parameters(aws)

	if (check_account_balance(len(l_attr[l_attr_name]), reward) == 1):
		#Create batches containing strings to match
		batches = create_batches(l_attr_name, l_attr, r_attr_name, r_attr, batch_size)

		#Create hits
		for i in xrange(0, len(batches)):
			create_hits(batches[i], num_assignments, title, description, keywords, duration, reward, examples)
		
	else:
		print 'Not enough balance in account to post hits'
		return


def main():
	aws = {}
	aws['access_key'] = 'AKIAJVQPL4WDMPIPJLJQ'
	aws['secret_key'] = 'g/u3rBKxvrxYV5Nvw9Rgm9pKkogRoudyzhpwm99C'
	# set_aws_parameters(aws)

	# mtc = MTurkConnection(aws_access_key_id = aws['access_key'],
 #                      aws_secret_access_key = aws['secret_key'],
 #                      debug = 1, 
 #                      host = DEV_HOST)
	# print mtc.get_account_balance()

	reward = 0.01
	batch_size = 2
	num_assignment = 3

	dict_str1 = {'s1' : ['a', 'b','c','d','e']}
	df_str1 = pd.DataFrame(dict_str1)

	dict_str2 = {'s2' : ['a', 'b','c','d','e']}
	df_str2 = pd.DataFrame(dict_str2)

	new_df = df_str1
	new_df['s2'] = df_str2['s2']

	tuples = ("(abc, aabc) - not match", "(abc, abc) - match")
	#utils.gen_html_for_instruction(tuples)
	label_using_crowd(new_df,'s1', 's2', df_str1, df_str2, aws, tuples, reward, num_assignment, batch_size)

if __name__ == '__main__':
	main()





	
