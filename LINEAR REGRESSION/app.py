from flask import Flask,render_template,request
import input
Output=5

app=Flask(__name__)

@app.route("/", methods=["GET","POST"])

def result():
    if request.method == 'POST':
        global Output
        Age=int(request.form['age'])
        Gender=int(request.form['gender'])
        Edu=int(request.form['edu'])
        Status=int(request.form['status'])
        Usage=int(request.form['use'])
        Fit=int(request.form['fit'])
        Income=int(request.form['income'])
        Mile=int(request.form['mile'])
        Output=int(input.predict(Age,Gender,Edu,Status,Usage,Fit,Income,Mile))
    
        
    return render_template("index.html",res=Output)









if __name__=="__main__":
    app.run(debug=True)