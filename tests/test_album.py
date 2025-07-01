from lib.album import Album

"""
Test the Album model class
"""

def test_album_constructs():
    """
    Test Album can be constructed with all attributes
    """
    album = Album(1, "Test Album", 2022, 1)
    assert album.id == 1
    assert album.title == "Test Album"
    assert album.release_year == 2022
    assert album.artist_id == 1

def test_albums_are_equal():
    """
    Test two albums with same data are equal
    """
    album1 = Album(1, "Test Album", 2022, 1)
    album2 = Album(1, "Test Album", 2022, 1)
    assert album1 == album2

def test_albums_format_nicely():
    """
    Test Album string representation
    """
    album = Album(1, "Test Album", 2022, 1)
    assert str(album) == "Album(1, Test Album, 2022, 1)"