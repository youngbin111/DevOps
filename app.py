from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
#N}6Pao4do%zfD8+3~Ytp2?-T'&Fo6|wD