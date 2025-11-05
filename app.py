from flask import Flask, render_template, send_from_directory, jsonify
import json
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

# === Главная страница ===
@app.route('/')
def index():
    return render_template('student_index.html')

# === Админка ===
@app.route('/admin')
def admin():
    return render_template('admin.html')

# === API для данных ===
@app.route('/api/content')
def get_content():
    with open('content.json', 'r', encoding='utf-8') as f:
        return jsonify(json.load(f))

@app.route('/api/news')
def get_news():
    with open('news.json', 'r', encoding='utf-8') as f:
        return jsonify(json.load(f))

@app.route('/api/tests')
def get_tests():
    with open('tests.json', 'r', encoding='utf-8') as f:
        return jsonify(json.load(f))

# === Статика ===
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

# === Точка входа ===
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
