from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

# Create a Dash instance
app = Dash(__name__, suppress_callback_exceptions=True)

# Read the data from 'train.csv'
df = pd.read_csv('train.csv')

# Define the number of variables per page
variables_per_page = 3  # Adjust this as needed

# Split the variable options into pages
variable_options = df.columns
variable_pages = [variable_options[i:i + variables_per_page] for i in range(0, len(variable_options), variables_per_page)]

# Define the neighborhood_labels in the global scope
neighborhood_labels = {
    'NAmes': 'North Ames',
    'CollgCr': 'College Creek',
    'Crawfor': 'Crawford',
    'NoRidge': "Northridge Heights",
    'Mitchel': 'Mitchell',
    'Somerst': 'Somerset',
    'NWAmes': 'Northwest Ames',
    'OldTown': 'Old Town',
    'BrkSide': 'Brookside',
    'SawyerW': 'Sawyer West',
    'NridgHt': 'Northridge Heights',
    'IDOTRR': 'Iowa Department of Transportation Railroad',
    'MeadowV': 'Meadow Village',
    'StoneBr': 'Stone Brooke',
    'ClearCr': 'Clear Creek',
    'NPkVill': 'Northpark Village',
    'Blmngtn': 'Bloomington Heights',
    'BrDale': 'Briardale',
    'SWISU': 'Southwest of the Iowa State University (ISU) campus',
    'Blueste': 'Bluestem'
    # Add more neighborhood labels here
}

# Define the layout for each page with specific variables
page1_variables = [
    {'label': 'Building class', 'value': 'MSSubClass'},
    {'label': 'General zoning classification', 'value': 'MSZoning'},
    {'label': 'Flatness of the property', 'value': 'LandContour'},
    {'label': 'General shape of property', 'value': 'LotShape'},
    {'label': 'Lot configuration', 'value': 'LotConfig'},
    {'label': 'Linear feet of street connected to property', 'value': 'LotFrontage'}]

page2_variables = [
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
]

page3_variables = [
    {'label': 'Basement quality', 'value': 'BsmtQual'},
    {'label': 'Walkout/garden level basement walls', 'value': 'BsmtExposure'},
    {'label': 'Quality of basement finished area', 'value': 'BsmtFinType1'},
    {'label': 'Quality of second finished area (if present)', 'value': 'BsmtFinType2'},
    {'label': 'Type 1 finished (in square feet)', 'value': 'BsmtFinSF1'},
    {'label': 'Type 2 finished (in square feet)', 'value': 'BsmtFinSF2'},
    {'label': 'Unfinished basement area (in square feet)', 'value': 'BsmtUnfSF'},
    {'label': 'Total basement area (in square feet)', 'value': 'TotalBsmtSF'}
]

page4_variables = [
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
]

page5_variables = [
    {'label': 'Garage location', 'value': 'GarageType'},
    {'label': 'Year garage was built', 'value': 'GarageYrBlt'},
    {'label': 'Interior finish of the garage', 'value': 'GarageFinish'},
    {'label': 'Size of garage in car capacity', 'value': 'GarageCars'},
    {'label': 'Size of garage in square feet', 'value': 'GarageArea'},
    {'label': 'Garage quality', 'value': 'GarageQual'},
    {'label': 'Garage condition', 'value': 'GarageCond'}
]

page6_variables = [
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
]

page7_variables = [
    {'label': 'Month sold', 'value': 'MoSold'},
    {'label': 'Year sold', 'value': 'YrSold'},
    {'label': 'Type of sale', 'value': 'SaleType'},
    {'label': 'Condition of sale', 'value': 'SaleCondition'}
]

# Define the layout for each page
page_variables = [
    page1_variables,
    page2_variables,
    page3_variables,
    page4_variables,
    page5_variables,
    page6_variables,
    page7_variables
]


# Modify the create_page_layout function to accept the page number
def create_page_layout(page_number):
    variables_on_page = page_variables[page_number]

    # Define a dictionary for custom labels
    neighborhood_labels = {
        'NAmes': 'North Ames',
        'CollgCr': 'College Creek',
        'Crawfor': 'Crawford',
        'NoRidge': "Northridge Heights",
        'Mitchel': 'Mitchell',
        'Somerst': 'Somerset',
        'NWAmes': 'Northwest Ames',
        'OldTown': 'Old Town',
        'BrkSide': 'Brookside',
        'SawyerW': 'Sawyer West',
        'NridgHt': 'Northridge Heights',
        'IDOTRR': 'Iowa Department of Transportation Railroad',
        'MeadowV': 'Meadow Village',
        'StoneBr': 'Stone Brooke',
        'ClearCr': 'Clear Creek',
        'NPkVill': 'Northpark Village',
        'Blmngtn': 'Bloomington Heights',
        'BrDale': 'Briardale',
        'SWISU': 'Southwest of the Iowa State University (ISU) campus',
        'Blueste': 'Bluestem'
        # Add more neighborhood labels here
    }

    # Create the neighborhood dropdown options using the custom labels
    neighborhood_options = [{'label': neighborhood_labels.get(neighborhood, neighborhood), 'value': neighborhood}
                            for neighborhood in df['Neighborhood'].unique()]
    return html.Div(children=[
        dcc.Dropdown(
            id='neighborhood-dropdown',
            options=neighborhood_options,
            multi=True,
            value=df['Neighborhood'].unique()[:3],
            style={'width': '300px', 'margin-top': '20px'}  # Add margin-top for spacing
        ),

        dcc.Dropdown(
            id='x-axis-variable',
            options=[{'label': var['label'], 'value': var['value']} for var in variables_on_page],
            value=variables_on_page[0]['value'],
            style={'margin-top': '15px', 'width': '400px'}
        ),

        dcc.Graph(id='example-graph'),
        dcc.Graph(id='sale-price-graph')
    ], style={'font-family': 'Roboto, sans-serif'})


# Create a list of tab labels and values for the pages
tab_labels = [
    "Property Analysis",
    "Building Analysis",
    "Basement Analysis",
    'Interior Analysis',
    "Garage Analysis",
    "Exterior Analysis",
    "Sale Analysis"
]
# Combine the tabs and page content
app.layout = html.Div([
    html.H1(children='Ames House Price Dashboard', style={'font-family': 'Roboto, sans-serif', 'text-align': 'center'}),
    
    dcc.Tabs(
        id='tabs',
        value='0',
        children=[dcc.Tab(label=label, value=str(i)) for i, label in enumerate(tab_labels)],
        style={'font-family': 'Roboto, sans-serif'}  # Set the font style for tabs
    ),
    html.Div(id='page-content')
])

# Callback to update the displayed page
@app.callback(Output('page-content', 'children'), Input('tabs', 'value'))
def display_page(tab_value):
    tab_value = int(tab_value)
    if 0 <= tab_value < len(tab_labels):
        return create_page_layout(tab_value)
    else:
        return html.Div(children=["Page not found"])
    
# Variable descriptions
variable_descriptions = {
    'MSSubClass': 'Building Class',
    'MSZoning': 'General Zoning Classification',
    'LandContour': 'Flatness of the Property',
    'LotShape': 'General Shape of Property',
    'LotConfig': 'Lot Configuration',
    'LotFrontage': 'Linear Feet of Street Connected to Property',

    'Condition1': 'Proximity to Main Road or Railroad',
    'BldgType': 'Type of Dwelling',
    'OverallQual': 'Overall Material and Finish Quality',
    'OverallCond': 'Overall Condition Rating',

    'YearBuilt': 'Original Construction Date',
    'YearRemodAdd': 'Remodel Date',
    'RoofStyle': 'Type of Roof',
    'RoofMatl': 'Roof Material',
    'ExterQual': 'Exterior Material Quality',
    'ExterCond': 'Present Condition of the Material on the Exterior',
    'Foundation': 'Type of Foundation',

    'BsmtQual': 'Basement Quality',
    'BsmtExposure': 'Walkout/Garden Level Basement Walls',
    'BsmtFinType1': 'Quality of Basement Finished Area',
    'BsmtFinType2': 'Quality of Second Finished Area (If Present)',
    'BsmtFinSF1': 'Type 1 Finished (in Square Feet)',
    'BsmtFinSF2': 'Type 2 Finished (in Square Feet)',
    'BsmtUnfSF': 'Unfinished Basement Area (in Square Feet)',
    'TotalBsmtSF': 'Total Basement Area (in Square Feet)',

    'HeatingQC': 'Heating Quality and Condition',
    '1stFlrSF': 'First Floor (in Square Feet)',
    '2ndFlrSF': 'Second Floor (in Square Feet)',
    'GrLivArea': 'Above Grade (Ground) Living Area (in Square Feet)',
    'BsmtFullBath': 'Number of Basement Full Bathrooms',
    'BsmtHalfBath': 'Number of Basement Half Bathrooms',
    'FullBath': 'Number of Full Bathrooms Above Grade (Ground)',
    'HalfBath': 'Number of Half Baths Above Grade (Ground)',
    'KitchenQual': 'Kitchen Quality',
    'TotRmsAbvGrd': 'Total Rooms Above Grade (Does Not Include Bathrooms)',
    'Fireplaces': 'Number of Fireplaces',
    'FireplaceQu': 'Fireplace Quality',

    'GarageType': 'Garage Location',
    'GarageYrBlt': 'Year Garage Was Built',
    'GarageFinish': 'Interior Finish of the Garage',
    'GarageCars': 'Size of Garage in Car Capacity',
    'GarageArea': 'Size of Garage in Square Feet',
    'GarageQual': 'Garage Quality',
    'GarageCond': 'Garage Condition',

    'WoodDeckSF': 'Wood Deck Area (in Square Feet)',
    'OpenPorchSF': 'Open Porch Area (in Square Feet)',
    'EnclosedPorch': 'Enclosed Porch Area (in Square Feet)',
    '3SsnPorch': 'Three Season Porch Area (in Square Feet)',
    'ScreenPorch': 'Screen Porch Area (in Square Feet)',
    'PoolArea': 'Pool Area (in Square Feet)',
    'PoolQC': 'Pool Quality',
    'Fence': 'Fence Quality',
    'MiscFeature': 'Miscellaneous Feature Not Covered in Other Categories',
    'MiscVal': 'Value of Miscellaneous Feature',

    'MoSold': 'Month Sold',
    'YrSold': 'Year Sold',
    'SaleType': 'Type of Sale',
    'SaleCondition': 'Condition of Sale'
}


custom_descriptions_df = pd.DataFrame({
    'Variable': ['Neighborhood', 'YearBuilt', 'YearRemodAdd', 'Frequency'],
    'Description': ['Neighborhood Name', 'Year Built Description', 'Year Remodel Description', 'Frequency']
})

neighborhood_label = neighborhood_labels.get('Neighborhood', 'Neighborhood')


# Define a callback for updating the graph
@app.callback(
    Output('example-graph', 'figure'),
    Output('sale-price-graph', 'figure'),
    Input('neighborhood-dropdown', 'value'),
    Input('x-axis-variable', 'value')
)

def update_graph(selected_neighborhoods, x_axis_variable):
    filtered_df = df[df['Neighborhood'].isin(selected_neighborhoods) & df['SalePrice'].notnull()]

    # Define fig with a default value
    fig = None
    sale_price_fig = None

    if x_axis_variable in variable_descriptions:
        # Get the description for the current variable
        x_variable_description = variable_descriptions[x_axis_variable]

        # Update the hover data to include the custom descriptions
        hover_data = ['Neighborhood', x_axis_variable, 'Frequency']
        custom_descriptions = {
            x_axis_variable: x_variable_description,
            'Neighborhood': 'Neighborhood Name',
            'Frequency': 'Frequency',
        }
        # Update the hover text using custom descriptions
        for key, value in custom_descriptions.items():
            hover_data[hover_data.index(key)] = value


    x_label = variable_descriptions.get(x_axis_variable, x_axis_variable)
    y_label = "Frequency"  # Default y-label

    # Custom descriptions for "Year Built" and "Year Remodel Description"
    custom_descriptions = {
        'YearBuilt': 'Year Built',
        'YearRemodAdd': 'Year Remodel'
    }

    if x_axis_variable in custom_descriptions:
        x_label = custom_descriptions[x_axis_variable]

    if x_axis_variable in ['YearBuilt', 'YearRemodAdd']:
        # Create line graphs for YearBuilt or YearRemodAdd
        grouped_counts = filtered_df.groupby([x_axis_variable, 'Neighborhood']).size().reset_index(name='Frequency')
        fig = px.line(grouped_counts, x=x_axis_variable, y='Frequency', color='Neighborhood',
                    labels={x_axis_variable: x_label, 'Frequency': y_label, 'Neighborhood': 'Neighborhood'},
                    markers=True, title=f'Frequency of {x_label} by Neighborhood')

        # Update the custom labels for the legend using for_each_trace
        custom_legend_labels = [neighborhood_labels.get(neighborhood, neighborhood) for neighborhood in fig.data[0].y]
        fig.for_each_trace(lambda trace: trace.update(name=neighborhood_labels.get(trace.name, trace.name)))

        grouped_sales = filtered_df.groupby([x_axis_variable, 'Neighborhood'])['SalePrice'].mean().reset_index()
        sale_price_fig = px.line(grouped_sales, x=x_axis_variable, y='SalePrice', color='Neighborhood',
                                labels={x_axis_variable: x_label, 'SalePrice': 'Sale Price', 'Neighborhood': 'Neighborhood'},
                                markers=True, title=f'Sale Price of {x_label} by Neighborhood')

        # Update the custom labels for the legend using for_each_trace for sale_price_fig
        custom_legend_labels_sale_price = [neighborhood_labels.get(neighborhood, neighborhood) for neighborhood in sale_price_fig.data[0].y]
        sale_price_fig.for_each_trace(lambda trace: trace.update(name=neighborhood_labels.get(trace.name, trace.name)))


    elif x_axis_variable in ['MSZoning', 'LandContour', 'LotShape', 'LotConfig',
                            'Condition1', 'BldgType', 'RoofStyle', 'RoofMatl', 'ExterQual', 'ExterCond', 'Foundation',
                            'BsmtQual', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2',
                            'HeatingQC', 'KitchenQual', 'FireplaceQu',
                            'GarageType', 'GarageFinish', 'GarageQual', 'GarageCond',
                            'Fence', 'MiscFeature',
                            'SaleType', 'SaleCondition']:
        # Create a bar chart for x_axis_variable
        grouped_counts = filtered_df.groupby([x_axis_variable, 'Neighborhood']).size().reset_index(name='Frequency')
        fig = px.bar(grouped_counts, x='Frequency', y=x_axis_variable, color='Neighborhood', barmode='stack',
                     labels={x_axis_variable: x_label, 'Frequency': 'Frequency', 'Neighborhood': 'Neighborhood'},
                     title=f'Frequency of {x_label} by Neighborhood')
        # Update the custom labels for the legend using for_each_trace
        custom_legend_labels = [neighborhood_labels.get(neighborhood, neighborhood) for neighborhood in fig.data[0].y]
        fig.for_each_trace(lambda trace: trace.update(name=neighborhood_labels.get(trace.name, trace.name)))


        # Calculate the sum of Sale Prices for each unique combination of x_axis_variable and its value
        grouped_sales = filtered_df.groupby([x_axis_variable, 'Neighborhood'])['SalePrice'].mean().reset_index()
        sale_price_fig = px.bar(grouped_sales, x=x_axis_variable, y='SalePrice', color='Neighborhood',
                                 labels={x_axis_variable: x_label, 'SalePrice': 'Sale Price', 'Neighborhood': 'Neighborhood'},
                                 barmode='group', title=f'Sale Price of {x_label} by Neighborhood')
        # Update the custom labels for the legend using for_each_trace for sale_price_fig
        custom_legend_labels_sale_price = [neighborhood_labels.get(neighborhood, neighborhood) for neighborhood in sale_price_fig.data[0].y]
        sale_price_fig.for_each_trace(lambda trace: trace.update(name=neighborhood_labels.get(trace.name, trace.name)))


    elif x_axis_variable in ['LotFrontage', 'BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF',
                         '1stFlrSF', '2ndFlrSF', 'LowQualFinSF', 'GrLivArea',
                         'GarageArea', 'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch',
                         '3SsnPorch', 'ScreenPorch', 'PoolArea']:
        # Create a bubble chart for the frequency of the selected variable
        grouped_counts = filtered_df.groupby([x_axis_variable, 'Neighborhood']).size().reset_index(name='Frequency')
        fig = px.scatter(grouped_counts, x=x_axis_variable, y='Frequency', color='Neighborhood',
                        size='Frequency',  # Use Frequency as the size variable
                        labels={x_axis_variable: x_label, 'Frequency': 'Frequency', 'Neighborhood': 'Neighborhood'},
                        title=f'Frequency of {x_label} by Neighborhood')
        # Update the custom labels for the legend using for_each_trace
        custom_legend_labels = [neighborhood_labels.get(neighborhood, neighborhood) for neighborhood in fig.data[0].y]
        fig.for_each_trace(lambda trace: trace.update(name=neighborhood_labels.get(trace.name, trace.name)))


        # Calculate the sum of Sale Prices for each unique combination of x_axis_variable and its value
        grouped_sales = filtered_df.groupby([x_axis_variable, 'Neighborhood'])['SalePrice'].mean().reset_index()
        sale_price_fig = px.scatter(grouped_sales, x=x_axis_variable, y='SalePrice', color='Neighborhood',
                                    size='SalePrice',  # Use Sale Price as the size variable
                                    labels={x_axis_variable: x_label, 'SalePrice': 'Sale Price', 'Neighborhood': 'Neighborhood'},
                                    title=f'Sale Price of {x_label} by Neighborhood')
        # Update the custom labels for the legend using for_each_trace for sale_price_fig
        custom_legend_labels_sale_price = [neighborhood_labels.get(neighborhood, neighborhood) for neighborhood in sale_price_fig.data[0].y]
        sale_price_fig.for_each_trace(lambda trace: trace.update(name=neighborhood_labels.get(trace.name, trace.name)))




    else:
        # Create a bar chart as before for other x-axis variables
        grouped_counts = filtered_df.groupby([x_axis_variable, 'Neighborhood']).size().reset_index(name='Frequency')
        fig = px.bar(grouped_counts, x=x_axis_variable, y='Frequency', color='Neighborhood', barmode='group',
                     labels={x_axis_variable: x_label, 'Frequency': 'Frequency', 'Neighborhood': 'Neighborhood'},
                     title=f'Frequency of {x_label} by Neighborhood')
        # Update the custom labels for the legend using for_each_trace
        custom_legend_labels = [neighborhood_labels.get(neighborhood, neighborhood) for neighborhood in fig.data[0].y]
        fig.for_each_trace(lambda trace: trace.update(name=neighborhood_labels.get(trace.name, trace.name)))

        # Calculate the sum of Sale Prices for each unique combination of x_axis_variable and its value
        grouped_sales = filtered_df.groupby([x_axis_variable, 'Neighborhood'])['SalePrice'].mean().reset_index()
        sale_price_fig = px.bar(grouped_sales, x=x_axis_variable, y='SalePrice', color='Neighborhood',
                                labels={x_axis_variable: x_label, 'SalePrice': 'Sale Price', 'Neighborhood': 'Neighborhood'},
                                barmode='group', title=f'Sale Price of {x_label} by Neighborhood')
        # Update the custom labels for the legend using for_each_trace for sale_price_fig
        custom_legend_labels_sale_price = [neighborhood_labels.get(neighborhood, neighborhood) for neighborhood in sale_price_fig.data[0].y]
        sale_price_fig.for_each_trace(lambda trace: trace.update(name=neighborhood_labels.get(trace.name, trace.name)))


    return fig, sale_price_fig

if __name__ == '__main__':
    app.run_server(debug=True)
