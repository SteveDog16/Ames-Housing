# Ames-Housing

Utilized Kaggle's extensive dataset to conduct a comprehensive analysis of housing data pertaining to Ames, Iowa

## Dashboard Landing Page
![image](https://github.com/SteveDog16/Ames-Housing/assets/96502117/1415b312-3244-484d-90e4-cc8d8f300c3c)
![image](https://github.com/SteveDog16/Ames-Housing/assets/96502117/b339af78-51c4-4b3c-a70f-007adb9d13f8)
- Upon accessing the dashboard, you'll be greeted by a welcoming landing page. This initial view offers a snapshot of valuable information, providing insights into the property dataset.

### Key Features:

- Property Count and Last Update Time: The landing page prominently displays the total property count, allowing you to quickly gauge the scope of the dataset. Additionally, it reveals the time of the last update, ensuring you're working with the latest data.
- Data Summaries: A concise list of summaries is available, highlighting significant findings and noteworthy trends discovered within the dataset. These summaries serve as a quick reference to important insights.
- Building Class Values: The first table presented on the dashboard delves into the world of building class values. It not only enumerates these values but also provides clear and concise explanations for each class, ensuring you understand the significance of each category.
- Cleaned Original Dataset: The second table showcases the original dataset, meticulously cleaned and optimized for clarity and ease of comprehension. You can confidently explore the data with the assurance that it's been refined for your convenience.
- Neighborhood Analysis: A dynamic bar graph enriches your understanding of the dataset. The x-axis features neighborhoods, and you have the flexibility to choose between two y-axis options: frequency (representing the count of each neighborhood value) and sale price (offering insights into the pricing trends within different neighborhoods).

![image](https://github.com/SteveDog16/Ames-Housing/assets/96502117/f5bd714f-e6bc-4b1e-b738-0f5a8070a258)

- Variables 1stFlrSF (first floor square feet) and 2ndFlrSF (second floor square feet) are visualized as scatter plots in the frequency and sale price graphs. They are grouped together each other since they both have numeric values.

![image](https://github.com/SteveDog16/Ames-Housing/assets/96502117/d635b0c5-ba57-4efe-8223-3423aff7ca41)

- Variables BsmtFullBath (basement full bathrooms), BsmtHalfBath (basement half bathrooms), FullBath (full bathrooms above grade), and HalfBath (half baths above grade) are visualized as bar graphs in the frequency and sale price graphs. They are grouped together since they contain the same values.


## How to use the Dash application

### General use

On the page, click on each tab. Every tab represents a unique category regarding the Ames Housing.

It will display two graphs: one representing the frequency of each variable, and another representing sale price in relation to each variable.

To display different variables, click on the dropdown button, which will display different variables. Click on each variable you are interested in and it will display the visuals regarding that variable.

It will be included with the variable that is already in the dropdown. If you want to remove that variable because you want to look at just the variable you chose or if you could not see the information of the variable you chose, remove the other variable by clicking on the X button.

If you want to include several variables in one graph, click on each variable you are interested in exploring.

Depending on the variable type, some variables are displayed as either histograms or scatter plots.

To look at the specific information of each data point/bar, hover your cursor over them and it will display the values from the x-axis and the y-axis.

To look at another category, click on any tab you are interested in and explore!

### Explore a graph

If you want to zoom into a specific area of a graph, click on an starting point, hold your cursor and move it towards the ending point of the area you want to explore, then release your cursor. 

If you want to go back to the original view, double click on the graph. This applies to every feature for the exploration of any graphs.

If you want to move the graph around, hover your cursor to the top right corner of a graph, click on an icon with 4 arrows, and hold and move your mouse to look at a specific area of the graph.

If you want to select a bar in a bar graph, click on a dotted square icon, hold and move your mouse on the box(es) you want to select.

If you want to select certain data points in a scatter plot, click on an oval-shaped icon, hold and move your mouse on the data points you want to select.

If you want to zoom in a graph, click on the square with a plus sign.

If you want to zoom out of a graph, click on the square with a minus sign.

## Link to the housing dataset

https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data
