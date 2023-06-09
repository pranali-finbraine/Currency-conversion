# Currency-conversion
# Data Retrieval and Conversion

This project provides functions for retrieving and converting financial data using the European Central Bank's Statistical Data Warehouse (SDW) API.

## Prerequisites

Before running the code, ensure that you have the following dependencies installed:

- pandas
- requests

You can install the dependencies by running the following command:

pip install pandas
pip install requests

## Files

The project consists of the following files:

1. `currency.py`: Contains the function `get_exchange_rate()` for retrieving exchange rate data, `get_raw_data()` for retrieving raw financial data and `get_data()` function for converting financial data to a target currency.
2. `currency.html`: Contains jupyter notebook view file with output (code with output)


To use the functions, follow these steps:

1.Retrieve exchange rate data:
exchange_rate_data = get_exchange_rate(source_currency, target_currency)


2.Retrieve raw financial data:
raw_data = get_raw_data(identifier)


3.Convert the raw data to the target currency:
converted_data = get_data(identifier, target_currency)

4.Access the converted data:
print(converted_data)



