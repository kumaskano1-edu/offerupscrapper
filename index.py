from pyOfferUp import fetch
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Define OfferUp API endpoint
@app.route('/offerup_posts', methods=['GET'])
def get_offerup_posts():
    filtered_array = []
    try:
        # Get query parameters from the request
        search_query = request.args.get('query', default='Samsung 55', type=str)
        min_price = request.args.get('min_price', default=80, type=float)
        max_price = request.args.get('max_price', default=180, type=float)
        # Make a GET request to the OfferUp API
        posts = fetch.get_listings(query=search_query, state="California", city="Los Angeles", limit=30)

        # Filter out listings based on price range
        for post in posts:
            price = float(post.get("price", 0))  # Safely get the price and default to 0 if missing
            if min_price < price <= max_price:
                filtered_array.append(post)

        # Return the filtered data as JSON
        return jsonify(filtered_array)
    except Exception as e:
        # Return an error message if something went wrong
        app.logger.error(f"Error fetching listings: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)