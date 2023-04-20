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
			message_out_of_order = request.form['message_out_of_order']
			data = [message_out_of_order]
			vect = cv.transform(data).toarray()
			prediction = clf.predict(vect)
			number_out_of_order = (prediction - random.randrange(1, 11))[0]
			if prediction == 1:
				result_out_of_order = "spam"
			elif prediction == 0:
				result_out_of_order = "Not a Spam" + "(It is a Wham)"
		
		except KeyError:
			pass

		try:
			message_caution = request.form['message_caution']
			data = [message_caution]
			vect = cv.transform(data).toarray()
			prediction = clf.predict(vect)
			number_caution_01 = (prediction - random.randrange(1, 11))[0]
			number_caution_02 = number_caution_01+1
			number_caution_03 = number_caution_01+2
			if prediction == 1:
				result_caution_01 = "spam"
				result_caution_02 = "spam"
				result_caution_03 = "spam"
			elif prediction == 0:
				result_caution_01 = "Not a Spam" +"(It is a Bam)"
				result_caution_02 = "Not a Spam"+"(It is a Ham)"
				result_caution_03 = "Not a Spam"+"(It is a Zam)"

		except KeyError:
			pass
		
		try:	
			message_take_measure = request.form['message_take_measure']
			data = [message_take_measure]
			vect = cv.transform(data).toarray()
			prediction = clf.predict(vect)
			number_take_measure_01 = (prediction - random.randrange(1, 11))[0]
			number_take_measure_02 = number_take_measure_01+4
			number_take_measure_03 = number_take_measure_01+5

			if prediction == 1:
				result_take_measure_01 = "spam"
				result_take_measure_02 = "spam"
				result_take_measure_03 = "spam"
			elif prediction == 0:
				result_take_measure_01 = "Not a Spam" +"(It is a Sam)"
				result_take_measure_02 = "Not a Spam" +"(It is a Pam)"
				result_take_measure_03 = "Not a Spam" +"(It is a Fam)"
		
		except KeyError:
			pass

		finally:
			try:
				result_out_of_order, number_out_of_order
				session['result_out_of_order'] = result_out_of_order
				session['number_out_of_order'] = int(number_out_of_order)

			except NameError:
				try:
					result_out_of_order = session['result_out_of_order']
					number_out_of_order = session['number_out_of_order']
				except KeyError:
					result_out_of_order = number_out_of_order = ""

			try:
				result_caution_01, number_caution_01,
				result_caution_02, number_caution_02,
				result_caution_03, number_caution_03
				session['result_caution_01'] = result_caution_01
				session['number_caution_01'] = int(number_caution_01)
				session['result_caution_02'] = result_caution_02
				session['number_caution_02'] = int(number_caution_02)
				session['result_caution_03'] = result_caution_03
				session['number_caution_03'] = int(number_caution_03)

			except NameError:
				try:
					result_caution_01 = session['result_caution_01']
					number_caution_01 = session['number_caution_01']
					result_caution_02 = session['result_caution_02']
					number_caution_02 = session['number_caution_02']
					result_caution_03 = session['result_caution_03']
					number_caution_03 = session['number_caution_03']				
				except KeyError:
					result_caution_01 = number_caution_01 = \
					result_caution_02 = number_caution_02 =  \
					result_caution_03 = number_caution_03 = ""

			try:
				result_take_measure_01, number_take_measure_01,
				result_take_measure_02, number_take_measure_02,
				result_take_measure_03, number_take_measure_03
				session['result_take_measure_01'] = result_take_measure_01
				session['number_take_measure_01'] = int(number_take_measure_01)
				session['result_take_measure_02'] = result_take_measure_02
				session['number_take_measure_02'] = int(number_take_measure_02)
				session['result_take_measure_03'] = result_take_measure_03
				session['number_take_measure_03'] = int(number_take_measure_03)

			except NameError:
				try:
					result_take_measure_01 = session['result_take_measure_01']
					number_take_measure_01 = session['number_take_measure_01']
					result_take_measure_02 = session['result_take_measure_02']
					number_take_measure_02 = session['number_take_measure_02']
					result_take_measure_03 = session['result_take_measure_03']
					number_take_measure_03 = session['number_take_measure_03']				
				except KeyError:
					result_take_measure_01 = number_take_measure_01 = \
					result_take_measure_02 = number_take_measure_02 = \
					result_take_measure_03 = number_take_measure_03 = ""

		return render_template('index.html', result_out_of_order=result_out_of_order, number_out_of_order=number_out_of_order,
			 result_caution_01=result_caution_01, number_caution_01=number_caution_01,
			 result_caution_02=result_caution_02, number_caution_02=number_caution_02,
			 result_caution_03=result_caution_03, number_caution_03=number_caution_03,
			 result_take_measure_01=result_take_measure_01, number_take_measure_01=number_take_measure_01,
			 result_take_measure_02=result_take_measure_02, number_take_measure_02=number_take_measure_02,
			 result_take_measure_03=result_take_measure_03, number_take_measure_03=number_take_measure_03)
	
	session.clear()

	return render_template('index.html')


if __name__ == '__main__':
	app.run()