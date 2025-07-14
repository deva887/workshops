import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
print(sns.get_dataset_names())#returns inbuilt datasets
tips = sns.load_dataset("tips")
print(tips.head())
planets = sns.load_dataset("planets")#returns the specific data set
sns.set_theme(style="darkgrid")
print(planets.head())
import os
import pandas as pd
tips.to_csv("tips_dataset.csv",index = False)
print(os.getcwd())

#Scattered_plot

plt.figure(figsize=(4,4))
sns.scatterplot(data = tips,x='total_bill', y='tip',hue = 'time',size='size',palette ='deep')
plt.title("Scattered plot for Bill vs Tip")
plt.show()

#line_plot

sns.lineplot(data=tips,x='size',y='total_bill',hue='sex',markers='o')
plt.title("Line plot of total Bill vs Size")
plt.show()

#bar_plot

sns.barplot(data = tips,x='day',y="total_bill",hue="sex")
plt.title("Total bill by day")
plt.show() 

#box_plot

sns.boxplot(data = tips,x='day',y='tip',hue='sex')
plt.title("box_plot")
plt.show()

#violin_plot

sns.violinplot(data=tips,x='day',y='total_bill',hue='time')
plt.title("violin_plot")
plt.show()

#count_plot

sns.countplot(data=tips,x='day',hue='smoker')
plt.title("countplot")
plt.show()

#regression_plot

sns.regplot(data=tips,x='total_bill',y='tip',scatter_kws={'s':50},line_kws = {'color':'red'})
plt.title("Regression_plot")
plt.show()

#histogram_plot

sns.histplot(data=tips,x='total_bill',bins=20,kde=True,color="Blue")
plt.title("Histogram_plot")
plt.show()

# pairplot

sns.pairplot(tips, hue='sex', vars=["total_bill", "tip", "size"], palette='husl')
plt.suptitle("pair plot: numerberic variables by gender", y=1.02)
plt.show()

#joint_plot

sns.catplot(data=tips, x='day', y='tip', hue='sex', kind='point', palette='bright')
plt.title("catplot(point):Tips by day and gender")
plt.show()

#joint_plot

sns.jointplot(data=tips, x='total_bill', y='tip', kind='scatter', hue='smoker', color='purple', palette='coolwarm')
plt.suptitle("Jointplot: Total Bill vs Tip", y=1.02)
plt.show()

sns.jointplot(data=tips, x='total_bill', y='tip', kind='scatter', hue='smoker',  palette='coolwarm')
plt.suptitle("Jointplot: Total Bill vs Tip", y=1.02)
plt.show()

#facetgrid

g = sns.FacetGrid(tips, col='time', row='smoker', margin_titles=True).map(sns.histplot, 'total_bill', bins=20, kde=True).add_legend()
print(g)

#strip_plot

sns.stripplot(data=tips, x='day', y='tip', hue='sex', jitter=True, palette='Set1')
plt.title("strip plot: Tips by data and gender")
plt.show()

#kde_plot

sns.kdeplot(data=tips, x='total_bill',hue='sex', fill=True, palette='tab10')
plt.title("kde plot:Total bill density by gender")
plt.show()