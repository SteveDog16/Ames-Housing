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
            {'label': 'Building class', 'value': 'MSSubClass'},
            {'label': 'General zoning classification', 'value': 'MSZoning'},
            {'label': 'Type of alley access', 'value': 'Alley'},
            {'label': 'Flatness of the property', 'value': 'LandContour'},
            {'label': 'General shape of property', 'value': 'LotShape'},
            {'label': 'Lot configuration', 'value': 'LotConfig'},
            {'label': 'Neighborhood', 'value': 'Neighborhood'},
            {'label': 'Linear feet of street connected to property', 'value': 'LotFrontage'},
            {'label': 'Lot size (in square feet)', 'value': 'LotArea'},
        ],
        value=['MSSubClass'],
        multi=True,
        id='page-1-dropdown-item',
        style={
            'width': '300px',
            'font-family': 'Roboto, sans-serif'
        },
        # Use CSS styles to add spacing
        className='dropdown-with-spacing'
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
            {'label': 'Proximity to main road or railroad', 'value': 'Condition1'},
            {'label': 'Type of dwelling', 'value': 'BldgType'},
            {'label': 'Overall material and finish quality', 'value': 'OverallQual'},
            {'label': 'Overall condition rating', 'value': 'OverallCond'},
            {'label': 'Original construction date', 'value': 'YearBuilt'},
            {'label': 'Remodel date', 'value': 'YearRemodAdd'},
            {'label': 'Type of roof', 'value': 'RoofStyle'},
            {'label': 'Roof material', 'value': 'RoofMatl'},
            {'label': 'Exterior material quality', 'value': 'ExterQual'},
            {'label': 'Present condition of the material on the exterior', 'value': 'ExterCond'},
            {'label': 'Type of foundation', 'value': 'Foundation'}
        ],
        value=['Condition1'],
        multi=True,
        id='page-2-dropdown-item',
        style={'width': '300px', 'font-family': 'Roboto, sans-serif'}
    ),
    dcc.Graph(figure={}, id='page-2-frequency-graph'),
    dcc.Graph(figure={}, id='page-2-saleprice-graph'),
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
            {'label': 'Basement quality', 'value': 'BsmtQual'},
            {'label': 'Walkout/garden level basement walls', 'value': 'BsmtExposure'},
            {'label': 'Quality of basement finished area', 'value': 'BsmtFinType1'},
            {'label': 'Quality of second finished area (if present)', 'value': 'BsmtFinType2'},
            {'label': 'Type 1 finished (in square feet)', 'value': 'BsmtFinSF1'},
            {'label': 'Type 2 finished (in square feet)', 'value': 'BsmtFinSF2'},
            {'label': 'Unfinished basement area (in square feet)', 'value': 'BsmtUnfSF'},
            {'label': 'Total basement area (in square feet)', 'value': 'TotalBsmtSF'},
            {'label': 'Percentage of unfinished squre feet out of total basement area (in square feet)', 'value': 'UnfBsmtSFPercent'}
        ],
        value=['BsmtQual'],
        multi=True,
        id='page-3-dropdown-item',
        style={
            'width': '350px',
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
            {'label': 'Heating quality and condition', 'value': 'HeatingQC'},
            {'label': 'First floor (in square feet)', 'value': '1stFlrSF'},
            {'label': 'Second floor (in square feet)', 'value': '2ndFlrSF'},
            {'label': 'Above grade (ground) living area (in square feet)', 'value': 'GrLivArea'},
            {'label': 'Number of basement full bathrooms', 'value': 'BsmtFullBath'},
            {'label': 'Number of basement half bathrooms', 'value': 'BsmtHalfBath'},
            {'label': 'Number of full bathrooms above grade (ground)', 'value': 'FullBath'},
            {'label': 'Number of half baths above grade (ground)', 'value': 'HalfBath'},
            {'label': 'Kitchen quality', 'value': 'KitchenQual'},
            {'label': 'Total rooms above grade (does not include bathrooms)', 'value': 'TotRmsAbvGrd'},
            {'label': 'Number of fireplaces', 'value': 'Fireplaces'},
            {'label': 'Fireplace quality', 'value': 'FireplaceQu'}
        ],
        value=['HeatingQC'],
        multi=True,
        id='page-4-dropdown-item',
        style={
            'width': '350px',
            'font-family': 'Roboto, sans-serif'
        }
    ),
    dcc.Graph(figure={}, id='page-4-frequency-graph'),
    dcc.Graph(figure={}, id='page-4-saleprice-graph')
])


# Define the layout for the fifth page (page_5)
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
            {'label': 'Garage location', 'value': 'GarageType'},
            {'label': 'Year garage was built', 'value': 'GarageYrBlt'},
            {'label': 'Interior finish of the garage', 'value': 'GarageFinish'},
            {'label': 'Size of garage in car capacity', 'value': 'GarageCars'},
            {'label': 'Size of garage in square feet', 'value': 'GarageArea'},
            {'label': 'Garage quality', 'value': 'GarageQual'},
            {'label': 'Garage condition', 'value': 'GarageCond'}
        ],
        value=['GarageType'],
        multi=True,
        id='page-5-dropdown-item',
        style={
            'width': '300px',
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
            {'label': 'Wood deck area (in square feet)', 'value': 'WoodDeckSF'},
            {'label': 'Open porch area (in square feet)', 'value': 'OpenPorchSF'},
            {'label': 'Enclosed porch area (in square feet)', 'value': 'EnclosedPorch'},
            {'label': 'Three season porch area (in square feet)', 'value': '3SsnPorch'},
            {'label': 'Screen porch area (in square feet)', 'value': 'ScreenPorch'},
            {'label': 'Pool area (in square feet)', 'value': 'PoolArea'},
            {'label': 'Pool quality', 'value': 'PoolQC'},
            {'label': 'Fence quality', 'value': 'Fence'},
            {'label': 'Miscellaneous feature not covered in other categories', 'value': 'MiscFeature'},
            {'label': 'Value of miscellaneous feature', 'value': 'MiscVal'}
        ],
        value=['WoodDeckSF'],
        multi=True,
        id='page-6-dropdown-item',
        style={
            'width': '300px',
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
            {'label': 'Month sold', 'value': 'MoSold'},
            {'label': 'Year sold', 'value': 'YrSold'},
            {'label': 'Type of sale', 'value': 'SaleType'},
            {'label': 'Condition of sale', 'value': 'SaleCondition'}
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

    for col_chosen in selected_variables:
        if col_chosen in ['WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'MiscVal']:
            # For the selected variables, create bar graphs for frequency
            value_counts = df[col_chosen].value_counts()
            freq_fig.add_trace(go.Bar(x=value_counts.index, y=value_counts.values, name=f'Frequency of {col_chosen}'))

            # For the selected variables, create scatter plots for Sale Price
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
            if col_chosen == 'GarageArea':
                # Create a bar graph for frequency
                value_counts = df[col_chosen].value_counts()
                freq_fig.add_trace(go.Bar(x=value_counts.index, y=value_counts.values, name=f'Frequency of {col_chosen}'))
            else:
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

    freq_fig = go.Figure()
    sale_price_fig = go.Figure()

    # Define a custom color sequence for the variables
    color_sequence = ['rgb(31, 119, 180)', 'rgb(255, 127, 14)', 'rgb(44, 160, 44)', 'rgb(214, 39, 40)', 'rgb(148, 103, 189)']

    for i, col_chosen in enumerate(selected_variables):
        # Create histograms for all selected variables in the frequency graph
        if col_chosen in ['1stFlrSF', '2ndFlrSF', 'GrLivArea']:
            hist_fig = go.Histogram(x=df[col_chosen], name=f'Frequency of {col_chosen}', marker_color=color_sequence[i % len(color_sequence)])
            freq_fig.add_trace(hist_fig)
        else:
            value_counts = df[col_chosen].value_counts()
            freq_fig.add_trace(go.Bar(x=value_counts.index, y=value_counts.values, name=f'Frequency of {col_chosen}', marker_color=color_sequence[i % len(color_sequence)]))

        # Check if the variable is one of the specified scatter plot variables for the sale price graph
        if col_chosen in ['1stFlrSF', '2ndFlrSF', 'GrLivArea']:
            scatter_plot = go.Scatter(x=df[col_chosen], y=df['SalePrice'], mode='markers', name=f'{col_chosen} and Sale Price')
            scatter_plot.marker.color = color_sequence[i % len(color_sequence)]
            sale_price_fig.add_trace(scatter_plot)
        else:
            # For other variables in the sale price graph, create histograms
            hist_fig = go.Histogram(x=df[col_chosen], name=f'Sale Price vs. {col_chosen}', marker_color=color_sequence[i % len(color_sequence)])
            sale_price_fig.add_trace(hist_fig)

    freq_fig.update_layout(title="Frequency Graph")
    sale_price_fig.update_layout(title="Sale Price Graph")

    return freq_fig, sale_price_fig



@app.callback(
    [Output(component_id='page-3-frequency-graph', component_property='figure'),
     Output(component_id='page-3-saleprice-graph', component_property='figure')],
    [Input(component_id='page-3-dropdown-item', component_property='value')]
)
def update_page_3_graph(selected_variables):
    if not selected_variables:
        return {}, {}

    freq_fig = go.Figure()
    sale_price_fig = go.Figure()

    # Define a custom color sequence for the variables
    color_sequence = ['rgb(31, 119, 180)', 'rgb(255, 127, 14)', 'rgb(44, 160, 44)', 'rgb(214, 39, 40)', 'rgb(148, 103, 189)']

    for i, col_chosen in enumerate(selected_variables):
        # Create histograms for all selected variables in the frequency graph using Plotly Express
        hist_fig = px.histogram(df, x=col_chosen, title=f'Frequency of {col_chosen}')
        hist_fig.update_traces(marker_color=color_sequence[i % len(color_sequence)])  # Set distinct colors
        freq_fig.add_trace(hist_fig['data'][0])

        # Check if the variable is one of the specified scatter plot variables for the sale price graph
        if col_chosen in ['BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', 'UnfBsmtSFPercent']:
            scatter_plot = go.Scatter(x=df[col_chosen], y=df['SalePrice'], mode='markers', name=f'{col_chosen} and Sale Price')
            scatter_plot.marker.color = color_sequence[i % len(color_sequence)]  # Set distinct colors
            sale_price_fig.add_trace(scatter_plot)
        else:
            # For other variables in the sale price graph, create histograms
            hist_fig = px.histogram(df, x=col_chosen, title=f'Sale Price vs. {col_chosen}')
            hist_fig.update_traces(marker_color=color_sequence[i % len(color_sequence)])  # Set distinct colors
            sale_price_fig.add_trace(hist_fig['data'][0])

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
        if col_chosen in ['YearBuilt', 'YearRemodAdd']:
            # For 'YearBuilt' and 'YearRemodAdd', create line graphs for frequency
            value_counts = df[col_chosen].value_counts().sort_index()
            freq_fig.add_trace(go.Scatter(x=value_counts.index, y=value_counts.values, mode='lines+markers', name=f'Frequency of {col_chosen}'))

            # Create a line graph for sale price
            sale_price_line = df.groupby(col_chosen)['SalePrice'].median().reset_index().sort_values(by=col_chosen)
            sale_price_fig.add_trace(go.Scatter(x=sale_price_line[col_chosen], y=sale_price_line['SalePrice'], mode='lines+markers', name=f'{col_chosen} and Sale Price'))
        else:
            # For other variables, create bar graphs for frequency
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
            # For 'LotFrontage' and 'LotArea', create histoplots for frequency
            if col_chosen == 'LotFrontage':
                hist_fig = px.histogram(df, x=col_chosen, title=f'{col_chosen} Frequency')
            elif col_chosen == 'LotArea':
                hist_fig = px.histogram(df, x=col_chosen, title=f'{col_chosen} Frequency')

            freq_fig.add_trace(hist_fig['data'][0])  # Add the histogram trace to the figure

            # Create scatter plots for sale price
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
