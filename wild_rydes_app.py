from flask import Flask
app = Flask(_name_)

@app.route('/')
def home():
    return "Company Name: Wild Rydes, Developer Name: Renee Osbourne, Company ID: 100939044"

if _name_ == '_main_':
    app.run(debug=True)