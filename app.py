from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def run_home():
    print("We received GET from HOME")
    return render_template("mypage.html", )

@app.route('/mypage/me')
def run_me():
    print("We received GET from ME")
    return render_template("me.html" )

@app.route('/mypage/contact', methods=['GET','POST'])
def message():
   if request.method == 'GET':
       print("We received GET from CONTACT")
       return render_template("contact.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")
   

if __name__ == "__main__":
    app.run(debug=True)