from flask import Flask,render_template,request,session
import joblib

app = Flask(__name__)

pipeline = joblib.load('./AxisBankModel.pkl')

global x_train, y_train, x_test, y_test
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/predict1',methods =['POST','GET'])
def pred():
    s = []
    if request.method== 'POST':
        date= request.form['date']
        Previous_CP = request.form['pcp']
        OpenPrice = request.form['op']
        HighPrice = request.form['hp']
        LowPrice = request.form['lp']
        LastPrice = request.form['lap']
        ClosePrice = request.form['cp']
        s.extend([date,Previous_CP,OpenPrice,HighPrice,LowPrice,LastPrice,ClosePrice])
        pred = pipeline.predict([s])
        return render_template('predict.html', msg="success", op=pred)

if __name__ == '__main__':
    app.secret_key = "hai"
    app.run(port=8080, debug=True)