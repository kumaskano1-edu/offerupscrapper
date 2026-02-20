from pyOfferUp import fetch
from flask import Flask, jsonify, request

app = Flask(__name__)

# Define OfferUp API endpoint
@app.route('/offerup_posts', methods=['GET'])
def get_offerup_posts():
    combined_results = {}
    try:
        # Multiple search queries
        search_queries = ["samsung 65", "lg 65", "samsung 75 tv", "lg 75 tv", "oled lg", "qled tv",]

        min_price = request.args.get('min_price', default=100, type=float)
        max_price = request.args.get('max_price', default=180, type=float)

        for query in search_queries:
            posts = fetch.get_listings(query=query, state="California", city="Los Angeles", limit=50)
            
            for post in posts:
                # Safely get price and default to 0
                price = float(post.get("price", 0))
                listing_id = post.get("listingId")  # Use listingId for uniqueness

                if min_price < price <= max_price and listing_id not in combined_results:
                    combined_results[listing_id] = post

        # Convert dict values to list
        filtered_array = list(combined_results.values())

        print("Combined results:")
        print(filtered_array)
        return jsonify(filtered_array)

    except Exception as e:
        app.logger.error(f"Error fetching listings: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
