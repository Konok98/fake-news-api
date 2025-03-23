from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get('text', '')

    # Replace this with your actual fake news detection model
    prediction = "Fake" if "fake" in text.lower() else "Real"

    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
