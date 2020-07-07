import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import seaborn as sns
import dash_table
from dash.dependencies import Input, Output, State
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="asdf1234",
  database="tsa"
)

mycursor = mydb.cursor(dictionary=True)

mycursor.execute('SELECT * FROM tsa.datatsa')
result = mycursor.fetchall()
df = pd.DataFrame(result)

def generate_table(dataframe, page_size = 10):
    return dash_table.DataTable(
        id= 'dataTable',
        columns= [{
            'name': i,
            'id': i
        }for i in dataframe.columns],
        data = dataframe.to_dict('records'),
        page_action = 'native',
        page_current = 0,
        page_size = page_size
    )

tips = sns.load_dataset('tips')
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1('Ujian Modul 2 Dashboard TSA'),
    html.Div(children='Created by: Widoseno N.S. Atri'),


############################ Make Tabs ############################
    dcc.Tabs(children= [

############################ Make tab in Tabs ############################

        dcc.Tab(value ='Tab1', label ='dataprem', children=[
                html.Div(children =[
                    html.Div([
                        html.P('Claim Site: '),
                        dcc.Dropdown(value='All',
                                    id='filter-site',
                                    options=[{'label':'Checkpoint', 'value': 'Checkpoint'},
                                    {'label':'Checked Baggage', 'value': 'Checked Baggage'},
                                    {'label':'Other', 'value': 'Other'},
                                    {'label':'All', 'value': 'All'}])
                    ], className='col-3')
                ], className='row'),

                html.Div([
                    html.Div([
                        html.P('Max Rows:'),
                        dcc.Input(id ='filter-row',
                                placeholder= 'Enter a value...',
                                type='number',
                                value= 10)
                    ], className='row col-3'),

                    html.Div(children =[
                                    html.Button('Search',id = 'filter')
                             ],className = 'row col-4'),
                    html.Div(id='div-table', children=[generate_table(tips)])
                ])     
        ]),


        dcc.Tab(value= 'Tab2', label= 'Bar-Chart', children= [
            html.Div([
                html.Div([
                    dcc.Graph(
                        id='bar-graph',
                        figure={
                            'data': [
                                {'x': df['Close Amount'], 'y': df['Close Amount'], 'type': 'bar', 'name': 'bar'}
                            ],
                            'layout': {
                                'title': 'Bar Chart'
                            }
                        }
                    )
                ])
            ])
            
        ]),


        dcc.Tab(value= 'Tab3', label= 'Scatter Chart', children= [
            html.Div(children = dcc.Graph(
                id = 'graph-scatter1',
                figure = {'data': [
                    go.Scatter(
                        x = df[df['Claim Type'] == i]['Claim Amount'],
                        y = df[df['Claim Type'] == i]['Close Amount'],
                        mode = 'markers',
                        name = '{}'.format(i)
                    ) for i in df['Claim Type'].unique()
                ],
                'layout': go.Layout(
                    xaxis= {'title': 'Claim Amount'},
                    yaxis= {'title': 'Close Amount'},
                    title = 'TSA Scatter Visualization',
                    hovermode = 'closest'
                )
                }
            ))
        ]),


        dcc.Tab(value= 'Tab4', label= 'Pie Chart', children= [
            html.Div(children =[
                    html.Div([
                        dcc.Dropdown(value='Close Amount',
                                    id='filter-pie',
                                    options=[{'label':'Claim Amount', 'value': 'Claim Amount'},
                                    {'label':'Close Amount', 'value': 'Close Amount'},
                                    {'label':'Day Differences', 'value': 'Day Differences'},
                                    {'label':'Amount Differences', 'value': 'Amount Differences'}])
                    ], className='col-3')
                ], className='row'),

            html.Div(children = dcc.Graph(
                id = 'pie-chart',
                figure = {'data': [
                    go.Pie(
                        labels= df['Claim Type'].unique(),
                        values= df.groupby('Claim Type').mean()['Close Amount'],
                        hoverinfo= 'label+percent',
                    )
                ],
                'layout': go.Layout(
                    title = 'Mean Pie Chart',
                )
                }
            ))
        ])
    ],
        ### Tabs Content Style
        content_style= {
            'fontFamily': 'Arial',
            'borderBottom': '1px solid #d6d6d6',
            'borderLeft': '1px solid #d6d6d6',
            'borderRight': '1px solid #d6d6d6',
            'padding': '44px'
        }
    )
], 
    style={
        'maxWidth': '1200px',
        'margin':'0 auto'
    }
)

@app.callback(
    Output(component_id = 'div-table', component_property = 'children'),
    [Input(component_id = 'filter', component_property = 'n_clicks')],    
    [State(component_id = 'filter-row', component_property = 'value'),
    State(component_id = 'filter-site', component_property = 'value')]
)

def update_table(n_clicks, row, site):
    if (site == 'All'):   
        children = [generate_table(df, page_size = row)]
    elif (site == 'Checkpoint'):   
        children = [generate_table(df[(df['Claim Site'] == 'Checkpoint')], page_size = row)]
    elif (site == 'Other'):   
        children = [generate_table(df[(df['Claim Site'] == 'Other')], page_size = row)]
    elif (site == 'Checked Baggage'):   
        children = [generate_table(df[(df['Claim Site'] == 'Checked Baggage')], page_size = row)]

    return children



    # ### CARA PINTAR ###
    # import seaborn as sns
    # tips = sns.load_dataset('tips')
    # if smoker != 'All':
    #     tips = tips[tips['smoker'] == smoker]
    # if sex != 'None':
    #     tips = tips[tips['sex'] == sex]
    # if day != 'None':
    #     tips = tips[tips['day'] == day]
    # if time != 'None':
    #     tips = tips[tips['time'] == time]
    
    # children = [generate_table(tips, page_size = row)]
    # return children




if __name__ == '__main__':
    app.run_server(debug=True)