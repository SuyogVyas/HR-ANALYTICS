from flask import Flask,render_template,request
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def ValuePredictor(to_predict_list): 
	to_predict = np.array(to_predict_list).reshape(1,12) 
	loaded_model = pickle.load(open("model.pkl", "rb")) 
	result = loaded_model.predict(to_predict) 
	return result[0] 

@app.route('/result', methods = ["POST"]) 
def result(): 
	if request.method == "POST": 
		to_predict_list = request.form.to_dict() 
		to_predict_list = list(to_predict_list.values()) 
		to_predict_list = list(map(int, to_predict_list)) 
		result = ValuePredictor(to_predict_list)		 
		if result == 1: 
			prediction ="Promoted"
		else: 
			prediction ="Not Promoted"			
		return render_template("result.html", prediction = prediction) 


if __name__ == '__main__':
    app.run()