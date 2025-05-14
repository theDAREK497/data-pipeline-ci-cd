# Automated Data Pipeline with CI/CD  

A simple automated data pipeline that collects, processes, and visualizes data using Python, Docker, and GitHub Actions.  

## Features  
- **Data Collection**: Load data from CSV files.  
- **Data Processing**: Aggregate and analyze data (e.g., sales by category).  
- **Visualization**: Generate bar charts for insights.  
- **CI/CD Integration**: Automate pipeline execution via GitHub Actions.  

## Technologies Used  
- **Python**: Pandas, Matplotlib  
- **Docker**: Containerization  
- **GitHub Actions**: CI/CD automation  
- **PostgreSQL**: Data storage (optional)  

## Requirements  
- **Local Development**:  
  - Docker  
  - Docker Compose  
- **GitHub Actions**: No setup required (runs in the cloud).  

## How to Run Locally  
1. **Clone the repository**:  
   ```bash  
   git clone https://github.com/theDAREK497/data-pipeline-ci-cd.git   
   cd data-pipeline-ci-cd
   ```
2. **Prepare input data**:
   Place a CSV file named sales_data.csv in the data/ folder with columns:
   ```bash 
   category,sales  
   electronics,1000  
   clothing,800  
   books,500  
   ```
3. **Run the pipeline**:
   ```bash 
   docker-compose up
   ```
4. **View results**:
   - **Processed data**: data/processed_data.csv
   - **Visualization**: docs/sales_plot.png

## CI/CD Workflow
Every push to the **main** branch triggers:
1. Docker image build
2. Pipeline execution
3. Artifact generation (CSV + plot)

## License
MIT License

## Contributing
Contributions are welcome! Fork the repo and submit a pull request.
