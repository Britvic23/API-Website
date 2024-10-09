from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Home Route
@app.route('/')
def index():
    return render_template('index.html')

# Route to Fetch Food Data
@app.route('/get_food', methods=['POST'])
def get_food():
    food_name = request.form['food_name']
    api_url = f'https://api.foodfacts.com/v1/food/{food_name}'
    headers = {'Authorization': 'Bearer your_api_key'}
    
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({'error': 'Food not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
