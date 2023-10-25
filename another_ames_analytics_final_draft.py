import random
import duckdb
import math
import pandas as pd
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import plotly.graph_objects as go
import seaborn as sns
import streamlit as st
from streamlit import components

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

    col1, col2 = st.columns(2)

    # Replace 5 with 1 in variable names in col1
    with col1:
        st.title("Building Class Explanation Table")
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

    # Replace 6 with 2 in variable names in col2
    with col2:
        st.title("Building Class")
        selected_feature2 = st.selectbox("Select a Building Class Feature", [
            'Building Class'
        ], key="feature2")

        # Replace 6 with 2 in variable names
        price_range2 = st.slider("Price Range", min_value=int(df_copy['SalePrice'].min()), max_value=int(df_copy['SalePrice'].max()), step=1000, value=(int(df_copy['SalePrice'].min()), int(df_copy['SalePrice'].max())), key="price_range2")

        # Replace 6 with 2 in variable names
        original_construction_date_range_2 = st.slider("Original Construction Date Range", int(df_copy['Original Construction Date'].min()), int(df_copy['Original Construction Date'].max()), (int(df_copy['Original Construction Date'].min()), int(df_copy['Original Construction Date'].max())), key="original_construction_date_range2")

        # Replace 6 with 2 in variable names
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
        st.title("Property Assessment Metrics")

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

        # Slider for selecting price ranges for the first feature
        price_range3 = st.slider("Price Range", min_value=int(df_copy['SalePrice'].min()), max_value=int(df_copy['SalePrice'].max()), step=1000, value=(int(df_copy['SalePrice'].min()), int(df_copy['SalePrice'].max())), key="price_range3")

        # Range slider for selecting Original Construction Date for the first feature
        original_construction_date_range_3 = st.slider("Original Construction Date", int(df_copy['Original Construction Date'].min()), int(df_copy['Original Construction Date'].max()), key="original_construction_date_range_3")

        # Slider for selecting Remodel Date for the first feature
        remodel_date_range_3 = st.slider("Remodel Date", int(df_copy['Remodel Date'].min()), int(df_copy['Remodel Date'].max()), key="remodel_date_range_3")

        # Filter the data based on the selected criteria for the first graph
        filtered_data3 = df_copy[
            (df_copy['SalePrice'] >= price_range3[0]) &
            (df_copy['SalePrice'] <= price_range3[1]) &
            (df_copy['Original Construction Date'] >= original_construction_date_range_3) &
            (df_copy['Remodel Date'] >= remodel_date_range_3)
        ]

        # Create a frequency count of the selected feature and neighborhood for the first graph
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
    # Dropdown for selecting the second feature in the second column
    with col4:
        st.title("Dwelling")
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

        # Filter the data based on the selected criteria for the first graph
        filtered_data4 = df_copy[
            (df_copy['SalePrice'] >= price_range4[0]) &
            (df_copy['SalePrice'] <= price_range4[1]) &
            (df_copy['Original Construction Date'] >= original_construction_date_range_4[0]) &
            (df_copy['Original Construction Date'] <= original_construction_date_range_4[1]) &
            (df_copy['Remodel Date'] >= remodel_date_range_4[0]) &
            (df_copy['Remodel Date'] <= remodel_date_range_4[1])
        ]

        # Create a frequency count of the selected feature and neighborhood for the second graph
        feature_counts4 = filtered_data4.groupby([selected_feature4, 'Neighborhood']).size().reset_index()
        feature_counts4.columns = [selected_feature4, 'Neighborhood', 'Frequency']

        # Get the top 10 neighborhoods based on frequency for the selected feature and price range for the second graph
        top_neighborhoods4 = feature_counts4.groupby('Neighborhood').sum().nlargest(10, 'Frequency').index

        # Filter data to include only the top 10 neighborhoods for the selected feature and price range for the second graph
        filtered_feature_counts4 = feature_counts4[(feature_counts4['Neighborhood'].isin(top_neighborhoods4)) & (feature_counts4[selected_feature4] != 'N/A')]

        # Create a stacked bar chart using Plotly Express for the second feature
        fig4 = px.bar(
            filtered_feature_counts4,
            x=selected_feature4,
            y='Frequency',
            color='Neighborhood',  # Color by neighborhood
            barmode='stack',  # Create a stacked bar chart
            labels={'x': selected_feature4, 'Frequency': 'Frequency'},
            title=f"Top Neighborhoods for {selected_feature4}",
        )

        # Display the second stacked bar chart
        st.plotly_chart(fig4)



    # Create a new row for the third graph
    #st.write("---")  # Horizontal line to separate rows

    # Create two columns for the third graph
    col5, col6 = st.columns(2)

    # Replace 4 with 5 in variable names in col5
    with col5:
        st.title("Rooms")
        selected_feature5 = st.selectbox("Select a Room Feature", [
            'Total Number of Full Bathrooms',
            'Total Number of Half Bathrooms',
            'Total Rooms Above Grade (Does Not Include Bathrooms)'
        ], key="feature5")

        # Replace 4 with 5 in variable names
        price_range5 = st.slider("Price Range", min_value=int(df_copy['SalePrice'].min()), max_value=int(df_copy['SalePrice'].max()), step=1000, value=(int(df_copy['SalePrice'].min()), int(df_copy['SalePrice'].max())), key="price_range5")

        # Replace 4 with 5 in variable names
        original_construction_date_range_5 = st.slider("Original Construction Date Range", int(df_copy['Original Construction Date'].min()), int(df_copy['Original Construction Date'].max()), (int(df_copy['Original Construction Date'].min()), int(df_copy['Original Construction Date'].max())), key="original_construction_date_range5")

        # Replace 4 with 5 in variable names
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


    # Replace 7 with 6 in variable names in col7
    with col6:
        st.title("Unique Features")
        selected_feature6 = st.selectbox("Select a Unique Feature", [
            'Pool Quality',
            'Fence Quality',
            'Flatness of the Property',
            'Miscellaneous Feature',
            'General Shape of Property'
        ], key="feature6")

        # Replace 7 with 6 in variable names
        price_range6 = st.slider("Price Range", min_value=int(df_copy['SalePrice'].min()), max_value=int(df_copy['SalePrice'].max()), step=1000, value=(int(df_copy['SalePrice'].min()), int(df_copy['SalePrice'].max())), key="price_range6")

        # Replace 7 with 6 in variable names
        original_construction_date_range_6 = st.slider("Original Construction Date Range", int(df_copy['Original Construction Date'].min()), int(df_copy['Original Construction Date'].max()), (int(df_copy['Original Construction Date'].min()), int(df_copy['Original Construction Date'].max())), key="original_construction_date_range_6")

        # Replace 7 with 6 in variable names
        remodel_date_range_6 = st.slider("Remodel Date Range", int(df_copy['Remodel Date'].min()), int(df_copy['Remodel Date'].max()), (int(df_copy['Remodel Date'].min()), int(df_copy['Remodel Date'].max())), key="remodel_date_range_6")

        # Filter the data based on the selected criteria for the seventh graph
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

        # Get the top 10 neighborhoods based on frequency for the selected feature and price range for the sixth graph
        top_neighborhoods6 = feature_counts6.groupby('Neighborhood').sum().nlargest(10, 'Frequency').index

        # Filter data to include only the top 10 neighborhoods for the selected feature and price range for the sixth graph
        filtered_feature_counts6 = feature_counts6[(feature_counts6['Neighborhood'].isin(top_neighborhoods6)) & (feature_counts6[selected_feature6] != 'N/A')]

        # Create a stacked bar chart using Plotly Express for the sixth feature
        fig6 = px.bar(
            filtered_feature_counts6,
            x=selected_feature6,
            y='Frequency',
            color='Neighborhood',  # Color by neighborhood
            barmode='stack',  # Create a stacked bar chart
            labels={'x': selected_feature6, 'Frequency': 'Frequency'},
            title=f"Top Neighborhoods for {selected_feature6}",
        )

        # Display the sixth stacked bar chart
        st.plotly_chart(fig6)


    st.write("---")

    col7, col8 = st.columns(2)

    # Dropdown for selecting the seventh feature in the first column of the second row
    with col7:
        st.title("Indoor Size")
        # Replace 3 with 7 in selected_feature3
        selected_feature7 = st.selectbox("Select an Indoor Size Feature", [
            'Total Finished Basement Area (in Square Feet)',
            'Unfinished Basement Area (in Square Feet)',
            'Total Basement Area (in Square Feet)',
            'Above Grade (Ground) Living Area (in Square Feet)'
        ], key="feature7")

        # Replace 3 with 7 in price_range3
        price_range7 = st.slider("Price Range", min_value=int(df_copy['SalePrice'].min()), max_value=int(df_copy['SalePrice'].max()), step=1000, value=(int(df_copy['SalePrice'].min()), int(df_copy['SalePrice'].max())), key="price_range7")

        # Replace 3 with 7 in original_construction_date_range_3
        original_construction_date_range_7 = st.slider("Original Construction Date Range", int(df_copy['Original Construction Date'].min()), int(df_copy['Original Construction Date'].max()), (int(df_copy['Original Construction Date'].min()), int(df_copy['Original Construction Date'].max())), key="original_construction_date_range_7")

        # Replace 3 with 7 in remodel_date_range_3
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
        top_neighborhoods7 = feature_counts7.groupby('Neighborhood').sum().nlargest(10, 'Frequency').index

        # Filter data to include only the top 10 neighborhoods for the selected feature and price range for the seventh graph
        filtered_feature_counts7 = feature_counts7[(feature_counts7['Neighborhood'].isin(top_neighborhoods7)) & (feature_counts7[selected_feature7] != 'N/A')]

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

        # Display the seventh stacked bar chart
        st.plotly_chart(fig7)

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
        fig_pie = px.pie(df_pie, names='Category', values='Values', title='Percentage of Finished/Unfinished Basement Area')

        fig_pie.update_traces(hole=0.4)  # Adjust the hole size (0.4 makes it a donut)

        # Adjust the size of the pie chart
        fig_pie.update_layout(width=350, height=350)  # Adjust the size

        fig_pie.update_layout(title_font=dict(size=15))  # Adjust the title text size

        # Display the pie chart
        st.plotly_chart(fig_pie)

        # Calculate the sum of 1stFlrSF, 2ndFlrSF, and LowQualFinSF
        total_sf = df['1stFlrSF'] + df['2ndFlrSF'] + df['LowQualFinSF']

        # Create a DataFrame with the calculated values
        data = {'Category': ['1stFlrSF', '2ndFlrSF', 'LowQualFinSF'],
                'Total Square Feet': [df['1stFlrSF'].sum(), df['2ndFlrSF'].sum(), df['LowQualFinSF'].sum()]}

        df_pie = pd.DataFrame(data)

        # Create a pie chart using Plotly Express
        fig_pie = px.pie(df_pie, names='Category', values='Total Square Feet', title='Percentage of Above Ground Living Area')

        # Turn the pie chart into a donut chart by setting the hole parameter
        fig_pie.update_traces(hole=0.4)  # Adjust the hole size (0.4 makes it a donut)

        fig_pie.update_layout(title_font=dict(size=15))  # Adjust the title text size

        # Adjust the size of the pie chart
        fig_pie.update_layout(width=350, height=350)  # Adjust the size

        # Display the donut chart
        st.plotly_chart(fig_pie)


    
    with col8:
        st.title("Outdoor Size")
        selected_feature8 = st.selectbox("Select an Outdoor Size Feature", [
            'Lot Size (in Square Feet)',
            'Wood Deck Area (in Square Feet)',
            'Open Porch Area (in Square Feet)',
            'Enclosed Porch Area (in Square Feet)',
            'Three Season Porch Area (in Square Feet)',
            'Screen Porch Area (in Square Feet)',
            'Pool Area (in Square Feet)',
        ], key="feature8")

        # Replace 4 with 8 in variable names
        price_range8 = st.slider("Price Range", min_value=int(df_copy['SalePrice'].min()), max_value=int(df_copy['SalePrice'].max()), step=1000, value=(int(df_copy['SalePrice'].min()), int(df_copy['SalePrice'].max())), key="price_range8")

        # Replace 4 with 8 in variable names
        original_construction_date_range_8 = st.slider("Original Construction Date Range", int(df_copy['Original Construction Date'].min()), int(df_copy['Original Construction Date'].max()), (int(df_copy['Original Construction Date'].min()), int(df_copy['Original Construction Date'].max())), key="original_construction_date_range_8")

        # Replace 4 with 8 in variable names
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
        fig_pie = px.pie(data_pie_chart, names='Variable', values='Count', title='Distribution of Porch Areas')

        # Turn the pie chart into a donut chart by setting the hole parameter
        fig_pie.update_traces(hole=0.4)  # Adjust the hole size (0.4 makes it a donut)

        # Adjust the size of the pie chart
        fig_pie.update_layout(width=430, height=430)  # Adjust the size

        fig_pie.update_layout(title_font=dict(size=15))  # Adjust the title text size

        # Display the donut chart

        # Display the donut chart
        st.plotly_chart(fig_pie)

elif selected_tab == "Sales Analysis":
    # Content for the Sales Analysis tab
    st.header("Sales Analysis Tab")
    st.write("This is the Sales Analysis tab content.")

    # Display the loaded data in an expander for data preview
    with st.expander("Data Preview"):
        st.dataframe(df_copy)

    # Create a slider for selecting a price range with two draggers
    price_range = st.slider("Price Range", min_value=int(df_copy['SalePrice'].min()), max_value=int(df_copy['SalePrice'].max()), value=(int(df_copy['SalePrice'].min()), int(df_copy['SalePrice'].max())), step=1000)

    # Create a line graph for Original Construction Date vs. Frequency
    st.subheader("Original Construction Date vs. Frequency")
    original_construction_counts = df_copy[(df_copy['SalePrice'] >= price_range[0]) & (df_copy['SalePrice'] <= price_range[1])].groupby('Original Construction Date').size().reset_index()
    original_construction_counts.columns = ['Original Construction Date', 'Frequency']
    st.line_chart(original_construction_counts.set_index('Original Construction Date'))

    # Create a line graph for Remodel Date vs. Frequency
    st.subheader("Remodel Date vs. Frequency")
    remodel_date_counts = df_copy[(df_copy['SalePrice'] >= price_range[0]) & (df_copy['SalePrice'] <= price_range[1])].groupby('Remodel Date').size().reset_index()
    remodel_date_counts.columns = ['Remodel Date', 'Frequency']
    st.line_chart(remodel_date_counts.set_index('Remodel Date'))
