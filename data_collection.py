import pandas as pd
from pytrends.request import TrendReq
from pytrends import dailydata


def get_weekly_data(kw_list, pytrends, cur_year, start_year):
    '''
    Gets weekly data for keywords in kw_list starting from January 1 of start_year to the current time

    kw_list: List of keywords
    pytrends: TrendReq object
    cur_year: current year
    start_year: year to start collecting data from 
    '''

    df_list = []

    for i in range(cur_year - start_year + 1):
        timeframe_start = f'{start_year + i}-01-01'
        timeframe_end = f'{start_year + i}-12-31'
        
        pytrends.build_payload(kw_list, timeframe=f'{timeframe_start} {timeframe_end}')

        yearly_df = pytrends.interest_over_time()
        df_list.append(yearly_df)
    
    return pd.concat(df_list, axis=0)



    
# Getting monthly data:
pytrends = TrendReq(hl='en-US', tz=360)
kw_list = ['bitcoin']
weekly_df = get_weekly_data(kw_list, pytrends, 2022, 2015)

# Filtering and renaming columns, then saving
output_weekly_df = weekly_df.filter(items=['date', 'bitcoin']).rename(columns={'bitcoin': 'value_week'})
output_weekly_df.to_csv('output/weekly_data_2015_present.csv')



# Getting daily data:
daily_df = dailydata.get_daily_data('bitcoin', start_year=2015, start_mon=1, stop_year=2022, stop_mon=9)

# Filtering and renaming columns, then saving
output_daily_df = daily_df.filter(items = ['date', 'bitcoin_unscaled']).rename(columns={'bitcoin_unscaled': 'value_day'})
output_daily_df.to_csv('output/daily_data_2015_present.csv')
