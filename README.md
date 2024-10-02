# Tesla Stock Price Prediction

This project aims to predict the stock price of Tesla using historical data collected from the `yfinance` module in Python. The dataset spans from 2014-01-01 to 2024-09-01. The project is divided into five Jupyter notebooks, each focusing on different aspects of data analysis and model training.

## Notebooks

1. **Visualize and Statistically Analyze the Data**
    - This notebook focuses on visualizing the historical stock prices and performing statistical analysis to understand the underlying patterns and trends in the data.

2. **Train Statistical ARIMA Models with the 1st Difference of the Series**
    - This notebook involves training ARIMA models on the first difference of the time series data to make it stationary and suitable for forecasting.

3. **Visualize the Performance of the ARIMA Models**
    - This notebook visualizes the performance of the trained ARIMA models, comparing the predicted values with the actual stock prices.

4. **Train LSTM Neural Network on the Training Data**
    - This notebook trains a Long Short-Term Memory (LSTM) neural network on the training data to capture the temporal dependencies and make future stock price predictions.

5. **Visualize the Performance of the LSTM Model**
    - This notebook visualizes the performance of the LSTM model, comparing its predictions with the actual stock prices to evaluate its accuracy.

## Getting Started

### Prerequisites

- Python 3.11
- Jupyter Notebook
- `yfinance` module
- `pandas` module
- `numpy` module
- `matplotlib` module
- `seaborn` module
- `statsmodels` module
- `tensorflow` module

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/aritra-github26/Tesla-stock-price-time-series.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Tesla-stock-price-time-series
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Open Jupyter Notebook:
    ```bash
    jupyter notebook
    ```
2. Open and run the notebooks in the following order:
    - `get_data.py`
    - `01_visualize_data.ipynb`
    - `02_ARIMA_model.ipynb`
    - `03_ARIMA_forecast.ipynb`
    - `04_LSTM_model.ipynb`
    - `05_LSTM_forecast.ipynb`

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.

## Acknowledgements

- The `yfinance` module for providing easy access to historical stock price data.
- The open-source community for providing valuable libraries and tools.
