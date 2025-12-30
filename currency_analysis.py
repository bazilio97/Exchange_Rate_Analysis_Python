import pandas as pd
import matplotlib.pyplot as plt

# Functions

# Function to clean and prepare data for visualization 

def clean_country_data(df, country_name, val_col_name):
    
    df = df[df['Country Name'] == country_name].dropna(axis=1)
    
    df_formatted = df.melt(
        id_vars = ['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'],
        var_name = 'Year',
        value_name = val_col_name
        )

    df_formatted['Year'] = df_formatted['Year'].astype(int)
    
    return df_formatted

# Importing data from a csv file

dollar_stat = pd.read_csv(
    '/path/to/your/csv/API_PA.NUS.FCRF_DS2_en_csv_v2_21.csv',
    skiprows=4
)

# retrieving data for Ukraine

dollar_stat_ukraine = clean_country_data(dollar_stat, 'Ukraine', 'USD_UAH')

# plot initialization

plt.figure(figsize=(16,9))
plt.plot(
    dollar_stat_ukraine['Year'],
    dollar_stat_ukraine['USD_UAH'],
    label = 'USD/UAH'
    )


# retrieving data for Germany

dollar_stat_germany = clean_country_data(dollar_stat, 'Germany', 'USD_EUR')
dollar_stat_germany = dollar_stat_germany[dollar_stat_germany['Year'] > 1992]
dollar_stat_germany = dollar_stat_germany.reset_index(drop=True)


dollar_stat_ukraine['EUR_UAH'] = dollar_stat_ukraine['USD_UAH'] / dollar_stat_germany['USD_EUR'] 

# sharp currency grow explanation

crisis_years = [1998, 2008, 2013, 2022]

crisis_points = dollar_stat_ukraine[dollar_stat_ukraine['Year'].isin(crisis_years)]


plt.plot(
    dollar_stat_ukraine['Year'],
    dollar_stat_ukraine['EUR_UAH'],
    color = 'black',
    label = 'EUR/UAH'
    )

plt.scatter(
    crisis_points['Year'],
    crisis_points['USD_UAH'],
    color = 'red',
    label = 'Crisis points'
    )

plt.scatter(
    crisis_points['Year'],
    crisis_points['EUR_UAH'],
    color = 'red'
    )

plt.xlabel('Year')
plt.ylabel('USD and EUR per UAH')
plt.title("(USD EUR)/UAH Exchange Rate Since Ukraine's Independency")
plt.legend()
plt.show()

