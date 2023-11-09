import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
import streamlit as st
import calendar


st.set_page_config(page_title="Ames House Price Dashboard", page_icon=":bar_chart:", layout="wide")

st.title('Ames House Price Dashboard')

# Load dataset
df = pd.read_csv('train.csv')

# Make copy of dataset
df_copy = df.copy()

df_copy['TotalFullBath'] = df_copy['FullBath'] + df_copy['BsmtFullBath']
df_copy['TotalHalfBath'] = df_copy['HalfBath'] + df_copy['BsmtHalfBath']

# Add tabs to the Streamlit sidebar
with st.sidebar:
    selected_tab = st.radio("Select a Tab", ["Home", "Property and Building Analysis", "Sales Analysis"])

# Define a mapping of abbreviations for data cleaning
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
    'FR2': 'Frontage 2',
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
    'Abnormal': 'Abnormal Sale',
    '1.5Fin': '1.5-Story House with Finished Area',
    '1.5Unf': '1.5-Story House with Unfinished Area',
    '1Story': 'One-Story House',
    '2.5Unf': '2.5-Story House with Unfinished Area',
    '2Story': 'Two-Story House',
    '2.5Fin': '2.5-Story House with Finished Area',
    'SFoyer': 'Split Foyer',
    'SLvl': 'Split Level'
}

# List of columns to replace using the abbreviations map
columns_to_replace = ['Neighborhood', 'MSZoning', 'LandContour', 'LotShape', 'LotConfig',
                      'Condition1', 'BldgType', 'HouseStyle', 'RoofMatl', 'ExterQual', 'Foundation', 'ExterCond',
                      'BsmtQual', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2',
                      'HeatingQC', 'KitchenQual', 'FireplaceQu',
                      'GarageType', 'GarageFinish', 'GarageQual', 'GarageCond',
                      'Fence', 'MiscFeature',
                      'MoSold', 'SaleType', 'SaleCondition',
                      'PoolQC'
                      ]
df_copy[columns_to_replace] = df_copy[columns_to_replace].replace(abbreviations_map)

# Fill missing values with 'N/A'
df_copy = df_copy.fillna('N/A')

df_copy['Total Finished Basement Area (in Square Feet)'] = df['1stFlrSF'] + df['2ndFlrSF']

new_column_names = {
    'MSSubClass': 'Building Class',
    'MSZoning': 'General Zoning Classification',
    'LandContour': 'Flatness of the Property',
    'LotShape': 'General Shape of Property',
    'LotConfig': 'Lot Configuration',
    'LotFrontage': 'Linear Feet of Street Connected to Property',
    'LotArea': 'Lot Size (in Square Feet)',

    'Condition1': 'Proximity to Main Road or Railroad',
    'BldgType': 'Type of Dwelling',
    'HouseStyle': 'Style of Dwelling',
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
    'Total Finished Basement Area (in Square Feet)': 'Total Finished Basement Area (in Square Feet)',
    'BsmtUnfSF': 'Unfinished Basement Area (in Square Feet)',
    'TotalBsmtSF': 'Total Basement Area (in Square Feet)',

    'HeatingQC': 'Heating Quality and Condition',
    '1stFlrSF': 'First Floor (in Square Feet)',
    '2ndFlrSF': 'Second Floor (in Square Feet)',
    'LowQualFinSF': 'Low-Quality Finished Area (in Square Feet)',
    'GrLivArea': 'Above Grade (Ground) Living Area (in Square Feet)',
    'BsmtFullBath': 'Number of Basement Full Bathrooms',
    'BsmtHalfBath': 'Number of Basement Half Bathrooms',
    'TotalFullBath': 'Total Number of Full Bathrooms',
    'FullBath': 'Number of Full Bathrooms Above Grade (Ground)',
    'HalfBath': 'Number of Half Baths Above Grade (Ground)',
    'TotalHalfBath': 'Total Number of Half Bathrooms',
    'TotRmsAbvGrd': 'Total Rooms Above Grade (Does Not Include Bathrooms)',
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
    'MiscFeature': 'Miscellaneous Feature',
    'MiscVal': 'Value of Miscellaneous Feature',

    'MoSold': 'Month Sold',
    'YrSold': 'Year Sold',
    'SaleType': 'Type of Sale',
    'SaleCondition': 'Condition of Sale'
}

# Convert these columns to float, replacing 'N/A' with NaN
df_copy['LotFrontage'] = pd.to_numeric(df_copy['LotFrontage'], errors='coerce')
df_copy['MasVnrArea'] = pd.to_numeric(df_copy['MasVnrArea'], errors='coerce')
df_copy['GarageYrBlt'] = pd.to_numeric(df_copy['GarageYrBlt'], errors='coerce')

df_copy = df_copy.rename(columns=new_column_names)

# Depending on the selected tab, display different content
if selected_tab == "Home":
    # Content for the Property tab
    st.header("Home")
    # Display the loaded data in an expander for data preview
    with st.expander("Data Preview"):
        st.dataframe(df_copy)

    st.subheader("About Ames")

    # https://en.wikipedia.org/wiki/Ames,_Iowa
    st.markdown("<p style='font-size: 20px;'>Ames is a city in Story County, Iowa, United States, located approximately 30 miles north of Des Moines in central Iowa. It is best known as the home of Iowa State University (ISU).</p>", unsafe_allow_html=True)
    st.subheader("Geographical and Home Value Summary")

    # Create a layout with two rows of 5 columns each
    row1 = st.columns(4)
    row2 = st.columns(2)

    with row1[0]:
        st.markdown(
            f"""
            <div style="background-color: #5B3B5A; border-radius: 5px; height: 75px; padding: 5px; text-align: center; margin-bottom: 20px;">
                <h3 style="font-size: 15px; color: white; padding: 1px;">Population (in 2010)</h3>
                <h2 style="font-size: 30px; color: white; padding-top: 0px; padding: 1px;">59,103</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # https://medium.com/@ying.geng5/house-price-analysis-of-ames-iowa-2006-2010-266e307f836f#:~:text=The%20median%20sale%20price%20for,cheaper%20than%20the%20national%20average.
    with row1[1]:
        st.markdown(
            f"""
            <div style="background-color: #84659C; border-radius: 5px; padding: 5px; text-align: center; margin-bottom: 20px;">
                <h3 style="font-size: 15px; color: white; padding: 1px;">Median Home Value (in 2006-2010)</h3>
                <h2 style="font-size: 30px; color: white; padding-bottom: 25px; padding: 1px;">$163,000</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Define the data
        city_distances = {
            "Des Moines": 37,
            "Iowa City": 129,
            "Cedar Rapids": 110,
        }
    with row1[2]:
        # Create a dropdown for selecting a city
        selected_city = st.selectbox("Select a City", list(city_distances.keys()))

    with row1[3]:
        # Display the selected city's distance in the same Markdown block
        st.write(
            f"""
            <div style="background-color: #5B3B5A; border-radius: 5px; padding: 5px; text-align: center; margin-bottom: 20px;">
                <h3 style="font-size: 15px; color: white; padding-top: 25px; padding: 1px;">Distance from Ames to {selected_city}</h3>
                <h2 style="font-size: 30px; color: white; padding-bottom: 25px; padding: 1px;">{city_distances[selected_city]} miles</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # https://www.census.gov/quickfacts/fact/table/amescityiowa#
    
    with row2[0]:
        # Display the selected city's distance in the same Markdown block
        st.write(
            f"""
            <div style="background-color: #5B3B5A; border-radius: 5px; padding: 5px; text-align: center; margin-bottom: 20px;">
                <h3 style="font-size: 15px; color: white; padding-top: 25px; padding: 1px;">Population per square mile (in 2010)</h3>
                <h2 style="font-size: 30px; color: white; padding-bottom: 25px; padding: 1px;">2,435.2</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with row2[1]:
        # Display the selected city's distance in the same Markdown block
        st.write(
            f"""
            <div style="background-color: #84659C; border-radius: 5px; padding: 5px; text-align: center; margin-bottom: 20px;">
                <h3 style="font-size: 15px; color: white; padding-top: 25px; padding: 1px;">Land area in square miles (in 2010)</h3>
                <h2 style="font-size: 30px; color: white; padding-bottom: 25px; padding: 1px;">24.21</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.subheader("Crime Rate Summary")

    row3 = st.columns(4)
    row4 = st.columns(4)

    # https://www.bestplaces.net/crime/city/iowa/ames
    # Define the crimes data
    crimes = {
        "Murder": 1.7,
        "Rape": 41.5,
        "Robbery": 17.3,
        "Assault": 245.6,
        'Property Crime': 2691.2,
        'Burglary': 499.9,
        'Larceny': 2104.9,
        'Auto Theft': 86.5,
    }
    
    with row3[0]:
        # Create a smaller gauge chart
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=crimes['Murder'],  # Default value
            title={
                "text": f"Murder Rate per 100,000 People (in 2010)",
                "font": {"size": 14}  # Adjust the font size here
            },
            gauge={
                "axis": {"range": [0, 8], "dtick": 2},
                "bar": {"color": "blue"},
                "steps": [
                    {"range": [0, 2], "color": "green"},
                    {"range": [2, 4], "color": "yellow"},
                    {"range": [4, 6], "color": "orange"},
                    {"range": [6, 8], "color": "red"},
                ]
            }
        ))

        fig.update_layout(width=280, height=280)

        # Display the smaller gauge chart
        st.plotly_chart(fig)

    with row3[1]:
        # Create a smaller gauge chart
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=crimes['Rape'],  # Default value
            title={
                "text": f"Rape Rate per 100,000 People (in 2010)",
                "font": {"size": 14}  # Adjust the font size here
            },
            gauge={
                "axis": {"range": [0, 80], "dtick": 20},
                "bar": {"color": "blue"},
                "steps": [
                    {"range": [0, 20], "color": "green"},
                    {"range": [20, 40], "color": "yellow"},
                    {"range": [40, 60], "color": "orange"},
                    {"range": [60, 80], "color": "red"},
                ]
            }
        ))

        fig.update_layout(width=280, height=280)

        # Display the smaller gauge chart
        st.plotly_chart(fig)

    with row3[2]:
        # Create a smaller gauge chart
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=crimes['Robbery'],  # Default value
            title={
                "text": f"Robbery Rate per 100,000 People (in 2010)",
                "font": {"size": 14}  # Adjust the font size here
            },
            gauge={
                "axis": {"range": [0, 200], "dtick": 50},
                "bar": {"color": "blue"},
                "steps": [
                    {"range": [0, 50], "color": "green"},
                    {"range": [50, 100], "color": "yellow"},
                    {"range": [100, 150], "color": "orange"},
                    {"range": [150, 200], "color": "red"},
                ]
            }
        ))

        fig.update_layout(width=280, height=280)

        # Display the smaller gauge chart
        st.plotly_chart(fig)

    with row3[3]:
        # Create a smaller gauge chart
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=crimes['Assault'],  # Default value
            title={
                "text": f"Assault Rate per 100,000 People (in 2010)",
                "font": {"size": 14}  # Adjust the font size here
            },
            gauge={
                "axis": {"range": [0, 600], "dtick": 150},
                "bar": {"color": "blue"},
                "steps": [
                    {"range": [0, 150], "color": "green"},
                    {"range": [150, 300], "color": "yellow"},
                    {"range": [300, 450], "color": "orange"},
                    {"range": [450, 600], "color": "red"},
                ]
            }
        ))

        fig.update_layout(width=280, height=280)

        # Display the smaller gauge chart
        st.plotly_chart(fig)

    with row4[0]:
        # Create a smaller gauge chart
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=crimes['Property Crime'],  # Default value
            title={
                "text": f"Property Crime Rate per 100,000 People (in 2010)",
                "font": {"size": 12}  # Adjust the font size here
            },
            gauge={
                "axis": {"range": [1500, 4000], "dtick": 625},
                "bar": {"color": "blue"},
                "steps": [
                    {"range": [1500, 2125], "color": "green"},
                    {"range": [2125, 2750], "color": "yellow"},
                    {"range": [2750, 3375], "color": "orange"},
                    {"range": [3375, 4000], "color": "red"},
                ]
            }
        ))

        fig.update_layout(width=260, height=260)

        # Display the smaller gauge chart
        st.plotly_chart(fig)

    with row4[1]:
        # Create a smaller gauge chart
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=crimes['Burglary'],  # Default value
            title={
                "text": f"Burglary Rate per 100,000 People (in 2010)",
                "font": {"size": 12}  # Adjust the font size here
            },
            gauge={
                "axis": {"range": [0, 1250], "dtick": 312.5},
                "bar": {"color": "blue"},
                "steps": [
                    {"range": [0, 312.5], "color": "green"},
                    {"range": [312.5, 625], "color": "yellow"},
                    {"range": [625, 937.5], "color": "orange"},
                    {"range": [937.5, 1250], "color": "red"},
                ]
            }
        ))

        fig.update_layout(width=260, height=260)

        # Display the smaller gauge chart
        st.plotly_chart(fig)

    with row4[2]:
        # Create a smaller gauge chart
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=crimes['Larceny'],  # Default value
            title={
                "text": f"Larceny Rate per 100,000 People (in 2010)",
                "font": {"size": 12}  # Adjust the font size here
            },
            gauge={
                "axis": {"range": [1000, 3500], "dtick": 625},
                "bar": {"color": "blue"},
                "steps": [
                    {"range": [1000, 1625], "color": "green"},
                    {"range": [1625, 2250], "color": "yellow"},
                    {"range": [2250, 2875], "color": "orange"},
                    {"range": [2875, 3500], "color": "red"},
                ]
            }
        ))

        fig.update_layout(width=260, height=260)

        # Display the smaller gauge chart
        st.plotly_chart(fig)

    with row4[3]:
        # Create a smaller gauge chart
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=crimes['Auto Theft'],  # Default value
            title={
                "text": f"Auto Theft Rate per 100,000 People (in 2010)",
                "font": {"size": 12}  # Adjust the font size here
            },
            gauge={
                "axis": {"range": [0, 500], "dtick": 125},
                "bar": {"color": "blue"},
                "steps": [
                    {"range": [0, 125], "color": "green"},
                    {"range": [125, 250], "color": "yellow"},
                    {"range": [250, 375], "color": "orange"},
                    {"range": [375, 500], "color": "red"},
                ]
            }
        ))

        fig.update_layout(width=260, height=260)

        # Display the smaller gauge chart
        st.plotly_chart(fig)

    st.subheader("Price and Sale Summary")

    average_sale_price = df['SalePrice'].mean()
    median_sale_price = df['SalePrice'].median()
    number_of_properties = len(df)
    price_change_over_time = df['SalePrice'].sum
    min_sale_price = df['SalePrice'].min()
    max_sale_price = df['SalePrice'].max()
    price_range = max_sale_price - min_sale_price
    # Calculate the price per square foot for each row
    df_copy['PricePerSqFtGround'] = df['SalePrice'] / df['GrLivArea']
    # Calculate the average price per square foot
    average_price_per_sqft_ground = df_copy['PricePerSqFtGround'].mean()
    # Calculate the median price per square foot
    median_price_per_sqft_ground = df_copy['PricePerSqFtGround'].median()
    # Calculate the price per square foot for each row
    df_copy['PricePerSqFtBasement'] = df['SalePrice'] / df['TotalBsmtSF']
    df_copy = df_copy[~np.isinf(df_copy['PricePerSqFtBasement'])]
    # Calculate the average price per square foot
    average_price_per_sqft_basement = df_copy['PricePerSqFtBasement'].mean()
    # Calculate the median price per square foot
    median_price_per_sqft_basement = df_copy['PricePerSqFtBasement'].median()

    # Create a layout with two rows of 5 columns each
    row1 = st.columns(5)
    row2 = st.columns(4)

    # Average Sale Price card
    with row1[0]:
        st.markdown(
            f"""
            <div style="background-color: #2E727D; border-radius: 5px; padding: 5px; text-align: center; margin-bottom: 20px;">
                <h3 style="font-size: 15px; color: white; padding-top: 25px; padding: 1px;">Average Sale Price</h3>
                <h2 style="font-size: 30px; color: white; padding-bottom: 25px; padding: 1px;">${average_sale_price:,.2f}</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Median Sale Price card
    with row1[1]:
        st.markdown(
            f"""
            <div style="background-color: #61A7B4; border-radius: 5px; padding: 5px; text-align: center;">
                <h3 style="font-size: 15px; color: white; padding-top: 25px; padding: 1px;">Median Sale Price</h3>
                <h2 style="font-size: 30px; color: white; padding-bottom: 25px; padding: 1px;">${median_sale_price:,.2f}</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Total Sales card
    with row1[2]:
        st.markdown(
            f"""
            <div style="background-color: #2E727D; border-radius: 5px; padding: 5px; text-align: center;">
                <h3 style="font-size: 15px; color: white; padding-top: 25px; padding: 1px;">Total Sales</h3>
                <h2 style="font-size: 30px; color: white; padding-bottom: 25px; padding: 1px;">{number_of_properties}</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Minimum Sale Price card
    with row1[3]:
        st.markdown(
            f"""
            <div style="background-color: #61A7B4; border-radius: 5px; padding: 5px; text-align: center;">
                <h3 style="font-size: 15px; color: white; padding-top: 25px; padding: 1px;">Minimum Sale Price</h3>
                <h2 style="font-size: 30px; color: white; padding-bottom: 25px; padding: 1px;">${min_sale_price:,.2f}</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Maximum Sale Price card
    with row1[4]:
        st.markdown(
            f"""
            <div style="background-color: #2E727D; border-radius: 5px; padding: 5px; text-align: center;">
                <h3 style="font-size: 15px; color: white; padding-top: 25px; padding: 1px;">Maximum Sale Price</h3>
                <h2 style="font-size: 30px; color: white; padding-bottom: 25px; padding: 1px;">${max_sale_price:,.2f}</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Average Price of Ground Floor Per Square Foot card
    with row2[0]:
        st.markdown(
            f"""
            <div style="background-color: #61A7B4; border-radius: 5px; padding: 5px; text-align: center;">
                <h3 style="font-size: 15px; color: white; padding-top: 25px; padding: 1px;">Average Price of Ground Floor (per sq ft)</h3>
                <h2 style="font-size: 30px; color: white; padding-bottom: 25px; padding: 1px;">${average_price_per_sqft_ground:,.2f}/ft²</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Median Price of Ground Floor Per Square Foot card
    with row2[1]:
        st.markdown(
            f"""
            <div style="background-color: #2E727D; border-radius: 5px; padding: 5px; text-align: center;">
                <h3 style="font-size: 15px; color: white; padding-top: 25px; padding: 1px;">Median Price of Ground Floor (per sq ft) </h3>
                <h2 style="font-size: 30px; color: white; padding-bottom: 25px; padding: 1px;">${median_price_per_sqft_ground:,.2f}/ft²</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Average Price of Basement Floor Per Square Foot card
    with row2[2]:
        st.markdown(
            f"""
            <div style="background-color: #61A7B4; border-radius: 5px; padding: 5px; text-align: center;">
                <h3 style="font-size: 15px; color: white; padding-top: 25px; padding: 1px;">Average Price of Basement Floor (per sq ft)</h3>
                <h2 style="font-size: 30px; color: white; padding-bottom: 25px; padding: 1px;">${average_price_per_sqft_basement:,.2f}/ft²</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Median Price of Basement Floor Per Square Foot card
    with row2[3]:
        st.markdown(
            f"""
            <div style="background-color: #2E727D; border-radius: 5px; padding: 5px; text-align: center; margin-bottom: 50px;">
                <h3 style="font-size: 15px; color: white; padding-top: 25px; padding: 1px;">Median Price of Basement Floor (per sq ft)</h3>
                <h2 style="font-size: 30px; color: white; padding-bottom: 25px; padding: 1px;">${median_price_per_sqft_basement:,.2f}/ft²</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Calculate neighborhood frequency
    neighborhood_counts = df_copy['Neighborhood'].value_counts()

    # Calculate average SalePrice per neighborhood
    neighborhood_saleprice = df_copy.groupby('Neighborhood')['SalePrice'].mean().reset_index()
    neighborhood_saleprice = neighborhood_saleprice.sort_values(by='SalePrice', ascending=False)

    # Create two columns for layout
    col1, col2 = st.columns(2)

    # Display the first bar chart in the first column
    with col1:
        st.subheader("Neighborhood Frequency")
        fig1 = px.bar(
            x=neighborhood_counts.index,
            y=neighborhood_counts.values,
            labels={'x': 'Neighborhood', 'y': 'Frequency'},
            width=600,
            height=500,
            title="Neighborhood Frequency Analysis",
        )
        st.plotly_chart(fig1)

    # Display the second bar chart in the second column
    with col2:
        st.subheader("Neighborhood Average Sale Price")
        fig2 = px.bar(
            neighborhood_saleprice,
            x='Neighborhood',
            y='SalePrice',
            labels={'x': 'Neighborhood', 'SalePrice': 'Average Sale Price'},
            title="Neighborhood Average Sale Price Analysis",
        )
        fig2.update_layout(
            xaxis_title="Neighborhood",
            yaxis_title="Average Sale Price",
            width=600,
            height=500,
        )
        st.plotly_chart(fig2)

        # Sort the DataFrame by Sale Price in descending order
        df_copy_sorted = df_copy.sort_values(by='SalePrice', ascending=False)

        # Format the 'SalePrice' column to include commas
        df_copy_sorted['SalePrice'] = df_copy_sorted['SalePrice'].apply(lambda x: f"${x:,}")

        # Streamlit app
        st.subheader("Top 10 Neighborhoods by Average Sale Price")

        # Display the table with custom headers to prevent key errors and without displaying the index
        st.table(df_copy_sorted[['Neighborhood', 'SalePrice']].head(10).rename(columns={'Neighborhood': 'Neighborhood', 'SalePrice': 'Average Sale Price'}).reset_index(drop=True))

elif selected_tab == "Property and Building Analysis":
    # Content for the Building tab
    st.header("Property and Building Analysis")
    # Display the loaded data in an expander for data preview
    with st.expander("Data Preview"):
        st.dataframe(df_copy)

    data_explanation = [
            {'Building Class': 20, 'Meaning': '1-Story 1946 & Newer'},
            {'Building Class': 30, 'Meaning': '1-Story 1945 & Older'},
            {'Building Class': 40, 'Meaning': 'Multi-Residence Properties'},
            {'Building Class': 45, 'Meaning': '1-1/2 Story - Unfinished'},
            {'Building Class': 50, 'Meaning': '1-1/2 Story Finished'},
            {'Building Class': 60, 'Meaning': '2-Story 1946 & Newer'},
            {'Building Class': 70, 'Meaning': '2-Story 1945 & Older'},
            {'Building Class': 75, 'Meaning': '2-1/2 Story'},
            {'Building Class': 80, 'Meaning': 'Split or Multi-Level'},
            {'Building Class': 85, 'Meaning': 'Split Foyer'},
            {'Building Class': 90, 'Meaning': 'Duplex - All Styles and Ages'},
            {'Building Class': 120, 'Meaning': '1-Story PUD (Planned Unit Development)'},
            {'Building Class': 160, 'Meaning': 'Two-Story Homes'},
            {'Building Class': 180, 'Meaning': 'Three-Story Homes'},
            {'Building Class': 190, 'Meaning': '2-Story PUD'}
        ]
    
    building_class_counts = pd.DataFrame(columns=['Building Class', 'Count'])

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Building Class Explanation Table")
        # Display a data table based on the data_explanation list
        st.table(data_explanation)

        # Calculate the distribution of Building Classes based on counts in df_copy
        building_class_counts = df_copy['Building Class'].value_counts().reset_index()
        building_class_counts.columns = ['Building Class', 'Count']

        # Create a pie chart based on the distribution of Building Class counts
        fig_pie = px.pie(building_class_counts, names='Building Class', values='Count', title='Distribution of Building Classes')
        fig_pie.update_traces(hole=0.4)  # Adjust the hole size (0.4 makes it a donut)

        # Display the pie chart
        st.plotly_chart(fig_pie)

    with col2:
        st.subheader("Building Class")
        selected_feature2 = st.selectbox("Select a Building Class Feature", [
            'Building Class'
        ], key="feature2")

        price_range2 = st.slider("Price Range", min_value=int(df_copy['SalePrice'].min()), max_value=int(df_copy['SalePrice'].max()), step=1000, value=(int(df_copy['SalePrice'].min()), int(df_copy['SalePrice'].max())), key="price_range2")
        original_construction_date_range_2 = st.slider("Original Construction Date Range", int(df_copy['Original Construction Date'].min()), int(df_copy['Original Construction Date'].max()), (int(df_copy['Original Construction Date'].min()), int(df_copy['Original Construction Date'].max())), key="original_construction_date_range2")
        remodel_date_range_2 = st.slider("Remodel Date Range", int(df_copy['Remodel Date'].min()), int(df_copy['Remodel Date'].max()), (int(df_copy['Remodel Date'].min()), int(df_copy['Remodel Date'].max())), key="remodel_date_range2")

        # Filter the data based on the selected criteria for the second graph
        filtered_data2 = df_copy[
            (df_copy['SalePrice'] >= price_range2[0]) &
            (df_copy['SalePrice'] <= price_range2[1]) &
            (df_copy['Original Construction Date'] >= original_construction_date_range_2[0]) &
            (df_copy['Original Construction Date'] <= original_construction_date_range_2[1]) &
            (df_copy['Remodel Date'] >= remodel_date_range_2[0]) &
            (df_copy['Remodel Date'] <= remodel_date_range_2[1])
        ]

        # Create a frequency count of the selected feature and neighborhood for the second graph
        feature_counts2 = filtered_data2.groupby([selected_feature2, 'Neighborhood']).size().reset_index()
        feature_counts2.columns = [selected_feature2, 'Neighborhood', 'Frequency']

        # Get the top 10 neighborhoods based on frequency for the selected feature and price range for the second graph
        top_neighborhoods2 = feature_counts2.groupby('Neighborhood').sum().nlargest(10, 'Frequency').index

        # Filter data to include only the top 10 neighborhoods for the selected feature and price range for the second graph
        filtered_feature_counts2 = feature_counts2[(feature_counts2['Neighborhood'].isin(top_neighborhoods2)) & (feature_counts2[selected_feature2] != 'N/A')]

        # Create a stacked bar chart using Plotly Express for the second feature
        fig2 = px.bar(
            filtered_feature_counts2,
            x=selected_feature2,
            y='Frequency',
            color='Neighborhood',  # Color by neighborhood
            barmode='stack',  # Create a stacked bar chart
            labels={'x': selected_feature2, 'Frequency': 'Frequency'},
            title=f"Top Neighborhoods for {selected_feature2}",
        )

        # Display the second stacked bar chart
        st.plotly_chart(fig2)

    st.write("---")

    # Create two columns with equal width to place the graphs side by side
    col3, col4 = st.columns(2)

    # Add a horizontal rule to create spacing
    st.write("---")

    with col3:
        # Dropdown for selecting the first feature in the first column
        st.subheader("Property Assessment Metrics")

        selected_feature3 = st.selectbox("Select a Property Feature", [
            'Overall Material and Finish Quality',
            'Overall Condition Rating',
            'Exterior Material Quality',
            'Present Condition of the Material on the Exterior',
            'Basement Quality',
            'Heating Quality and Condition',
            'Kitchen Quality',
            'Fireplace Quality',
            'Garage Quality',
            'Garage Condition'
        ], key="feature3")

        price_range3 = st.slider("Price Range", min_value=int(df_copy['SalePrice'].min()), max_value=int(df_copy['SalePrice'].max()), step=1000, value=(int(df_copy['SalePrice'].min()), int(df_copy['SalePrice'].max())), key="price_range3")
        original_construction_date_range_3 = st.slider("Original Construction Date Range", int(df_copy['Original Construction Date'].min()), int(df_copy['Original Construction Date'].max()), (int(df_copy['Original Construction Date'].min()), int(df_copy['Original Construction Date'].max())), key="original_construction_date_range3")
        remodel_date_range_3 = st.slider("Remodel Date Range", int(df_copy['Remodel Date'].min()), int(df_copy['Remodel Date'].max()), (int(df_copy['Remodel Date'].min()), int(df_copy['Remodel Date'].max())), key="remodel_date_range3")

        # Filter the data based on the selected criteria for the fifth graph
        filtered_data3 = df_copy[
            (df_copy['SalePrice'] >= price_range3[0]) &
            (df_copy['SalePrice'] <= price_range3[1]) &
            (df_copy['Original Construction Date'] >= original_construction_date_range_3[0]) &
            (df_copy['Original Construction Date'] <= original_construction_date_range_3[1]) &
            (df_copy['Remodel Date'] >= remodel_date_range_3[0]) &
            (df_copy['Remodel Date'] <= remodel_date_range_3[1])
        ]

        # Create a frequency count of the selected feature and neighborhood
        feature_counts3 = filtered_data3.groupby([selected_feature3, 'Neighborhood']).size().reset_index()
        feature_counts3.columns = [selected_feature3, 'Neighborhood', 'Frequency']

        # Sort the data by 'Frequency' and get the top 10 neighborhoods
        top_neighborhoods3 = feature_counts3.groupby('Neighborhood')['Frequency'].sum().nlargest(10).index

        # Filter data to include only the top 10 neighborhoods
        filtered_feature_counts3 = feature_counts3[feature_counts3['Neighborhood'].isin(top_neighborhoods3)]

        # Calculate the average value for "Overall Material and Finish Quality"
        average_quality3 = filtered_data3['Overall Material and Finish Quality'].mean()
        # Calculate the average value for "Overall Condition Rating"
        average_condition3 = filtered_data3['Overall Condition Rating'].mean()

        # Create a stacked bar chart using Plotly Express for the top 10 neighborhoods
        fig_stacked_bar3 = px.bar(
            filtered_feature_counts3,
            x=selected_feature3,
            y='Frequency',
            color='Neighborhood',
            barmode='stack',
            labels={'x': selected_feature3, 'Frequency': 'Frequency'},
            title=f"Stacked Bar Charts of Top 10 Neighborhoods, {selected_feature3}, and Frequency",
        )

        # Display the stacked bar chart using st.plotly_chart
        st.plotly_chart(fig_stacked_bar3)

        # Create the gauge chart based on the selected feature
        average_value3 = 0
        title_text3 = "Average Value"  # Set a default title text

        if selected_feature3 == 'Overall Material and Finish Quality':
            average_value3 = average_quality3
            title_text3 = "Average Overall Quality"
        elif selected_feature3 == 'Overall Condition Rating':
            average_value3 = average_condition3
            title_text3 = "Average Overall Condition"
        elif selected_feature3 == 'Fireplace Quality':
            fireplace_quality_counts3 = filtered_data3['Fireplace Quality'].value_counts().reset_index()
            fireplace_quality_counts3.columns = ['Fireplace Quality', 'Number of Fireplaces']

            # Create a donut chart based on "Fireplace Quality" and display the number of fireplaces
            fig_donut_chart3 = px.pie(fireplace_quality_counts3, names='Fireplace Quality', values='Number of Fireplaces', hole=0.4, labels={'Number of Fireplaces': 'Number of Fireplaces'})
            fig_donut_chart3.update_layout(
                height=300,  # Adjust the height
                width=300,    # Adjust the width
                title="Distribution of Fireplace Quality"
            )
            st.plotly_chart(fig_donut_chart3)
        else:
            average_value3 = 0
            title_text3 = "Average Value"

        # Create a smaller gauge chart
        fig_quality3 = go.Figure(go.Indicator(
            mode="gauge+number",
            value=average_value3,
            title={"text": title_text3},
            gauge={
                "axis": {"range": [0, 10]},
                "steps": [
                    {"range": [0, 4], "color": "lightgray"},
                    {"range": [4, 7], "color": "lightgreen"},
                    {"range": [7, 10], "color": "lightblue"},
                ],
            },
        ))

        fig_quality3.update_layout(height=250, width=250)  # Adjust the size

        # Display the gauge chart
        st.plotly_chart(fig_quality3)

    with col4:
        st.subheader("Dwelling")
        selected_feature4 = st.selectbox("Select a Dwelling Feature", [
            'Type of Dwelling',
            'Style of Dwelling'
        ], key="feature4")

        # Slider for selecting price ranges for the first feature
        price_range4 = st.slider("Price Range", 
            min_value=int(df_copy['SalePrice'].min()), 
            max_value=int(df_copy['SalePrice'].max()), 
            step=1000, 
            value=(int(df_copy['SalePrice'].min()), int(df_copy['SalePrice'].max())), 
            key="price_range4"
        )
        # Slider for selecting Original Construction Date for the first feature
        original_construction_date_range_4 = st.slider("Original Construction Date",
            min_value=int(df_copy['Original Construction Date'].min()),
            max_value=int(df_copy['Original Construction Date'].max()),
            value=(int(df_copy['Original Construction Date'].min()), int(df_copy['Original Construction Date'].max())),
            key="original_construction_date_range_4",
            step=None  # Ensure only one dragger
        )
        # Slider for selecting Remodel Date for the first feature
        remodel_date_range_4 = st.slider("Remodel Date",
            min_value=int(df_copy['Remodel Date'].min()),
            max_value=int(df_copy['Remodel Date'].max()),
            value=(int(df_copy['Remodel Date'].min()), int(df_copy['Remodel Date'].max())),
            key="remodel_date_range_4",
            step=None  # Ensure only one dragger
        )

        # Filter the data based on the selected criteria
        filtered_data4 = df_copy[
            (df_copy['SalePrice'] >= price_range4[0]) &
            (df_copy['SalePrice'] <= price_range4[1]) &
            (df_copy['Original Construction Date'] >= original_construction_date_range_4[0]) &
            (df_copy['Original Construction Date'] <= original_construction_date_range_4[1]) &
            (df_copy['Remodel Date'] >= remodel_date_range_4[0]) &
            (df_copy['Remodel Date'] <= remodel_date_range_4[1])
        ]

        # Create a frequency count of the selected feature and neighborhood
        feature_counts4 = filtered_data4.groupby([selected_feature4, 'Neighborhood']).size().reset_index()
        feature_counts4.columns = [selected_feature4, 'Neighborhood', 'Frequency']

        # Get the top 10 neighborhoods based on frequency for the selected feature and price range
        top_neighborhoods4 = feature_counts4.groupby('Neighborhood').sum().nlargest(10, 'Frequency').index

        # Filter data to include only the top 10 neighborhoods for the selected feature and price range
        filtered_feature_counts4 = feature_counts4[(feature_counts4['Neighborhood'].isin(top_neighborhoods4)) & (feature_counts4[selected_feature4] != 'N/A')]

        # Create a stacked bar chart using Plotly Express
        fig4 = px.bar(
            filtered_feature_counts4,
            x=selected_feature4,
            y='Frequency',
            color='Neighborhood',  # Color by neighborhood
            barmode='stack',  # Create a stacked bar chart
            labels={'x': selected_feature4, 'Frequency': 'Frequency'},
            title=f"Top Neighborhoods for {selected_feature4}",
        )

        # Display the stacked bar chart
        st.plotly_chart(fig4)

    # Create two columns with equal width to place the graphs side by side
    col5, col6 = st.columns(2)

    with col5:
        st.subheader("Rooms")
        selected_feature5 = st.selectbox("Select a Room Feature", [
            'Total Number of Full Bathrooms',
            'Total Number of Half Bathrooms',
            'Total Rooms Above Grade (Does Not Include Bathrooms)'
        ], key="feature5")

        price_range5 = st.slider("Price Range", min_value=int(df_copy['SalePrice'].min()), max_value=int(df_copy['SalePrice'].max()), step=1000, value=(int(df_copy['SalePrice'].min()), int(df_copy['SalePrice'].max())), key="price_range5")
        original_construction_date_range_5 = st.slider("Original Construction Date Range", int(df_copy['Original Construction Date'].min()), int(df_copy['Original Construction Date'].max()), (int(df_copy['Original Construction Date'].min()), int(df_copy['Original Construction Date'].max())), key="original_construction_date_range5")
        remodel_date_range_5 = st.slider("Remodel Date Range", int(df_copy['Remodel Date'].min()), int(df_copy['Remodel Date'].max()), (int(df_copy['Remodel Date'].min()), int(df_copy['Remodel Date'].max())), key="remodel_date_range5")

        # Filter the data based on the selected criteria for the fifth graph
        filtered_data5 = df_copy[
            (df_copy['SalePrice'] >= price_range5[0]) &
            (df_copy['SalePrice'] <= price_range5[1]) &
            (df_copy['Original Construction Date'] >= original_construction_date_range_5[0]) &
            (df_copy['Original Construction Date'] <= original_construction_date_range_5[1]) &
            (df_copy['Remodel Date'] >= remodel_date_range_5[0]) &
            (df_copy['Remodel Date'] <= remodel_date_range_5[1])
        ]

        # Create a frequency count of the selected feature and neighborhood for the fifth graph
        feature_counts5 = filtered_data5.groupby([selected_feature5, 'Neighborhood']).size().reset_index()
        feature_counts5.columns = [selected_feature5, 'Neighborhood', 'Frequency']

        # Get the top 10 neighborhoods based on frequency for the selected feature and price range for the fifth graph
        top_neighborhoods5 = feature_counts5.groupby('Neighborhood').sum().nlargest(10, 'Frequency').index

        # Filter data to include only the top 10 neighborhoods for the selected feature and price range for the fifth graph
        filtered_feature_counts5 = feature_counts5[(feature_counts5['Neighborhood'].isin(top_neighborhoods5)) & (feature_counts5[selected_feature5] != 'N/A')]

        # Create a stacked bar chart using Plotly Express for the fifth feature
        fig5 = px.bar(
            filtered_feature_counts5,
            x=selected_feature5,
            y='Frequency',
            color='Neighborhood',  # Color by neighborhood
            barmode='stack',  # Create a stacked bar chart
            labels={'x': selected_feature5, 'Frequency': 'Frequency'},
            title=f"Top Neighborhoods for {selected_feature5}",
        )

        # Display the fifth stacked bar chart
        st.plotly_chart(fig5)

    with col6:
        st.subheader("Unique Features")
        selected_feature6 = st.selectbox("Select a Unique Feature", [
            'Pool Quality',
            'Fence Quality',
            'Flatness of the Property',
            'Miscellaneous Feature',
            'General Shape of Property'
        ], key="feature6")

        price_range6 = st.slider("Price Range", min_value=int(df_copy['SalePrice'].min()), max_value=int(df_copy['SalePrice'].max()), step=1000, value=(int(df_copy['SalePrice'].min()), int(df_copy['SalePrice'].max())), key="price_range6")
        original_construction_date_range_6 = st.slider("Original Construction Date Range", int(df_copy['Original Construction Date'].min()), int(df_copy['Original Construction Date'].max()), (int(df_copy['Original Construction Date'].min()), int(df_copy['Original Construction Date'].max())), key="original_construction_date_range_6")
        remodel_date_range_6 = st.slider("Remodel Date Range", int(df_copy['Remodel Date'].min()), int(df_copy['Remodel Date'].max()), (int(df_copy['Remodel Date'].min()), int(df_copy['Remodel Date'].max())), key="remodel_date_range_6")

        # Filter the data based on the selected criteria for the sixth graph
        filtered_data6 = df_copy[
            (df_copy['SalePrice'] >= price_range6[0]) &
            (df_copy['SalePrice'] <= price_range6[1]) &
            (df_copy['Original Construction Date'] >= original_construction_date_range_6[0]) &
            (df_copy['Original Construction Date'] <= original_construction_date_range_6[1]) &
            (df_copy['Remodel Date'] >= remodel_date_range_6[0]) &
            (df_copy['Remodel Date'] <= remodel_date_range_6[1])
        ]

        # Create a frequency count of the selected feature and neighborhood for the sixth graph
        feature_counts6 = filtered_data6.groupby([selected_feature6, 'Neighborhood']).size().reset_index()
        feature_counts6.columns = [selected_feature6, 'Neighborhood', 'Frequency']

        # Get the top 10 neighborhoods based on frequency for the selected feature and price range for the fifth graph
        top_neighborhoods6 = feature_counts6.groupby('Neighborhood').sum().nlargest(10, 'Frequency').index

        # Filter data to include only the top 10 neighborhoods for the selected feature and price range for the fifth graph
        filtered_feature_counts6 = feature_counts6[(feature_counts6['Neighborhood'].isin(top_neighborhoods6)) & (feature_counts6[selected_feature6] != 'N/A')]


        # Create a stacked bar chart using Plotly Express for the sixth feature
        fig6 = px.bar(
            filtered_feature_counts6,
            x=selected_feature6,
            y='Frequency',
            color='Neighborhood',  # Color by neighborhood
            barmode='stack',  # Create a stacked bar chart
            labels={'x': selected_feature6, 'Frequency': 'Frequency'},
            title=f"Neighborhoods for {selected_feature6}",
        )

        # Display the sixth stacked bar chart
        st.plotly_chart(fig6)

    st.write("---")

    col7, col8 = st.columns(2)

    with col7:
        st.subheader("Indoor Size")
        selected_feature7 = st.selectbox("Select an Indoor Size Feature", [
            'Total Finished Basement Area (in Square Feet)',
            'Unfinished Basement Area (in Square Feet)',
            'Total Basement Area (in Square Feet)',
            'Above Grade (Ground) Living Area (in Square Feet)',
        ], key="feature7")

        price_range7 = st.slider("Price Range", min_value=int(df_copy['SalePrice'].min()), max_value=int(df_copy['SalePrice'].max()), step=1000, value=(int(df_copy['SalePrice'].min()), int(df_copy['SalePrice'].max())), key="price_range7")
        original_construction_date_range_7 = st.slider("Original Construction Date Range", int(df_copy['Original Construction Date'].min()), int(df_copy['Original Construction Date'].max()), (int(df_copy['Original Construction Date'].min()), int(df_copy['Original Construction Date'].max())), key="original_construction_date_range_7")
        remodel_date_range_7 = st.slider("Remodel Date Range", int(df_copy['Remodel Date'].min()), int(df_copy['Remodel Date'].max()), (int(df_copy['Remodel Date'].min()), int(df_copy['Remodel Date'].max())), key="remodel_date_range_7")

        # Filter the data based on the selected criteria for the seventh graph
        filtered_data7 = df_copy[
            (df_copy['SalePrice'] >= price_range7[0]) &
            (df_copy['SalePrice'] <= price_range7[1]) &
            (df_copy['Original Construction Date'] >= original_construction_date_range_7[0]) &
            (df_copy['Original Construction Date'] <= original_construction_date_range_7[1]) &
            (df_copy['Remodel Date'] >= remodel_date_range_7[0]) &
            (df_copy['Remodel Date'] <= remodel_date_range_7[1])
        ]

        # Create a frequency count of the selected feature and neighborhood for the seventh graph
        feature_counts7 = filtered_data7.groupby([selected_feature7, 'Neighborhood']).size().reset_index()
        feature_counts7.columns = [selected_feature7, 'Neighborhood', 'Frequency']

        # Get the top 10 neighborhoods based on frequency for the selected feature and price range for the seventh graph
        top_neighborhoods7 = feature_counts7.groupby('Neighborhood').sum().nlargest  (10, 'Frequency').index

        # Filter data to include only the top 10 neighborhoods for the selected feature and price range for the seventh graph
        filtered_feature_counts7 = feature_counts7[(feature_counts7['Neighborhood'].isin(top_neighborhoods7)) & (feature_counts7[selected_feature7] != 'N/A')]

        # Create a histogram using Plotly Express for the seventh feature
        fig7 = px.histogram(
            filtered_feature_counts7,
            x=selected_feature7,
            color='Neighborhood',  # Color by neighborhood
            labels={'x': selected_feature7, 'Frequency': 'Frequency'},
            title=f"Top Neighborhoods for {selected_feature7}",
        )

        # Update the axis labels
        fig7.update_xaxes(title_text=selected_feature7)
        fig7.update_yaxes(title_text='Frequency')
        fig7.update_layout(width=600, height=450)  # Adjust the width and height as needed

        # Display the seventh stacked bar chart
        st.plotly_chart(fig7)

        # Calculate the sum of 1stFlrSF, 2ndFlrSF, and LowQualFinSF
        total_type_finished = filtered_data7['Type 1 Finished (in Square Feet)'] + filtered_data7['Type 2 Finished (in Square Feet)']

        # Calculate the ratio of the sum of Type 1 and Type 2 Finished to Total Basement Area
        basement_ratio = (total_type_finished / df['TotalBsmtSF']).mean() * 100
        basement_ratio = round(basement_ratio, 2)

        data_pie_chart = {'Variable': ['Finished Basement Area', 'Unfinished Basement Area'],
                'Count': [basement_ratio, 100 - basement_ratio]}

        # Create a pie chart using Plotly Express
        fig_pie = px.pie(data_pie_chart, names='Variable', values='Count', title='Pecentage of Finished/Unfinished Basement Area')

        # Turn the pie chart into a donut chart by setting the hole parameter
        fig_pie.update_traces(hole=0.4)  # Adjust the hole size (0.4 makes it a donut)

        # Adjust the size of the pie chart
        fig_pie.update_layout(width=350, height=350)  # Adjust the size
        fig_pie.update_layout(title_font=dict(size=15))  # Adjust the title text size

        # Display the donut chart
        st.plotly_chart(fig_pie)

        # Calculate the count of each variable for the filtered data
        first_floor = (filtered_data7['First Floor (in Square Feet)'] != 0).sum()
        second_floor = (filtered_data7['Second Floor (in Square Feet)'] != 0).sum()
        finished_area = (filtered_data7['Low-Quality Finished Area (in Square Feet)'] != 0).sum()

        # Create a DataFrame for the pie chart data
        data_pie_chart = {
            'Variable': ['First Floor', 'Second Floor', 'Low-Quality Finished Floor'],
            'Count': [first_floor, second_floor, finished_area]
        }

        # Create a pie chart using Plotly Express
        fig_pie = px.pie(data_pie_chart, names='Variable', values='Count', title='Distribution of Ground Floors')

        # Turn the pie chart into a donut chart by setting the hole parameter
        fig_pie.update_traces(hole=0.4)  # Adjust the hole size (0.4 makes it a donut)

        # Adjust the size of the pie chart
        fig_pie.update_layout(width=350, height=350)  # Adjust the size
        fig_pie.update_layout(title_font=dict(size=15))  # Adjust the title text size

        # Display the donut chart
        st.plotly_chart(fig_pie)
    
    with col8:
        st.subheader("Outdoor Size")
        selected_feature8 = st.selectbox("Select an Outdoor Size Feature", [
            'Lot Size (in Square Feet)',
            'Wood Deck Area (in Square Feet)',
            'Open Porch Area (in Square Feet)',
            'Enclosed Porch Area (in Square Feet)',
            'Three Season Porch Area (in Square Feet)',
            'Screen Porch Area (in Square Feet)',
            'Pool Area (in Square Feet)',
        ], key="feature8")

        price_range8 = st.slider("Price Range", min_value=int(df_copy['SalePrice'].min()), max_value=int(df_copy['SalePrice'].max()), step=1000, value=(int(df_copy['SalePrice'].min()), int(df_copy['SalePrice'].max())), key="price_range8")
        original_construction_date_range_8 = st.slider("Original Construction Date Range", int(df_copy['Original Construction Date'].min()), int(df_copy['Original Construction Date'].max()), (int(df_copy['Original Construction Date'].min()), int(df_copy['Original Construction Date'].max())), key="original_construction_date_range_8")
        remodel_date_range_8 = st.slider("Remodel Date Range", int(df_copy['Remodel Date'].min()), int(df_copy['Remodel Date'].max()), (int(df_copy['Remodel Date'].min()), int(df_copy['Remodel Date'].max())), key="remodel_date_range_8")

        # Filter the data based on the selected criteria for the eighth graph
        filtered_data8 = df_copy[
            (df_copy['SalePrice'] >= price_range8[0]) &
            (df_copy['SalePrice'] <= price_range8[1]) &
            (df_copy['Original Construction Date'] >= original_construction_date_range_8[0]) &
            (df_copy['Original Construction Date'] <= original_construction_date_range_8[1]) &
            (df_copy['Remodel Date'] >= remodel_date_range_8[0]) &
            (df_copy['Remodel Date'] <= remodel_date_range_8[1])
        ]

        # Create a frequency count of the selected feature and neighborhood for the eighth graph
        feature_counts8 = filtered_data8.groupby([selected_feature8, 'Neighborhood']).size().reset_index()
        feature_counts8.columns = [selected_feature8, 'Neighborhood', 'Frequency']

        # Get the top 10 neighborhoods based on frequency for the selected feature and price range for the eighth graph
        top_neighborhoods8 = feature_counts8.groupby('Neighborhood').sum().nlargest(10, 'Frequency').index

        # Filter data to include only the top 10 neighborhoods for the selected feature and price range for the eighth graph
        filtered_feature_counts8 = feature_counts8[(feature_counts8['Neighborhood'].isin(top_neighborhoods8)) & (feature_counts8[selected_feature8] != 'N/A')]

        # Create a histogram using Plotly Express for the eighth feature
        fig8 = px.histogram(
            filtered_feature_counts8,
            x=selected_feature8,
            color='Neighborhood',  # Color by neighborhood
            labels={'x': selected_feature8, 'Frequency': 'Frequency'},
            title=f"Top Neighborhoods for {selected_feature8}",
        )

        # Update the axis labels
        fig8.update_xaxes(title_text=selected_feature8)
        fig8.update_yaxes(title_text='Frequency')
        fig8.update_layout(width=600, height=450)  # Adjust the width and height as needed

        # Display the eighth stacked bar chart
        st.plotly_chart(fig8)

        # Calculate the count of each variable for the filtered data
        count_wood_deck = (filtered_data8['Wood Deck Area (in Square Feet)'] != 0).sum()
        count_open_porch = (filtered_data8['Open Porch Area (in Square Feet)'] != 0).sum()
        count_enclosed_porch = (filtered_data8['Enclosed Porch Area (in Square Feet)'] != 0).sum()
        count_three_season_porch = (filtered_data8['Three Season Porch Area (in Square Feet)'] != 0).sum()
        count_screen_porch = (filtered_data8['Screen Porch Area (in Square Feet)'] != 0).sum()

        # Create a DataFrame for the pie chart data
        data_pie_chart = {
            'Variable': ['Wood Deck', 'Open Porch', 'Enclosed Porch', 'Three Season Porch', 'Screen Porch'],
            'Count': [count_wood_deck, count_open_porch, count_enclosed_porch, count_three_season_porch, count_screen_porch]
        }

        # Create a pie chart using Plotly Express
        fig_pie = px.pie(data_pie_chart, names='Variable', values='Count', title='Distribution of Porch Counts')

        # Turn the pie chart into a donut chart by setting the hole parameter
        fig_pie.update_traces(hole=0.4)  # Adjust the hole size (0.4 makes it a donut)

        # Adjust the size of the pie chart
        fig_pie.update_layout(width=430, height=430)  # Adjust the size

        fig_pie.update_layout(title_font=dict(size=15))  # Adjust the title text size

        # Display the donut chart
        st.plotly_chart(fig_pie)

df_copy_yearstring = df.copy()

# List of columns to replace using the abbreviations map
columns_to_replace = ['Neighborhood', 'MSZoning', 'LandContour', 'LotShape', 'LotConfig',
                      'Condition1', 'BldgType', 'HouseStyle', 'RoofMatl', 'ExterQual', 'Foundation', 'ExterCond',
                      'BsmtQual', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2',
                      'HeatingQC', 'KitchenQual', 'FireplaceQu',
                      'GarageType', 'GarageFinish', 'GarageQual', 'GarageCond',
                      'Fence', 'MiscFeature',
                      'SaleType', 'SaleCondition',
                      'PoolQC'
                      ]
df_copy_yearstring[columns_to_replace] = df_copy_yearstring[columns_to_replace].replace(abbreviations_map)

# Fill missing values with 'N/A'
df_copy_yearstring = df_copy_yearstring.fillna('N/A')
df_copy_yearstring = df_copy_yearstring.rename(columns=new_column_names)

# Remove commas from the 'Original Construction Date' and 'Remodel Date' columns
df_copy_yearstring['Original Construction Date'] = df_copy_yearstring['Original Construction Date'].apply(lambda x: str(x).replace(',', ''))
df_copy_yearstring['Remodel Date'] = df_copy_yearstring['Remodel Date'].apply(lambda x: str(x).replace(',', ''))

if selected_tab == "Sales Analysis":
    # Content for the Sales Analysis tab
    st.header("Sales Analysis Tab")
    st.write("This is the Sales Analysis tab content.")

    # Display the loaded data in an expander for data preview
    with st.expander("Data Preview"):
        st.dataframe(df_copy_yearstring)

    # Create a slider for selecting a price range with two draggers
    price_range = st.slider("Price Range", min_value=int(df_copy_yearstring['SalePrice'].min()), max_value=int(df_copy_yearstring['SalePrice'].max()), value=(int(df_copy_yearstring['SalePrice'].min()), int(df_copy_yearstring['SalePrice'].max())), step=1000)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Construction Date Frequency")
        original_construction_counts = df_copy_yearstring[(df_copy_yearstring['SalePrice'] >= price_range[0]) & (df_copy_yearstring['SalePrice'] <= price_range[1])].groupby('Original Construction Date').size().reset_index()
        original_construction_counts.columns = ['Original Construction Date', 'Frequency']

        # Create a line chart using Plotly Express
        fig_original_construction = px.line(original_construction_counts, x='Original Construction Date', y='Frequency', labels={'Original Construction Date': 'Year', 'Frequency': 'Frequency'})
        # Customize x-axis rotation, tick values, and graph size
        fig_original_construction.update_layout(
            xaxis_tickangle=45,
            xaxis_dtick=10,  # Show every 5th year
            width=600,  # Adjust the width
            height=400  # Adjust the height
        )

        # Add data points
        fig_original_construction.add_trace(px.scatter(original_construction_counts, x='Original Construction Date', y='Frequency').data[0])

        st.plotly_chart(fig_original_construction)

    with col2:
        st.subheader("Remodel Date Frequency")
        remodel_date_counts = df_copy_yearstring[(df_copy_yearstring['SalePrice'] >= price_range[0]) & (df_copy_yearstring['SalePrice'] <= price_range[1])].groupby('Remodel Date').size().reset_index()
        remodel_date_counts.columns = ['Remodel Date', 'Frequency']

        # Create a line chart using Plotly Express
        fig_remodel_date = px.line(remodel_date_counts, x='Remodel Date', y='Frequency', labels={'Remodel Date': 'Year', 'Frequency': 'Frequency'})
        # Customize x-axis rotation, tick values, and graph size
        fig_remodel_date.update_layout(
            xaxis_tickangle=45,
            xaxis_dtick=5,  # Show every 5th year
            width=600,  # Adjust the width
            height=400  # Adjust the height
        )

        # Add data points
        fig_remodel_date.add_trace(px.scatter(remodel_date_counts, x='Remodel Date', y='Frequency').data[0])

        st.plotly_chart(fig_remodel_date)

    st.write("---")

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Original Construction Date Average Sale Price")
        year_sold_price = df_copy_yearstring[(df_copy_yearstring['SalePrice'] >= price_range[0]) & (df_copy_yearstring['SalePrice'] <= price_range[1])]
        year_sold_price = year_sold_price.groupby('Original Construction Date')['SalePrice'].mean().reset_index()
        fig_year_sold_price = px.line(year_sold_price, x='Original Construction Date', y='SalePrice', labels={'Original Construction Date': 'Original Construction Date', 'SalePrice': 'Average Sale Price'})

        # Add data points as a scatter plot
        fig_year_sold_price.add_trace(px.scatter(year_sold_price, x='Original Construction Date', y='SalePrice').data[0])

        st.plotly_chart(fig_year_sold_price)

    with col4:
        st.subheader("Remodel Date Average Sale Price")
        year_sold_price = df_copy_yearstring[(df_copy_yearstring['SalePrice'] >= price_range[0]) & (df_copy_yearstring['SalePrice'] <= price_range[1])]
        year_sold_price = year_sold_price.groupby('Remodel Date')['SalePrice'].mean().reset_index()
        fig_year_sold_price = px.line(year_sold_price, x='Remodel Date', y='SalePrice', labels={'Remodel Date': 'Remodel Date', 'SalePrice': 'Average Sale Price'})

        # Add data points as a scatter plot
        fig_year_sold_price.add_trace(px.scatter(year_sold_price, x='Remodel Date', y='SalePrice').data[0])

        st.plotly_chart(fig_year_sold_price)

    st.write("---")

    col5, col6 = st.columns(2)

    with col5:
        st.subheader("Original Construction Date Average Sale Price by Neighborhood")
        selected_neighborhood_orig = st.selectbox("Select Neighborhood for Original Construction Date", df_copy_yearstring['Neighborhood'].unique())
        original_construction_price = df_copy_yearstring[(df_copy_yearstring['SalePrice'] >= price_range[0]) & (df_copy_yearstring['SalePrice'] <= price_range[1]) & (df_copy_yearstring['Neighborhood'] == selected_neighborhood_orig)]
        original_construction_price = original_construction_price.groupby('Original Construction Date')['SalePrice'].mean().reset_index()
        fig_original_construction_price = px.line(original_construction_price, x='Original Construction Date', y='SalePrice', labels={'Original Construction Date': 'Year', 'SalePrice': 'Average Sale Price'})

        # Add data points as a scatter plot
        fig_original_construction_price.add_trace(px.scatter(original_construction_price, x='Original Construction Date', y='SalePrice').data[0])

        # Customize x-axis tick values to show every 5th year
        fig_original_construction_price.update_xaxes(
            dtick=5  # Show every 5th year
        )

        st.plotly_chart(fig_original_construction_price)

    with col6:
        st.subheader("Remodel Date Average Sale Price by Neighborhood")
        selected_neighborhood_remodel = st.selectbox("Select Neighborhood for Remodel Date", df_copy_yearstring['Neighborhood'].unique())
        remodel_price = df_copy_yearstring[(df_copy_yearstring['SalePrice'] >= price_range[0]) & (df_copy_yearstring['SalePrice'] <= price_range[1]) & (df_copy_yearstring['Neighborhood'] == selected_neighborhood_remodel)]
        remodel_price = remodel_price.groupby('Remodel Date')['SalePrice'].mean().reset_index()
        fig_remodel_price = px.line(remodel_price, x='Remodel Date', y='SalePrice', labels={'Remodel Date': 'Year', 'SalePrice': 'Average Sale Price'})

        # Add data points as a scatter plot
        fig_remodel_price.add_trace(px.scatter(remodel_price, x='Remodel Date', y='SalePrice').data[0])

        # Customize x-axis tick values to show every 5th year
        fig_remodel_price.update_xaxes(
            dtick=5  # Show every 5th year
        )

        st.plotly_chart(fig_remodel_price)

    st.write("---")    

    # Create a slider to control the price range for all graphs
    price_range = st.slider(
        "Price Range",
        min_value=int(df_copy_yearstring['SalePrice'].min()),
        max_value=int(df_copy_yearstring['SalePrice'].max()),
        value=(int(df_copy_yearstring['SalePrice'].min()), int(df_copy_yearstring['SalePrice'].max()))
    )

    # Create a single row container for all graphs
    col7, col8 = st.columns(2)

    with col7:
        st.subheader("Month Sold Frequency")
        month_sold_counts = df_copy_yearstring[(df_copy_yearstring['SalePrice'] >= price_range[0]) & (df_copy_yearstring['SalePrice'] <= price_range[1])].groupby('Month Sold').size().reset_index()
        month_sold_counts.columns = ['Month Sold', 'Frequency']

        # Create a line chart using Plotly Express
        fig_month_sold = px.line(month_sold_counts, x='Month Sold', y='Frequency', labels={'Month Sold': 'Month', 'Frequency': 'Frequency'})

        # Customize x-axis rotation, tick values, and graph size
        fig_month_sold.update_layout(
            xaxis_tickangle=-45,  # No rotation
            width=600,  # Adjust the width
            height=400  # Adjust the height
        )

        # Convert integer month values to month names
        month_names = [calendar.month_name[i] for i in range(1, 13)]

        # Set custom tickvals and ticktext for the x-axis
        fig_month_sold.update_xaxes(
            tickvals=list(range(1, 13)),  # Integer values for months
            ticktext=month_names,  # Corresponding month names
        )

        # Add data points
        fig_month_sold.add_trace(px.scatter(month_sold_counts, x='Month Sold', y='Frequency').data[0])

        st.plotly_chart(fig_month_sold)

    with col8:
        st.subheader("Year Sold Frequency")
        year_sold_counts = df_copy_yearstring[(df_copy_yearstring['SalePrice'] >= price_range[0]) & (df_copy_yearstring['SalePrice'] <= price_range[1])].groupby('Year Sold').size().reset_index()
        year_sold_counts.columns = ['Year Sold', 'Frequency']

        # Create a line chart using Plotly Express
        fig_year_sold = px.line(year_sold_counts, x='Year Sold', y='Frequency', labels={'Year Sold': 'Year', 'Frequency': 'Frequency'})

        # Customize x-axis rotation, tick values, and graph size
        fig_year_sold.update_layout(
            xaxis_tickangle=0,
            width=600,  # Adjust the width
            height=400  # Adjust the height
        )

        # Set custom category order for the x-axis
        custom_order = list(range(2006, 2011))
        fig_year_sold.update_xaxes(categoryarray=custom_order)

        # Add data points
        fig_year_sold.add_trace(px.scatter(year_sold_counts, x='Year Sold', y='Frequency').data[0])

        st.plotly_chart(fig_year_sold)

    col9, col10 = st.columns(2)

    with col9:
        st.subheader("Month Sold Average Sale Price")
        year_sold_price = df_copy_yearstring[(df_copy_yearstring['SalePrice'] >= price_range[0]) & (df_copy_yearstring['SalePrice'] <= price_range[1])]
        year_sold_price = year_sold_price.groupby('Month Sold')['SalePrice'].mean().reset_index()
        fig_year_sold_price = px.line(year_sold_price, x='Month Sold', y='SalePrice', labels={'Month Sold': 'Month Sold', 'SalePrice': 'Average Sale Price'})

        # Customize x-axis rotation, tick values, and graph size
        fig_year_sold_price.update_layout(
            xaxis_tickangle=-45,  # No rotation
            width=600,  # Adjust the width
            height=400  # Adjust the height
        )

        # Convert integer month values to month names
        month_names = [calendar.month_name[i] for i in range(1, 13)]

        # Set custom tickvals and ticktext for the x-axis
        fig_year_sold_price.update_xaxes(
            tickvals=list(range(1, 13)),  # Integer values for months
            ticktext=month_names,  # Corresponding month names
        )

        # Add data points
        fig_year_sold_price.add_trace(px.scatter(year_sold_price, x='Month Sold', y='SalePrice').data[0])

        st.plotly_chart(fig_year_sold_price)

    with col10:
        st.subheader("Year Sold Average Sale Price")
        year_sold_price = df_copy_yearstring[(df_copy_yearstring['SalePrice'] >= price_range[0]) & (df_copy_yearstring['SalePrice'] <= price_range[1])]
        year_sold_price = year_sold_price.groupby('Year Sold')['SalePrice'].mean().reset_index()
        fig_year_sold_price = px.line(year_sold_price, x='Year Sold', y='SalePrice', labels={'Year Sold': 'Year Sold', 'SalePrice': 'Average Sale Price'})

        # Add data points as a scatter plot
        fig_year_sold_price.add_trace(px.scatter(year_sold_price, x='Year Sold', y='SalePrice').data[0])

        st.plotly_chart(fig_year_sold_price)

    st.write("---")

    col11, col12 = st.columns(2)

    with col11:
        st.subheader("Month Sold Average Sale Price by Neighborhood")
        selected_neighborhood_month = st.selectbox("Select Neighborhood for Month Sold", df_copy_yearstring['Neighborhood'].unique())
        month_sold_price = df_copy_yearstring[(df_copy_yearstring['SalePrice'] >= price_range[0]) & (df_copy_yearstring['SalePrice'] <= price_range[1]) & (df_copy_yearstring['Neighborhood'] == selected_neighborhood_month)]
        month_sold_price = month_sold_price.groupby('Month Sold')['SalePrice'].mean().reset_index()
        fig_month_sold_price = px.line(month_sold_price, x='Month Sold', y='SalePrice', labels={'Month Sold': 'Month', 'SalePrice': 'Average Sale Price'})

        # Customize x-axis rotation, tick values, and graph size
        fig_month_sold_price.update_layout(
            xaxis_tickangle=-45,  # Rotate the x-axis labels by 45 degrees
            width=600,  # Adjust the width
            height=400  # Adjust the height
        )

        # Convert integer month values to month names
        month_names = [calendar.month_name[i] for i in range(1, 13)]

        # Set custom tickvals and ticktext for the x-axis
        fig_month_sold_price.update_xaxes(
            tickvals=list(range(1, 13)),  # Integer values for months
            ticktext=month_names,  # Corresponding month names
        )

        # Add data points as a scatter plot
        fig_month_sold_price.add_trace(px.scatter(month_sold_price, x='Month Sold', y='SalePrice').data[0])

        st.plotly_chart(fig_month_sold_price)

    with col12:
        st.subheader("Year Sold Average Sale Price by Neighborhood")
        selected_neighborhood_year = st.selectbox("Select Neighborhood for Year Sold", df_copy_yearstring['Neighborhood'].unique())
        year_sold_price = df_copy_yearstring[(df_copy_yearstring['SalePrice'] >= price_range[0]) & (df_copy_yearstring['SalePrice'] <= price_range[1]) & (df_copy_yearstring['Neighborhood'] == selected_neighborhood_year)]
        year_sold_price = year_sold_price.groupby('Year Sold')['SalePrice'].mean().reset_index()
        fig_year_sold_price = px.line(year_sold_price, x='Year Sold', y='SalePrice', labels={'Year Sold': 'Year', 'SalePrice': 'Average Sale Price'})

        # Add data points as a scatter plot
        fig_year_sold_price.add_trace(px.scatter(year_sold_price, x='Year Sold', y='SalePrice').data[0])

        st.plotly_chart(fig_year_sold_price)

    st.write("---")
