import pandas as pd 

cases = pd.read_csv('cases-by-day.csv')
deaths = pd.read_csv('deaths-by-day.csv')
hosp = pd.read_csv('hosp-by-day.csv')
tests = pd.read_csv('tests.csv')

print(cases.head())

cases = cases[3:]

print(cases.info())