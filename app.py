from flask import Flask,render_template,request
app=Flask(__name__)
youtube=[]
@app.route("/hello",methods=["POST","GET"])
def hello():
    if request.method=="POST":
        user=request.json
        youtube.append(user)
    return render_template("sample.html",u=youtube)

if __name__=="__main__":
    app.run(debug=True)