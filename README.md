# Ames Housing Price Dashboard

Utilized Kaggle's extensive dataset to conduct a comprehensive analysis of housing data pertaining to Ames, Iowa.

Primary Objective: Empower individuals seeking residence in Ames, Iowa to assess neighborhood characteristics and make informed decisions on their choice of residence, guided by the frequency and sale prices of these characteristics within each neighborhood.

## Dashboard Landing Page
![image](https://github.com/SteveDog16/Ames-Housing/assets/96502117/483d62d4-d929-42ad-8555-f8f0f201209b)
![image](https://github.com/SteveDog16/Ames-Housing/assets/96502117/e5211f6d-8d39-46c4-9201-3faf6c73a6e3)
![image](https://github.com/SteveDog16/Ames-Housing/assets/96502117/ae7d621a-091f-4592-ae4e-40d3651e751f)
![image](https://github.com/SteveDog16/Ames-Housing/assets/96502117/6a0140f2-a965-4f8d-961c-846420e72b5a)


- Upon accessing the dashboard, you'll be greeted by a welcoming landing page. This initial view offers a snapshot of valuable information, providing insights into the property dataset.

### Key Features:

- **Property Count and Last Update Time:** The landing page prominently displays the total property count, allowing you to quickly gauge the scope of the dataset. Additionally, it reveals the time of the last update, ensuring you're working with the latest data.
- **Data Summaries:** A concise list of summaries is available, highlighting significant findings and noteworthy trends discovered within the dataset. These summaries serve as a quick reference to important insights.
- **Building Class Values:** The first table presented on the dashboard delves into the world of building class values. It not only enumerates these values but also provides clear and concise explanations for each class, ensuring you understand the significance of each category.
- **Cleaned Original Dataset:** The second table showcases the original dataset, meticulously cleaned and optimized for clarity and ease of comprehension. You can confidently explore the data with the assurance that it's been refined for your convenience.
- **Neighborhood Analysis:** A dynamic bar graph enriches your understanding of the dataset. The x-axis features neighborhoods, and you have the flexibility to choose between two y-axis options: frequency (representing the count of each neighborhood value) and sale price (offering insights into the pricing trends within different neighborhoods).

![image](https://github.com/SteveDog16/Ames-Housing/assets/96502117/37c455f5-940c-41c0-acc4-a728d12e8126)
![image](https://github.com/SteveDog16/Ames-Housing/assets/96502117/c12e18a5-1cb7-4528-ad3f-8cde53800c29)
- In the second dropdown menu, the selected variable is 'Building Class,' utilized for the x-axis. Two stacked bar charts are presented: one illustrating the frequency of each building class value, and the other displaying the sale prices associated with each building class value.
- The first dropdown menu provides a selection of neighborhoods, enabling users to pick specific neighborhoods for their analysis. These neighborhoods are conveniently labeled on the right side of each graph, with distinct colors corresponding to each one. On the graphs, they are clearly presented beneath each value in the stacked bar charts.Certain neighborhoods are absent from specific values within the graphs due to their absence in the dataset.

## How to run the project

Run the ames_analytics_final_draft.py file, and you will see the dashboard in your locally hosted site

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
