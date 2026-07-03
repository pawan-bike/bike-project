from flask import Flask, render_template,url_for,request
# flask for web application,render templates for html page(text file ),request import data user form
import joblib
model = joblib.load(r"C:\Users\abc\OneDrive\Desktop\anand collage 45 days traning\project\bike\model\RandomForestRegressor.lb")
# joblib for load ml model
app =Flask(__name__)
# initialization of flask

@app.route('/')
def index():
    return render_template('index.html') 
# web page me index ko show karvane ke liye

@app.route('/contact')
def contact():
    return render_template('contact.html')
# web page me contact page show karvane ke liye

@app.route('/about')
def about():
    return render_template('about.html') 
# url par about  show kar wane ke liye

@app.route('/history')
def history():
    return render_template('history.html')
# url par history show hoga

@app.route('/project',methods=['GET','POST'])
# route mean url path,and get use for server se data lene ke liye and post for server ko data bhej ne ke liye
def predict():
    prediction=None
    if request.method=="POST":
        brand_name=request.form['brand_name']
        owner=int(request.form['owner'])
        age=int(request.form['age'])
        power=int(request.form['power'])
        kms_driven=int(request.form['kms_driven'])
        
        brand_dict = {
            'TVS':1,   'Royal Enfield':2,         'Triumph':3,          'Yamaha':4,
           'Honda':5,            'Hero':6,           'Bajaj':7,          'Suzuki':8,
         'Benelli':9,             'KTM':10,        'Mahindra':11,        'Kawasaki':12,
          'Ducati':13,         'Hyosung':14, 'Harley-Davidson':15,            'Jawa':16,
             'BMW':17,          'Indian':18,         'Rajdoot':19,             'LML':20,
           'Yezdi':21,              'MV':22,           'Ideal':23
              }
        brand_name=brand_dict.get(brand_name)
        
        prediction=model.predict([[brand_name,age,kms_driven,power,owner]])[0]
    
    return render_template("project.html",prediction=prediction)

if __name__=="__main__":
    app.run(debug=True)
 