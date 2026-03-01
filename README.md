# Fetchly

A lightweight Python HTTP library with automatic retries, timeouts, and headers.

## Installation

```bash
pip install fetchly
```

## Usage

```python
import fetchly

# Set headers once
fetchly.set_headers({"Authorization": "Bearer your_api_key"})

# GET request
response = fetchly.get("https://api.example.com/data")
print(response.json())

# POST request
response = fetchly.post("https://api.example.com/data", json={"name": "John"})
print(response.json())

# PUT request
response = fetchly.put("https://api.example.com/data/1", json={"name": "Jane"})

# DELETE request
response = fetchly.delete("https://api.example.com/data/1")
```

## Features

- Automatic retries (default: 3)
- Timeout protection (default: 10 seconds)
- Clean error messages
- Set headers once, works everywhere
