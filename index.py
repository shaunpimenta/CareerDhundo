from flask import Flask,request,jsonify
import ast
import os
app=Flask(__name__)
import pandas as pd

data=pd.read_csv("data.csv")
ques=pd.read_csv("questions.csv")
data=data.fillna("NA")
data.drop(['University','Rating','Country'],axis=1,inplace=True)

# data
def filterdata(regiont,location):
    loc=data[data[regiont]==location]
    return loc['College Name'].reset_index().drop(['index'],axis=1)
def coldetails(name):
    details=data[data['College Name']==name]
    return details
@app.route('/', methods=['GET'])
def handle_call():
    print("Connected")
    return "Successfully Connected"
@app.route('/ques',methods=['POST'])
def ques():
    if request.method=="PSOT":
        print("Connected")
        return ques
    return "Questions"
        
    
#the get method. when we call this, it just return the text "Hey!! I'm the fact you got!!!"
@app.route('/getfact', methods=['POST'])
def get_fact():
    if request.method=="POST":
        a=request.get_data()
        vals = a.decode()
        print(vals)
        res = ast.literal_eval(vals)
        print(type(res))
        print("Done")
        print(list((filterdata(res[0],res[1])["College Name"])))
        # returnprint("Done")
        return jsonify(list(filterdata(res[0],res[1])["College Name"]))
    return "Hello"

#the post method. when we call this with a string containing a name, it will return the name with the text "I got your name"
@app.route('/getname', methods=['POST'])
def extract_name():
    if request.method=="POST":
        a=request.get_data()
        res = a.decode()
        # print(vals)
        # res = ast.literal_eval(vals)
        print(type(res))
        print("Done")
        print(coldetails(res).values.tolist()[0])
        # returnprint("Done")
        return jsonify(coldetails(res).values.tolist()[0])

    return "Successful"

#this commands the script to run in the given port
if __name__ == '__main__':
    default_port=5000
    port = int(os.environ.get('PORT',default_port))
    app.run(host="0.0.0.0", debug=True)
