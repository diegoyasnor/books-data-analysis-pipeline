# Books Data Analysis Pipeline 📚

This project demonstrates an **end-to-end data analysis workflow**, from web scraping
to data cleaning, exploratory data analysis, and experimental design.

The goal of this project is to showcase core **Data Analyst** skills such as:
data extraction, data validation, exploratory analysis, and data-driven decision making.

---

## Project Overview

In this project, I built a complete data pipeline that includes:

- Web scraping a public book catalog website
- Cleaning and standardizing raw data using pandas
- Performing exploratory data analysis (EDA)
- Designing and analyzing a simulated A/B test
- Drawing business-oriented conclusions from data

---

## Data Extraction

Initial exploration of the website’s HTML structure was performed in a Jupyter notebook
to identify and validate CSS selectors.

The final, reproducible scraping logic was implemented as a standalone Python script
to ensure consistency and scalability.

- Script: `src/extract/scrape_all_pages.py`
- Output: `data/raw/books_raw.csv`

---

## Data Cleaning

The raw dataset was cleaned and prepared using pandas:

- Standardized numeric fields (price)
- Converted categorical ratings into numerical values
- Validated data types and missing values
- Created basic features for analysis and experimentation

- Notebook: `notebooks/01_cleaning.ipynb`
- Output: `data/processed/books_clean.csv`

---

## Exploratory Data Analysis (EDA)

Exploratory analysis focused on identifying pricing and rating patterns:

- Distribution of book prices
- Relationship between ratings and prices
- Identification of data limitations and potential extensions

- Notebook: `notebooks/02_eda.ipynb`

---

## A/B Testing (Simulated)

A simulated A/B test was designed to evaluate whether highlighting
highly-rated books could improve conversion rates.

Since real user-level conversion data was not available, conversion outcomes
were simulated to demonstrate experimental design and statistical reasoning.

The analysis includes:
- Hypothesis formulation
- Random assignment to control and variant groups
- Conversion rate comparison
- Statistical significance testing

- Notebook: `notebooks/03_ab_testing.ipynb`

---

## Key Takeaways

- Book prices are not evenly distributed and tend to cluster within a mid-price range
- Higher ratings are associated with slightly higher prices, but rating alone does not
  fully explain pricing differences
- The simulated A/B test did not show statistically significant results, highlighting
  the importance of data-driven validation before making product decisions

---

## Future Improvements

Potential extensions of this project include:

- Scraping category and product description data from individual product pages
- Incorporating text-based features using basic NLP techniques
- Running additional experiments with alternative treatments or larger samples

---

## Tools Used

- Python
- pandas
- NumPy
- BeautifulSoup
- requests
- matplotlib
- scipy

---

## Author

Diego Yasno
