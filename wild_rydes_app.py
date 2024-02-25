from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    company_name = "Wild Rydes"
    developer_name = "Renee Osbourne"
    company_id = "100939044"

    return f"Company Name: {company_name}, Developer Name: {developer_name}, Company ID: {company_id}"

if __name__ == '__main__':
    app.run(debug=True, port=8080)
