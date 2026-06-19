# Apple Music Chart Explorer

Let's have some fun with requests & marimo. Bring in some top 50 chart data of a set of genres, organize it in duckdb, use marimo to make some interactive charts.

## Plan
1. Pull top 50 chart data for a set of genres
    - Start with a set list of genres (Pop, Alternative, R&B, Country, Rock, Hip Hop)
    - Maybe later figure out a way to more dynamically collect genres
    - Chart data refreshes daily 12:00a UTC?
2. Organize & store chart data in duckdb
    - Would like to store chart data going back 14 days; will need rolling replacement logic
    - Unsure if we can request historical data...
    - Should be able to make duckdb data persistent (sqlite maybe?)
3. Set a base query to pull data from duckdb
    - *I wonder if I have the sequencing off here.*
4. Visualization layer using marimo
    - Show up/down position shifts based on previous day (calculated on historical dataset)
    - Dynamically switch between genres
