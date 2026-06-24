from requests.models import Response
from src.fetch import request_chart_data
from dotenv import load_dotenv
import os

load_dotenv()

LASTFM_KEY: str | None = os.getenv(key="LASTFM_API_KEY")
LASTFM_CHART_URL: str = f"http://ws.audioscrobbler.com/2.0/?method=chart.gettoptracks&api_key={LASTFM_KEY}&format=json"

def main():
    chart_data: Response | None = request_chart_data(api_key=LASTFM_KEY, url=LASTFM_CHART_URL)

if __name__ == "__main__":
    main()