import pandas as pd #library for working with data
import matplotlib.pyplot as plt
import gradio as gd
data = {
    "Months":["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales":[10000, 12000, 15000, 13000, 17000, 16000],
    "Profits":[2000, 3000, 4000, 2500, 3500, 3000]
}
df = pd.DataFrame(data)
print(df)

#line plot for monthly sales
plt.figure(figsize=(6,5))#to generate a figure with 6 inch width and 5 inch heiht
plt.plot(df['Months'],df["Sales"],color = "blue",linestyle = "-",marker = 'o',label = "Sales")#color is line color,linestyle is type of line
plt.title('Sales trends over Months')#heading
plt.xlabel("Months")#name for x axis
plt.ylabel("Sales")#name for y axis
plt.grid(True)#figure will be in form of grid
plt.legend()#used to print the label as sales
plt.show()#to represent all of them

#profit ans sales

plt.figure(figsize=(6,3))
width = 0.3
plt.bar(df["Months"],df["Sales"], color = "green", width=width,label = "Sales")
plt.bar(df["Months"],df["Profits"], color = "yellow", width=width, label = "Profit",bottom = df["Sales"])
plt.xlabel("Months")
plt.ylabel("Amount")
plt.title("Sales and Profit trends Over months")
plt.grid(True)
plt.legend()
plt.show()

#pie_chart

plt.figure(figsize=(6,3))
plt.pie(df["Profits"],labels=df["Months"], autopct = '%1.2f%%',startangle = 90,colors = plt.cm.Paired.colors )
plt.title("Profit by Month")
plt.show()

#scatterd_plot

plt.figure(figsize=(6,6))
plt.scatter(df["Sales"],df["Profits"],color='green',s=100, edgecolors='black')
plt.xlabel("Sales")
plt.ylabel("Profits")
plt.title("Sales Vs Profits Scatter plot")
plt.show()

#histogram

plt.figure(figsize=(5,5))
plt.hist(df["Sales"], bins = 5, color = "purple", edgecolor = 'black')
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

#box_plot

plt.figure(figsize=(5,5))
plt.boxplot(df["Profits"])
plt.title("Sales box plot")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()