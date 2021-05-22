from flask import Flask
from flask import render_template

app = Flask(__name__)

visit = [0]
like = [0]

print("Hello")
@app.route('/')
def main(name=None):
    visit[0] += 1
    return render_template('main.html',visit=visit, like = like)

@app.route('/info')
def info(name=None):
    return render_template('info.html', name=name)



if __name__ == '__main__':
    app.run()