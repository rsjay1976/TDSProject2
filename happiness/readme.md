# README

## Overview

This project analyzes life satisfaction and its correlates across different countries and years using a CSV dataset. The dataset includes various indicators such as Life Ladder, GDP per capita, social support, and others. The project also generates visualizations including a correlation heatmap and an outlier detection image.

## Dataset

The dataset is in CSV format and consists of the following columns:

- **Country name**: The name of the country.
- **Year**: The year of the data point.
- **Life Ladder**: A measure of life satisfaction.
- **Log GDP per capita**: The logarithm of GDP per capita, which serves as an economic indicator.
- **Social support**: A measure of social support available to individuals.
- **Healthy life expectancy at birth**: The average number of years a newborn can expect to live in good health.
- **Freedom to make life choices**: A measure of the perceived freedom individuals have in making life choices.
- **Generosity**: A measure of generosity, reflecting the extent of giving in the population.
- **Perceptions of corruption**: The level of perceived corruption in the society.
- **Positive affect**: A measure of positive emotions experienced by individuals.
- **Negative affect**: A measure of negative emotions experienced by individuals.

### Sample Data

```csv
Country name,year,Life Ladder,Log GDP per capita,Social support,Healthy life expectancy at birth,Freedom to make life choices,Generosity,Perceptions of corruption,Positive affect,Negative affect
Afghanistan,2008,3.724,7.35,0.451,50.5,0.718,0.164,0.882,0.414,0.258
Afghanistan,2009,4.402,7.509,0.552,50.8,0.679,0.187,0.85,0.481,0.237
```

## Visualization

The project generates the following visualizations:

1. **Correlation Heatmap**: This heatmap illustrates the correlation between different indicators in the dataset. Each value represents the strength and direction of the relationship between two variables.

   ![Correlation Heatmap](path/to/correlation_heatmap.png)

2. **Outlier Detection Image**: This image highlights any outliers detected in the data, which may indicate unusual observations that deviate significantly from the norm.

   ![Outlier