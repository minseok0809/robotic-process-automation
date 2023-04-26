from flask import Flask, render_template, request, session, app
import pandas as pd 
import pickle5 as pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
import random

app = Flask(__name__)

@app.before_request
def make_session_permanent():
    app.secret_key = 'secretkey'
    session.permanent = True
    
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
			number_task1 = prediction[0]
			if prediction == 1:
				result_task1 = "spam"
			elif prediction == 0:
				result_task1 = "Not a Spam" + "(It is a Wham)"
		
		except KeyError:
			pass

		try:
			message_task2 = request.form['input_task2']
		except KeyError:
			pass

		try:
			message_task2 = request.form['message_task2']
			data = [message_task2]
			vect = cv.transform(data).toarray()
			prediction = clf.predict(vect)
			number_task2_01 = prediction[0]
			number_task2_02 = prediction[0]
			number_task2_03 = prediction[0]
			if prediction == 1:
				result_task2_01 = "spam"
				result_task2_02 = "spam"
				result_task2_03 = "spam"
			elif prediction == 0:
				result_task2_01 = "Not a Spam" +"(It is a Bam)"
				result_task2_02 = "Not a Spam"+"(It is a Ham)"
				result_task2_03 = "Not a Spam"+"(It is a Zam)"

		except KeyError:
			pass

		
		try:
			message_task3 = request.form['input_task3']
		except KeyError:
			pass
		
		try:	
			message_task3 = request.form['message_task3']
			data = [message_task3]
			vect = cv.transform(data).toarray()
			prediction = clf.predict(vect)
			number_task3_01 = prediction[0]
			number_task3_02 = prediction[0]
			number_task3_03 = prediction[0]

			if prediction == 1:
				result_task3_01 = "spam"
				result_task3_02 = "spam"
				result_task3_03 = "spam"
			elif prediction == 0:
				result_task3_01 = "Not a Spam" +"(It is a Sam)"
				result_task3_02 = "Not a Spam" +"(It is a Pam)"
				result_task3_03 = "Not a Spam" +"(It is a Fam)"
		
		except KeyError:
			pass

		finally:

			try:
				result_task1, number_task1
				session['result_task1'] = result_task1
				session['number_task1'] = int(number_task1)

			except NameError:
				try:
					result_task1 = session['result_task1']
					number_task1 = session['number_task1']
				except KeyError:
					result_task1 = number_task1 = ""

			try:
				result_task2_01, number_task2_01,
				result_task2_02, number_task2_02,
				result_task2_03, number_task2_03
				session['result_task2_01'] = result_task2_01
				session['number_task2_01'] = int(number_task2_01)
				session['result_task2_02'] = result_task2_02
				session['number_task2_02'] = int(number_task2_02)
				session['result_task2_03'] = result_task2_03
				session['number_task2_03'] = int(number_task2_03)

			except NameError:
				try:
					result_task2_01 = session['result_task2_01']
					number_task2_01 = session['number_task2_01']
					result_task2_02 = session['result_task2_02']
					number_task2_02 = session['number_task2_02']
					result_task2_03 = session['result_task2_03']
					number_task2_03 = session['number_task2_03']				
				except KeyError:
					result_task2_01 = number_task2_01 = \
					result_task2_02 = number_task2_02 =  \
					result_task2_03 = number_task2_03 = ""

			try:
				result_task3_01, number_task3_01,
				result_task3_02, number_task3_02,
				result_task3_03, number_task3_03
				session['result_task3_01'] = result_task3_01
				session['number_task3_01'] = int(number_task3_01)
				session['result_task3_02'] = result_task3_02
				session['number_task3_02'] = int(number_task3_02)
				session['result_task3_03'] = result_task3_03
				session['number_task3_03'] = int(number_task3_03)

			except NameError:
				try:
					result_task3_01 = session['result_task3_01']
					number_task3_01 = session['number_task3_01']
					result_task3_02 = session['result_task3_02']
					number_task3_02 = session['number_task3_02']
					result_task3_03 = session['result_task3_03']
					number_task3_03 = session['number_task3_03']				
				except KeyError:
					result_task3_01 = number_task3_01 = \
					result_task3_02 = number_task3_02 = \
					result_task3_03 = number_task3_03 = ""
					
			try:
				message_task1
				session['message_task1'] = message_task1
			except:
				try:
					message_task1 = session['message_task1'] 
				except:
					message_task1 = ""

			try:
				message_task2
				session['message_task2'] = message_task2
			except:
				try:
					message_task2 = session['message_task2'] 
				except:
					message_task2 = ""

			try:
				message_task3
				session['message_task3'] = message_task3
			except:
				try:
					message_task3 = session['message_task3'] 
				except:
					message_task3 = ""

		return render_template('index.html', message_task1=message_task1,
		message_task2=message_task2, message_task3=message_task3,
		result_task1=result_task1, number_task1=number_task1,
		result_task2_01=result_task2_01, number_task2_01=number_task2_01,
		result_task2_02=result_task2_02, number_task2_02=number_task2_02,
		result_task2_03=result_task2_03, number_task2_03=number_task2_03,
		result_task3_01=result_task3_01, number_task3_01=number_task3_01,
		result_task3_02=result_task3_02, number_task3_02=number_task3_02,
		result_task3_03=result_task3_03, number_task3_03=number_task3_03)
	
	session.clear()

	return render_template('index.html')


if __name__ == '__main__':
	app.run()