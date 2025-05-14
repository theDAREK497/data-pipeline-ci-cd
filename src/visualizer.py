import pandas as pd  
import matplotlib.pyplot as plt  

def generate_plot():  
    df = pd.read_csv("data/processed_data.csv")  
    df.plot(kind="bar", x="category", y="total_sales", title="Sales by Category")  
    plt.savefig("docs/sales_plot.png")  

if __name__ == "__main__":  
    generate_plot()