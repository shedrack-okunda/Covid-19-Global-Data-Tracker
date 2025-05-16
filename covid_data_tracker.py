# Load and clean the data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("owid-covid-data.csv")

# Preview data
print(df.head())
print(df.columns)

# Convert 'date' to datetime
df['date'] = pd.to_datetime(df['date'])

# Filter countries of interest
countries = ['Kenya', 'United States', 'India']
df = df[df['location'].isin(countries)]

# Drop rows with missing critical values
df = df.dropna(subset=['total_cases', 'total_deaths'])

# Fill missing numeric values
df.fillna(0, inplace=True)

# Exploratory data analysis
# Total cases over time
plt.figure(figsize=(12,6))
for country in countries:
    temp = df[df['location'] == country]
    plt.plot(temp['date'], temp['total_cases'], label=country)
plt.title('Total COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Total deaths over time
plt.figure(figsize=(12,6))
for country in countries:
    temp = df[df['location'] == country]
    plt.plot(temp['date'], temp['total_deaths'], label=country)
plt.title('Total COVID-19 Deaths Over Time')
plt.xlabel('Date')
plt.ylabel('Total Deaths')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Daily new cases comparison
plt.figure(figsize=(12,6))
for country in countries:
    temp = df[df['location'] == country]
    plt.plot(temp['date'], temp['new_cases'], label=country)
plt.title('Daily New COVID-19 Cases')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Calculate and visualize death rate
df['death_rate'] = df['total_deaths'] / df['total_cases']
plt.figure(figsize=(12,6))
for country in countries:
    temp = df[df['location'] == country]
    plt.plot(temp['date'], temp['death_rate'], label=country)
plt.title('COVID-19 Death Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Death Rate')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Vaccination progress
# Vaccination trend
plt.figure(figsize=(12,6))
for country in countries:
    temp = df[df['location'] == country]
    plt.plot(temp['date'], temp['total_vaccinations'], label=country)
plt.title('Total Vaccinations Over Time')
plt.xlabel('Date')
plt.ylabel('Total Vaccinations')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Choropleth map using plotly
import plotly.express as px

# Latest data per country
latest = df[df['date'] == df['date'].max()]
choropleth_df = latest[['iso_code', 'location', 'total_cases']].dropna()

fig = px.choropleth(choropleth_df,
                    locations="iso_code",
                    color="total_cases",
                    hover_name="location",
                    color_continuous_scale="Reds",
                    title="Global Total COVID-19 Cases (Latest Date)")
fig.show()
