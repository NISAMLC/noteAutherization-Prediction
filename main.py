from flask import Flask,render_template,request
import pandas as pd
import pickle

app=Flask(__name__)




##creating routes
@app.route('/',methods=['GET'])

@app.route('/result',methods=['POST'])
def home():
    if request.method =='POST':
        variance = request.form['variance']
        skewness = request.form['skewness']
        curtosis = request.form['curtosis']
        entropy = request.form['entropy']
        model = pickle.load(open('classifier.pkl', 'rb'))
        y_pred = [[variance,skewness,curtosis,entropy]]
        predictedVal = model.predict(y_pred)
        outcome = ""
        if predictedVal ==0:
            outcome = 'Not Authenticated'+ '❌'
        else:
            outcome = 'Authenticated' + '✅'

        return render_template('index.html',output=outcome)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)