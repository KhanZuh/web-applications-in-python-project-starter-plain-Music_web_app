from lib.album_repository import AlbumRepository
from lib.album import Album

"""
Test the AlbumRepository class
"""

def test_get_all_albums(db_connection):
    """
    Test getting all albums from database
    """
    db_connection.seed("seeds/record_store.sql")
    repository = AlbumRepository(db_connection)
    
    albums = repository.all()
    
    assert len(albums) == 5
    assert albums[0] == Album(1, 'Doolittle', 1989, 1)
    assert albums[1] == Album(2, 'Surfer Rosa', 1988, 1)
    assert albums[2] == Album(3, 'Waterloo', 1974, 2)
    assert albums[3] == Album(4, 'Super Trouper', 1980, 2)
    assert albums[4] == Album(5, 'Bossanova', 1990, 1)

def test_create_album(db_connection):
    """
    Test creating a new album
    """
    db_connection.seed("seeds/record_store.sql")
    repository = AlbumRepository(db_connection)
    
    # Create new album
    new_album = Album(None, "Test Album", 2023, 1)
    repository.create(new_album)
    
    # Verify it was created
    albums = repository.all()
    assert len(albums) == 6
    assert albums[5].title == "Test Album"
    assert albums[5].release_year == 2023
    assert albums[5].artist_id == 1

def test_find_album(db_connection):
    """
    Test finding a specific album by ID
    """
    db_connection.seed("seeds/record_store.sql")
    repository = AlbumRepository(db_connection)
    
    album = repository.find(1)
    assert album == Album(1, 'Doolittle', 1989, 1)

def test_find_nonexistent_album(db_connection):
    """
    Test finding an album that doesn't exist returns None
    """
    db_connection.seed("seeds/record_store.sql")
    repository = AlbumRepository(db_connection)
    
    album = repository.find(999)
    assert album is None