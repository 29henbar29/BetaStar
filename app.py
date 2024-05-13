from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/proxy', methods=['GET'])
def proxy():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'Missing URL parameter'}), 400

    try:
        response = requests.get(url)
        return response.content, response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # You can change the port if needed
