from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/deneme')
def deneme():

    content = "hello"
    return render_template('deneme.html', content=content)


@app.route('/')
def mapp():
    f = open('C:/Users/oğuzhan/PycharmProjects/WebCrawler/json_data.json')
    gemiler = json.load(f)
    f = open('C:/Users/oğuzhan/PycharmProjects/WebCrawler/json_data2.json')
    limanlar = json.load(f)

    return render_template('map.html', gemiler=gemiler, limanlar=limanlar)


if __name__ == "__main__":
    app.run(debug=True)
