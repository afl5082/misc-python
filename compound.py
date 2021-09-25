#cohort of year invested as column and top header as years since invested. 

data_dict = {}
years = [2015,2016,2017]
returns = {2015:.27,
           2016:.12,
           2017:.06,
           2018:.06,
           2019:.06,
           2020:.06,}

for year in years:
    years_since = 2021 - year
    
    cash_return = 10000

    for i in range(years_since):
        year_years_since = year + i
        for yr, return_pct in returns.items():
            if yr == year_years_since:
                pct_return = return_pct 

        cash_return = cash_return + (cash_return * pct_return)
        data_dict[year] = [cash_return,i]

print(data_dict)
        #print(cash_return)
        #print(year)
        #print(i)
