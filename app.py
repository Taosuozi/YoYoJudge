from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index_save_2():
    return render_template('index-TE.html')

@app.route('/index.html')
def index():
    return render_template('index-FE.html')

if __name__ == "__main__":
    app.run(debug=True)
