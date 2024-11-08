# steam-game-analysis

## Project Overview
This project analyzes the top Steam games over the years using SQL, Python, Excel, and Power BI to gain insights into trends, player counts, and other game metrics.

## Workflow

### 1. Data Collection and Storage with SQL
   - **Objective**: Use SQL to create and manage a database for storing data on top Steam games.
   - **Process**:
      - Use Python to fetch data from sources like the Steam API, SteamCharts, or Kaggle datasets.
      - Clean and preprocess the data in Python, then load it into a SQL database (e.g., MySQL, PostgreSQL, or SQLite).
      - Create tables for different aspects of game data (e.g., `game_info`, `player_counts`, `game_reviews`, etc.).

### 2. Data Analysis with Python
   - **Objective**: Conduct deeper analysis and transformations using Python libraries like Pandas and Matplotlib.
   - **Process**:
      - Query data from the SQL database using Python’s SQL libraries (e.g., SQLAlchemy or sqlite3).
      - Perform data wrangling and calculations in Python (e.g., calculate average player growth rates, analyze trends, or identify patterns among top genres).
      - Visualize preliminary findings with Matplotlib or Seaborn to explore trends and insights.

### 3. Data Export to Excel
   - **Objective**: Use Excel for data validation and as an additional tool for manual calculations.
   - **Process**:
      - Export SQL query results or processed data from Python as CSV files, which can be opened in Excel.
      - Perform further analysis or create pivot tables in Excel as needed.

### 4. Visualization and Reporting with Power BI
   - **Objective**: Create an interactive dashboard to showcase insights and analysis results.
   - **Process**:
      - Import data from the SQL database or CSV exports into Power BI.
      - Design interactive visuals such as:
         - Top games by year or genre,
         - Trends in player counts over time,
         - Correlations between player counts and game ratings.
      - Use Power BI’s DAX (Data Analysis Expressions) for calculated fields if needed.

## Suggested Insights to Showcase in the Dashboard
   - **Player Trends**: Visualizations showing player counts over time for top games.
   - **Genre Analysis**: Breakdown of popular game genres and how they’ve shifted over the years.
   - **Rating vs. Popularity**: Correlation between ratings and player numbers.
   - **Release Year Trends**: Insights into which years saw the highest releases of popular games.

## Project Structure
- **Database (SQL)**: Stores raw and cleaned data.
- **Python Scripts**: For data extraction, transformation, and analysis.
- **Excel**: For intermediate data analysis, pivot tables, and quick data validation.
- **Power BI Dashboard**: Comprehensive, interactive dashboard to showcase findings.

---

This project workflow showcases a full-stack data analytics process, integrating SQL for data management, Python for data processing, Excel for validation, and Power BI for visualization.

## Required Fields For Analysis
- Price
- Rating
- Negative/Positive review count

## Example of using Steam API
- https://store.steampowered.com/api/appdetails?appids=550
- https://store.steampowered.com/api/appdetails/?appids=550,570,1623730&filters=price_overview
   - If price/initial price = 0 = Free!
- https://partner.steamgames.com/doc/store/getreviews (NOT NEEDED, shows up in steamspy api)
   - Get total number of positive/negative reviews

## Resources
- https://www.kaggle.com/datasets/fronkongames/steam-games-dataset
- https://steamspy.com/api.php -> https://steamspy.com/api.php?request=top100forever
- https://wiki.teamfortress.com/wiki/User:RJackson/StorefrontAPI
- https://www.kaggle.com/datasets/nikdavis/steam-store-games/data
- https://nik-davis.github.io/posts/2019/steam-data-collection/
- https://www.kaggle.com/datasets/nikdavis/steam-store-raw?select=steamspy_data.csv
