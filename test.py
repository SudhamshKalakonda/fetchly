from fetchly import get, post, put, delete, set_headers

set_headers({"Authorization": "Bearer my_secret_key_123"})

# Test GET
response = get("https://jsonplaceholder.typicode.com/posts/1")
print("GET:", response.json())

# Test POST
response = post("https://jsonplaceholder.typicode.com/posts", json={
    "title": "my first post",
    "body": "fetchly is awesome",
    "userId": 1
})
print("POST:", response.json())

# Test PUT
response = put("https://jsonplaceholder.typicode.com/posts/1", json={
    "title": "updated title",
    "body": "updated body",
    "userId": 1
})
print("PUT:", response.json())

# Test DELETE
response = delete("https://jsonplaceholder.typicode.com/posts/1")
print("DELETE status:", response.status_code)