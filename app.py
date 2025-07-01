import os
from flask import Flask, request
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository
from lib.album import Album
from lib.artist import Artist



# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/albums', methods=['POST'])
def create_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = Album(None, request.form['title'], (request.form['release_year']), (request.form['artist_id']))
    repository.create(album)
    return "", 200 # REST API convention for successfull creation operations --> HTTP 200 OK with no content - This indicates the operation was successful but there's no meaningful data to return

@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    
    # Format albums as strings for the response
    album_strings = []
    for album in albums:
        album_strings.append(str(album))
    
    return '\n'.join(album_strings) # test expects string format

@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    # test expects comma-separated artist names
    artist_names = []
    for artist in artists:
        artist_names.append(artist.name)
    return ', '.join(artist_names)

@app.route('/artists', methods=['POST'])
def create_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = Artist(None, request.form['name'], request.form['genre'])
    repository.create(artist)
    return "", 200







# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"



# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

