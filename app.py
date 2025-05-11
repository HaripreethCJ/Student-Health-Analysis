import os
from flask import Flask, render_template_string
import pandas as pd

app = Flask(__name__)

# Use the full path to the CSV file
file_path = os.path.join("C:", "Users", "DELL", "Documents", "project", "student_mental_health.csv")
df = pd.read_csv("student_mental_health.csv")

# Convert DataFrame to HTML
table_html = df.to_html(classes='table table-striped', index=False)

# Simple HTML template
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>CSV Table Viewer</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body class="p-5">
    <h1 class="mb-4">CSV Data</h1>
    {{ table | safe }}
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_template, table=table_html)

if __name__ == "__main__":
    app.run(debug=True)
