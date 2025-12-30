PROJECT TITLE: Exchange Rate Analysis: USD/UAH & EUR/UAH Since Ukraine’s Independence

PRIJECT OVERVIEW:

This project analyzes historical exchange rate data to explore the dynamics of:
 - USD / UAH (US Dollar to Ukrainian Hryvnia);
 - EUR / UAH (Euro to Ukrainian Hryvnia).
  
The analysis covers the period from 1991 (Ukraine’s independence) to the most recent available year.
The project focuses on:

 - Cleaning and reshaping macroeconomic data;
 - Time-series analysis;
 - Identifying major economic crisis periods;
 - Calculating cross-currency exchange rates using USD as a base currency.

DATA SOURCE:

The data was obtained from the World Bank Open Data platform.

Data link: https://data.worldbank.org/indicator/PA.NUS.FCRF?name_desc=false&utm_source=chatgpt.com&year=1991

METHODOLOGY:

1. Data Preparation
 - Loaded World Bank CSV data using pandas;
 - Removed empty columns;
 - Filtered data by country (Ukraine, Germany as a source of EUR);
 - Converted wide-format year columns into long-format time series;
 - Converted year values to numeric format.
2. Exchange Rate Calculations
 - USD/UAH was taken directly from World Bank data;
 - EUR/UAH was calculated using the cross-rate formula: EUR/UAH = USD/UAH ÷ USD/EUR
3. Crisis Year Highlighting
The following major crisis years were highlighted:
 - 1998 – Post-Soviet and Russian financial crisis;
 - 2008 – Global financial crisis;
 - 2013 – Kyiv demonstration and Annexation of Crimea and start of war;
 - 2022 – Full-scale invasion of Ukraine;
