# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

# Incorporate data
df = pd.read_csv('train.csv')

# Add new column
new_column_data = df['BsmtUnfSF'] / df['TotalBsmtSF'] * 100
df['UnfBsmtSFPercent'] = new_column_data

# Initialize the app
app = Dash(__name__)

# Update the columns you want to display in Page 1
page_1_columns = ['MSSubClass', 'MSZoning', 'Alley', 'LandContour', 'LotShape', 'LotConfig', 'Neighborhood', 'LotFrontage', 'LotArea']
scatter_variables_page_1 = ['LotFrontage', 'LotArea']  # Variables for scatter plots in Page 1

# Create a separate dropdown for Page 1 scatter plot variables
page_1_scatter_dropdown_items = [
    {'label': col, 'value': col}
    for col in scatter_variables_page_1
]

# Define the layout for the first page (page_1)
page_1_layout = html.Div([
    html.Div(
        children='Property Analysis',
        style={
            'font-size': '24px',
            'font-weight': 'bold',
            'text-align': 'center',
            'font-family': 'Roboto, sans-serif',
            'padding': '20px 0'
        }
    ),
    html.Hr(),
    dcc.Dropdown(
        options=[
            {'label': col, 'value': col}
            for col in page_1_columns
        ],
        value=['MSSubClass'],
        multi=True,
        id='page-1-dropdown-item',
        style={
            'width': '200px',
            'font-family': 'Roboto, sans-serif'
        }
    ),
    dcc.Graph(figure={}, id='page-1-frequency-graph'),
    dcc.Graph(figure={}, id='page-1-saleprice-graph'),
])


# Define the layout for the second page (page_2)
page_2_layout = html.Div([
    html.Div(
        children='Building Analysis',
        style={
            'font-size': '24px',
            'font-weight': 'bold',
            'text-align': 'center',
            'font-family': 'Roboto, sans-serif',
            'padding': '20px 0'
        }
    ),
    html.Hr(),
    dcc.Dropdown(
        options=[
            {'label': 'Condition1', 'value': 'Condition1'},
            {'label': 'BldgType', 'value': 'BldgType'},
            {'label': 'OverallQual', 'value': 'OverallQual'},
            {'label': 'OverallCond', 'value': 'OverallCond'},
            {'label': 'YearBuilt', 'value': 'YearBuilt'},
            {'label': 'YearRemodAdd', 'value': 'YearRemodAdd'},
            {'label': 'RoofStyle', 'value': 'RoofStyle'},
            {'label': 'RoofMatl', 'value': 'RoofMatl'},
            {'label': 'ExterQual', 'value': 'ExterQual'},
            {'label': 'ExterCond', 'value': 'ExterCond'},
            {'label': 'Foundation', 'value': 'Foundation'}
        ],
        value=['Condition1'],
        multi=True,
        id='page-2-dropdown-item',
        style={'width': '200px', 'font-family': 'Roboto, sans-serif'}
    ),
    dcc.Graph(figure={}, id='page-2-frequency-graph'),
    dcc.Graph(figure={}, id='page-2-saleprice-graph')
])


# Define the layout for the third page (page_3)
page_3_layout = html.Div([
    html.Div([
        html.Div(
            children='Basement Analysis',
            style={
                'font-size': '24px',
                'font-weight': 'bold',
                'text-align': 'center',
                'font-family': 'Roboto, sans-serif',
                'padding': '20px 0'
            }
        ),
        html.Hr(),
    ]),

    dcc.Dropdown(
        options=[
            {'label': 'BsmtQual', 'value': 'BsmtQual'},
            {'label': 'BsmtExposure', 'value': 'BsmtExposure'},
            {'label': 'BsmtFinType1', 'value': 'BsmtFinType1'},
            {'label': 'BsmtFinType2', 'value': 'BsmtFinType2'},
            {'label': 'BsmtFinSF1', 'value': 'BsmtFinSF1'},
            {'label': 'BsmtFinSF2', 'value': 'BsmtFinSF2'},
            {'label': 'BsmtUnfSF', 'value': 'BsmtUnfSF'},
            {'label': 'TotalBsmtSF', 'value': 'TotalBsmtSF'},
            {'label': 'UnfBsmtSFPercent', 'value': 'UnfBsmtSFPercent'}
        ],
        value=['BsmtQual'],
        multi=True,
        id='page-3-dropdown-item',
        style={
            'width': '200px',
            'font-family': 'Roboto, sans-serif'
        }
    ),
    dcc.Graph(figure={}, id='page-3-frequency-graph'),
    dcc.Graph(figure={}, id='page-3-saleprice-graph')
])

page_4_layout = html.Div([
    html.Div([
        html.Div(
            children='Interior Analysis',
            style={
                'font-size': '24px',
                'font-weight': 'bold',
                'text-align': 'center',
                'font-family': 'Roboto, sans-serif',
                'padding': '20px 0'
            }
        ),
        html.Hr(),
    ]),

    dcc.Dropdown(
        options=[
            {'label': 'HeatingQC', 'value': 'HeatingQC'},
            {'label': '1stFlrSF', 'value': '1stFlrSF'},
            {'label': '2ndFlrSF', 'value': '2ndFlrSF'},
            {'label': 'GrLivArea', 'value': 'GrLivArea'},
            {'label': 'BsmtFullBath', 'value': 'BsmtFullBath'},
            {'label': 'BsmtHalfBath', 'value': 'BsmtHalfBath'},
            {'label': 'FullBath', 'value': 'FullBath'},
            {'label': 'HalfBath', 'value': 'HalfBath'},
            {'label': 'KitchenQual', 'value': 'KitchenQual'},
            {'label': 'TotRmsAbvGrd', 'value': 'TotRmsAbvGrd'},
            {'label': 'Fireplaces', 'value': 'Fireplaces'},
            {'label': 'FireplaceQu', 'value': 'FireplaceQu'}
        ],
        value=['HeatingQC'],
        multi=True,
        id='page-4-dropdown-item',
        style={
            'width': '200px',
            'font-family': 'Roboto, sans-serif'
        }
    ),
    dcc.Graph(figure={}, id='page-4-frequency-graph'),
    dcc.Graph(figure={}, id='page-4-saleprice-graph')
])


# Define the layout for the fifth page (page_5)
page_5_layout = html.Div([
    html.Div([
        html.Div(
            children='Garage Analysis',
            style={
                'font-size': '24px',
                'font-weight': 'bold',
                'text-align': 'center',
                'font-family': 'Roboto, sans-serif',
                'padding': '20px 0'
            }
        ),
        html.Hr(),
    ]),

    dcc.Dropdown(
        options=[
            {'label': 'GarageType', 'value': 'GarageType'},
            {'label': 'GarageYrBlt', 'value': 'GarageYrBlt'},
            {'label': 'GarageFinish', 'value': 'GarageFinish'},
            {'label': 'GarageCars', 'value': 'GarageCars'},
            {'label': 'GarageArea', 'value': 'GarageArea'},
            {'label': 'GarageQual', 'value': 'GarageQual'},
            {'label': 'GarageCond', 'value': 'GarageCond'}
        ],
        value=['GarageType'],
        multi=True,
        id='page-5-dropdown-item',
        style={
            'width': '200px',
            'font-family': 'Roboto, sans-serif'
        }
    ),
    dcc.Graph(figure={}, id='page-5-frequency-graph'),
    dcc.Graph(figure={}, id='page-5-saleprice-graph')
])


# Define the layout for the sixth page (page_6)
page_6_layout = html.Div([
    html.Div([
        html.Div(
            children='Exterior Analysis',
            style={
                'font-size': '24px',
                'font-weight': 'bold',
                'text-align': 'center',
                'font-family': 'Roboto, sans-serif',
                'padding': '20px 0'
            }
        ),
        html.Hr(),
    ]),

    dcc.Dropdown(
        options=[
            {'label': 'WoodDeckSF', 'value': 'WoodDeckSF'},
            {'label': 'OpenPorchSF', 'value': 'OpenPorchSF'},
            {'label': 'EnclosedPorch', 'value': 'EnclosedPorch'},
            {'label': '3SsnPorch', 'value': '3SsnPorch'},
            {'label': 'ScreenPorch', 'value': 'ScreenPorch'},
            {'label': 'PoolArea', 'value': 'PoolArea'},
            {'label': 'PoolQC', 'value': 'PoolQC'},
            {'label': 'Fence', 'value': 'Fence'},
            {'label': 'MiscFeature', 'value': 'MiscFeature'},
            {'label': 'MiscVal', 'value': 'MiscVal'}
        ],
        value=['WoodDeckSF'],
        multi=True,
        id='page-6-dropdown-item',
        style={
            'width': '200px',
            'font-family': 'Roboto, sans-serif'
        }
    ),
    dcc.Graph(figure={}, id='page-6-frequency-graph'),
    dcc.Graph(figure={}, id='page-6-saleprice-graph')
])

# Define the layout for the seventh page (page_7)
page_7_layout = html.Div([
    html.Div([
        html.Div(
            children='Sale Analysis',
            style={
                'font-size': '24px',
                'font-weight': 'bold',
                'text-align': 'center',
                'font-family': 'Roboto, sans-serif',
                'padding': '20px 0'
            }
        ),
        html.Hr(),
    ]),

    dcc.Dropdown(
        options=[
            {'label': 'MoSold', 'value': 'MoSold'},
            {'label': 'YrSold', 'value': 'YrSold'},
            {'label': 'SaleType', 'value': 'SaleType'},
            {'label': 'SaleCondition', 'value': 'SaleCondition'}
        ],
        value=['MoSold'],
        multi=True,
        id='page-7-dropdown-item',
        style={
            'width': '200px',
            'font-family': 'Roboto, sans-serif'
        }
    ),
    dcc.Graph(figure={}, id='page-7-frequency-graph'),
    dcc.Graph(figure={}, id='page-7-saleprice-graph')
])

	# Create a main title above the tabs
main_title_layout = html.Div(
    children='Ames Housing Price Analysis Dashboard',
    style={
        'font-size': '36px',
        'font-weight': 'bold',
        'text-align': 'center',
        'font-family': 'Roboto, sans-serif',
        'padding-top': '20px',  # Adjust the top padding as needed
        'padding-bottom': '20px',
    }
)

# Define the Tabs component to switch between pages
app.layout = html.Div([
    main_title_layout,
    html.Link(
        rel="stylesheet",
        href="https://fonts.googleapis.com/css?family=Roboto",
    ),
    dcc.Tabs([
        dcc.Tab(label='Property Analysis', value='page-1', children=page_1_layout, style={'font-family': 'Roboto, sans-serif'}),
        dcc.Tab(label='Building Analysis', value='page-2', children=page_2_layout, style={'font-family': 'Roboto, sans-serif'}),
        dcc.Tab(label='Basement Analysis', value='page-3', children=page_3_layout, style={'font-family': 'Roboto, sans-serif'}),
        dcc.Tab(label='Interior Analysis', value='page-4', children=page_4_layout, style={'font-family': 'Roboto, sans-serif'}),
        dcc.Tab(label='Garage Analysis', value='page-5', children=page_5_layout, style={'font-family': 'Roboto, sans-serif'}),
        dcc.Tab(label='Exterior Analysis', value='page-6', children=page_6_layout, style={'font-family': 'Roboto, sans-serif'}),
        dcc.Tab(label='Sale Analysis', value='page-7', children=page_7_layout, style={'font-family': 'Roboto, sans-serif'}),
    ],
    style={'font-family': 'Roboto, sans-serif'}  
    ),
])

# Define the callback for Page 7
@app.callback(
    [Output(component_id='page-7-frequency-graph', component_property='figure'),
     Output(component_id='page-7-saleprice-graph', component_property='figure')],
    [Input(component_id='page-7-dropdown-item', component_property='value')]
)
def update_page_7_graph(selected_variables):
    if not selected_variables:
        return {}, {}

    # Create an empty figure for frequency and sale price graphs
    freq_fig = go.Figure()
    sale_price_fig = go.Figure()

    # Lists to store the selected variables for which scatter plots should be displayed
    scatter_variables = []  # Update this list with any specific scatter variables you want for page 7

    for col_chosen in selected_variables:
        if col_chosen in scatter_variables:
            # For selected scatter variables, create scatter plots
            value_counts = df[col_chosen].value_counts()
            freq_fig.add_trace(go.Scatter(x=value_counts.index, y=value_counts.values, mode='markers', name=f'Frequency of {col_chosen}'))
            sale_price_fig.add_trace(go.Scatter(x=df[col_chosen], y=df['SalePrice'], mode='markers', name=f'{col_chosen} and Sale Price'))
        else:
            # For other variables, create bar graphs for frequency
            value_counts = df[col_chosen].value_counts()
            freq_fig.add_trace(go.Bar(x=value_counts.index, y=value_counts.values, name=f'Frequency of {col_chosen}'))
            avg_values = df.groupby(col_chosen)['SalePrice'].mean().reset_index()
            sale_price_fig.add_trace(go.Bar(x=avg_values[col_chosen], y=avg_values['SalePrice'], name=f'{col_chosen} and Sale Price'))

    freq_fig.update_layout(title="Frequency Graph")
    sale_price_fig.update_layout(title="Sale Price Graph")

    return freq_fig, sale_price_fig

# Correct the callback for Page 6
@app.callback(
    [Output(component_id='page-6-frequency-graph', component_property='figure'),
     Output(component_id='page-6-saleprice-graph', component_property='figure')],
    [Input(component_id='page-6-dropdown-item', component_property='value')]
)
def update_page_6_graph(selected_variables):
    if not selected_variables:
        return {}, {}

    # Create an empty figure for frequency and sale price graphs
    freq_fig = go.Figure()
    sale_price_fig = go.Figure()

    # Lists to store the selected variables for which scatter plots should be displayed
    scatter_variables = ['WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'MiscVal']

    for col_chosen in selected_variables:
        if col_chosen in scatter_variables:
            # For selected scatter variables, create scatter plots
            value_counts = df[col_chosen].value_counts()
            freq_fig.add_trace(go.Scatter(x=value_counts.index, y=value_counts.values, mode='markers', name=f'Frequency of {col_chosen}'))
            sale_price_fig.add_trace(go.Scatter(x=df[col_chosen], y=df['SalePrice'], mode='markers', name=f'{col_chosen} and Sale Price'))
        else:
            # For other variables, create bar graphs for frequency
            value_counts = df[col_chosen].value_counts()
            freq_fig.add_trace(go.Bar(x=value_counts.index, y=value_counts.values, name=f'Frequency of {col_chosen}'))
            avg_values = df.groupby(col_chosen)['SalePrice'].mean().reset_index()
            sale_price_fig.add_trace(go.Bar(x=avg_values[col_chosen], y=avg_values['SalePrice'], name=f'{col_chosen} and Sale Price'))

    freq_fig.update_layout(title="Frequency Graph")
    sale_price_fig.update_layout(title="Sale Price Graph")

    return freq_fig, sale_price_fig


@app.callback(
    [Output(component_id='page-5-frequency-graph', component_property='figure'),
     Output(component_id='page-5-saleprice-graph', component_property='figure')],
    [Input(component_id='page-5-dropdown-item', component_property='value')]
)
def update_page_5_graph(selected_variables):
    if not selected_variables:
        return {}, {}

    # Create an empty figure for frequency and sale price graphs
    freq_fig = go.Figure()
    sale_price_fig = go.Figure()

    # Lists to store the selected variables for which scatter plots should be displayed
    scatter_variables = ['GarageYrBlt', 'GarageArea']

    for col_chosen in selected_variables:
        if col_chosen in scatter_variables:
            # For selected scatter variables, create scatter plots
            value_counts = df[col_chosen].value_counts()
            freq_fig.add_trace(go.Scatter(x=value_counts.index, y=value_counts.values, mode='markers', name=f'Frequency of {col_chosen}'))
            sale_price_fig.add_trace(go.Scatter(x=df[col_chosen], y=df['SalePrice'], mode='markers', name=f'{col_chosen} and Sale Price'))
        else:
            # For other variables, create bar graphs for frequency
            value_counts = df[col_chosen].value_counts()
            freq_fig.add_trace(go.Bar(x=value_counts.index, y=value_counts.values, name=f'Frequency of {col_chosen}'))
            avg_values = df.groupby(col_chosen)['SalePrice'].mean().reset_index()
            sale_price_fig.add_trace(go.Bar(x=avg_values[col_chosen], y=avg_values['SalePrice'], name=f'{col_chosen} and Sale Price'))

    freq_fig.update_layout(title="Frequency Graph")
    sale_price_fig.update_layout(title="Sale Price Graph")

    return freq_fig, sale_price_fig

@app.callback(
    [Output(component_id='page-4-frequency-graph', component_property='figure'),
     Output(component_id='page-4-saleprice-graph', component_property='figure')],
    [Input(component_id='page-4-dropdown-item', component_property='value')]
)
def update_page_4_graph(selected_variables):
    if not selected_variables:
        return {}, {}

    # Create an empty figure for frequency and sale price graphs
    freq_fig = go.Figure()
    sale_price_fig = go.Figure()

    # Lists to store the selected variables for which scatter plots should be displayed
    scatter_variables = ['1stFlrSF', '2ndFlrSF', 'GrLivArea']

    for col_chosen in selected_variables:
        if col_chosen in scatter_variables:
            # For selected scatter variables, create scatter plots
            value_counts = df[col_chosen].value_counts()
            freq_fig.add_trace(go.Scatter(x=value_counts.index, y=value_counts.values, mode='markers', name=f'Frequency of {col_chosen}'))
            sale_price_fig.add_trace(go.Scatter(x=df[col_chosen], y=df['SalePrice'], mode='markers', name=f'{col_chosen} and Sale Price'))
        else:
            # For other variables, create bar graphs for frequency
            value_counts = df[col_chosen].value_counts()
            freq_fig.add_trace(go.Bar(x=value_counts.index, y=value_counts.values, name=f'Frequency of {col_chosen}'))
            avg_values = df.groupby(col_chosen)['SalePrice'].mean().reset_index()
            sale_price_fig.add_trace(go.Bar(x=avg_values[col_chosen], y=avg_values['SalePrice'], name=f'{col_chosen} and Sale Price'))

    freq_fig.update_layout(title="Frequency Graph")
    sale_price_fig.update_layout(title="Sale Price Graph")

    return freq_fig, sale_price_fig



# Update the callback for Page 3
@app.callback(
    [Output(component_id='page-3-frequency-graph', component_property='figure'),
     Output(component_id='page-3-saleprice-graph', component_property='figure')],
    [Input(component_id='page-3-dropdown-item', component_property='value')]
)
def update_page_3_graph(selected_variables):
    if not selected_variables:
        return {}, {}

    # Create an empty figure for frequency and sale price graphs
    freq_fig = go.Figure()
    sale_price_fig = go.Figure()

    # Lists to store the selected variables for which scatter plots should be displayed
    scatter_variables = ['BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', 'UnfBsmtSFPercent']

    for col_chosen in selected_variables:
        if col_chosen in scatter_variables:
            # For selected scatter variables, create scatter plots
            value_counts = df[col_chosen].value_counts()
            freq_fig.add_trace(go.Scatter(x=value_counts.index, y=value_counts.values, mode='markers', name=f'Frequency of {col_chosen}'))
            sale_price_fig.add_trace(go.Scatter(x=df[col_chosen], y=df['SalePrice'], mode='markers', name=f'{col_chosen} and Sale Price'))
        else:
            # For other variables, create bar graphs for frequency
            value_counts = df[col_chosen].value_counts()
            freq_fig.add_trace(go.Bar(x=value_counts.index, y=value_counts.values, name=f'Frequency of {col_chosen}'))
            avg_values = df.groupby(col_chosen)['SalePrice'].mean().reset_index()
            sale_price_fig.add_trace(go.Bar(x=avg_values[col_chosen], y=avg_values['SalePrice'], name=f'{col_chosen} and Sale Price'))

    freq_fig.update_layout(title="Frequency Graph")
    sale_price_fig.update_layout(title="Sale Price Graph")

    return freq_fig, sale_price_fig

# Update the callback for Page 2
@app.callback(
    [Output(component_id='page-2-frequency-graph', component_property='figure'),
     Output(component_id='page-2-saleprice-graph', component_property='figure')],
    [Input(component_id='page-2-dropdown-item', component_property='value')]
)
def update_page_2_graph(selected_variables):
    if not selected_variables:
        selected_variables = []

    # Create an empty figure for frequency and sale price graphs
    freq_fig = go.Figure()
    sale_price_fig = go.Figure()

    for col_chosen in selected_variables:
        # For selected variables, create bar graphs for frequency
        value_counts = df[col_chosen].value_counts()
        freq_fig.add_trace(go.Bar(x=value_counts.index, y=value_counts.values, name=f'Frequency of {col_chosen}'))
        avg_values = df.groupby(col_chosen)['SalePrice'].mean().reset_index()
        sale_price_fig.add_trace(go.Bar(x=avg_values[col_chosen], y=avg_values['SalePrice'], name=f'{col_chosen} and Sale Price'))

    freq_fig.update_layout(title="Frequency Graph")
    sale_price_fig.update_layout(title="Sale Price Graph")

    return freq_fig, sale_price_fig




# Define the callback for Page 1
@app.callback(
    [Output(component_id='page-1-frequency-graph', component_property='figure'),
     Output(component_id='page-1-saleprice-graph', component_property='figure')],
    [Input(component_id='page-1-dropdown-item', component_property='value')]
)
def update_page_1_graph(selected_variables):
    if not selected_variables:
        selected_variables = []

    # Create empty figures for frequency and sale price
    freq_fig = go.Figure()
    sale_price_fig = go.Figure()

    for col_chosen in selected_variables:
        if col_chosen in ['LotFrontage', 'LotArea']:
            # For 'LotFrontage' and 'LotArea', create scatter plots
            scatter_plot = go.Scatter(x=df[col_chosen], y=df['SalePrice'], mode='markers', name=f'{col_chosen} and Sale Price')
            sale_price_fig.add_trace(scatter_plot)
        else:
            # For other selected variables, create bar graphs for frequency
            value_counts = df[col_chosen].value_counts()
            freq_fig.add_trace(go.Bar(x=value_counts.index, y=value_counts.values, name=f'Frequency of {col_chosen}'))
            avg_values = df.groupby(col_chosen)['SalePrice'].mean().reset_index()
            sale_price_fig.add_trace(go.Bar(x=avg_values[col_chosen], y=avg_values['SalePrice'], name=f'{col_chosen} and Sale Price'))

    freq_fig.update_layout(title="Frequency Graph")
    sale_price_fig.update_layout(title="Sale Price Graph")

    return freq_fig, sale_price_fig



# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
