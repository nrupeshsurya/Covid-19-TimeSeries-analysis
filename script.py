# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %%
import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd
import matplotlib.dates as mdates
import mplcyberpunk
plt.style.use('classic')
get_ipython().run_line_magic('matplotlib', 'inline')


# %%
df = pd.read_csv('data.csv', index_col=0)


# %%
df.info()


# %%
df = df.rename_axis('Dates').reset_index()
df['Dates'] = pd.to_datetime(df['Dates'])


# %%
plt.plot(df['Dates'],df['CASE_COUNT'])
plt.xticks(rotation='vertical')
plt.xlabel('Time--->')
plt.ylabel('New Cases--->')
plt.title('New Cases in NYC')
plt.show()


# %%
plt.plot(df['Dates'],df['DEATH_COUNT'])
plt.xticks(rotation='vertical')
plt.xlabel('Time--->')
plt.ylabel('Deaths--->')
plt.title('Deaths in NYC')
plt.show()


# %%
p1, = plt.plot(df['Dates'],df['TOTAL_TESTS'],label='total tests')
p2, = plt.plot(df['Dates'],df['POSITIVE_TESTS'],label = 'positive tests')
p3, = plt.plot(df['Dates'],df['TOTAL_ANTIGEN_TESTS'],label = 'antigen tests')
plt.legend(handles=[p1, p2, p3], title='Legend', bbox_to_anchor=(1.05, 1), loc='upper left', prop=fontP)
plt.xticks(rotation='vertical')
plt.xlabel('Time--->')
plt.ylabel('Frequency--->')
plt.title('Testing data')
plt.show()


# %%
p1, = plt.plot(df['Dates'],df['driving'],label='driving')
p2, = plt.plot(df['Dates'],df['walking'],label = 'walking')
p3, = plt.plot(df['Dates'],df['transit'],label = 'transit')
p4, = plt.plot(df['Dates'],[100 for i in range(len(df))], label = 'baseline')
plt.legend(handles=[p1, p2, p3,p4], title='Legend', bbox_to_anchor=(1.05, 1), loc='upper left', prop=fontP)
plt.xticks(rotation='vertical')
plt.xlabel('Time--->')
plt.ylabel('Value--->')
plt.title('Apple Mobility data')
plt.show()


# %%
p1, = plt.plot(df['Dates'],[i+100 for i in df['retail_and_recreation_percent_change_from_baseline'].to_list()],label='retail and recreation')
p2, = plt.plot(df['Dates'],[i+100 for i in df['grocery_and_pharmacy_percent_change_from_baseline'].to_list()],label = 'grocery and pharmacy')
p3, = plt.plot(df['Dates'],[i+100 for i in df['parks_percent_change_from_baseline'].to_list()],label = 'parks')
p4, = plt.plot(df['Dates'],[i+100 for i in df['transit_stations_percent_change_from_baseline'].to_list()], label = 'transit')
p5, = plt.plot(df['Dates'],[i+100 for i in df['workplaces_percent_change_from_baseline'].to_list()], label = 'workplace')
p6, = plt.plot(df['Dates'],[i+100 for i in df['residential_percent_change_from_baseline'].to_list()], label = 'residential')
p7, = plt.plot(df['Dates'],[100 for i in range(len(df))], label = 'baseline')
plt.legend(handles=[p1, p2, p3, p4, p5, p6, p7], title='Legend', bbox_to_anchor=(1.05, 1), loc='upper left', prop=fontP)
plt.xticks(rotation='vertical')
plt.xlabel('Time--->')
plt.ylabel('Value--->')
plt.title('Google mobility Data')
plt.show()


# %%



