import pandas as pd  
import os  

def collect_data():  
    data = pd.read_csv("data/sales_data.csv")  
    return data  

if __name__ == "__main__":  
    df = collect_data()  
    df.to_csv("data/raw_data.csv", index=False)