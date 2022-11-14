from flask import Flask, render_template

from controllers.songs_controller import songs_blueprint
from controllers.bands_controller import bands_blueprint
from controllers.setlists_controller import setlists_blueprint

app = Flask(__name__)

app.register_blueprint(songs_blueprint)
app.register_blueprint(bands_blueprint)
app.register_blueprint(setlists_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()