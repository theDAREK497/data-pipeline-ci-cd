import pandas as pd  

def process_data():  
    df = pd.read_csv("data/raw_data.csv")  
    # Пример: агрегация данных  
    summary = df.groupby("category").agg(total_sales=("sales", "sum"))  
    return summary  

if __name__ == "__main__":  
    summary_df = process_data()  
    summary_df.to_csv("data/processed_data.csv")