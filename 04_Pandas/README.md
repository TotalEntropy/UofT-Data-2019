# Heroes of Pymoli Data Analysis

## Summary
* Of the 576 players the vast majority (84.03%) are male with the remainder being female and non-disclosed. The majority of the purchase value of is provided by these male players although the average purchase value of the smaller female and non-disclosed players is actually higher.

* The largest age group of players is from 20-24 followed by 15-19 and 25-34. The largest total purchase value is from the 20-24 age group who also have a very high average total purchase per person.

* With one exception the top 5 most purchased items are priced over $4. This suggests that there is no relationship between the price of the items and the amount purchased. Three of these items are also on the top 3 most profitable items.

```python
# Dependencies and Setup
%autosave 60
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
csv_file = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(csv_file)
raw = pd.read_csv(csv_file)
```

    Autosaving every 60 seconds
    
## Player Count

```python
# Counting the number of unique SN assumed to be ID names
player_count = pd.DataFrame(data = {'Total Players' : raw['SN'].nunique()}, index = [0])
player_count.head()
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>576</td>
    </tr>
  </tbody>
</table>
</div>

## Purchasing Analysis

```python
# Counting the unique number of item IDs
purchase_analysis = pd.DataFrame(data = {'Number of Unique Items' : raw['Item ID'].nunique()}, index = [0])

# Taking the mean of the item purchase price
purchase_analysis['Average Purchase Price'] = raw['Price'].mean()

# Calculating the number of unique purchases
purchase_analysis['Total Number of Purchases'] = raw['Purchase ID'].nunique()

#Calculating the sum of all of the purchases
purchase_analysis['Total Revenue'] = raw['Price'].sum()

# Displaying the price as currency
purchase_analysis.style.format({'Average Purchase Price' : '${:.2f}', 'Total Revenue' : '${:,.2f}'})
```

<table id="T_5e7d7180_34b4_11e9_b800_10c37b702c42" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Number of Unique Items</th> 
        <th class="col_heading level0 col1" >Average Purchase Price</th> 
        <th class="col_heading level0 col2" >Total Number of Purchases</th> 
        <th class="col_heading level0 col3" >Total Revenue</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_5e7d7180_34b4_11e9_b800_10c37b702c42level0_row0" class="row_heading level0 row0" >0</th> 
        <td id="T_5e7d7180_34b4_11e9_b800_10c37b702c42row0_col0" class="data row0 col0" >183</td> 
        <td id="T_5e7d7180_34b4_11e9_b800_10c37b702c42row0_col1" class="data row0 col1" >$3.05</td> 
        <td id="T_5e7d7180_34b4_11e9_b800_10c37b702c42row0_col2" class="data row0 col2" >780</td> 
        <td id="T_5e7d7180_34b4_11e9_b800_10c37b702c42row0_col3" class="data row0 col3" >$2,379.77</td> 
    </tr></tbody> 
</table> 



## Gender Demographics


```python
# Generating a data frame with the number of players group by gender
group_gender = raw.groupby('Gender')
gender_demographics = pd.DataFrame(group_gender.nunique()['SN'])
gender_demographics = gender_demographics.rename(columns = {'SN' : 'Total Count'})

# Calculating the percentage of players by gender
gender_demographics['Percentage of Players'] = (gender_demographics['Total Count']
                                                .div(gender_demographics['Total Count'].sum()) * 100)

# Sorting the number of players in descending order
gender_demographics = gender_demographics.sort_values(["Total Count"], ascending = False)

# Fisplaying the percentage as percent
gender_demographics.style.format({'Percentage of Players' : '{:.2f}%'})
```

<table id="T_5e82a138_34b4_11e9_8e6a_10c37b702c42" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Total Count</th> 
        <th class="col_heading level0 col1" >Percentage of Players</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Gender</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_5e82a138_34b4_11e9_8e6a_10c37b702c42level0_row0" class="row_heading level0 row0" >Male</th> 
        <td id="T_5e82a138_34b4_11e9_8e6a_10c37b702c42row0_col0" class="data row0 col0" >484</td> 
        <td id="T_5e82a138_34b4_11e9_8e6a_10c37b702c42row0_col1" class="data row0 col1" >84.03%</td> 
    </tr>    <tr> 
        <th id="T_5e82a138_34b4_11e9_8e6a_10c37b702c42level0_row1" class="row_heading level0 row1" >Female</th> 
        <td id="T_5e82a138_34b4_11e9_8e6a_10c37b702c42row1_col0" class="data row1 col0" >81</td> 
        <td id="T_5e82a138_34b4_11e9_8e6a_10c37b702c42row1_col1" class="data row1 col1" >14.06%</td> 
    </tr>    <tr> 
        <th id="T_5e82a138_34b4_11e9_8e6a_10c37b702c42level0_row2" class="row_heading level0 row2" >Other / Non-Disclosed</th> 
        <td id="T_5e82a138_34b4_11e9_8e6a_10c37b702c42row2_col0" class="data row2 col0" >11</td> 
        <td id="T_5e82a138_34b4_11e9_8e6a_10c37b702c42row2_col1" class="data row2 col1" >1.91%</td> 
    </tr></tbody> 
</table> 



## Purchasing Analysis (Gender)


```python
# Generating a data frame with the number of purchases group by gender
purchasing_analysis = pd.DataFrame(group_gender.count()['Item ID'])
purchasing_analysis = purchasing_analysis.rename(columns = {'Item ID' : 'Purchase Count'})

# Calculating the average purchase price by gender
purchasing_analysis['Average Purchase Price'] = group_gender.mean()['Price']

# Calculating the Average value of the purchases by gender
purchasing_analysis['Total Purchase Value'] = group_gender.sum()['Price']

# Calculating the average total purchase per person by gender
purchasing_analysis['Avg Total Purchase per Person'] = (purchasing_analysis['Total Purchase Value'] /
                                                        gender_demographics['Total Count'])

#Displaying as currency
purchasing_analysis.style.format({'Average Purchase Price' : '${:,.2f}', 'Total Purchase Value' : '${:,.2f}',
                                 'Avg Total Purchase per Person' : '${:,.2f}'})
```
 
<table id="T_5e85d540_34b4_11e9_816d_10c37b702c42" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Purchase Count</th> 
        <th class="col_heading level0 col1" >Average Purchase Price</th> 
        <th class="col_heading level0 col2" >Total Purchase Value</th> 
        <th class="col_heading level0 col3" >Avg Total Purchase per Person</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Gender</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_5e85d540_34b4_11e9_816d_10c37b702c42level0_row0" class="row_heading level0 row0" >Female</th> 
        <td id="T_5e85d540_34b4_11e9_816d_10c37b702c42row0_col0" class="data row0 col0" >113</td> 
        <td id="T_5e85d540_34b4_11e9_816d_10c37b702c42row0_col1" class="data row0 col1" >$3.20</td> 
        <td id="T_5e85d540_34b4_11e9_816d_10c37b702c42row0_col2" class="data row0 col2" >$361.94</td> 
        <td id="T_5e85d540_34b4_11e9_816d_10c37b702c42row0_col3" class="data row0 col3" >$4.47</td> 
    </tr>    <tr> 
        <th id="T_5e85d540_34b4_11e9_816d_10c37b702c42level0_row1" class="row_heading level0 row1" >Male</th> 
        <td id="T_5e85d540_34b4_11e9_816d_10c37b702c42row1_col0" class="data row1 col0" >652</td> 
        <td id="T_5e85d540_34b4_11e9_816d_10c37b702c42row1_col1" class="data row1 col1" >$3.02</td> 
        <td id="T_5e85d540_34b4_11e9_816d_10c37b702c42row1_col2" class="data row1 col2" >$1,967.64</td> 
        <td id="T_5e85d540_34b4_11e9_816d_10c37b702c42row1_col3" class="data row1 col3" >$4.07</td> 
    </tr>    <tr> 
        <th id="T_5e85d540_34b4_11e9_816d_10c37b702c42level0_row2" class="row_heading level0 row2" >Other / Non-Disclosed</th> 
        <td id="T_5e85d540_34b4_11e9_816d_10c37b702c42row2_col0" class="data row2 col0" >15</td> 
        <td id="T_5e85d540_34b4_11e9_816d_10c37b702c42row2_col1" class="data row2 col1" >$3.35</td> 
        <td id="T_5e85d540_34b4_11e9_816d_10c37b702c42row2_col2" class="data row2 col2" >$50.19</td> 
        <td id="T_5e85d540_34b4_11e9_816d_10c37b702c42row2_col3" class="data row2 col3" >$4.56</td> 
    </tr></tbody> 
</table> 



## Age Demographics


```python
# Creating bins for age groups
bin_age = [0, 10, 15, 20, 25, 30, 35, 40, 200]
bin_label = ['<10', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40+']

# Adding the age groups to the original data frame
raw['Age Group'] = pd.cut(raw['Age'], bin_age, labels = bin_label, right = False)

# Creating a data frame group by the age groups
group_age = raw.groupby('Age Group')

# Generating a new data frame counting the number of unique players
age_demographics = pd.DataFrame(group_age.nunique()['SN'])

# Renaming the columns to Total Count
age_demographics = age_demographics.rename(columns = {'SN' : 'Total Count'})

# Calculating the percentage of players in each age group
age_demographics['Percentage of Players'] = (age_demographics['Total Count'] / age_demographics['Total Count'].sum() * 100)

# Displaying as percentage
age_demographics.style.format({'Percentage of Players' : '{:.2f}%'})
```
 
<table id="T_5e890950_34b4_11e9_9b43_10c37b702c42" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Total Count</th> 
        <th class="col_heading level0 col1" >Percentage of Players</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Age Group</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_5e890950_34b4_11e9_9b43_10c37b702c42level0_row0" class="row_heading level0 row0" ><10</th> 
        <td id="T_5e890950_34b4_11e9_9b43_10c37b702c42row0_col0" class="data row0 col0" >17</td> 
        <td id="T_5e890950_34b4_11e9_9b43_10c37b702c42row0_col1" class="data row0 col1" >2.95%</td> 
    </tr>    <tr> 
        <th id="T_5e890950_34b4_11e9_9b43_10c37b702c42level0_row1" class="row_heading level0 row1" >10-14</th> 
        <td id="T_5e890950_34b4_11e9_9b43_10c37b702c42row1_col0" class="data row1 col0" >22</td> 
        <td id="T_5e890950_34b4_11e9_9b43_10c37b702c42row1_col1" class="data row1 col1" >3.82%</td> 
    </tr>    <tr> 
        <th id="T_5e890950_34b4_11e9_9b43_10c37b702c42level0_row2" class="row_heading level0 row2" >15-19</th> 
        <td id="T_5e890950_34b4_11e9_9b43_10c37b702c42row2_col0" class="data row2 col0" >107</td> 
        <td id="T_5e890950_34b4_11e9_9b43_10c37b702c42row2_col1" class="data row2 col1" >18.58%</td> 
    </tr>    <tr> 
        <th id="T_5e890950_34b4_11e9_9b43_10c37b702c42level0_row3" class="row_heading level0 row3" >20-24</th> 
        <td id="T_5e890950_34b4_11e9_9b43_10c37b702c42row3_col0" class="data row3 col0" >258</td> 
        <td id="T_5e890950_34b4_11e9_9b43_10c37b702c42row3_col1" class="data row3 col1" >44.79%</td> 
    </tr>    <tr> 
        <th id="T_5e890950_34b4_11e9_9b43_10c37b702c42level0_row4" class="row_heading level0 row4" >25-29</th> 
        <td id="T_5e890950_34b4_11e9_9b43_10c37b702c42row4_col0" class="data row4 col0" >77</td> 
        <td id="T_5e890950_34b4_11e9_9b43_10c37b702c42row4_col1" class="data row4 col1" >13.37%</td> 
    </tr>    <tr> 
        <th id="T_5e890950_34b4_11e9_9b43_10c37b702c42level0_row5" class="row_heading level0 row5" >30-34</th> 
        <td id="T_5e890950_34b4_11e9_9b43_10c37b702c42row5_col0" class="data row5 col0" >52</td> 
        <td id="T_5e890950_34b4_11e9_9b43_10c37b702c42row5_col1" class="data row5 col1" >9.03%</td> 
    </tr>    <tr> 
        <th id="T_5e890950_34b4_11e9_9b43_10c37b702c42level0_row6" class="row_heading level0 row6" >35-39</th> 
        <td id="T_5e890950_34b4_11e9_9b43_10c37b702c42row6_col0" class="data row6 col0" >31</td> 
        <td id="T_5e890950_34b4_11e9_9b43_10c37b702c42row6_col1" class="data row6 col1" >5.38%</td> 
    </tr>    <tr> 
        <th id="T_5e890950_34b4_11e9_9b43_10c37b702c42level0_row7" class="row_heading level0 row7" >40+</th> 
        <td id="T_5e890950_34b4_11e9_9b43_10c37b702c42row7_col0" class="data row7 col0" >12</td> 
        <td id="T_5e890950_34b4_11e9_9b43_10c37b702c42row7_col1" class="data row7 col1" >2.08%</td> 
    </tr></tbody> 
</table> 



## Purchasing Analysis (Age)


```python
# Generating initial data frame with purchase count
purchasing_analysis_age = pd.DataFrame(group_age.count()['Item ID'])
purchasing_analysis_age = purchasing_analysis_age.rename(columns = {'Item ID' : 'Purchase Count'})

# Calculating the Average Purchase Price
purchasing_analysis_age['Average Purchase Price'] = group_age.mean()['Price']

# Calculating total purchase value
purchasing_analysis_age['Total Purchase Value'] = group_age.sum()['Price']

# Calculating average total purchase per person
purchasing_analysis_age['Avg Total Purchase per Person'] = (purchasing_analysis_age['Total Purchase Value'] /
                                                            age_demographics['Total Count'])

# Displaying as currency
purchasing_analysis_age.style.format({'Average Purchase Price' : '${:,.2f}', 'Total Purchase Value' : '${:,.2f}',
                                      'Avg Total Purchase per Person' : '${:,.2f}'})
```

<table id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Purchase Count</th> 
        <th class="col_heading level0 col1" >Average Purchase Price</th> 
        <th class="col_heading level0 col2" >Total Purchase Value</th> 
        <th class="col_heading level0 col3" >Avg Total Purchase per Person</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Age Group</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42level0_row0" class="row_heading level0 row0" ><10</th> 
        <td id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42row0_col0" class="data row0 col0" >23</td> 
        <td id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42row0_col1" class="data row0 col1" >$3.35</td> 
        <td id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42row0_col2" class="data row0 col2" >$77.13</td> 
        <td id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42row0_col3" class="data row0 col3" >$4.54</td> 
    </tr>    <tr> 
        <th id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42level0_row1" class="row_heading level0 row1" >10-14</th> 
        <td id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42row1_col0" class="data row1 col0" >28</td> 
        <td id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42row1_col1" class="data row1 col1" >$2.96</td> 
        <td id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42row1_col2" class="data row1 col2" >$82.78</td> 
        <td id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42row1_col3" class="data row1 col3" >$3.76</td> 
    </tr>    <tr> 
        <th id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42level0_row2" class="row_heading level0 row2" >15-19</th> 
        <td id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42row2_col0" class="data row2 col0" >136</td> 
        <td id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42row2_col1" class="data row2 col1" >$3.04</td> 
        <td id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42row2_col2" class="data row2 col2" >$412.89</td> 
        <td id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42row2_col3" class="data row2 col3" >$3.86</td> 
    </tr>    <tr> 
        <th id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42level0_row3" class="row_heading level0 row3" >20-24</th> 
        <td id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42row3_col0" class="data row3 col0" >365</td> 
        <td id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42row3_col1" class="data row3 col1" >$3.05</td> 
        <td id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42row3_col2" class="data row3 col2" >$1,114.06</td> 
        <td id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42row3_col3" class="data row3 col3" >$4.32</td> 
    </tr>    <tr> 
        <th id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42level0_row4" class="row_heading level0 row4" >25-29</th> 
        <td id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42row4_col0" class="data row4 col0" >101</td> 
        <td id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42row4_col1" class="data row4 col1" >$2.90</td> 
        <td id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42row4_col2" class="data row4 col2" >$293.00</td> 
        <td id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42row4_col3" class="data row4 col3" >$3.81</td> 
    </tr>    <tr> 
        <th id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42level0_row5" class="row_heading level0 row5" >30-34</th> 
        <td id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42row5_col0" class="data row5 col0" >73</td> 
        <td id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42row5_col1" class="data row5 col1" >$2.93</td> 
        <td id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42row5_col2" class="data row5 col2" >$214.00</td> 
        <td id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42row5_col3" class="data row5 col3" >$4.12</td> 
    </tr>    <tr> 
        <th id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42level0_row6" class="row_heading level0 row6" >35-39</th> 
        <td id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42row6_col0" class="data row6 col0" >41</td> 
        <td id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42row6_col1" class="data row6 col1" >$3.60</td> 
        <td id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42row6_col2" class="data row6 col2" >$147.67</td> 
        <td id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42row6_col3" class="data row6 col3" >$4.76</td> 
    </tr>    <tr> 
        <th id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42level0_row7" class="row_heading level0 row7" >40+</th> 
        <td id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42row7_col0" class="data row7 col0" >13</td> 
        <td id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42row7_col1" class="data row7 col1" >$2.94</td> 
        <td id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42row7_col2" class="data row7 col2" >$38.24</td> 
        <td id="T_5e8c1652_34b4_11e9_9d4e_10c37b702c42row7_col3" class="data row7 col3" >$3.19</td> 
    </tr></tbody> 
</table> 

## Top Spendors

```python
# Generating a df group by SN with the Purchase Count
group_sn = raw.groupby('SN')
top_spendors = pd.DataFrame(group_sn.count()['Purchase ID'])
top_spendors = top_spendors.rename(columns = {'Purchase ID' : 'Purchase Count'})

# Calculating the Average Purchase Price
top_spendors['Average Purchase Price'] = group_sn.mean()['Price']

# Calculating the Total Purchase Value
top_spendors['Total Purchase Value'] = group_sn.sum()['Price']

# Sorting the table by the Total Purchase Value and taking top 5
top_5_spendors = top_spendors.sort_values('Total Purchase Value', ascending = False).head()

# Displaying as currency
top_5_spendors.style.format({'Average Purchase Price' : '${:,.2f}', 'Total Purchase Value' : '${:,.2f}'})
```

<table id="T_5e8f2352_34b4_11e9_bcbe_10c37b702c42" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Purchase Count</th> 
        <th class="col_heading level0 col1" >Average Purchase Price</th> 
        <th class="col_heading level0 col2" >Total Purchase Value</th> 
    </tr>    <tr> 
        <th class="index_name level0" >SN</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_5e8f2352_34b4_11e9_bcbe_10c37b702c42level0_row0" class="row_heading level0 row0" >Lisosia93</th> 
        <td id="T_5e8f2352_34b4_11e9_bcbe_10c37b702c42row0_col0" class="data row0 col0" >5</td> 
        <td id="T_5e8f2352_34b4_11e9_bcbe_10c37b702c42row0_col1" class="data row0 col1" >$3.79</td> 
        <td id="T_5e8f2352_34b4_11e9_bcbe_10c37b702c42row0_col2" class="data row0 col2" >$18.96</td> 
    </tr>    <tr> 
        <th id="T_5e8f2352_34b4_11e9_bcbe_10c37b702c42level0_row1" class="row_heading level0 row1" >Idastidru52</th> 
        <td id="T_5e8f2352_34b4_11e9_bcbe_10c37b702c42row1_col0" class="data row1 col0" >4</td> 
        <td id="T_5e8f2352_34b4_11e9_bcbe_10c37b702c42row1_col1" class="data row1 col1" >$3.86</td> 
        <td id="T_5e8f2352_34b4_11e9_bcbe_10c37b702c42row1_col2" class="data row1 col2" >$15.45</td> 
    </tr>    <tr> 
        <th id="T_5e8f2352_34b4_11e9_bcbe_10c37b702c42level0_row2" class="row_heading level0 row2" >Chamjask73</th> 
        <td id="T_5e8f2352_34b4_11e9_bcbe_10c37b702c42row2_col0" class="data row2 col0" >3</td> 
        <td id="T_5e8f2352_34b4_11e9_bcbe_10c37b702c42row2_col1" class="data row2 col1" >$4.61</td> 
        <td id="T_5e8f2352_34b4_11e9_bcbe_10c37b702c42row2_col2" class="data row2 col2" >$13.83</td> 
    </tr>    <tr> 
        <th id="T_5e8f2352_34b4_11e9_bcbe_10c37b702c42level0_row3" class="row_heading level0 row3" >Iral74</th> 
        <td id="T_5e8f2352_34b4_11e9_bcbe_10c37b702c42row3_col0" class="data row3 col0" >4</td> 
        <td id="T_5e8f2352_34b4_11e9_bcbe_10c37b702c42row3_col1" class="data row3 col1" >$3.40</td> 
        <td id="T_5e8f2352_34b4_11e9_bcbe_10c37b702c42row3_col2" class="data row3 col2" >$13.62</td> 
    </tr>    <tr> 
        <th id="T_5e8f2352_34b4_11e9_bcbe_10c37b702c42level0_row4" class="row_heading level0 row4" >Iskadarya95</th> 
        <td id="T_5e8f2352_34b4_11e9_bcbe_10c37b702c42row4_col0" class="data row4 col0" >3</td> 
        <td id="T_5e8f2352_34b4_11e9_bcbe_10c37b702c42row4_col1" class="data row4 col1" >$4.37</td> 
        <td id="T_5e8f2352_34b4_11e9_bcbe_10c37b702c42row4_col2" class="data row4 col2" >$13.10</td> 
    </tr></tbody> 
</table> 

## Most Popular Items

```python
# Create new DF with the Item Id and name
group_item = raw.groupby(['Item ID', 'Item Name'])
popular_item = pd.DataFrame(group_item.nunique()['Purchase ID'])

# Rename to Purchase Count
popular_item = popular_item.rename(columns = {'Purchase ID' : 'Purchase Count'})

# Add Item Price columns
popular_item['Item Price'] = group_item.sum()['Price'] / popular_item['Purchase Count']

# Calculate Total Purchase Value
popular_item['Total Purchase Value'] = popular_item['Purchase Count'] * popular_item['Item Price']

# Sorting based on Total Purchase Value taking top 5
popular_item_5 = popular_item.sort_values('Purchase Count', ascending = False).head()

# Displaying as currency
popular_item_5.style.format({'Item Price' : '${:,.2f}', 'Total Purchase Value' : '${:,.2f}'})
```

<table id="T_5e92a57a_34b4_11e9_9026_10c37b702c42" > 
<thead>    <tr> 
        <th class="blank" ></th> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Purchase Count</th> 
        <th class="col_heading level0 col1" >Item Price</th> 
        <th class="col_heading level0 col2" >Total Purchase Value</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Item ID</th> 
        <th class="index_name level1" >Item Name</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_5e92a57a_34b4_11e9_9026_10c37b702c42level0_row0" class="row_heading level0 row0" >178</th> 
        <th id="T_5e92a57a_34b4_11e9_9026_10c37b702c42level1_row0" class="row_heading level1 row0" >Oathbreaker, Last Hope of the Breaking Storm</th> 
        <td id="T_5e92a57a_34b4_11e9_9026_10c37b702c42row0_col0" class="data row0 col0" >12</td> 
        <td id="T_5e92a57a_34b4_11e9_9026_10c37b702c42row0_col1" class="data row0 col1" >$4.23</td> 
        <td id="T_5e92a57a_34b4_11e9_9026_10c37b702c42row0_col2" class="data row0 col2" >$50.76</td> 
    </tr>    <tr> 
        <th id="T_5e92a57a_34b4_11e9_9026_10c37b702c42level0_row1" class="row_heading level0 row1" >145</th> 
        <th id="T_5e92a57a_34b4_11e9_9026_10c37b702c42level1_row1" class="row_heading level1 row1" >Fiery Glass Crusader</th> 
        <td id="T_5e92a57a_34b4_11e9_9026_10c37b702c42row1_col0" class="data row1 col0" >9</td> 
        <td id="T_5e92a57a_34b4_11e9_9026_10c37b702c42row1_col1" class="data row1 col1" >$4.58</td> 
        <td id="T_5e92a57a_34b4_11e9_9026_10c37b702c42row1_col2" class="data row1 col2" >$41.22</td> 
    </tr>    <tr> 
        <th id="T_5e92a57a_34b4_11e9_9026_10c37b702c42level0_row2" class="row_heading level0 row2" >108</th> 
        <th id="T_5e92a57a_34b4_11e9_9026_10c37b702c42level1_row2" class="row_heading level1 row2" >Extraction, Quickblade Of Trembling Hands</th> 
        <td id="T_5e92a57a_34b4_11e9_9026_10c37b702c42row2_col0" class="data row2 col0" >9</td> 
        <td id="T_5e92a57a_34b4_11e9_9026_10c37b702c42row2_col1" class="data row2 col1" >$3.53</td> 
        <td id="T_5e92a57a_34b4_11e9_9026_10c37b702c42row2_col2" class="data row2 col2" >$31.77</td> 
    </tr>    <tr> 
        <th id="T_5e92a57a_34b4_11e9_9026_10c37b702c42level0_row3" class="row_heading level0 row3" >82</th> 
        <th id="T_5e92a57a_34b4_11e9_9026_10c37b702c42level1_row3" class="row_heading level1 row3" >Nirvana</th> 
        <td id="T_5e92a57a_34b4_11e9_9026_10c37b702c42row3_col0" class="data row3 col0" >9</td> 
        <td id="T_5e92a57a_34b4_11e9_9026_10c37b702c42row3_col1" class="data row3 col1" >$4.90</td> 
        <td id="T_5e92a57a_34b4_11e9_9026_10c37b702c42row3_col2" class="data row3 col2" >$44.10</td> 
    </tr>    <tr> 
        <th id="T_5e92a57a_34b4_11e9_9026_10c37b702c42level0_row4" class="row_heading level0 row4" >19</th> 
        <th id="T_5e92a57a_34b4_11e9_9026_10c37b702c42level1_row4" class="row_heading level1 row4" >Pursuit, Cudgel of Necromancy</th> 
        <td id="T_5e92a57a_34b4_11e9_9026_10c37b702c42row4_col0" class="data row4 col0" >8</td> 
        <td id="T_5e92a57a_34b4_11e9_9026_10c37b702c42row4_col1" class="data row4 col1" >$1.02</td> 
        <td id="T_5e92a57a_34b4_11e9_9026_10c37b702c42row4_col2" class="data row4 col2" >$8.16</td> 
    </tr></tbody> 
</table> 

```python
# Copying df
profitable_items = popular_item

# Sorting based on Total Purchase Value taking top 5
profitable_items_5 = profitable_items.sort_values('Total Purchase Value', ascending = False).head()

# Displaying as currency
profitable_items_5.style.format({'Item Price' : '${:,.2f}', 'Total Purchase Value' : '${:,.2f}'})
```
 
<table id="T_5e942bfa_34b4_11e9_8075_10c37b702c42" > 
<thead>    <tr> 
        <th class="blank" ></th> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Purchase Count</th> 
        <th class="col_heading level0 col1" >Item Price</th> 
        <th class="col_heading level0 col2" >Total Purchase Value</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Item ID</th> 
        <th class="index_name level1" >Item Name</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_5e942bfa_34b4_11e9_8075_10c37b702c42level0_row0" class="row_heading level0 row0" >178</th> 
        <th id="T_5e942bfa_34b4_11e9_8075_10c37b702c42level1_row0" class="row_heading level1 row0" >Oathbreaker, Last Hope of the Breaking Storm</th> 
        <td id="T_5e942bfa_34b4_11e9_8075_10c37b702c42row0_col0" class="data row0 col0" >12</td> 
        <td id="T_5e942bfa_34b4_11e9_8075_10c37b702c42row0_col1" class="data row0 col1" >$4.23</td> 
        <td id="T_5e942bfa_34b4_11e9_8075_10c37b702c42row0_col2" class="data row0 col2" >$50.76</td> 
    </tr>    <tr> 
        <th id="T_5e942bfa_34b4_11e9_8075_10c37b702c42level0_row1" class="row_heading level0 row1" >82</th> 
        <th id="T_5e942bfa_34b4_11e9_8075_10c37b702c42level1_row1" class="row_heading level1 row1" >Nirvana</th> 
        <td id="T_5e942bfa_34b4_11e9_8075_10c37b702c42row1_col0" class="data row1 col0" >9</td> 
        <td id="T_5e942bfa_34b4_11e9_8075_10c37b702c42row1_col1" class="data row1 col1" >$4.90</td> 
        <td id="T_5e942bfa_34b4_11e9_8075_10c37b702c42row1_col2" class="data row1 col2" >$44.10</td> 
    </tr>    <tr> 
        <th id="T_5e942bfa_34b4_11e9_8075_10c37b702c42level0_row2" class="row_heading level0 row2" >145</th> 
        <th id="T_5e942bfa_34b4_11e9_8075_10c37b702c42level1_row2" class="row_heading level1 row2" >Fiery Glass Crusader</th> 
        <td id="T_5e942bfa_34b4_11e9_8075_10c37b702c42row2_col0" class="data row2 col0" >9</td> 
        <td id="T_5e942bfa_34b4_11e9_8075_10c37b702c42row2_col1" class="data row2 col1" >$4.58</td> 
        <td id="T_5e942bfa_34b4_11e9_8075_10c37b702c42row2_col2" class="data row2 col2" >$41.22</td> 
    </tr>    <tr> 
        <th id="T_5e942bfa_34b4_11e9_8075_10c37b702c42level0_row3" class="row_heading level0 row3" >92</th> 
        <th id="T_5e942bfa_34b4_11e9_8075_10c37b702c42level1_row3" class="row_heading level1 row3" >Final Critic</th> 
        <td id="T_5e942bfa_34b4_11e9_8075_10c37b702c42row3_col0" class="data row3 col0" >8</td> 
        <td id="T_5e942bfa_34b4_11e9_8075_10c37b702c42row3_col1" class="data row3 col1" >$4.88</td> 
        <td id="T_5e942bfa_34b4_11e9_8075_10c37b702c42row3_col2" class="data row3 col2" >$39.04</td> 
    </tr>    <tr> 
        <th id="T_5e942bfa_34b4_11e9_8075_10c37b702c42level0_row4" class="row_heading level0 row4" >103</th> 
        <th id="T_5e942bfa_34b4_11e9_8075_10c37b702c42level1_row4" class="row_heading level1 row4" >Singed Scalpel</th> 
        <td id="T_5e942bfa_34b4_11e9_8075_10c37b702c42row4_col0" class="data row4 col0" >8</td> 
        <td id="T_5e942bfa_34b4_11e9_8075_10c37b702c42row4_col1" class="data row4 col1" >$4.35</td> 
        <td id="T_5e942bfa_34b4_11e9_8075_10c37b702c42row4_col2" class="data row4 col2" >$34.80</td> 
    </tr></tbody> 
</table> 




```python

```
