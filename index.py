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
    filteredArray = []
    try:
        # Make a GET request to the OfferUp API
        posts = fetch.get_listings(query="Toyota Prius", state="California", city="Los Angeles", limit=30)
        # Define a lambda function to filter out listings with a price over $300
        # for post in posts:
        #     price = int(post["price"])
        #     if price <= 200:
        #         filteredArray.append(post)
        # filtered_posts = json.dumps(filteredArray)
        return posts
        # Return the data as JSON
    except Exception as e:
        # Return an error message if something went wrong
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)