from flask import Flask, request, jsonify
import pandas as pd
import json

app = Flask(__name__)

@app.route('/processdata', methods=['POST'])
def calculate_stats():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']
    column_name = request.form.get('column_name')

    if not column_name:
        return jsonify({"error": "No column name provided"}), 400

    try:
        df = pd.read_csv(file)

        if column_name not in df.columns:
            return jsonify({"error": f"Column '{column_name}' not found in the dataset"}), 400

        if not pd.api.types.is_numeric_dtype(df[column_name]):
            return jsonify({"error": f"Column '{column_name}' must contain numeric values"}), 400

        min_value = df[column_name].min()
        max_value = df[column_name].max()
        mean_value = df[column_name].mean()

        response_data = {
            "column name": column_name,
            "min": min_value,
            "max": max_value,
            "mean": mean_value
        }

        return app.response_class(
            response=json.dumps(response_data, indent=2),
            status=200,
            mimetype='application/json'
        )

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)