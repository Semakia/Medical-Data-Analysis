# Project: Medical Examination Analysis

This project analyzes a dataset (medical_examination.csv) containing information about medical examinations. The script generates two visualizations to explore potential relationships between various health factors and cardiovascular disease:

Categorical Plot: This plot investigates the distribution of features like cholesterol, blood sugar, smoking habits, alcohol consumption, physical activity level, and overweight status across patients with and without cardiovascular disease.
Heatmap: This visualization explores the correlation between different health factors. It helps identify potential associations between features, such as a positive correlation between weight and blood pressure.
Script Functionality:

The script utilizes Python libraries like pandas (pd), seaborn (sns), matplotlib (plt), and numpy (np) to achieve the following:

## 1- Data Loading and Cleaning:
Imports the CSV data
Creates a new column named "overweight" to indicate weight status based on Body Mass Index (BMI).
Normalizes cholesterol and blood sugar values (0 indicates good, 1 indicates bad).
## 2- Categorical Plot Generation
Uses df.melt to reshape the data for the categorical plot.
Groups the data by cardiovascular disease presence ("cardio") and the variable of interest.
Creates a bar chart using sns.catplot to visualize the distribution of each feature value within each cardiovascular disease category.
## 3- Heatmap Generation:
Cleans the data by removing outliers in blood pressure, height, and weight.
Calculates the correlation matrix to identify relationships between features.
Generates a heatmap using sns.heatmap to represent the correlation values.
# Output:
The script saves the generated visualizations as follows:

Categorical Plot: catplot.png
Heatmap: heatmap.png
