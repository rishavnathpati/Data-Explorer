# Dataset Explorer

Dataset Explorer is a web application built with Streamlit that allows users to upload, explore, and manipulate CSV datasets. The application is designed with a modular approach, each module handling a specific functionality.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed the latest version of Python (3.7 or higher) and pip. If not, you can download Python from [here](https://www.python.org/downloads/) and pip will be installed with Python.
- You have a Windows/Linux/Mac machine.

## Modules

- `DataLoader`: Handles the loading of data either by uploading a CSV file or inputting a URL to a CSV file.
- `DataAnalyzer`: Provides summary statistics and data types of the loaded dataset.
- `DataFilter`: Allows users to filter rows based on user-defined conditions.
- `DataTransformer`: Enables users to perform operations on columns.
- `DataVisualizer`: Visualizes data with various types of plots (Histogram, Box Plot, Pie Chart, Scatter Plot, Heatmap).

## Features

- Upload CSV files or load data from a URL.
- Display the uploaded dataset.
- Show summary statistics and data types.
- Filter rows based on user-defined conditions.
- Perform operations on columns.
- Visualize data with various types of plots (Histogram, Box Plot, Pie Chart, Scatter Plot, Heatmap).
- Transform data.

## Detailed Installation Instructions

1. Clone the repository:
   Open your terminal and run the following git command:
   ```
   git clone https://github.com/rishavnathpati/Data-Explorer
   ```
2. Navigate to the project directory:
   Use the change directory command to navigate into the cloned repository:
   ```
   cd Data-Explorer
   ```
3. Create a virtual environment:
   It's recommended to create a virtual environment to keep the project's dependencies isolated from your system. Use the following command to create a new virtual environment named 'env':
   ```
   python3 -m venv env
   ```
4. Activate the virtual environment:
   Before installing the project's dependencies, you need to activate the virtual environment. Use the following command:
   ```
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```
5. Install the required packages:
   The project's dependencies are listed in the 'requirements.txt' file. You can install all of them using pip:
   ```
   pip install -r requirements.txt
   ```
6. Run the application:
   Now, you're ready to run the application. Use the following command to start the Streamlit server:
   ```
   streamlit run app.py
   ```

## Usage

After running the application, open your web browser and go to `http://localhost:8501` to start exploring your datasets!