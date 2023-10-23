import random
import duckdb
import math
import pandas as pd
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

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
                      'MoSold', 'SaleType', 'SaleCondition'
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
    'MiscFeature': 'Miscellaneous Feature Not Covered in Other Categories',
    'MiscVal': 'Value of Miscellaneous Feature',

    'MoSold': 'Month Sold',
    'YrSold': 'Year Sold',
    'SaleType': 'Type of Sale',
    'SaleCondition': 'Condition of Sale'
}
# Convert 'LotFrontage' column to float, replacing 'N/A' with NaN
df_copy['LotFrontage'] = pd.to_numeric(df_copy['LotFrontage'], errors='coerce')
df_copy['MasVnrArea'] = pd.to_numeric(df_copy['MasVnrArea'], errors='coerce')
df_copy['GarageYrBlt'] = pd.to_numeric(df_copy['GarageYrBlt'], errors='coerce')
df_copy = df_copy.rename(columns=new_column_names)

# Depending on the selected tab, display different content
if selected_tab == "Home":
    # Content for the Property tab
    st.header("Home")
    st.write("This is the Home tab content.")
    # Display the loaded data in an expander for data preview
    with st.expander("Data Preview"):
        st.dataframe(df_copy)

    # Create a frequency count of each neighborhood
    neighborhood_counts = df_copy['Neighborhood'].value_counts()
    
    # Create a bar chart using Plotly Express
    fig = px.bar(
        x=neighborhood_counts.index,
        y=neighborhood_counts.values,
        labels={'x': 'Neighborhood', 'y': 'Frequency'},
        title="Neighborhood Frequency Analysis",
    )

    st.plotly_chart(fig)
    

elif selected_tab == "Property and Building Analysis":
    # Content for the Building tab
    st.header("Property and Building Analysis")
    st.write("This is the Property and Building Analysis tab content.")
    # Display the loaded data in an expander for data preview
    with st.expander("Data Preview"):
        st.dataframe(df_copy)

    # Create two columns with equal width to place the graphs side by side
    col1, col2 = st.columns(2)
    
    # Add a horizontal rule to create spacing
    st.write("---")
    
    # Dropdown for selecting the first feature in the first column
    with col1:
        selected_feature1 = st.selectbox("Select a Property Assessment Metrics Feature", [
            "Overall Material and Finish Quality",
            "Overall Condition Rating"
        ], key="feature1")

        # Slider for selecting price ranges for the first feature
        price_range1 = st.slider("Price Range for Property Assessment Metrics", min_value=int(df_copy['SalePrice'].min()), max_value=int(df_copy['SalePrice'].max()), step=1000, value=(int(df_copy['SalePrice'].min()), int(df_copy['SalePrice'].max())), key="price_range1")

        # Slider for selecting Original Construction Date
        original_construction_date = st.slider("Original Construction Date Range for Dwelling", int(df_copy['Original Construction Date'].min()), int(df_copy['Original Construction Date'].max()), (int(df_copy['Original Construction Date'].min()), int(df_copy['Original Construction Date'].max())), key="original_construction_date_range_1")

        # Slider for selecting Remodel Date
        remodel_date = st.slider("Remodel Date Range for Dwelling", int(df_copy['Remodel Date'].min()), int(df_copy['Remodel Date'].max()), (int(df_copy['Remodel Date'].min()), int(df_copy['Remodel Date'].max())), key="remodel_date_range_1")

        # Filter the data based on the selected criteria for the second graph
        filtered_data1 = df_copy[
            (df_copy['SalePrice'] >= price_range1[0]) &
            (df_copy['SalePrice'] <= price_range1[1]) &
            (df_copy['Original Construction Date'] >= original_construction_date[0]) &
            (df_copy['Original Construction Date'] <= original_construction_date[1]) &
            (df_copy['Remodel Date'] >= remodel_date[0]) &
            (df_copy['Remodel Date'] <= remodel_date[1])
        ]

        # Calculate the average value for "Overall Material and Finish Quality"
        average_quality = filtered_data1['Overall Material and Finish Quality'].mean()

        # Calculate the average value for "Overall Condition Rating"
        average_condition = filtered_data1['Overall Condition Rating'].mean()

        # Create a smaller gauge chart for "Overall Material and Finish Quality"
        fig_quality = go.Figure(go.Indicator(
            mode="gauge+number",
            value=average_quality,
            title={"text": "Average Overall Quality"},
            gauge={
                "axis": {"range": [0, 10]},
                "steps": [
                    {"range": [0, 4], "color": "lightgray"},
                    {"range": [4, 7], "color": "lightgreen"},
                    {"range": [7, 10], "color": "lightblue"},
                ],
            },
        ))

        fig_quality.update_layout(height=250, width=250)  # Adjust the size

        # Create a smaller gauge chart for "Overall Condition Rating"
        fig_condition = go.Figure(go.Indicator(
            mode="gauge+number",
            value=average_condition,
            title={"text": "Average Overall Condition"},
            gauge={
                "axis": {"range": [0, 10]},
                "steps": [
                    {"range": [0, 4], "color": "lightgray"},
                    {"range": [4, 7], "color": "lightgreen"},
                    {"range": [7, 10], "color": "lightblue"},
                ],
            },
        ))
        fig_condition.update_layout(height=250, width=250)  # Adjust the size

        # Display the smaller gauge charts in the same row
        st.write('<div style="display: flex;">', unsafe_allow_html=True)
        with col1:
            st.plotly_chart(fig_quality)

        with col1:
            st.plotly_chart(fig_condition)

        st.write('</div>', unsafe_allow_html=True)

    # Dropdown for selecting the second feature in the second column
    with col2:
        selected_feature2 = st.selectbox("Select a Dwelling Feature", [
            'Type of Dwelling',
            'Style of Dwelling'
        ], key="feature2")

        # Slider for selecting price ranges for the second feature
        price_range2 = st.slider("Price Range for Dwelling", min_value=int(df_copy['SalePrice'].min()), max_value=int(df_copy['SalePrice'].max()), step=1000, value=(int(df_copy['SalePrice'].min()), int(df_copy['SalePrice'].max())), key="price_range2")

        # Range slider for selecting Original Construction Date for the second feature
        original_construction_date_range_2 = st.slider("Original Construction Date Range for Dwelling", int(df_copy['Original Construction Date'].min()), int(df_copy['Original Construction Date'].max()), (int(df_copy['Original Construction Date'].min()), int(df_copy['Original Construction Date'].max())), key="original_construction_date_range_2")

        # Range slider for selecting Remodel Date for the second feature
        remodel_date_range_2 = st.slider("Remodel Date Range for Dwelling", int(df_copy['Remodel Date'].min()), int(df_copy['Remodel Date'].max()), (int(df_copy['Remodel Date'].min()), int(df_copy['Remodel Date'].max())), key="remodel_date_range_2")

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

    # Create a new row for the third graph
    #st.write("---")  # Horizontal line to separate rows

    # Create two columns for the third graph
    col3, col4 = st.columns(2)
    
    # Dropdown for selecting the third feature and related controls
    # Dropdown for selecting the fourth feature and related controls
    # Dropdown for selecting the third feature in the first column of the second row
    with col3:

        # Replace 4 with 3 in selected_feature3
        selected_feature3 = st.selectbox("Select a Room Feature", [
            'Total Finished Basement Area (in Square Feet)'
        ], key="feature3")

        # Replace 4 with 3 in price_range3
        price_range3 = st.slider("Price Range for Rooms", min_value=int(df_copy['SalePrice'].min()), max_value=int(df_copy['SalePrice'].max()), step=1000, value=(int(df_copy['SalePrice'].min()), int(df_copy['SalePrice'].max())), key="price_range3")

        # Replace 4 with 3 in original_construction_date_range_3
        original_construction_date_range_3 = st.slider("Original Construction Date Range for Rooms", int(df_copy['Original Construction Date'].min()), int(df_copy['Original Construction Date'].max()), (int(df_copy['Original Construction Date'].min()), int(df_copy['Original Construction Date'].max())), key="original_construction_date_range_3")

        # Replace 4 with 3 in remodel_date_range_3
        remodel_date_range_3 = st.slider("Remodel Date Range for Rooms", int(df_copy['Remodel Date'].min()), int(df_copy['Remodel Date'].max()), (int(df_copy['Remodel Date'].min()), int(df_copy['Remodel Date'].max())), key="remodel_date_range_3")

        # Filter the data based on the selected criteria for the third graph
        filtered_data3 = df_copy[
            (df_copy['SalePrice'] >= price_range3[0]) &
            (df_copy['SalePrice'] <= price_range3[1]) &
            (df_copy['Original Construction Date'] >= original_construction_date_range_3[0]) &
            (df_copy['Original Construction Date'] <= original_construction_date_range_3[1]) &
            (df_copy['Remodel Date'] >= remodel_date_range_3[0]) &
            (df_copy['Remodel Date'] <= remodel_date_range_3[1])
        ]

        # Create a frequency count of the selected feature and neighborhood for the third graph
        feature_counts3 = filtered_data3.groupby([selected_feature3, 'Neighborhood']).size().reset_index()
        feature_counts3.columns = [selected_feature3, 'Neighborhood', 'Frequency']

        # Get the top 10 neighborhoods based on frequency for the selected feature and price range for the third graph
        top_neighborhoods3 = feature_counts3.groupby('Neighborhood').sum().nlargest(10, 'Frequency').index

        # Filter data to include only the top 10 neighborhoods for the selected feature and price range for the third graph
        filtered_feature_counts3 = feature_counts3[(feature_counts3['Neighborhood'].isin(top_neighborhoods3)) & (feature_counts3[selected_feature3] != 'N/A')]

        # Create a histogram using Plotly Express for the third feature
        fig3 = px.histogram(
            filtered_feature_counts3,
            x=selected_feature3,
            color='Neighborhood',  # Color by neighborhood
            labels={'x': selected_feature3, 'Frequency': 'Frequency'},
            title=f"Top Neighborhoods for {selected_feature3}",
        )

        # Display the third stacked bar chart
        st.plotly_chart(fig3)

        # Calculate the sum of Type 1 Finished and Type 2 Finished square feet
        total_type_finished = df['BsmtFinSF1'] + df['BsmtFinSF2']

        # Calculate the ratio of the sum of Type 1 and Type 2 Finished to Total Basement Area
        basement_ratio = (total_type_finished / df['TotalBsmtSF']).mean() * 100
        basement_ratio = round(basement_ratio, 2)

        data = {'Category': ['Finished', 'Unfinished'],
                'Values': [basement_ratio, 100 - basement_ratio]}

        # Create a DataFrame
        df_pie = pd.DataFrame(data)

        # Create a pie chart using Plotly Express
        fig_pie = px.pie(df_pie, names='Category', values='Values', title='Percentage of Finished Basement Area')

        # Adjust the size of the pie chart
        fig_pie.update_layout(width=300, height=300)  # Adjust the size

        # Display the pie chart
        st.plotly_chart(fig_pie)


    # Replace 3 with 4 in variable names in col4
    with col4:
        selected_feature4 = st.selectbox("Select a Room Feature", [
            'Total Number of Full Bathrooms',
            'Total Number of Half Bathrooms',
            'Total Rooms Above Grade (Does Not Include Bathrooms)'
        ], key="feature4")

        # Replace 3 with 4 in variable names
        price_range4 = st.slider("Price Range for Rooms", min_value=int(df_copy['SalePrice'].min()), max_value=int(df_copy['SalePrice'].max()), step=1000, value=(int(df_copy['SalePrice'].min()), int(df_copy['SalePrice'].max())), key="price_range4")

        # Replace 3 with 4 in variable names
        original_construction_date_range_4 = st.slider("Original Construction Date Range for Rooms", int(df_copy['Original Construction Date'].min()), int(df_copy['Original Construction Date'].max()), (int(df_copy['Original Construction Date'].min()), int(df_copy['Original Construction Date'].max())), key="original_construction_date_range_4")

        # Replace 3 with 4 in variable names
        remodel_date_range_4 = st.slider("Remodel Date Range for Rooms", int(df_copy['Remodel Date'].min()), int(df_copy['Remodel Date'].max()), (int(df_copy['Remodel Date'].min()), int(df_copy['Remodel Date'].max())), key="remodel_date_range_4")

        # Filter the data based on the selected criteria for the fourth graph
        filtered_data4 = df_copy[
            (df_copy['SalePrice'] >= price_range4[0]) &
            (df_copy['SalePrice'] <= price_range4[1]) &
            (df_copy['Original Construction Date'] >= original_construction_date_range_4[0]) &
            (df_copy['Original Construction Date'] <= original_construction_date_range_4[1]) &
            (df_copy['Remodel Date'] >= remodel_date_range_4[0]) &
            (df_copy['Remodel Date'] <= remodel_date_range_4[1])
        ]

        # Create a frequency count of the selected feature and neighborhood for the fourth graph
        feature_counts4 = filtered_data4.groupby([selected_feature4, 'Neighborhood']).size().reset_index()
        feature_counts4.columns = [selected_feature4, 'Neighborhood', 'Frequency']

        # Get the top 10 neighborhoods based on frequency for the selected feature and price range for the fourth graph
        top_neighborhoods4 = feature_counts4.groupby('Neighborhood').sum().nlargest(10, 'Frequency').index

        # Filter data to include only the top 10 neighborhoods for the selected feature and price range for the fourth graph
        filtered_feature_counts4 = feature_counts4[(feature_counts4['Neighborhood'].isin(top_neighborhoods4)) & (feature_counts4[selected_feature4] != 'N/A')]

        # Create a stacked bar chart using Plotly Express for the fourth feature
        fig4 = px.bar(
            filtered_feature_counts4,
            x=selected_feature4,
            y='Frequency',
            color='Neighborhood',  # Color by neighborhood
            barmode='stack',  # Create a stacked bar chart
            labels={'x': selected_feature4, 'Frequency': 'Frequency'},
            title=f"Top Neighborhoods for {selected_feature4}",
        )

        # Display the fourth stacked bar chart
        st.plotly_chart(fig4)


    

elif selected_tab == "Sales Analysis":
    # Content for the Sales Analysis tab
    st.header("Sales Analysis Tab")
    st.write("This is the Sales Analysis tab content.")
    # Display the loaded data in an expander for data preview
    with st.expander("Data Preview"):
        st.dataframe(df_copy)

