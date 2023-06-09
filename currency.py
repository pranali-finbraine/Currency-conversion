
import requests
import pandas as pd
import io


# #### Part 1 - Retrieving exchange rates


def get_exchange_rate(source: str, target: str = "EUR") -> pd.DataFrame:
    """
    Returns a dataframe with columns time_period and obs_value
    Parameters:
        source(str) : A source currency
        target(str) : A target currency, default currency is EUR
    return:
        data(dataframe) : Returns a dataframe with column Time_period and ob_value
    """
    url = "https://sdw-wsrest.ecb.europa.eu/service/data/EXR/"
    currency = "M"+"."+source+"."+target+"."+"SP00"+"."+"A"+"?detail=dataonly"
    requested_url = url+currency
    response = requests.get(requested_url, headers={'Accept': 'text/csv'})
    data = pd.read_csv(io.StringIO(response.text), usecols=['TIME_PERIOD', 'OBS_VALUE'])
    data.rename(columns={'OBS_VALUE': 'obs_value'}, inplace=True)
    return data


try:
    # Test get_exchange_rate function
    print(get_exchange_rate("GBP"))
except Exception as ex:
    print(ex)


# #### Part 2 - Retrieving other data

def get_raw_data(identifier: str) -> pd.DataFrame:
    """
    Returns a dataframe with columns time_period and obs_value
    Parameters:
        identifier(str) : Data Identifier
    return:
        data(dataframe) : Returns a dataframe with column Time_period and ob_value
    """
    url = "https://sdw-wsrest.ecb.europa.eu/service/data/BP6/"
    key = identifier+"?detail=dataonly"
    requested_url = url+key
    response = requests.get(requested_url, headers={'Accept': 'text/csv'})
    data = pd.read_csv(io.StringIO(response.text), usecols=['TIME_PERIOD', 'OBS_VALUE'])
    return data


try:
    # Test get_raw_data function
    print(get_raw_data("M.N.I8.W1.S1.S1.T.N.FA.F.F7.T.EUR._T.T.N"))
except Exception as ex:
    print(ex)


# #### Part 3 - Data transformation

def get_data(identifier: str, target_currency=None) -> pd.DataFrame:
    """
    Returns a dataframe with columns time_period and obs_value
    Parameters:
        identifier(str) : Data Identifier
        target_currency : A target currency, default currency is None
    return:
        data(dataframe) : Returns a dataframe with column Time_period and ob_value
    """
    if target_currency is not None:
        exchange_rate_data = get_exchange_rate(target_currency)
        raw_data = get_raw_data(identifier)
        data = pd.merge(raw_data, exchange_rate_data, on='TIME_PERIOD')
        data['OBS_VALUE'] = data['OBS_VALUE'] * data['obs_value']
        return data[['TIME_PERIOD', 'OBS_VALUE']]
    else:
        return get_raw_data(identifier)

try:
    # Test get_data function with currency conversion
    print(get_data("M.N.I8.W1.S1.S1.T.N.FA.F.F7.T.EUR._T.T.N", "GBP"))
except Exception as ex:
    print(ex)





