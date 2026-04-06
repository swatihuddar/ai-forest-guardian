from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/alert', methods=['POST'])
def alert():
    data = request.json

    sound = data['sound']
    zone = data['zone']
    confidence = data['confidence']

    print("🚨 ALERT RECEIVED")
    print(f"Sound: {sound}")
    print(f"Zone: {zone}")
    print(f"Confidence: {confidence}%")

    with open("alerts.txt", "a") as f:
        f.write(f"{sound} detected in Zone {zone} with {confidence}%\n")

    return jsonify({"status": "Alert logged successfully"})

if __name__ == "__main__":
    app.run(debug=True)