

# Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
POST /albums
  title: string (body parameter)
  release_year: int (body parameter)  
  artist_id: int (body parameter)

Expected response (200 OK)
(No content)

GET /albums 
Expected response (200 OK)
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```
<!-- Scenario 1 -->
# POST /albums

# With body parameters:
# title=Voyage
# release_year=2022
# artist_id=2
# Expected response: 200 OK
# (No content)



# GET /albums
#   (returns list of all albums) 
# Expected response (200 OK)
""
Album(1, Doolittle, 1989, 1 )
Album(2, Surfer Rosa, 1988, 1 )
Album(3, Waterloo, 1974, 2)
Album(4, Super Trouper, 1980, 2)
Album(5, Bossanova, 1990, 1)
Album(6, voyage, 2022, 2)
""

<!-- Scenario 2 -->
# POST /albums
# Expected response: 400 bad request
""
You need to submit a title, release_year, and artist_id
""

# GET /albums
""
Album(1, Doolittle, 1989, 1 )
Album(2, Surfer Rosa, 1988, 1 )
Album(3, Waterloo, 1974, 2)
Album(4, Super Trouper, 1980, 2)
Album(5, Bossanova, 1990, 1)
""

```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
GET /home
  Expected response (200 OK):
  "This is my home page!"
"""
def test_get_home(web_client):
    response = web_client.get('/home')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'This is my home page!'

"""
POST /submit
  Parameters:
    name: Leo
    message: Hello world
  Expected response (200 OK):
  "Thanks Leo, you sent this message: "Hello world""
"""
def test_post_submit(web_client):
    response = web_client.post('/submit', data={'name': 'Leo', 'message': 'Hello world'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Thanks Leo, you sent this message: "Hello world"'
```

