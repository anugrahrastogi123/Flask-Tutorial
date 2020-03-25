from flask import Flask, render_template, redirect, request

app = Flask(__name__)

friends = ["Anugrah", "Yajur", "Ritesh"]

num = 5

@app.route('/')
def hello():
    return render_template("index.html", my_friends = friends, number = num) # here my_friends is the variable for the html file
                                                               # and friends is the variable in python

@app.route('/about')
def about():
    return "<h1>About Page</h1>"

@app.route('/home')
def home():
    return redirect('/') # redirects to the root page because home page is not available

@app.route('/submit', methods = ['POST']) # method is by default GET
def submit_data():
    if request.method == 'POST':
        # print(request.form) # return an immutable multi dictionary
        name = request.form['username']

    return "<h1>Hello {}</h1>".format(name)

# adding two numbers
@app.route('/add', methods = ['POST'])
def add():
    if request.method == 'POST':
        no1 = int(request.form['no1'])
        no2 = int(request.form['no2'])

    return str(no1+no2)

@app.route('/file', methods = ['POST'])
def save_file():
    if request.method == 'POST':
        f = request.files['userfile']
        # print(f) # <FileStorage: 'image.jpeg' ('image/jpeg')>
        f.save(f.filename) # the uploaded file is saved under the Flask Tutorial folder

    return "File has been saved"

if __name__ == "__main__":
    app.run(debug = True)
