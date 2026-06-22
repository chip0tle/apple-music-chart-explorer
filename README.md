# Last.fm Show Finder

Let's have some fun with requests & marimo. Find top songs on last.fm charts & find nearby shows via Bandsintown.

## Plan
1. Pull top 10 songs from US
    - See if there are charts by genre; if yes, then also grab top 10 from Pop, R&B, Alternative
2. Organize & store chart data in duckdb
    - Would like to store chart data going back 14 days; will need rolling replacement logic
    - Unsure if we can request historical data...
    - Should be able to make duckdb data persistent (sqlite maybe?)
3. Set a base query to pull data from duckdb
    - *I wonder if I have the sequencing off here.*
4. Visualization layer using marimo
    - Show up/down position shifts based on previous day (calculated on historical dataset)
    - Dynamically switch between genres
5. Find nearby shows via Bandsintown
    - User selects a song featured on the chart, use the artist to query Bandsintown
    - Default geo is NYC but maybe there's a way to use user geo?

[Last.fm API docs] <https://www.last.fm/api>
[Bandsintown API docs] <https://app.swaggerhub.com/apis/Bandsintown/PublicAPI/3.0.0>

### Shout out to [public-apis] <https://github.com/public-apis/public-apis#index> repo!
