from requests.models import Response
from requests.exceptions import HTTPError, Timeout, ConnectionError
import requests

def request_chart_data(api_key: str | None, url: str) -> Response | None:
    try:
        r: Response = requests.get(url)
        r.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(f"Response body: {r.text}")
    except ConnectionError as conn_err:
        print(f"Connection error: {conn_err}")
        print(f"Response body: {r.text}")
    except Timeout:
        print("Request timed out.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    else:
        # do something else?
        return r
