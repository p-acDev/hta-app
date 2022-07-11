from cProfile import label
import pandas as pd
import plotly.graph_objects as go
from dateutil import parser
import plotly.offline
from pandas_profiling import ProfileReport
import os
from request_api import get_all_data
import pylab as plt
plt.style.use('bmh')
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages


def create_df():
    
    data = get_all_data()
    
    # transform into dataframe
    df = pd.DataFrame(data)
    df['datetime'] = df['date_mesure'].apply(lambda elem:parser.parse(elem))
    df = df.drop(columns='date_mesure')
    
    return df

def create_report():
    
    df = create_df()
    df_report = df[['systolic', 'diastolic']]
    
    profile = ProfileReport(df_report, minimal=True)
    profile.to_file(output_file="report.html")
    
    # create box plots
    plt.subplot(1, 2, 1)
    plt.boxplot(x='systolic',
            data=df,
            showmeans=True,
            )
    plt.xlabel('Systolique')
    plt.ylabel('mmHg')
    
    plt.subplot(1, 2, 2)
    plt.boxplot(x='diastolic',
            data=df,
            showmeans=True
            )
    plt.xlabel('Diastolique')
    plt.ylabel('mmHg')
    
    plt.tight_layout()
    plt.savefig('boxplot.png')
    
    
    return None

if __name__ == "__main__":
    
    create_report()
    

    
    