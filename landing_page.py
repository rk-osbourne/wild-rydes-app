from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Company Name: Wild Rydes, Developer Name: Renee Osbourne, Company ID: Your 100939044"

if __name__ == '__main__':
    app.run(debug=True)
