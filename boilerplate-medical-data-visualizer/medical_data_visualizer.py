import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('../medical_examination.csv')

# Add 'overweight' column
weight = df['weight']/((df['height']/100)**2)
#df['overweight'] = np.where(weight > 25, 1, 0)
df['overweight'] = weight.apply(lambda x : 1 if x > 25 else  0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
#df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, 1)
df['cholesterol'] = df['cholesterol'].apply(lambda x : 0 if x==1 else  1)
#df['gluc'] = np.where(df['gluc'] == 1, 0, 1)
df['gluc'] = df['gluc'].apply(lambda x : 0 if x==1 else  1)
# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars = ['cardio'] , value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    

    
    df_cat['total'] = 1
    df_cat = df_cat.groupby(['cardio', 'variable' , 'value'], as_index=False).count()
    print(df_cat)


    

    # Draw the catplot with 'sns.catplot()'

    

    # Get the figure for the output
    fig = sns.catplot( x = "variable", y = "total", data = df_cat,  hue = "value", kind="bar", col ="cardio").fig

    """fig = sns.catplot(
    data=df_cat, x='variable', hue='value', col='cardio',
    kind='bar', sharey=False, order=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']"""


    # Set plot labels and titles
    
    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[df['ap_lo'] <= df['ap_hi']]
    df_heat = df_heat[df['height'] >= df['height'].quantile(0.025)]
    df_heat = df_heat[df['height'] <= df['height'].quantile(0.975)]
    df_heat = df_heat[df['weight'] >= df['weight'].quantile(0.025)]
    df_heat = df_heat[df['weight'] <= df['weight'].quantile(0.975)]
    # Calculate the correlation matrix
    print(df_heat)
    corr = df_heat.corr(method="pearson")
    print(corr)
    # Generate a mask for the upper triangle
    mask = np.triu(corr)


    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12,12))
    sns.heatmap(corr, vmin=None,  center=0.08, annot=True, fmt='.1f',  linewidth= 1,   square=True,  mask=mask, )

    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
