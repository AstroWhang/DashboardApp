# -*- coding: utf-8 -*-
import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

temperaturechange = pd.read_csv('Temperature.csv')

emissions = pd.read_csv('Emissions.csv')

totalProduction = pd.read_csv('AgricultureProduction.csv')

meatproduction = pd.read_csv('meatproduction.csv')

df = pd.read_csv('LandUse.csv')

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label='Summary', children=[
           html.Div(className='row',  # Define the row element
                               children=[
                                  html.Div(className='two columns div-user-controls',
                                  children = [
                                   
                                    html.H2('Climate Change On Agricultural Production'),
                                    html.H2(''),
                      

                                    html.Div(className='div-for-dropdown',
                                            children=[
                                              
                                                dcc.Dropdown(id='geo-dropdown', multi=True,
                                                options=[{'label': i, 'value': i}
                                                for i in temperaturechange['Area'].unique()],
                                                value=['USA','Brazil']),
                                                     ],
                                style={'color': '#1E1E1E'})
                                ]),  
                                # Define the left element
                                  
                                  html.Div(className='five columns div-for-charts bg-grey',
                                    children=[
                                        dcc.Graph(id='temperature-graph',
                                                config={'displayModeBar': False},
                                                ),
                                         dcc.Graph(id='production-graph',config={'displayModeBar': False}),
                                       
                                                    
                                    ]
                                  ),

                                   html.Div(className='five columns div-for-charts bg-grey',
                                    children=[
                                        dcc.Graph(id='emission-graph',
                                                config={'displayModeBar': False},
                                                ),
                                         dcc.Graph(id='meat-graph',
                                                config={'displayModeBar': False},
                                                ),
                                
                                       
                                                    
                                    ]
                                  ),
                        
                                  ])
        ]),
        dcc.Tab(label='Detail', children=[
          html.Div(className='row',  # Define the row element
                               children=[
                                  html.Div(className='two columns div-user-controls',
                                  children = [
                                    # html.Nav(className = "nav nav-pills", children =[
                                    #       html.A('App1', className="nav-item nav-link btn", href='/app1'),
                                    #         html.A('App2', className="nav-item nav-link active btn", href='app2.py') 
                                    # ]),
                                    html.H2('Agricultural Breakdown By Country'),
                                    html.H2(''),
                      

                                
                                    html.Div(className='div-for-dropdown',
                                            children=[
                                                # dcc.Dropdown(id='countryselector', value=['United States of America','China'], multi=True,
                                                # options=[{'label': x, 'value': x} for x in
                                                # temperaturechange['Area'].unique()]),
                                                dcc.Dropdown(id='country-dropdown', multi=False,
                                                options=[{'label': i, 'value': i}
                                                for i in df['Area'].unique()],
                                                value='Area'),
                                                     ],
                                style={'color': '#1E1E1E'})
                                    
                                
                                ]),  
                                # Define the left element
                                  
                                  html.Div(className='eight columns div-for-charts bg-grey',
                                    children=[
                                  
                                        dcc.Graph(id='item-graph'),
                                        dcc.Graph(id='gas-graph')
                                                                            
                                                    
                                    ]
                                  ),
                        
                                  ])
                                ])



        ]),
        # dcc.Tab(label='Tab three', children=[
          
        # ]),
    ])


@app.callback(
    Output(component_id='temperature-graph', component_property='figure'),
    Input(component_id='geo-dropdown', component_property='value'),
    
)

# callback function is dependent on the dropdown
def update_graph(selected_country):
    # filtered_temperature = temperaturechange[temperaturechange['Area'] == selected_country]
    filteredtemp = temperaturechange[temperaturechange.Area.isin(selected_country)]
    line_fig = px.line(filteredtemp,
                        x='Year', y='Celcius',
                        color='Area',
                        title=f'Change in Temperature Over Time (Celcius)')
    return line_fig

# AGRICULTURE VALUE
@app.callback(
    Output(component_id='production-graph', component_property='figure'),
    Input(component_id='geo-dropdown', component_property='value'),
    
)

# callback function is dependent on the dropdown
def update_graph(selected_country):
    filteredproduction = totalProduction[totalProduction.Area.isin(selected_country)]
    # filtered_production = totalProduction[totalProduction['Area'] == selected_country]
    line_fig2 = px.line(filteredproduction,
                        x='Year', y='Dollars',
                        color='Area',
                        title=f'Agricultural Production (USD Thousands)')
    return line_fig2

# EMISSIONS
@app.callback(
    Output(component_id='emission-graph', component_property='figure'),
    Input(component_id='geo-dropdown', component_property='value'),
    
)

# callback function is dependent on the dropdown
def update_graph(selected_country):
    # filtered_emissions = emissions[emissions['Area'] == selected_country]
    filteredemissions = emissions[emissions.Area.isin(selected_country)]
    line_fig3 = px.line(filteredemissions,
                        x='Year', y='Kilotonnes',
                        color='Area',
                        title=f'Greenhouse Gas Emissions (Kilotonnes)')
    return line_fig3

# Meat Production Value
@app.callback(
    Output(component_id='meat-graph', component_property='figure'),
    Input(component_id='geo-dropdown', component_property='value'),
    
)

# callback function is dependent on the dropdown
def update_graph(selected_country):
    # filtered_meat = meatproduction[meatproduction['Area'] == selected_country]
    filteredmeat = meatproduction[meatproduction.Area.isin(selected_country)]
    line_fig4 = px.line(filteredmeat,
                        x='Year', y='Dollars',
                        color='Area',
                        title=f'Meat Production Value (USD Thousands)')
    return line_fig4


######## SECOND TAB
# TEMPERATURE CHANGE
@app.callback(
    Output(component_id='item-graph', component_property='figure'),
    Input(component_id='country-dropdown', component_property='value'),
    
)

# callback function is dependent on the dropdown
def update_graph(selected_country):
    # filtered_temperature = temperaturechange[temperaturechange['Area'] == selected_country]
    item = df[df['Area'] == selected_country]
    item_fig = px.bar(item,
                        x='Year', y='Value',
                        color='Item',
                        title=f'Land Use Change Over Time')
    return item_fig

# EMISSIONS
@app.callback(
    Output(component_id='gas-graph', component_property='figure'),
    Input(component_id='country-dropdown', component_property='value'),
    
)

# callback function is dependent on the dropdown
def update_graph(selected_country):
    filtered_emissions = emissions[emissions['Area'] == selected_country]
    #filteredemissions = emissions[emissions.Area.isin(selected_country)]
    gas_fig = px.line(filtered_emissions,
                        x='Year', y='Kilotonnes',
                        color='Area',
                        title=f'Greenhouse Gas Emissions (Kilotonnes)')
    return gas_fig


if __name__ == '__main__':
    app.run_server(debug=False)
