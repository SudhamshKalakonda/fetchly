import requests
import time

default_headers={}

def set_headers(key):
    default_headers .update(key)





def get(url, timeout=10, retries=3, **kwargs):
    kwargs.setdefault("headers", {}).update(default_headers)
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, timeout=timeout, **kwargs)
            response.raise_for_status()
            return response
        except requests.exceptions.Timeout:
            print(f"Attempt {attempt} timed out...")
        except requests.exceptions.HTTPError as e:
            raise Exception(f"HTTP error: {e}")
        except requests.exceptions.ConnectionError:
            print(f"Attempt {attempt} failed. Retrying...")
        
        if attempt < retries:
            time.sleep(2)

    raise Exception(f"All {retries} attempts failed for {url}")


def post(url, timeout=10, retries=3, **kwargs):
    kwargs.setdefault("headers", {}).update(default_headers)
    for attempt in range(1, retries + 1):
        try:
            response = requests.post(url, timeout=timeout, **kwargs)
            response.raise_for_status()
            return response
        except requests.exceptions.Timeout:
            print(f"Attempt {attempt} timed out...")
        except requests.exceptions.HTTPError as e:
            raise Exception(f"HTTP error: {e}")
        except requests.exceptions.ConnectionError:
            print(f"Attempt {attempt} failed. Retrying...")
        
        if attempt < retries:
            time.sleep(2)

    raise Exception(f"All {retries} attempts failed for {url}")

def put(url, timeout=10, retries=3, **kwargs):
    kwargs.setdefault("headers", {}).update(default_headers)
    for attempt in range(1, retries + 1):
        try:
            response = requests.put(url, timeout=timeout, **kwargs)
            response.raise_for_status()
            return response
        except requests.exceptions.Timeout:
            print(f"Attempt {attempt} timed out...")
        except requests.exceptions.HTTPError as e:
            raise Exception(f"HTTP error: {e}")
        except requests.exceptions.ConnectionError:
            print(f"Attempt {attempt} failed. Retrying...")
        
        if attempt < retries:
            time.sleep(2)

    raise Exception(f"All {retries} attempts failed for {url}")

def delete(url, timeout=10, retries=3, **kwargs):
    kwargs.setdefault("headers", {}).update(default_headers)
    for attempt in range(1, retries + 1):
        try:
            response = requests.delete(url, timeout=timeout, **kwargs)
            response.raise_for_status()
            return response
        except requests.exceptions.Timeout:
            print(f"Attempt {attempt} timed out...")
        except requests.exceptions.HTTPError as e:
            raise Exception(f"HTTP error: {e}")
        except requests.exceptions.ConnectionError:
            print(f"Attempt {attempt} failed. Retrying...")
        
        if attempt < retries:
            time.sleep(2)

    raise Exception(f"All {retries} attempts failed for {url}")
