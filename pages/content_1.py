import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

def content1(app):

    ################## Data Analysis ##################
    
    #2019
    j19_df = pd.read_csv('Jan_2019_ontime.csv')
    f19_df = pd.read_csv('Feb_2019_ontime.csv')

    #2020
    j20_df = pd.read_csv('Jan_2020_ontime.csv')
    f20_df = pd.read_csv('Feb_2020_ontime.csv')

    # Number of flights by airline

    f_num = j19_df.groupby('OP_CARRIER')[['DEST']].count()
    f_num = f_num.sort_values('DEST',ascending=False)
    f_num.reset_index(level=0, inplace=True)

    f_num_fev = f19_df.groupby('OP_CARRIER')[['DEST']].count()
    f_num_fev = f_num_fev.sort_values('DEST',ascending=False)
    f_num_fev.reset_index(level=0, inplace=True)

    f_num20 = j20_df.groupby('OP_CARRIER')[['DEST']].count()
    f_num20 = f_num20.sort_values('DEST',ascending=False)
    f_num20.reset_index(level=0, inplace=True)

    f_num_fev_20 = f20_df.groupby('OP_CARRIER')[['DEST']].count()
    f_num_fev_20 = f_num_fev_20.sort_values('DEST',ascending=False)
    f_num_fev_20.reset_index(level=0, inplace=True)

    # Number of delayed flights by airline

    f_del = j19_df.groupby('OP_CARRIER')[['DEP_DEL15']].sum()
    f_del = f_del.sort_values('DEP_DEL15',ascending=False)
    f_del.reset_index(level=0, inplace=True)

    f_del_fev = f19_df.groupby('OP_CARRIER')[['DEP_DEL15']].sum()
    f_del_fev = f_del_fev.sort_values('DEP_DEL15',ascending=False)
    f_del_fev.reset_index(level=0, inplace=True)

    f_del20 = j20_df.groupby('OP_CARRIER')[['DEP_DEL15']].sum()
    f_del20 = f_del20.sort_values('DEP_DEL15',ascending=False)
    f_del20.reset_index(level=0, inplace=True)

    f_del_fev_20 = f20_df.groupby('OP_CARRIER')[['DEP_DEL15']].sum()
    f_del_fev_20 = f_del_fev_20.sort_values('DEP_DEL15',ascending=False)
    f_del_fev_20.reset_index(level=0, inplace=True)

    # Number of cancelled flights by airline

    f_cancel = j19_df.groupby('OP_CARRIER')[['CANCELLED']].sum()
    f_cancel.reset_index(level=0, inplace=True)

    f_cancel_fev = f19_df.groupby('OP_CARRIER')[['CANCELLED']].sum()
    f_cancel_fev.reset_index(level=0, inplace=True)

    f_cancel20 = j20_df.groupby('OP_CARRIER')[['CANCELLED']].sum()
    f_cancel20.reset_index(level=0, inplace=True)

    f_cancel_fev_20 = f20_df.groupby('OP_CARRIER')[['CANCELLED']].sum()
    f_cancel_fev_20.reset_index(level=0, inplace=True)

    # Number of diverted flights by airline

    f_div = j19_df.groupby('OP_CARRIER')[['DIVERTED']].sum()
    f_div.reset_index(level=0, inplace=True)

    f_div_fev = f19_df.groupby('OP_CARRIER')[['DIVERTED']].sum()
    f_div_fev.reset_index(level=0, inplace=True)

    f_div20 = j20_df.groupby('OP_CARRIER')[['DIVERTED']].sum()
    f_div20.reset_index(level=0, inplace=True)

    f_div_fev_20 = f20_df.groupby('OP_CARRIER')[['DIVERTED']].sum()
    f_div_fev_20.reset_index(level=0, inplace=True)

    #delayed, cancelled, diverted percentage

    f_del_perc = f_del['DEP_DEL15']/ f_num['DEST']
    f_del_perc_fev = f_del_fev['DEP_DEL15']/ f_num_fev['DEST']
    f_del_perc20 = f_del20['DEP_DEL15']/ f_num20['DEST']
    f_del_perc_fev_20 = f_del_fev_20['DEP_DEL15']/ f_num_fev_20['DEST']

    ##################  Figures ##################
    #Figure 1
    overall_figure = make_subplots(rows=2, cols=2, subplot_titles=("January 2019", "February 2019", "January 2020", "February 2020"))

    overall_figure.add_trace(go.Bar(x= f_del.OP_CARRIER, y = f_del_perc, marker_color = 'gray'),row=1, col=1)
    overall_figure.add_trace(go.Bar(x= f_del.OP_CARRIER, y = f_del_perc_fev, marker_color = 'gray'), row=1, col=2 )
    overall_figure.add_trace(go.Bar(x= f_del.OP_CARRIER, y = f_del_perc20, marker_color = 'gray'), row=2, col=1 )
    overall_figure.add_trace(go.Bar(x= f_del.OP_CARRIER, y = f_del_perc_fev_20, marker_color = 'gray', ), row=2, col=2 )

    overall_figure.update_layout(
    title_text="Delayed Airplanes", 
    title_x = 0.5,
    plot_bgcolor='white',
    paper_bgcolor = 'white',
    showlegend = False,
    )
    
    overall_figure.update_xaxes(showline=True, linewidth=2, linecolor='black')
    overall_figure.update_yaxes(range= [0,0.2], showline=True, linewidth=2, linecolor='black')

    #Figure 1

    flights =  make_subplots(rows=2, cols=2, subplot_titles=("January 2019", "February 2019", "January 2020", "February 2020"))

    flights.add_trace(go.Bar(x= f_num.OP_CARRIER, y = f_num.DEST, marker_color = 'gray'),row=1, col=1)
    flights.add_trace(go.Bar(x= f_num_fev.OP_CARRIER, y = f_num_fev.DEST, marker_color = 'gray'), row=1, col=2 )
    flights.add_trace(go.Bar(x= f_num20.OP_CARRIER, y = f_num20.DEST, marker_color = 'gray'), row=2, col=1 )
    flights.add_trace(go.Bar(x= f_num_fev_20.OP_CARRIER, y = f_num_fev_20.DEST, marker_color = 'gray', ), row=2, col=2 )


    flights.update_layout(
    title_text="Flights in January & February 2019-2020", 
    title_x = 0.5,
    plot_bgcolor='white',
    paper_bgcolor = 'white',
    showlegend = False,
    )
    
    overall_figure.update_xaxes(showline=True, linewidth=2, linecolor='black')
    overall_figure.update_yaxes(range= [0,0.2], showline=True, linewidth=2, linecolor='black')



################## Texts ##################
    text_1 = '''
      
    The project consists in creating a model to predict flight delay and was downloaded from Kaggle. The data consists of four files with records from the months of January and February of 2019 and 2020, with more than 2 million observations from all air carriers operating domestic flights in the US on that period.  \
    \
    We performed an exploratory data analysis to assess if there were missing values and to understand the features and market dynamic before creating a model. 


    '''

    text_2 = '''
    Overall we can see that flight volumes did not fluctuate much from 2019 to 2020, apparently with small impact from the pandemic.  \
    \
    After analyzing all features we have decided that our target variable should be the *‘ARR_DEL15’* that records if the flight arrived late on destination by more than 15 minutes and due to high correlation we should drop the variable **‘DEP_DEL15’** that records if the flight left the origin by more than 15 minutes.


    '''
################## Layout ##################
    b = html.Div(children = [

        dcc.Markdown(
            children = text_1,
            style = {'textAlign' : 'left','marginLeft' : 20}
        ),

        dcc.Graph(
            id='graph2',
            figure= flights
        ),
        
        dcc.Markdown(
            children = text_2,
            style = {'textAlign' : 'left','marginLeft' : 20}
        )

    ]
    )


    return b