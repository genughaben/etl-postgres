import psycopg2
import pandas.io.sql as sqlio
import numpy as np
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html

conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")

query = "select * from songplays as sp, time as t where sp.start_time = t.start_time;"
df = sqlio.read_sql_query(query, conn)
ds1 = df[['songplay_id','day']].groupby('day').agg(['count'])
x1 = list(ds1.index)
y1 = list(ds1[('songplay_id', 'count')])

ds2 = df[['songplay_id','user_id']].groupby('user_id').agg(['count'])
ds2 = ds2.sort_values(by=[('songplay_id', 'count')], ascending=False)
x2 = list( np.arange(len(ds2)))
y2 = list(ds2[('songplay_id', 'count')])

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# top_songs =

def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


app.layout = html.Div(children=[
    html.H1(children='Sparkify Dashboard'),

    html.Div(children='''
        Inspect users music listening behaviour
    '''),

    dcc.Graph(
            id='total_songplays_per_day',
            figure={
                'data': [
                    {'x': x1, 'y': y1, 'type': 'bar', 'name': 'SF'},
                ],
                'layout': {
                    'type':'category',
                    'title': 'Songplays per day (all users)'
                }
            }
        ),

    dcc.Graph(
        id='total_songplays_per_user',
        figure={
            'data': [
                {'x': x2, 'y': y2, 'type': 'bar', 'name': 'SF'},
            ],
            'layout': {
                'title': 'Songplays per user (all days)'
            }
        }
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)