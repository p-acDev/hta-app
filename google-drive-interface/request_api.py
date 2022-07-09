import requests
import pandas as pd
import plotly.graph_objects as go
from dateutil import parser
import plotly.offline
from pandas_profiling import ProfileReport
import os

# get back the data via requests
r = requests.get(f'http://backend:{os.environ.get("BACKEND_PORT")}/api/mesure')
data = r.json()

# transform into dataframe
df = pd.DataFrame(data)
df['datetime'] = df['date_mesure'].apply(lambda elem:parser.parse(elem))
df = df.drop(columns='date_mesure')

# do the plot
fig = go.Figure()
fig.add_trace(go.Scatter(x=df['datetime'], y=df['systolic'],
                         name='systolique',
                         mode='markers'))
fig.add_trace(go.Scatter(x=df['datetime'], y=df['diastolic'],
                         name='systolique',
                         mode='markers'))
plotly.offline.plot(fig, filename='report_data_plot.html')

# do the report stats
profile = ProfileReport(df, title="Rapport de mesures TA")
profile.to_file('data_report.html')