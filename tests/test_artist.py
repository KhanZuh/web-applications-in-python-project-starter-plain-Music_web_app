from lib.artist import Artist

"""
Test the artist model class
"""

"""
Test Artist can be constructed with all attributes
"""
def test_artist_constructs():
    artist = Artist(1, "Test Artist", "Rock")
    assert artist.id == 1
    assert artist.name == "Test Artist"
    assert artist.name == "Test Artist"
    assert artist.genre == "Rock"


"""
Test two artists with same data are equal
"""
def test_artists_are_equal():
    artist1 = Artist(1, "Test Artist", "Rock")
    artist2 = Artist(1, "Test Artist", "Rock")
    assert artist1 == artist2

"""
Test Artist string representation
"""
def test_artists_format_nicely():
    artist = Artist(1, "Test Artist", "Rock")
    assert str(artist) == "Artist(1, Test Artist, Rock)"