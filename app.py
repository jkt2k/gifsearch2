from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    # TODO: Extract the query term from url using request.args.get()
    return render_template('index.html')
    # TODO: Make 'params' dictionary containing:
    # a) the query term, 'q'
    # b) your API key, 'key'
    # c) how many GIFs to return, 'limit'
    params = {
        "q": "query",
        "apikey": "7KOU0A3XQ2BG",
        "limit" : 10
    }
    response = request.get(
        'http://api.tenor.com/v1/search',
        params=params
    )
    # TODO: Make an API call to Tenor using the 'requests' library. For 
    # reference on how to use Tenor, see: 
    # https://tenor.com/gifapi/documentation
    r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (params['q'], params['apikey'], limit))
    
    # TODO: Use the '.json()' function to get the JSON of the returned response
    # object
    if r.status_code == 200:
        gifs = json.loads(r.content)
        
    else:
        gifs = None

    # TODO: Using dictionary notation, get the 'results' field of the JSON,
    # which contains the GIFs as a list
    

    # TODO: Render the 'index.html' template, passing the list of gifs as a
    # named parameter called 'gifs'

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
