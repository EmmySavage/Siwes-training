from flask import Flask, request, render_template

app = Flask(__name__)
@app.route('/login', methods=["GET","POST"])
def login():
    if request.method =="GET":
        return render_template("login.html")
    
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        return f"welcome,{username}"

if __name__ == "__main__":
    app.run(debug=True)
