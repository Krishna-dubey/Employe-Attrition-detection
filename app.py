from flask import Flask, render_template,url_for,request
import pickle

app=Flask(__name__)

filename = 'RandomForest_Attrition_model.sav'
model = pickle.load(open(filename, 'rb'))


@app.route('/')
def landing():
    return render_template("index.html")

@app.route('/predict_page',methods=['GET','POST'])
def predict_page():
    if request.method == "POST":
        data=request.form
        k=["TotalWorkingYears","YearsAtCompany", "YearsInCurrentRole", "YearsWithCurrManager", "Age", "JobLevel","MaritalStatus","OverTime"]
        val=[int(data[value]) for value in k]
        ans=model.predict([val])
        if ans[0]==0:
            return render_template('/result.html',prediction=0)
        else:
            return render_template('/result.html',prediction=1)
    


app.run(debug=True)