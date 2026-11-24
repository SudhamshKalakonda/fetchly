# Fetchly 🚀

> The simplest, safest way to make HTTP requests in Python.

![PyPI version](https://img.shields.io/pypi/v/fetchly)
![Downloads](https://img.shields.io/pypi/dm/fetchly)
![License](https://img.shields.io/pypi/l/fetchly)
![Python](https://img.shields.io/pypi/pyversions/fetchly)

## Why Fetchly?

Every Python developer writes this same boilerplate over and over:

Without fetchly - 15 lines every single time
With fetchly - 2 lines, always.

## Installation

pip install fetchly

## Quick Start

import fetchly

# Set your API key once - works for every request automatically
fetchly.set_headers({"Authorization": "Bearer your_api_key"})

# GET
response = fetchly.get("https://api.example.com/users")
print(response.json())

# POST
response = fetchly.post("https://api.example.com/users", json={"name": "John"})
print(response.json())

# PUT
fetchly.put("https://api.example.com/users/1", json={"name": "Jane"})

# DELETE
fetchly.delete("https://api.example.com/users/1")

## Features

- Automatic timeout (10s default)
- Automatic retries (3 retries default)
- Clean error messages
- Set headers once, works everywhere

## License

MIT - Sudhamsh Kalakonda
