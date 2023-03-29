from flask import Flask, render_template
from controllers.tracks_controller import tracks_blueprint
from controllers.note_controller import notes_blueprint

app = Flask(__name__)

app.register_blueprint(tracks_blueprint)
app.register_blueprint(notes_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)