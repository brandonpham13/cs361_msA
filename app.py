from flask import Flask, request, jsonify
import pandas as pd
from scipy import stats

app = Flask(__name__)


@app.route("/calculate", methods=["POST"])
def calculate_statistics():
    # Check if a file is provided
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    column_name = request.form.get("column_name")

    if not column_name:
        return jsonify({"error": "No column name provided"}), 400

    try:
        # Read the CSV file
        df = pd.read_csv(file)

        # Check if the column exists in the DataFrame
        if column_name not in df.columns:
            return (
                jsonify({"error": f"Column '{column_name}' not found in the dataset"}),
                400,
            )

        # Calculate mean, median, and mode
        mean = df[column_name].mean()
        median = df[column_name].median()
        mode = stats.mode(df[column_name]).mode[0]  # mode returns a ModeResult object

        return jsonify(
            {"column_name": column_name, "mean": mean, "median": median, "mode": mode}
        )

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
