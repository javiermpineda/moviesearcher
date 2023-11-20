from flask import Flask, render_template, request
import requests


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    services = request.form['service']
    country = request.form['country']
    keyword = request.form['title']

    url = "https://streaming-availability.p.rapidapi.com/search/filters"
    querystring = {
        "services":services,
        "country": country,
        "keyword":keyword,
        "output_language": "en",
        "order_by": "original_title",
        "genres_relation": "and",
        "show_type": "all"
    }

    print("Querystring:", querystring)

    headers = {
        "X-RapidAPI-Key": "2226a5ffcbmsh41e5138dc667816p1a05f8jsn125f54b44b23",
        "X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()

    # Pass the response data to the template
    return render_template('results.html', data=data,services=services)


if __name__ == '__main__':
    app.run(debug=True)
