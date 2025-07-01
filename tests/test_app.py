from lib.database_connection import get_flask_database_connection



# # <!-- Scenario 1 -->
# # POST /albums

# # With body parameters:
# # title=Voyage
# # release_year=2022
# # artist_id=2
# # Expected response: 200 OK
# # (No content)



# # GET /albums
# #   (returns list of all albums) 
# # Expected response (200 OK)

# """
# Album(1, Doolittle, 1989, 1 )
# Album(2, Surfer Rosa, 1988, 1 )
# Album(3, Waterloo, 1974, 2)
# Album(4, Super Trouper, 1980, 2)
# Album(5, Bossanova, 1990, 1)
# Album(6, voyage, 2022, 2)
# """

"""
When i call POST / albums with the album info
THat album is now in the list of GET /albums  
"""

def test_post_album(db_connection, web_client):
    # Set up test data by seeding the database
    db_connection.seed("seeds/record_store.sql")
    
    # Send POST request to create a new album
    response = web_client.post("/albums", data={
        "title": "Voyage",
        "release_year": "2022",
        "artist_id": "2"
    })
    
    # Verify the POST request was successful
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ""
    
    # Verify the album was created by checking GET /albums
    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    
    response_text = get_response.data.decode("utf-8")
    # Check that our new album appears in the list
    assert "Album(6, Voyage, 2022, 2)" in response_text
    # Verify we have all expected albums (5 original + 1 new)
    assert response_text.count("Album(") == 6



# <!-- Scenario 2 -->
# POST /albums
# Expected response: 400 bad request
"""
You need to submit a title, release_year, and artist_id
"""

# GET /albums
"""
Album(1, Doolittle, 1989, 1 )
Album(2, Surfer Rosa, 1988, 1 )
Album(3, Waterloo, 1974, 2)
Album(4, Super Trouper, 1980, 2)
Album(5, Bossanova, 1990, 1)
"""

def test_get_artists(db_connection, web_client):
    """
    Test GET /artists returns list of artist names
    """
    # seed databse 
    db_connection.seed("seeds/record_store.sql")
    # GET request
    response = web_client.get("/artists")
    # Assert successful response
    assert response.status_code == 200
    # Assert expected content (comma-separated artist names)
    assert response.data.decode("utf-8") == "Pixies, ABBA, Taylor Swift, Nina Simone"

def test_post_artist(db_connection, web_client):
    """
    Test POST /artists creates new artist and appears in GET /artists
    """
    # seed databse 
    db_connection.seed("seeds/record_store.sql")
    # POST new artist
    post_response = web_client.post("/artists", data={
        "name": "Wild nothing",
        "genre": "Indie"
    })
    # Assert POST - see makers workbook for successfull response
    assert post_response.status_code == 200
    assert post_response.data.decode("utf-8") == ""
    # Verify artist appears in GET /artists
    get_response = web_client.get("/artists")
    assert get_response.status_code == 200
    assert get_response.data.decode("utf-8") == "Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing"









# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===
