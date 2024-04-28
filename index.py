from pyOfferUp import fetch
from flask import Flask, jsonify
import json

# app.py

from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Define OfferUp API endpoint
@app.route('/offerup_posts', methods=['GET'])
def get_offerup_posts():
    try:
        # Make a GET request to the OfferUp API
        posts = fetch.get_listings(query="samsung 55", state="California", city="Los Angeles", limit=100)
        json_posts = json.dumps(posts)
        return json_posts
        # Return the data as JSON
    except Exception as e:
        # Return an error message if something went wrong
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)