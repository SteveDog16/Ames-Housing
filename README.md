# Ames Housing Price Dashboard

Utilized Kaggle's extensive dataset to conduct a comprehensive analysis of housing data pertaining to Ames, Iowa.

Primary Objective: Empower individuals seeking residence in Ames, Iowa to assess neighborhood characteristics and make informed decisions on their choice of residence, guided by the frequency and sale prices of these characteristics within each neighborhood.

## Dashboard Landing Page
![image](https://github.com/SteveDog16/Ames-Housing/assets/96502117/483d62d4-d929-42ad-8555-f8f0f201209b)
![image](https://github.com/SteveDog16/Ames-Housing/assets/96502117/e5211f6d-8d39-46c4-9201-3faf6c73a6e3)
![image](https://github.com/SteveDog16/Ames-Housing/assets/96502117/b2629f0e-96b7-4234-a456-5a7ce2838db3)
![image](https://github.com/SteveDog16/Ames-Housing/assets/96502117/62858b3c-5c99-4cf7-88d8-240641713556)


- Upon accessing the dashboard, you'll be greeted by a welcoming landing page. This initial view offers a snapshot of valuable information, providing insights into the property dataset.

### Key Features

- **About Ames:** The About Ames section provides a succinct overview of the city's background. Nestled in Story County, Iowa, Ames is recognized for its central location, situated approximately 30 miles north of Des Moines. Notably, it serves as the home of Iowa State University, a key hub of education and innovation. The summary offers a glimpse into Ames' significance, emphasizing its role as a vibrant community with cultural and academic richness.
- **Geographical and Home Value Summary:** The Geographical and Home Value Summary offers a concise overview of Ames, Iowa. It is a city situated in Story County, centrally located in Iowa and recognized as the home of Iowa State University. The summary touches upon general population trends, the median home value during a specific timeframe, and provides a glimpse into the geographical aspects of Ames, allowing for a quick understanding of its character and significance.
- **Crime Rate Summary:** The Crime Rate Summary provides a quick understanding of the safety landscape in Ames, Iowa. It presents key crime rates per 100,000 people in 2010, including metrics for murder, rape, robbery, assault, property crime, burglary, larceny, and auto theft. This succinct summary serves as an essential reference, allowing users to assess and compare crime trends within the community at a glance.
- **Price and Sale Summary:** The Price and Sale Summary delivers a snapshot of the real estate landscape in Ames. It encompasses essential indicators such as the average and median sale prices, total sales count, as well as the minimum and maximum sale prices, offering a comprehensive overview of the market's dynamics. Additionally, insights into the average price per square foot for both ground and basement areas provide a nuanced perspective on pricing trends, empowering users to make informed decisions in the real estate domain.
- **Neighborhood Analysis:** The Neighborhood Analysis section illuminates key aspects of Ames' various neighborhoods. Through dynamic visualizations, users can discern the frequency of different neighborhoods and gain insights into their popularity. Furthermore, the analysis extends to average sale prices across neighborhoods, aiding in the identification of areas with distinct market characteristics. The presentation of the top 10 neighborhoods by average sale price offers a quick reference to areas where property values may exhibit unique trends, facilitating a deeper understanding of the local real estate landscape.

### Property and Building Analysis Page

(at 50% zoom view)
![image](https://github.com/SteveDog16/Ames-Housing/assets/96502117/7206fac5-5c9f-4006-9a0d-4a829e24881f)
![image](https://github.com/SteveDog16/Ames-Housing/assets/96502117/9b12b2ff-aa1f-48cd-a371-2c0d68e6189b)
![image](https://github.com/SteveDog16/Ames-Housing/assets/96502117/df424f08-9989-4025-9684-97112f86ce12)
(at 33% zoom view)
![image](https://github.com/SteveDog16/Ames-Housing/assets/96502117/57eb5455-58f6-4f40-9dcc-1ce4a838ad27)



- In the second dropdown menu, the selected variable is 'Building Class,' utilized for the x-axis. Two stacked bar charts are presented: one illustrating the frequency of each building class value, and the other displaying the sale prices associated with each building class value.
- The first dropdown menu provides a selection of neighborhoods, enabling users to pick specific neighborhoods for their analysis. These neighborhoods are conveniently labeled on the right side of each graph, with distinct colors corresponding to each one. On the graphs, they are clearly presented beneath each value in the stacked bar charts.Certain neighborhoods are absent from specific values within the graphs due to their absence in the dataset.

## How to run the project

Run the ames_house_price_dashboard.py file, and you will see the dashboard in your locally hosted site

## How to use the Dash application

### General use

**Home Page Navigation:**
To begin exploring the wealth of information on the Ames Housing, simply navigate by clicking on the different tabs. Each tab, except for the home page, is dedicated to a unique category within the Ames Housing dataset.

**Graphical Insights:**
Inside each tab, you'll find two informative graphs. The first graph depicts the frequency distribution of various variables, while the second graph illustrates the relationship between sale prices and these variables.

**Variable Selection:**
Tailoring your analysis to specific variables is a breeze. Utilize the second dropdown menu to select the variable of interest. By selecting different variables, you can observe how they influence the graphs.

**Neighborhood Exploration:**
The first dropdown menu is dedicated to neighborhoods. Here, you can choose and compare different neighborhoods by examining their values within the frequency and sale price graphs.

**Adding and Removing Neighborhoods:**
Expanding your analysis is simple. To add neighborhoods, click the dropdown, select your desired neighborhoods, and watch the graphs adapt accordingly. Conversely, removing neighborhoods is equally straightforward; just click the 'X' button next to the neighborhood you wish to remove.

**Graph Types:**
Depending on your variable selections, you'll encounter various graph types. These include stacked bar charts, histograms, and line graphs. The choice of graph type enhances the clarity and depth of insights.

**Interactive Data Points:**
Dive deeper into the specifics of each data point or bar. Hover your cursor over them, and detailed information, such as neighborhood, x-axis, and y-axis values, will be readily displayed.

**Exploration at Your Fingertips:**
Ready to explore another category? Simply click on the tab of your choice and embark on your journey of discovery. The wealth of information within the Ames Housing dataset is right at your fingertips!

### Explore a graph

**Zooming In:**
For a closer look at a specific area within a graph, single-click your starting point, drag your cursor towards the desired ending point, and release.

**Resetting the View:**
To return to the original view, simply double-click anywhere on the graph. This user-friendly feature is consistent across all graph interactions.

**Moving the Graph:**
For adjusting the position of the graph, navigate to the top right corner and click on the icon featuring four arrows. Hold the click and move your mouse to explore specific areas of interest.

**Selecting Bars in Bar Graphs:**
To select individual bars in a bar graph, click on the dotted square icon, and then hold and move your mouse to encompass the desired bars.

**Selecting Data Points in Scatter Plots:**
For pinpointing specific data points in a scatter plot, click on the oval-shaped icon. Hold the click and move your mouse to highlight the data points you wish to select.

**Zooming In and Out:**
Enabling zoom functionality is a breeze. Click on the square icon with a plus sign to zoom in, or the square with a minus sign to zoom out.

**Viewing Data Point Details:**
To access specific value descriptions on the graph, hover over the data point of interest. A display box will appear, containing relevant information such as neighborhood, x-axis, and y-axis values.

**Customizing Neighborhood Display:**
Tailor your graph's presentation by choosing which neighborhoods to include or exclude. In the legend on the right side of the graph, simply click on the neighborhoods you wish to hide or reveal. Effortlessly refine your visualizations to meet your needs.

## Contributions
I want to express my gratitude to my fellow mentor, Charlie, for his invaluable guidance in dashboard design, chart selection, and variable choice, which greatly contributed to the quality of the project.

## Link to the housing dataset

https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data
