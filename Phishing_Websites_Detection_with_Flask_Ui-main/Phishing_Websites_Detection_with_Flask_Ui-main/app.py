from flask import Flask, render_template, request
from database import *
from redirecting_url import *
import FeatureExtraction
import pickle

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/getURL', methods=['GET', 'POST'])
def getURL():
    predicted_value = ""
    if request.method == 'POST':
        url = request.form['url']
        if url_in_database(url=url):
            predicted_value = 1
        else:
            data = FeatureExtraction.getAttributess(url)
            RFmodel = pickle.load(open('RandomForestModel.sav', 'rb'))
            predicted_value = RFmodel.predict(data)
        if predicted_value == 0:
            value = "Not a Phishy website"
            open_url(url)
            return render_template("home.html", error=value)
        else:
            value = "Phishing Website"
            add_url(url)
            return render_template("home.html", error=value)


if __name__ == "__main__":
    app.run(debug=True)
