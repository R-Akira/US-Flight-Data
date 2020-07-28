import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

def content2(app):

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


    ################## Texts ##################
    text_3 = '''
      
    Analyzing late arrivals we can identify an important drop in delays from 2019 to 2020, with the following changes:  \n
    - January 2019: 18.59%  \n
   \n
    - January 2020: 13.73%  \n
   \n
    - February 2019: 23.14%  \n
   \n
    - February 2020: 14.90%  \n

    The reasons for this drop in delays are not clear, since the number of flights remained at similar levels in both months in 2019 and 2020.  \

    Analyzing the distribution of delays(%) per company we get the following:  \n


    '''

    text_4 = '''

    It’s extremely surprising to see that delays(%) gives us an almost uniform distribution on all periods being analyzed. This might indicate that flight delays are being managed and companies are being helped or penalized in order to spread the risk across all airlines.  \

    If that is the case it will be useless to develop a predictive model, since the target variable will be mostly impacted by deliberate decisions.

    '''


    ################## Layout ##################

    a = html.Div(children = [
        
        dcc.Markdown(
            children = text_3,
            style = {'textAlign' : 'left','marginLeft' : 20}
        ),



        dcc.Graph(
            id='graph1',
            figure= overall_figure
        ),
        
        dcc.Markdown(
            children = text_4,
            style = {'textAlign' : 'left','marginLeft' : 20}
        )

    ]
    )


    return a