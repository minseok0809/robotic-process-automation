from flask import Flask, render_template, url_for, request
import pandas as pd 
import pickle5 as pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
import random

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def predict():

	df= pd.read_csv("spam.csv", encoding="latin-1")
	df.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)
	# Features and Labels
	df['label'] = df['v1'].map({'ham': 0, 'spam': 1})
	X = df['v2']
	y = df['label']
	
	# Extract Feature With CountVectorizer
	cv = CountVectorizer()
	X = cv.fit_transform(X) # Fit the Data
	from sklearn.model_selection import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
	#Naive Bayes Classifier
	from sklearn.naive_bayes import MultinomialNB

	clf = MultinomialNB()
	clf.fit(X_train,y_train)
	clf.score(X_test,y_test)
	#Alternative Usage of Saved Model
	# joblib.dump(clf, 'NB_spam_model.pkl')
	# NB_spam_model = open('NB_spam_model.pkl','rb')
	# clf = joblib.load(NB_spam_model)

	if request.method == 'POST':
		try:
			message_task1 = request.form['message_task1']
			data = [message_task1]
			vect = cv.transform(data).toarray()
			prediction = clf.predict(vect)
			number_task1 = (prediction - random.randrange(1, 11))[0]
			if prediction == 1:
				result_task1 = "spam"
			elif prediction == 0:
				result_task1 = "Not a Spam" + "(It is a Wham)"
		
		except KeyError:
			pass

		try:
			message_task2 = request.form['message_task2']
			data = [message_task2]
			vect = cv.transform(data).toarray()
			prediction = clf.predict(vect)
			number_task2 = (prediction - random.randrange(1, 11))[0]
			number_task2_01=number_task2+1
			number_task2_02=number_task2+2
			if prediction == 1:
				result_task2 = "spam"
			elif prediction == 0:
				result_task2 = "Not a Spam" +"(It is a Bam)"
				result_task2_01="Not a Spam"+"(It is a Ham)"
				result_task2_02="Not a Spam"+"(It is a Zam)"

		except KeyError:
			pass
		
		try:	
			message_task3 = request.form['message_task3']
			data = [message_task3]
			vect = cv.transform(data).toarray()
			prediction = clf.predict(vect)
			number_task3 = (prediction - random.randrange(1, 11))[0]
			number_task3_01=number_task3+4
			number_task3_02=number_task3+5

			if prediction == 1:
				result_task3 = "spam"
			elif prediction == 0:
				result_task3 = "Not a Spam" +"(It is a Sam)"
				result_task3_01="Not a Spam" +"(It is a Pam)"
				result_task3_02="Not a Spam" +"(It is a Fam)"
		
		except KeyError:
			pass

		finally:

			try:
				result_task1, number_task1

			except NameError:
				result_task1 = ""
				number_task1 = ""
				try:
					with open("variables_task1.txt", "r") as f:
						lines = f.readlines()
						result_task1 = lines[0].strip(); number_task1 = lines[1].strip()
				except IndexError: 
					pass

			try:
				result_task2, number_task2, \
				result_task2_01, number_task2_01, \
				result_task2_02, number_task2_02

			except NameError:
				result_task2 = ""; number_task2= ""
				result_task2_01= ""; number_task2_01= ""
				result_task2_02= ""; number_task2_02= ""
				try:
					with open("variables_task2.txt", "r") as f:
						lines = f.readlines()
						result_task2 = lines[0].strip(); number_task2 = lines[1].strip()
						result_task2_01 = lines[2].strip(); number_task2_01 = lines[3].strip()
						result_task2_02 = lines[4].strip(); number_task2_02 = lines[5].strip()
				except IndexError: 
					pass

			try:
				result_task3, number_task3, \
				result_task3_01, number_task3_01, \
				result_task3_02, number_task3_02

			except NameError:
				result_task3 = ""; number_task3= "" 
				result_task3_01= ""; number_task3_01= ""
				result_task3_02= ""; number_task3_02= ""
				try:
					with open("variables_task3.txt", "r") as f:
						lines = f.readlines()
						result_task3 = lines[0].strip(); number_task3 = lines[1].strip()
						result_task3_01 = lines[2].strip(); number_task3_01 = lines[3].strip()
						result_task3_02 = lines[4].strip(); number_task3_02 = lines[5].strip()
				except IndexError: 
					pass

		task1_list = [result_task1, number_task1]
		task2_list = [result_task2, number_task2, result_task2_01, number_task2_01,
		  result_task2_02, number_task2_02]
		task3_list = [result_task3, number_task3, result_task3_01, number_task3_01,
		  result_task3_02, number_task3_02]

		with open("variables_task1.txt", "w") as f:
			f.write("\n".join(map(str, task1_list)))

		with open("variables_task2.txt", "w") as f:
			f.write("\n".join(map(str, task2_list)))

		with open("variables_task3.txt", "w") as f:
			f.write("\n".join(map(str, task3_list)))

		return render_template('index.html',
		result_task1=result_task1, number_task1=number_task1,
	result_task2=result_task2, number_task2=number_task2,
	result_task2_01=result_task2_01, number_task2_01=number_task2_01,
	result_task2_02=result_task2_02, number_task2_02=number_task2_02,
	result_task3=result_task3, number_task3=number_task3,
	result_task3_01=result_task3_01, number_task3_01=number_task3_01,
	result_task3_02=result_task3_02, number_task3_02=number_task3_02)

	with open("variables_task1.txt", "w") as f:
		f.write("")

	with open("variables_task2.txt", "w") as f:
		f.write("")

	with open("variables_task3.txt", "w") as f:
		f.write("")
		
	return render_template('index.html')



if __name__ == '__main__':
	app.run()