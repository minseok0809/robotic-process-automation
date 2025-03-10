from flask import Flask, render_template, request, session, app
import pandas as pd 
import requests
import pickle
import matplotlib.pyplot as plt
from pandas.plotting import table
from io import BytesIO, StringIO
import base64
import os

app = Flask(__name__)


@app.before_request
def make_session_permanent():
    app.secret_key = 'secretkey'
    session.permanent = True

# https://www.quora.com/How-do-I-call-function-from-my-Python-file-after-clicking-on-the-button-from-an-HTML-file

@app.route('/', methods=['GET', 'POST'])
def data():

	if request.method == 'POST':
		try:

			task_index = int(request.form['message_taskdata'])
			data_index = int(request.form['message_data'])

			with open('test_cls_dataset.pickle', 'rb') as f:
				test_dataset_dict = pickle.load(f)

			data = pd.DataFrame.from_dict(test_dataset_dict).T
			taskes = data['qa_input'].index
			full_data_list = []
			num = 0 

			for idx in taskes:
				num += 1
				if num == 1 and task_index == 1: 
					full_data_list = data['qa_input'][idx]
					full_label_list = list(set(data['qa_output'][idx]))
				elif num == 2 and task_index == 2: 
					full_data_list = data['qa_input'][idx]
					full_label_list = list(set(data['qa_output'][idx]))
				elif num == 3 and task_index == 3:  
					full_data_list = data['qa_input'][idx]
					full_label_list = list(set(data['qa_output'][idx]))
				elif num == 4 and task_index == 4: 
					full_data_list = data['qa_input'][idx]
					full_label_list = list(set(data['qa_output'][idx]))
				elif num == 5 and task_index == 5: 
					full_data_list = data['qa_input'][idx]
					full_label_list = list(set(data['qa_output'][idx]))

			data_sample = full_data_list[int(data_index)]

			number_task1 = task_index
			number_data1 = data_index
			message_data1 = data_sample
			result_data1 = message_data1.replace(" __ans__", "")
			url = 'http://xxx.xx.x.x:xxxx/generate'
			prediction = requests.get(url, params={"question": message_data1})
			prediction = prediction.text
			prediction = prediction.replace('"', '').replace('}', '').replace('{', '').split(":")[1].strip()
			result_task1 = prediction
			
			prediction_result = []
			for label in full_label_list:
				if prediction == label: prediction_result.append("O")
				elif prediction != label: prediction_result.append("X")

			df = pd.DataFrame()
			table_data = []
			for a, b in zip(full_label_list, prediction_result):
				table_data.append([a, b])

			fig, ax = plt.subplots()
			table = ax.table(cellText=table_data, loc='center')
			table.set_fontsize(14)
			table.scale(1,4)
			ax.axis('off')
			plt.show()

			img = BytesIO()
			plt.savefig(img, format='png', bbox_inches='tight',  transparent="True", pad_inches=0)
			img.seek(0)
			result_label = base64.b64encode(img.read()).decode('utf-8')
			plt.clf() 

		except KeyError:
			pass

		finally:

			try:
				result_data1, number_data1
				session['result_label'] = result_label
				session['result_data1'] = result_data1
				session['number_data1'] = number_data1 
				session['number_task1'] = number_task1 

				result_task1
				session['result_task1'] = result_task1

			except NameError:
				try:
					result_label = session['result_label']                    
					result_data1 = session['result_data1']
					number_data1 = session['number_data1']
					number_task1 = session['number_task1']
					result_task1 = session['result_task1']

				except KeyError:
					result_data1 = number_data1 = ""
					result_task1 =""

		return render_template('index.html', message_data1=data_index,
		result_data1=result_data1, number_data1=number_data1,
        result_task1=result_task1, number_task1=number_task1,
		img_data=result_label)
	
	session.clear()

	return render_template('index.html')


if __name__ == '__main__':
	app.run()