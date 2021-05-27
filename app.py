from flask import Flask,render_template,request,redirect
import sqlite3

app = Flask(__name__)



@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/help')
def help_page():
    return render_template('help.html')

@app.route('/faqs')
def faqs_page():
    return render_template('faqs.html')

@app.route('/contactus',methods = ['POST','GET'])
def contactus_page():
    if request.method == 'POST':
        return redirect(request.referrer)
    return render_template('contactus.html')



@app.route('/result_page',methods = ['POST','GET'])
def result_page():
    rank = request.form["rank"]
    gender = request.form["gender"]
    caste = request.form["caste"]
    if gender == "Male":
        gc = caste + "_" + "BOYS"
    if gender == "Female":
        gc = caste + "_" + "GIRLS"

    branch = request.form["branch"]

    return render_template("result.html",data=get_eamcet(rank,gc,branch))

def get_eamcet(rank,gc,branch):
    try:
        connection = sqlite3.connect("data.sqlite")
        cursor = connection.cursor()
        query = "SELECT inst_code,inst_name,REGION,DIST,PLACE,COED,AFFLIATION,branch_code FROM LAST_RANK_DETAILS WHERE CAST({} AS REAL) >= '{}' AND branch_code='{}' ".format(gc, rank, branch)
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    except:
        data = "<h1>Oops ! Something went wrong .</h1> </br>"
        return data

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=5000)