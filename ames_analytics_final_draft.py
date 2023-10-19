from dash import Dash, html, dcc, Input, Output, dash_table
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from dash import html
from dash.dependencies import Input, Output
from datetime import datetime  # Import the datetime module


# Create a Dash instance
app = Dash(__name__, suppress_callback_exceptions=True)

google_fonts_link = "https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap"

# Read the data from 'train.csv'
df = pd.read_csv('train.csv')


numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns


# Make a copy of the original dataframe
df_copy = df.copy()

abbreviations_map = {
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
    'IDOTRR': 'IDOTRR',
    'MeadowV': 'Meadow Village',
    'StoneBr': 'Stone Brooke',
    'ClearCr': 'Clear Creek',
    'NPkVill': 'Northpark Village',
    'Blmngtn': 'Bloomington Heights',
    'BrDale': 'Briardale',
    'SWISU': 'Southwest of the ISU campus',
    'Blueste': 'Bluestem',
    'RM': 'Residential Medium Density',
    'RL': 'Residential Low Density',
    'RH': 'Residential High Density',
    'Lvl': 'Level',
    'Low': 'Lowland/Low Slope',
    'HLS': 'Hillside',
    'Bnk': 'Banked',
    'Reg': 'Regular',
    'IR3': 'Irregular - 3rd Category',
    'IR2': 'Irregular - 2nd Category',
    'IR1': 'Irregular - 1st Category',
    'Inside': 'Inside',
    'FR2': 'Frontage 2)',
    'CulDSac': 'Cul-de-Sac',
    'Corner': 'Corner',
    'PosN': 'Near Positive Feature',
    'PosA': 'Adjacent to Positive Feature',
    'Norm': 'Normal Proximity',
    'Feedr': 'Adjacent to Feeder Street or Railroad',
    'Duplex': 'Duplex',
    '2fmCon': 'Two-Family Conversion',
    'TwnhsE': 'Townhouse End Unit',
    '1Fam': 'Single-Family',
    'WhShngl': 'Wood Shingle',
    'CompShg': 'Composition Shingle',
    'TA': 'Average',
    'Gd': 'Good',
    'Ex': 'Excellent',
    'Fa': 'Fair',
    'Stone': 'Stone Foundation',
    'PConc': 'Poured Concrete Foundation',
    'CBlock': 'Concrete Block Foundation',
    'BrkTil': 'Brick and Tile Foundation',
    'No': 'No Exposure',
    'Mn': 'Minimum Exposure',
    'Av': 'Average Exposure',
    'Unf': 'Unfinished',
    'Rec': 'Average Living Quarters',
    'LwQ': 'Low Quality',
    'GLQ': 'Good Living Quarters',
    'BLQ': 'Below Average Living Quarters',
    'ALQ': 'Average Living Quarters',
    'Po': 'Poor',
    'Detchd': 'Detached from House',
    'BuiltIn': 'Built-In Garage',
    'Basement': 'Basement Garage',
    'Attchd': 'Attached to House',
    '2Types': 'More than one type of Garage',
    'RFn': 'Rough Finished',
    'Fin': 'Finished',
    'MnPrv': 'Minimum Privacy',
    'GdWo': 'Good Wood',
    'GdPrv': 'Good Privacy',
    'TenC': 'Tennis Court',
    'Othr': 'Other',
    'Shed': 'Shed',
    'Gar2': 'Second Garage',
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
    'ConLw': 'Conventional with low down payment',
    'ConLD': 'Conventional with low down payment',
    'Con': 'Conventional',
    'WD': 'Warranty Deed - Conventional',
    'New': 'Home just constructed and sold',
    'CWD': 'Warranty Deed - Cash Conventional',
    'COD': 'Court Officer Deed/Estate',
    'Family': 'Family Sale',
    'Alloca': 'Allocation',
    'Partial': 'Partial',
    'Normal': 'Normal Sale',
    'Abnormal': 'Abnormal Sale'
}


columns_to_replace = ['Neighborhood', 'MSZoning', 'LandContour', 'LotShape', 'LotConfig',
                      'Condition1', 'BldgType', 'RoofMatl', 'ExterQual', 'Foundation', 'ExterCond',
                      'BsmtQual', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2',
                      'HeatingQC', 'KitchenQual', 'FireplaceQu',
                      'GarageType', 'GarageFinish', 'GarageQual', 'GarageCond',
                      'Fence', 'MiscFeature',
                      'MoSold', 'SaleType', 'SaleCondition'
                      ]
df_copy[columns_to_replace] = df_copy[columns_to_replace].replace(abbreviations_map)
df_copy = df_copy.fillna('N/A')

# Define the number of variables per page
variables_per_page = 3  # Adjust this as needed


# Split the variable options into pages
variable_options = df_copy.columns
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
    #{'label': 'Flatness of the property', 'value': 'LandContour'},
    {'label': 'General shape of property', 'value': 'LotShape'},
    {'label': 'Lot configuration', 'value': 'LotConfig'},
    {'label': 'Linear feet of street connected to property', 'value': 'LotFrontage'}]

page2_variables = [
    #{'label': 'Proximity to main road or railroad', 'value': 'Condition1'},
    {'label': 'Type of dwelling', 'value': 'BldgType'},
    {'label': 'Overall material and finish quality', 'value': 'OverallQual'},
    {'label': 'Overall condition rating', 'value': 'OverallCond'},
    {'label': 'Original construction date', 'value': 'YearBuilt'},
    {'label': 'Remodel date', 'value': 'YearRemodAdd'},
    #{'label': 'Type of roof', 'value': 'RoofStyle'},
    #{'label': 'Roof material', 'value': 'RoofMatl'},
    {'label': 'Exterior material quality', 'value': 'ExterQual'},
    #{'label': 'Present condition of the material on the exterior', 'value': 'ExterCond'},
    {'label': 'Type of foundation', 'value': 'Foundation'}
]

page3_variables = [
    {'label': 'Basement quality', 'value': 'BsmtQual'},
    #{'label': 'Walkout/garden level basement walls', 'value': 'BsmtExposure'},
    {'label': 'Quality of basement finished area', 'value': 'BsmtFinType1'},
    #{'label': 'Quality of second finished area (if present)', 'value': 'BsmtFinType2'},
    {'label': 'Type 1 finished (in square feet)', 'value': 'BsmtFinSF1'},
    #{'label': 'Type 2 finished (in square feet)', 'value': 'BsmtFinSF2'},
    {'label': 'Unfinished basement area (in square feet)', 'value': 'BsmtUnfSF'},
    {'label': 'Total basement area (in square feet)', 'value': 'TotalBsmtSF'}
]

page4_variables = [
    {'label': 'Heating quality and condition', 'value': 'HeatingQC'},
    {'label': 'First floor (in square feet)', 'value': '1stFlrSF'},
    {'label': 'Second floor (in square feet)', 'value': '2ndFlrSF'},
    {'label': 'Above grade (ground) living area (in square feet)', 'value': 'GrLivArea'},
    {'label': 'Number of basement full bathrooms', 'value': 'BsmtFullBath'},
    #{'label': 'Number of basement half bathrooms', 'value': 'BsmtHalfBath'},
    {'label': 'Number of full bathrooms above grade (ground)', 'value': 'FullBath'},
    {'label': 'Number of half baths above grade (ground)', 'value': 'HalfBath'},
    {'label': 'Kitchen quality', 'value': 'KitchenQual'},
    {'label': 'Total rooms above grade (does not include bathrooms)', 'value': 'TotRmsAbvGrd'},
    {'label': 'Number of fireplaces', 'value': 'Fireplaces'},
    #{'label': 'Fireplace quality', 'value': 'FireplaceQu'}
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
    #{'label': 'Pool area (in square feet)', 'value': 'PoolArea'},
    #{'label': 'Pool quality', 'value': 'PoolQC'},
    {'label': 'Fence quality', 'value': 'Fence'},
    #{'label': 'Miscellaneous feature not covered in other categories', 'value': 'MiscFeature'},
    #{'label': 'Value of miscellaneous feature', 'value': 'MiscVal'}
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

    # Define the neighborhood dropdown options using the custom labels
    neighborhood_options = [{'label': neighborhood_labels.get(neighborhood, neighborhood), 'value': neighborhood}
                            for neighborhood in df_copy['Neighborhood'].unique()]
    
    neighborhood_options = [{'label': neighborhood_labels.get(neighborhood, neighborhood), 'value': neighborhood}
                            for neighborhood in df_copy['Neighborhood'].unique()]

    # Create the x-axis variable dropdown
    variable_inputs = [dcc.Dropdown(
        id='x-axis-variable',
        options=[{'label': var['label'], 'value': var['value']} for var in variables_on_page],
        value=variables_on_page[0]['value'],
        style={'margin-top': '15px', 'width': '400px'}
    )]


    return html.Div(children=[
        dcc.Dropdown(
            id='neighborhood-dropdown',
            options=neighborhood_options,
            multi=True,
            value=df_copy['Neighborhood'].unique()[:3],
            style={'width': '300px', 'margin-top': '20px'}
        ),
        *variable_inputs,  # Use the * to unpack the list of variable inputs
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

app.layout = html.Div([
    html.H1(children='Ames House Price Dashboard', style={'font-family': 'Roboto, sans-serif', 'text-align': 'center'}),
    dcc.Tabs(
        id='tabs',
        value='home',
        children=[
            dcc.Tab(label='Home', value='home'),
            * [dcc.Tab(label=label, value=str(i)) for i, label in enumerate(tab_labels)]
        ],
        style={'font-family': 'Roboto, sans-serif'}  # Set the font style for tabs
    ),
    html.Div(id='page-content')
])


# Callback to update the displayed page
@app.callback(Output('page-content', 'children'), Input('tabs', 'value'))
def display_page(tab_value):
    if tab_value == 'home':
        return create_home_layout()
    tab_value = int(tab_value)
    if 0 <= tab_value < len(tab_labels):
        return create_page_layout(tab_value)
    else:
        return html.Div(children=["Page not found"])
    
# Create a new DataFrame with neighborhood frequencies
neighborhood_counts = df['Neighborhood'].value_counts().reset_index()
neighborhood_counts.columns = ['Neighborhood', 'Frequency']

df_copy['MSSubClass'] = df_copy['MSSubClass'].astype(str)
average_mssubclass = df_copy['MSSubClass'].mode().values[0]

average_saleprice = df_copy['SalePrice'].mean()

average_year_built = df_copy['YearBuilt'].mode().values[0]

most_common_mszoning = df_copy['MSZoning'].mode()[0]

most_common_neighborhood = df_copy['Neighborhood'].mode().values[0]

most_common_dwelling = df_copy['BldgType'].mode()[0]

average_month_sold = df_copy['MoSold'].mode()[0]

average_year_sold = df_copy['YrSold'].mode()[0]

average_year_remodeled = df_copy['YearRemodAdd'].mode().values[0]

average_ground_living_area = df_copy['GrLivArea'].mean()

average_lot_area = df_copy['LotArea'].mean()

average_overall_quality = df_copy['OverallQual'].mean()

data_explanation = [
    {'Building Class': 20, 'Meaning': '1-Story 1946 & Newer'},
    {'Building Class': 30, 'Meaning': '1-Story 1945 & Older'},
    {'Building Class': 45, 'Meaning': '1-1/2 Story - Unfinished'},
    {'Building Class': 50, 'Meaning': '1-1/2 Story Finished'},
    {'Building Class': 60, 'Meaning': '2-Story 1946 & Newer'},
    {'Building Class': 70, 'Meaning': '2-Story 1945 & Older'},
    {'Building Class': 75, 'Meaning': '2-1/2 Story'},
    {'Building Class': 80, 'Meaning': 'Split or Multi-Level'},
    {'Building Class': 85, 'Meaning': 'Split Foyer'},
    {'Building Class': 90, 'Meaning': 'Duplex - All Styles and Ages'},
    {'Building Class': 120, 'Meaning': '1-Story PUD (Planned Unit Development)'},
    {'Building Class': 190, 'Meaning': '2-Story PUD'}
]


table_rows = []
for index, row in enumerate(data_explanation):
    if index % 2 == 0:
        background_color = 'white'
    else:
        background_color = 'lightblue'

    table_rows.append(
        html.Tr(
            [
                html.Td(row['Building Class']),
                html.Td(row['Meaning']),
            ],
            style={'background-color': background_color},
        )
    )


# Define the home layout with Google Fonts
def create_home_layout():
    total_rows = len(df_copy)
    last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    layout = html.Div(
        className="home-layout",
        children=[
            html.H1("Landing Page", className="header-title", style={'font-family': 'Roboto, sans-serif', 'text-align': 'center'}),
            html.P("This is the landing page for your dashboard. You can navigate to different sections using the tabs above.", className="intro-text", style={'font-family': 'Roboto, sans-serif', 'text-align': 'center'}),
            html.Div(f"Last Updated: {last_updated} (EST)", className="info-text", style={'font-family': 'Roboto, sans-serif', 'text-align': 'right'}),
            html.Div(f"Property Count: {len(df)}", className="info-text", style={'font-family': 'Roboto, sans-serif', 'margin-top': '7.5px', 'margin-bottom': '7.5px', 'text-align': 'right'}),
            # White Line
            html.Div(className="white-line"),
                html.Div([
                    #html.Div([
                    #    html.Div('Property Count', style={'font-size': '1.2em', 'color': 'black', 'text-align': 'center', 'line-height': '2.35'}),
                    #    html.Div(f'{len(df)}', style={'font-size': '1em', 'color': 'black', 'text-align': 'center'}),
                    #], style={'background-color': 'lightgrey', 'padding': '10px', 'width': '200px', 'margin-top': '15px', 'margin-bottom': '10px', 'margin-left': '15px', 'display': 'inline-block'}),

                    html.Div([
                        html.Div('Most Common Building Class', style={'font-size': '1.2em', 'color': 'black', 'text-align': 'center'}),
                        html.Div(average_mssubclass + ' (1-Story 1946 & Newer)', style={'font-size': '1em', 'color': 'black', 'text-align': 'center'}),
                    ], style={'background-color': 'lightgrey', 'padding': '10px', 'width': '200px', 'margin-top': '7.5px', 'margin-bottom': '7.5px', 'margin-left': '15px', 'display': 'inline-block'}),

                    html.Div([
                        html.Div('Most Common Zoning Classification', style={'font-size': '1.2em', 'color': 'black', 'text-align': 'center'}),
                        html.Div(most_common_mszoning, style={'font-size': '1em', 'color': 'black', 'text-align': 'center'}),
                    ], style={'background-color': 'lightgrey', 'padding': '10px', 'width': '200px', 'margin-top': '7.5px', 'margin-bottom': '7.5px', 'margin-left': '15px', 'display': 'inline-block'}),

                    html.Div([
                        html.Div('Most Popular Neighborhood', style={'font-size': '1.2em', 'color': 'black', 'text-align': 'center'}),
                        html.Div(most_common_neighborhood, style={'font-size': '1em', 'color': 'black', 'text-align': 'center'}),
                    ], style={'background-color': 'lightgrey', 'padding': '10px', 'width': '200px', 'margin-top': '7.5px', 'margin-bottom': '7.5px', 'margin-left': '15px', 'display': 'inline-block'}),

                    html.Div([
                        html.Div('Most Common Dwelling', style={'font-size': '1.2em', 'color': 'black', 'text-align': 'center'}),
                        html.Div(most_common_dwelling, style={'font-size': '1em', 'color': 'black', 'text-align': 'center'}),
                    ], style={'background-color': 'lightgrey', 'padding': '10px', 'width': '200px', 'margin-top': '7.5px', 'margin-bottom': '7.5px', 'margin-left': '15px', 'display': 'inline-block'}),

                    html.Div([
                        html.Div('Average Overall Quality', style={'font-size': '1.2em', 'color': 'black', 'text-align': 'center'}),
                        html.Div(str(round(average_overall_quality)) + ' (Above Average)', style={'font-size': '1em', 'color': 'black', 'text-align': 'center'}),
                    ], style={'background-color': 'lightgrey', 'padding': '10px', 'width': '200px', 'margin-top': '7.5px', 'margin-bottom': '7.5px', 'margin-left': '15px', 'display': 'inline-block'}),


                    html.Div([
                        html.Div('Average Month Sold', style={'font-size': '1.2em', 'color': 'black', 'text-align': 'center', 'line-height': '2.35'}),
                        html.Div(average_month_sold, style={'font-size': '1em', 'color': 'black', 'text-align': 'center'}),
                    ], style={'background-color': 'lightgrey', 'padding': '10px', 'width': '200px', 'margin-top': '7.5px', 'margin-bottom': '7.5px', 'margin-left': '15px', 'display': 'inline-block'}),

                    html.Div([
                        html.Div('Average Year Sold', style={'font-size': '1.2em', 'color': 'black', 'text-align': 'center', 'line-height': '2.35'}),
                        html.Div(average_year_sold, style={'font-size': '1em', 'color': 'black', 'text-align': 'center'}),
                    ], style={'background-color': 'lightgrey', 'padding': '10px', 'width': '200px', 'margin-top': '7.5px', 'margin-bottom': '7.5px', 'margin-left': '15px', 'display': 'inline-block'}),

                    html.Div([
                        html.Div('Average Year of Houses Built', style={'font-size': '1.2em', 'color': 'black', 'text-align': 'center'}),
                        html.Div(average_year_built, style={'font-size': '1em', 'color': 'black', 'text-align': 'center'}),
                    ], style={'background-color': 'lightgrey', 'padding': '10px', 'width': '200px', 'margin-top': '7.5px', 'margin-bottom': '7.5px', 'margin-left': '15px', 'display': 'inline-block'}),

                    html.Div([
                        html.Div('Average Year of Houses Remodeled', style={'font-size': '1.2em', 'color': 'black', 'text-align': 'center'}),
                        html.Div(average_year_remodeled, style={'font-size': '1em', 'color': 'black', 'text-align': 'center'}),
                    ], style={'background-color': 'lightgrey', 'padding': '10px', 'width': '200px', 'margin-top': '7.5px', 'margin-bottom': '7.5px', 'margin-left': '15px', 'display': 'inline-block'}),

                    html.Div([
                        html.Div('Average Above Ground Living Area', style={'font-size': '1.2em', 'color': 'black', 'text-align': 'center'}),
                        html.Div(f'{(average_ground_living_area):,.2f} sq ft', style={'font-size': '1em', 'color': 'black', 'text-align': 'center'}),
                    ], style={'background-color': 'lightgrey', 'padding': '10px', 'width': '200px', 'margin-top': '7.5px', 'margin-bottom': '7.5px', 'margin-left': '15px', 'display': 'inline-block'}),

                    html.Div([
                        html.Div('Average Lot Area', style={'font-size': '1.2em', 'color': 'black', 'text-align': 'center', 'line-height': '2.35'}),
                        html.Div(f'{(average_lot_area):,.2f} sq ft', style={'font-size': '1em', 'color': 'black', 'text-align': 'center'}),
                    ], style={'background-color': 'lightgrey', 'padding': '10px', 'width': '200px', 'margin-top': '7.5px', 'margin-bottom': '7.5px', 'margin-left': '15px', 'display': 'inline-block'}),

                    html.Div([
                        html.Div('Average Sale Price', style={'font-size': '1.2em', 'color': 'black', 'text-align': 'center', 'line-height': '2.35'}),
                        html.Div(f'${(average_saleprice):,.2f}', style={'font-size': '1em', 'color': 'black', 'text-align': 'center'}),
                    ], style={'background-color': 'lightgrey', 'padding': '10px', 'width': '200px', 'margin-top': '7.5px', 'margin-bottom': '7.5px', 'margin-left': '15px', 'display': 'inline-block'}),



        ]),

            html.Table(
                [
                    html.Thead(
                        html.Tr(
                            [
                                html.Th('Building Class', style={'background-color': 'navy', 'color': 'white', 'border': '1px solid white', 'width': '150px', 'text-align': 'center'}),  # Adjust width
                                html.Th('Meaning', style={'background-color': 'navy', 'color': 'white', 'border': '1px solid white', 'width': '150px', 'text-align': 'center'}),  # Adjust width
                            ]
                        ),
                        style={'background-color': 'navy'},
                    ),
                    html.Tbody(
                        table_rows,  # Append the dynamic rows here
                        style={'text-align': 'center', 'width': 'auto'}  # Add text-align style to center data values and adjust width
                    ),
                ],
                style={
                    'width': '60%',  # Adjust the overall table width
                    'margin': '0 auto',
                    'border': '1px solid white',  # Add border for the entire table
                    'border-collapse': 'collapse',
                    'font-size': '1em',
                    'margin-top': '15px',
                    'margin-bottom': '25px',
                },
                className='table',
            ),
            dash_table.DataTable(
                id='data-table',
                data=df_copy.to_dict('records'),
                columns=[{'name': col, 'id': col} for col in df.columns],
                page_size=10,
                style_table={
                    'height': '440px',
                    'overflowY': 'auto',
                    'width': '60%',  # Adjust the width
                    'border': '1px solid white',  # Add border for the entire table
                    'border-collapse': 'collapse',
                    'font-size': '1em',
                    'margin': '0 auto',  # Center the table
                },
                style_cell={
                    'textAlign': 'center',  # Center the data values
                    'whiteSpace': 'normal',
                    'minWidth': '50px',
                    'maxWidth': '200px',  # Adjust the max width
                    'overflow': 'hidden',
                    'textOverflow': 'ellipsis',
                    'font-family': 'Roboto, sans-serif',
                    'border': '1px solid white',  # Add border for data cells
                },
                style_data_conditional=[
                    {
                        'if': {'row_index': 'odd'},
                        'backgroundColor': 'white',
                    },
                    {
                        'if': {'row_index': 'even'},
                        'backgroundColor': '#FFD580',
                    },
                ],
                style_header={
                    'backgroundColor': 'orange',
                    'color': 'white',
                    'fontWeight': 'bold',
                    'font-family': 'Roboto, sans-serif',
                    'border': '1px solid white',  # Add border for header cells
                },
            ),
            dcc.Dropdown(
                id='y-axis-dropdown',
                options=[
                    {'label': 'Frequency', 'value': 'Count'},
                    {'label': 'Sale Price', 'value': 'AvgSalePrice'},
                ],
                value='Count',
                style={'font-family': 'Roboto, sans-serif', 'margin-top': '15px', 'width': '400px'},
                
            ),
            dcc.Graph(id='bar-graph'),
        ],
        style={'font-family': 'Roboto, sans-serif'}
    )

    return layout


@app.callback(
    Output('bar-graph', 'figure'),
    Input('data-table', 'data'),
    Input('y-axis-dropdown', 'value')
)
def update_graph(data, selected_y_axis):
    # Create a DataFrame from the data
    #df = pd.DataFrame(data)

    if selected_y_axis == 'Count':
        # Count the occurrences of each neighborhood
        neighborhood_counts = df_copy['Neighborhood'].value_counts().reset_index()
        neighborhood_counts.columns = ['Neighborhood', 'Count']

        # Create the bar chart and add data values
        fig = px.bar(neighborhood_counts, x='Neighborhood', y='Count', text='Count', title='Neighborhood Count Bar Chart')
        fig.update_traces(marker_color='#0091D5')
    else:
        avg_sale_prices = df_copy.groupby('Neighborhood')['SalePrice'].mean().reset_index()
        avg_sale_prices['SalePrice'] = avg_sale_prices['SalePrice'].round(2)  # Round the SalePrice to two decimal places
        avg_sale_prices = avg_sale_prices.sort_values(by='SalePrice', ascending=False)

        # Create the bar chart and add data labels
        fig = px.bar(avg_sale_prices, x='Neighborhood', y='SalePrice', title='Neighborhood Average Sale Price Bar Chart',
                    text='SalePrice')  # This line adds the data labels

        fig.update_traces(texttemplate='%{text:,.2f}', textposition='outside', marker_color='#0091D5')  # Formats the labels to two decimal places



    return fig

# Define the layout for each page
def create_page_layout(page_number):
    # Add the neighborhood_labels dictionary here
    neighborhood_labels = {
        # ... (Your neighborhood labels go here)
    }

    # Define tab titles
    tab_titles = ["Property Analysis", "Building Analysis", "Basement Analysis", 'Interior Analysis', 'Garage Analysis', 'Exterior Analysis', 'Sale Analysis']  # Replace with your actual tab titles

    # Get the title for the current tab based on page_number
    tab_title = tab_titles[page_number]


    variables_on_page = page_variables[page_number]

    # Define the neighborhood dropdown options using the custom labels
    neighborhood_options = [{'label': neighborhood_labels.get(neighborhood, neighborhood), 'value': neighborhood}
                            for neighborhood in df_copy['Neighborhood'].unique()]

    # Create the x-axis variable dropdown
    variable_inputs = [dcc.Dropdown(
        id='x-axis-variable',
        options=[{'label': var['label'], 'value': var['value']} for var in variables_on_page],
        value=variables_on_page[0]['value'],
        style={'margin-top': '15px', 'width': '400px'}
    )]

    return html.Div(children=[
        html.H1(tab_title, className="header-title", style={'font-family': 'Roboto, sans-serif', 'text-align': 'center'}),
        dcc.Dropdown(
            id='neighborhood-dropdown',
            options=neighborhood_options,
            multi=True,
            value=df_copy['Neighborhood'].unique()[:3],
            style={'width': '300px', 'margin-top': '20px'}
        ),
        *variable_inputs,  # Use the * to unpack the list of variable inputs
        dcc.Graph(id='example-graph'),
        dcc.Graph(id='sale-price-graph')
    ], style={'font-family': 'Roboto, sans-serif'})

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


custom_colors = ['#0091D5', '#EA6A47', '#A5D8DD', '#1C4E80', '#7E909A', '#202020', '#F1F1F1']


# Define a callback for updating the graph
@app.callback(
    Output('example-graph', 'figure'),
    Output('sale-price-graph', 'figure'),
    Input('neighborhood-dropdown', 'value'),
    Input('x-axis-variable', 'value'),
)


def update_graph(selected_neighborhoods, x_axis_variable):
    try:
        if not selected_neighborhoods:
            # Handle the case where no neighborhoods are selected.
            fig = go.Figure()
            sale_price_fig = go.Figure()
            return fig, sale_price_fig


        filtered_df = df_copy[df_copy['Neighborhood'].isin(selected_neighborhoods) & df_copy['SalePrice'].notnull()]


        # Define fig and sale_price_fig with default values
        fig = go.Figure()
        sale_price_fig = go.Figure()


        if x_axis_variable in variable_descriptions:
            x_variable_description = variable_descriptions[x_axis_variable]
        else:
            x_variable_description = x_axis_variable


        x_label = variable_descriptions.get(x_axis_variable, x_axis_variable)
        y_label = "Frequency"


        if x_axis_variable in ['YearBuilt', 'YearRemodAdd']:
            grouped_counts = filtered_df.groupby([x_axis_variable, 'Neighborhood']).size().reset_index(name='Frequency')
            fig = px.line(grouped_counts, x=x_axis_variable, y='Frequency', color='Neighborhood', color_discrete_sequence=custom_colors,
                        labels={x_axis_variable: x_label, 'Frequency': y_label, 'Neighborhood': 'Neighborhood'},
                        markers=True, title=f'Frequency of {x_label} by Neighborhood')


            grouped_sales = filtered_df.groupby([x_axis_variable, 'Neighborhood'])['SalePrice'].mean().reset_index()
            sale_price_fig = px.line(grouped_sales, x=x_axis_variable, y='SalePrice', color='Neighborhood', color_discrete_sequence=custom_colors,
                                    labels={x_axis_variable: x_label, 'SalePrice': 'Sale Price', 'Neighborhood': 'Neighborhood'},
                                    markers=True, title=f'Sale Price of {x_label} by Neighborhood')

        
        # Update the code to apply the custom color palette
        elif x_axis_variable in ['MSZoning', 'LandContour', 'LotShape', 'LotConfig', 'Condition1', 'BldgType',
                                'RoofStyle', 'RoofMatl', 'ExterQual', 'ExterCond', 'Foundation', 'BsmtQual', 'BsmtExposure',
                                'BsmtFinType1', 'BsmtFinType2', 'HeatingQC', 'KitchenQual', 'FireplaceQu',
                                'GarageType', 'GarageFinish', 'GarageQual', 'GarageCond', 'Fence', 'MiscFeature', 'SaleType',
                                'SaleCondition']:
            grouped_counts = filtered_df.groupby([x_axis_variable, 'Neighborhood']).size().reset_index(name='Frequency')
            fig = px.bar(grouped_counts, x='Frequency', y=x_axis_variable, color='Neighborhood', barmode='stack',
                        labels={x_axis_variable: x_label, 'Frequency': 'Frequency', 'Neighborhood': 'Neighborhood'},
                        title=f'Frequency of {x_label} by Neighborhood',
                        color_discrete_sequence=custom_colors)

            grouped_sales = filtered_df.groupby([x_axis_variable, 'Neighborhood'])['SalePrice'].mean().reset_index()
            sale_price_fig = px.bar(grouped_sales, x=x_axis_variable, y='SalePrice', color='Neighborhood',
                                    labels={x_axis_variable: x_label, 'SalePrice': 'Sale Price', 'Neighborhood': 'Neighborhood'},
                                    barmode='group', title=f'Sale Price of {x_label} by Neighborhood',
                                    color_discrete_sequence=custom_colors)



        elif x_axis_variable in ['LotFrontage', 'BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF',
                                '1stFlrSF', '2ndFlrSF', 'LowQualFinSF', 'GrLivArea',
                                'GarageArea', 'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch',
                                '3SsnPorch', 'ScreenPorch', 'PoolArea']:
            fig = px.histogram(filtered_df, x=x_axis_variable, color='Neighborhood', barmode='overlay',
                            color_discrete_sequence=custom_colors,  # Set the color palette
                            labels={x_axis_variable: x_label, 'count': 'Frequency', 'Neighborhood': 'Neighborhood', x_axis_variable: variable_descriptions[x_axis_variable]},
                            title=f'Histogram of {x_label} by Neighborhood')

            grouped_sales = filtered_df.groupby([x_axis_variable, 'Neighborhood'])['SalePrice'].mean().reset_index()
            sale_price_fig = px.histogram(grouped_sales, x=x_axis_variable, color='Neighborhood', barmode='overlay',
                                        color_discrete_sequence=custom_colors,  # Set the color palette
                                        labels={x_axis_variable: x_label, 'SalePrice': 'Sale Price', 'Neighborhood': 'Neighborhood'},
                                        title=f'Histogram of Sale Price of {x_label} by Neighborhood')


        else:
            grouped_counts = filtered_df.groupby([x_axis_variable, 'Neighborhood']).size().reset_index(name='Frequency')
            fig = px.bar(grouped_counts, x=x_axis_variable, y='Frequency', color='Neighborhood', barmode='stack',
                        color_discrete_sequence=custom_colors, labels={x_axis_variable: x_label, 'Frequency': 'Frequency', 'Neighborhood': 'Neighborhood'},
                        title=f'Frequency of {x_label} by Neighborhood')


            # Create the sale price graph
            grouped_sales = filtered_df.groupby([x_axis_variable, 'Neighborhood'])['SalePrice'].mean().reset_index()
            sale_price_fig = px.bar(grouped_sales, x=x_axis_variable, y='SalePrice', color='Neighborhood',
                                    color_discrete_sequence=custom_colors, labels={x_axis_variable: x_label, 'SalePrice': 'Sale Price', 'Neighborhood': 'Neighborhood'},
                                    barmode='group', title=f'Sale Price of {x_label} by Neighborhood')


        return fig, sale_price_fig
    except Exception as e:
        print(str(e))
        return go.Figure(), go.Figure()




if __name__ == '__main__':
    app.run_server(debug=True)
