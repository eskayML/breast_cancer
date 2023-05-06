from flask import Flask, request, render_template
import pickle
from sklearn.ensemble import AdaBoostClassifier

app = Flask(__name__)


MODEL_PATH = "breast_cancer_model.pkl"
COLUMNS = [
    "radius_mean",
    "perimeter_mean",
    "area_mean",
    "concavity_mean",
    "concave points_mean",
    "radius_worst",
    "perimeter_worst",
    "area_worst",
    "concavity_worst",
    "concave points_worst",
]


with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        values = [request.form.get(i) for i in COLUMNS]
        prediction = model.predict_proba([values])[0]

        if prediction[1] > 0.5000:
            output_text = (
                f"The model predicted the output to be 'MALIGNANT' ({round(prediction[1] * 100, 2)}%) "
            )
        else:
            output_text = (
                f"The model predicted the output to be 'BENIGN' ({round(prediction[0] * 100, 2)}%)"
            )

        return render_template(
            "predict.html", COLUMNS=COLUMNS, output_text=output_text
        )

    return render_template("predict.html", COLUMNS=COLUMNS)


if __name__ == "__main__":
    app.run(debug=True)
