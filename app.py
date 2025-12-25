from flask import Flask, request, jsonify
from core_analyzer import analyze_vitals

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    vitals = request.json
    result = analyze_vitals(vitals)
    return jsonify(result)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "Vitals API running"})

if __name__ == "__main__":
    app.run(debug=True)
