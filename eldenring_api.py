from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Load the merged data file
with open('eldenring_items.json') as f:
    items = json.load(f)

@app.route('/api/items', methods=['GET'])
def get_items():
    # Query parameters from request
    name = request.args.get('name')
    item_type = request.args.get('type')
    primary_color = request.args.get('primaryColor')
    secondary_color = request.args.get('secondaryColor')

    # Filter items based on query parameters
    filtered_items = items
    if name:
        filtered_items = [item for item in filtered_items if item['name'].lower() == name.lower()]
    if item_type:
        filtered_items = [item for item in filtered_items if item['type'].lower() == item_type.lower()]
    if primary_color:
        filtered_items = [item for item in filtered_items if item['primaryColor'].lower() == primary_color.lower()]
    if secondary_color:
        filtered_items = [item for item in filtered_items if secondary_color.lower() in (color.lower() for color in item['secondaryColors'])]

    return jsonify(filtered_items)

# Route to get a single item by name
@app.route('/api/items/<string:name>', methods=['GET'])
def get_item(name):
    item = next((item for item in items if item['name'].lower() == name.lower()), None)
    if item:
        return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
