# README

## Overview

This project analyzes happiness and well-being data across various countries using several indicators, such as GDP per capita, social support, and freedom to make life choices. The data is represented in a CSV format, and correlation heatmaps and outlier images are generated to visualize the relationships between different indicators.

## Data

The dataset used in this project consists of the following columns:

- **Country name**: The name of the country.
- **Year**: The year the data corresponds to.
- **Life Ladder**: A measure of well-being or happiness.
- **Log GDP per capita**: The logarithm of Gross Domestic Product per capita.
- **Social support**: A measure of the support individuals receive from their social networks.
- **Healthy life expectancy at birth**: The number of years a newborn can expect to live in good health.
- **Freedom to make life choices**: A measure of individual freedom in life choices.
- **Generosity**: A measure of how generous people in the country are.
- **Perceptions of corruption**: A measure of how corrupt people perceive their government and institutions to be.
- **Positive affect**: The presence of positive emotions and moods.
- **Negative affect**: The presence of negative emotions and moods.

### Sample Data

The following is a snippet of the data:

```
Country name,year,Life Ladder,Log GDP per capita,Social support,Healthy life expectancy at birth,Freedom to make life choices,Generosity,Perceptions of corruption,Positive affect,Negative affect
Afghanistan,2008,3.724,7.35,0.451,50.5,0.718,0.164,0.882,0.414,0.258
Afghanistan,2009,4.402,7.509,0.552,50.8,0.679,0.187,0.85,0.481,0.237
```

## Visualizations

### Correlation Heatmap

A correlation heatmap is generated to visualize the relationships between the different indicators. This heatmap provides insights into how closely related the various factors are, helping to identify potential areas for further investigation.

### Outlier Detection

Outlier images are generated to identify unusual data points that deviate significantly from the expected pattern. This can assist in understanding anomalies in the dataset and determining the robustness of the findings.

## Requirements

To run this project