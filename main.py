from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/article/<int:article_id>')
def article(article_id):
    return render_template(f'article{article_id}.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
