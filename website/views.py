from flask import Flask, render_template, Blueprint, request, redirect, url_for
import numpy as np
import pickle

views = Blueprint('views',__name__)


@views.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		# load the pickle model
		model = pickle.load(open('website/iris_rfc.pkl', 'rb'))

		# convert all the input from the input boxes to floats
		float_features = [float(x) for x in request.form.values()]

		features = [np.array(float_features)]
		prediction = model.predict(features)

		results = f'The flower is predicted to be of {prediction} species.'
		return render_template('index.html',prediction_results=results)

	return render_template('index.html')
