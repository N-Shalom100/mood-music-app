from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# mood → Spotify playlist URL mapping
mood_to_playlist = {
    "happy": "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC",       # Happy Hits
    "sad": "https://open.spotify.com/playlist/37i9dQZF1DWVrtsSlLKzro",         # Life Sucks
    "angry": "https://open.spotify.com/playlist/37i9dQZF1DX1tyCD9QhIWF",       # Rock Hard
    "relaxed": "https://open.spotify.com/playlist/37i9dQZF1DX3PIPIT6lEg5",     # Chill Vibes
    "romantic": "https://open.spotify.com/playlist/37i9dQZF1DX50QitC6Oqtn",    # Love Pop
    "energetic": "https://open.spotify.com/playlist/37i9dQZF1DX70RN3TfWWJh",   # Power Workout
    "nostalgic": "https://open.spotify.com/playlist/37i9dQZF1DX4UtSsGT1Sbe",   # All Out 2000s
    "motivational": "https://open.spotify.com/playlist/37i9dQZF1DXdxcBWuJkbcy",# Beast Mode
    "chill": "https://open.spotify.com/playlist/37i9dQZF1DX4WYpdgoIcn6",       # Chill Hits
    "party": "https://open.spotify.com/playlist/37i9dQZF1DXaXB8fQg7xif"        # Party Starters
}


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/recommend', methods=['POST'])
def recommend():
    mood = request.form.get("mood")
    playlist_url = mood_to_playlist.get(mood)

    if playlist_url:
        return redirect(playlist_url)
    else:
        return "No playlist found for that mood.", 400
    
if __name__ == '__main__':
    app.run(debug=True)
