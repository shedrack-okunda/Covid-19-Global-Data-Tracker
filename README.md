# COVID-19 Global Data Tracker

## Project Description

This project is a data analysis and reporting notebook I built to track global COVID-19 trends. I worked with real-world data on cases, deaths, recoveries, and vaccinations across different countries and over time. Throughout the project, I cleaned and processed the data, performed exploratory data analysis (EDA), generated insights, and visualized trends using Python data tools.

By the end, I created a comprehensive data analysis report with visuals and narrative insights, suitable for sharing and presentation.

## 🚩 Project Objectives

- Imported and cleaned COVID-19 global data
- Analyzed time trends including cases, deaths, and vaccinations
- Compared key metrics across countries and regions
- Visualized trends with charts and maps
- Communicated my findings clearly in a Jupyter Notebook report

## 🗂️ How I Approached the Project

### 1️⃣ Data Collection

I obtained the COVID-19 dataset from Our World in Data by downloading the `owid-covid-data.csv` file and saved it to my working directory.

### 2️⃣ Data Loading & Exploration

Using pandas, I loaded the dataset and explored its structure by examining columns, previewing rows, and checking for missing values. This helped me understand the data before starting analysis.

### 3️⃣ Data Cleaning

I filtered the dataset for countries of interest (such as Kenya, USA, and India), removed rows with missing critical values, converted date columns to datetime format, and handled missing numeric values using interpolation and fillna to prepare the data for analysis.

### 4️⃣ Exploratory Data Analysis (EDA)

I generated descriptive statistics and explored trends by plotting total cases and deaths over time for selected countries. I compared daily new cases and calculated important indicators like the death rate.

### 5️⃣ Visualizing Vaccination Progress

I analyzed vaccination rollout progress by plotting cumulative vaccinations over time and comparing vaccination percentages across countries using line charts.

### 6️⃣ Optional Choropleth Map

To visualize case density globally, I created a choropleth map showing total cases by country using Plotly Express.

### 7️⃣ Insights & Reporting

Finally, I summarized key insights from the data, highlighted interesting patterns, and documented everything in a well-structured Jupyter Notebook combining code, visuals, and markdown explanations. I also exported the notebook to PDF for easy sharing.

## 🛠️ Tools & Libraries I Used

- Jupyter Notebook
- pandas
- matplotlib
- seaborn
- Plotly Express (for interactive maps)

## 🎯 Optional Stretch Goals I Explored

- Allowed dynamic selections of countries and date ranges (user inputs)
- Explored building interactive dashboards (future improvement areas)

## ✅ Final Outcome

I successfully built a reproducible and informative data analysis report tracking global COVID-19 trends. The project enhanced my skills in data cleaning, exploration, visualization, and storytelling with data.

Feel free to explore the notebook to see the detailed analysis, visualizations, and insights I’ve drawn from the data.

## 📝 Key Findings

- India had a sharp case surge in 2021.
- The US had the highest total deaths.
- Kenya’s vaccination rate rose steadily in late 2021.
