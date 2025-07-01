from lib.artist_repository import ArtistRepository
from lib.artist import Artist

"""
Test Artist repo class
"""

"""
Test getting all artists from database
"""
def test_get_all_artist(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = ArtistRepository(db_connection)
    artists = repository.all()
    assert len(artists) == 4
    assert artists[0] == Artist(1, 'Pixies', 'Alt rock')
    assert artists[1] == Artist(2, 'ABBA', 'Pop')
    assert artists[2] == Artist(3, 'Taylor Swift', 'Pop')
    assert artists[3] == Artist(4, 'Nina Simone', 'Jazz')


"""
Test creating a new artist
"""
def test_create_artist(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = ArtistRepository(db_connection)
    new_artist = Artist(None, "Wild nothing", "Indie")
    repository.create(new_artist)
    # Verify artist created
    artists = repository.all()
    assert len(artists) == 5
    assert artists[4].name == "Wild nothing"
    assert artists[4].genre == "Indie"



