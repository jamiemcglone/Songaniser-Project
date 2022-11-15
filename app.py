from flask import Flask, render_template, request

from controllers.songs_controller import songs_blueprint
from controllers.bands_controller import bands_blueprint
from controllers.setlists_controller import setlists_blueprint
from repositories import song_repository

app = Flask(__name__)

app.register_blueprint(songs_blueprint)
app.register_blueprint(bands_blueprint)
app.register_blueprint(setlists_blueprint)

@app.route("/")
def main():
    all_songs = song_repository.select_all()
    return render_template('index.html', all_songs=all_songs)

@app.route("/search", methods=["GET", "POST"])
def search():
    song_to_find = request.form['search']
    all_songs = song_repository.select_all()
    for song in all_songs:
        if song_to_find.lower() == song.title.lower():
            song_to_find_id = song.id
            song_to_return = song_repository.select(song_to_find_id)
            return render_template("songs/view.html", song=song_to_return)
    else:
        return render_template("search_error.html")
        

if __name__ == '__main__':
    app.run()