from flask import Flask, request, jsonify, Response
import joblib, io
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

app = Flask(__name__)
MODEL_PATH = os.path.join("model", "model.pkl")

# load model once before first request
@app.before_first_request
def load_model():
    global model
    model = joblib.load(MODEL_PATH)

@app.route("/predict", methods=["POST"])
def predict():
    """
    Example: POST /predict
    Body: {"feature1": 0.5, "feature2": 4.2}
    """
    try:
        data = request.get_json(force=True)
        f1 = float(data["feature1"])
        f2 = float(data["feature2"])
        df = pd.DataFrame([{"feature1": f1, "feature2": f2, "f1_x_f2": f1 * f2}])
        pred = model.predict(df)[0]
        return jsonify({"prediction": float(pred)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/plot", methods=["GET"])
def plot():
    # Simple sine curve for demo
    x = np.linspace(0, 2*np.pi, 200)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("Health Check Plot")
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    return Response(buf.getvalue(), mimetype="image/png")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

