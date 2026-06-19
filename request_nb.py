import marimo

__generated_with = "0.23.10"
app = marimo.App(width="medium")

with app.setup:
    import polars as pl
    import requests

    chart_request: str = "https://www.theaudiodb.com/api/v1/json/123/trending.php?country=us&type=itunes&format=singles"


@app.function
def request_music_data(url: str) -> dict:
    try:
        r = requests.get(url)
        r.raise_for_status()
        data = r.json()
        print(f"GET successful: {data}")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Request timed out: {timeout_err}")
    except Exception as e:
        print(f"General exception: {e}")


@app.cell
def _():
    chart_data: dict = request_music_data(chart_request)
    return (chart_data,)


@app.cell
def _(chart_data: dict):
    print(chart_data)
    return


if __name__ == "__main__":
    app.run()
