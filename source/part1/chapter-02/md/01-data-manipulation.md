---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.6.0
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

<!-- #region deletable=true editable=true -->
# Data manipulation and analysis

Now you have learned the basics of pandas data structures (i.e. *Series* and *DataFrame*) and you should be familiar with basic methods for loading and exploring data. Next, we will continue exploring the pandas functionalities, and see how it can be used for data manipulation, conducting simple calculations, and making selections based on specific criteria.

## Basic calculations

One of the most common things to do in pandas is to create new columns based on calculations between different variables (columns). Next, we will learn how to do that using the same input data (`'Kumpula-June-2016-w-metadata.txt'`) as in the previous section. We will first load it using the `pd.read_csv()` method. Remember, that the first 8 lines contains the metadata which we will skip. This time, let's store the filepath into a separate variable in order to make the code more readable and easier to change afterwards (a good practice).
<!-- #endregion -->

```python deletable=true editable=true jupyter={"outputs_hidden": false}
import pandas as pd

# Define file path:
fp = 'data/Kumpula-June-2016-w-metadata.txt'

# Read in the data from the file (starting at row 9):
data = pd.read_csv(fp, skiprows=8)
```

As a first step, it is always good to remember to check the data after reading it. This way we can be sure that everything looks as it should.

```python
data.head()
```

All good.

Now we can start by creating a new column `DIFF` in our DataFrame. This can be done by specifying the name of the column and giving it some default value (in this case the decimal number `0.0`).

```python deletable=true editable=true jupyter={"outputs_hidden": false}
# Define a new column "DIFF"
data['DIFF'] = 0.0

# Check how the dataframe looks like:
data.head()
```

<!-- #region deletable=true editable=true -->
As we can see, now we have a new column (`DIFF`) in our DataFrame that has value 0.0 for all rows. When creating a new column, you can *initialize* it with any value you want. Typically, the value could be a number 0 as in here, but it could also be `None` (i.e. nothing), some text (e.g. `"test text"`), or more or less any other value or object that can be represented as a single item. You could even initiliaze the column by storing a function inside the cells if you like.   

Let's continue by checking the datatype of our new column.
<!-- #endregion -->

```python deletable=true editable=true jupyter={"outputs_hidden": false}
data['DIFF'].dtypes
```

<!-- #region deletable=true editable=true -->
As we can see, pandas created a new column and automatically recognized that the data type is float as we passed a 0.0 value to it.

Okay great, but whatabout making those calculations with pandas as promised in the beginning? Next, we will calculate the difference between `MAX` and `MIN` columns to get an idea how much the temperatures have been varying during different days. The result will be updated into the column `DIFF` that we created earlier. A typical way of conducting calculations such as this, is to access the Series (columns) that interests us from the DataFrame and conduct the mathematical calculation using the selected columns. Typically you store the result directly into a column in the DataFrame, like following:
<!-- #endregion -->

```python deletable=true editable=true jupyter={"outputs_hidden": false}
# Calculate max min difference
data['DIFF'] = data['MAX'] - data['MIN']

# Check the result
data.head()
```

<!-- #region deletable=true editable=true -->
The calculations were stored into the ``DIFF`` column as planned. Conducting calculation like this is extremely fast in pandas because the math operations happen in *vectorized* manner. This means that instead of looping over individual values of the DataFrame and comparing them to each other, calculating the difference happens simultaneously at all rows.

You can also create new columns on-the-fly when doing the calculation (i.e. the column does not have to exist before). Furthermore, it is possible to use any kind of math algebra (e.g. subtracttion, addition, multiplication, division, exponentiation, etc.) when creating new columns.

We can for example convert the Fahrenheit temperatures in the `TEMP` column into Celsius using the formula that we have seen already many times. Let's do that and store it in a new column called `TEMP_CELSIUS`.
<!-- #endregion -->

```python deletable=true editable=true jupyter={"outputs_hidden": false}
# Create a new column and convert temp fahrenheit to celsius:
data['TEMP_CELSIUS'] = (data['TEMP'] - 32) / (9/5)

# Check output
data.head()
```

**Check your understanding**

**NOTE: THIS IS QUITE COMPLICATED TASK. MAKE AN EASIER ONE THAT DOES NOT REQUIRED GOING BACK TO OTHER MATERIALS.** Calculate the temperatures in Kelvins using the Celsius values **and store the result a new column** calle `TEMP_KELVIN` in our dataframe.
0 Kelvins is is -273.15 degrees Celsius as we learned in Chapter 1.

```python
# Add column "TEMP_KELVIN" and populate it with Kelvin values

```

<!-- #region deletable=true editable=true -->
## Selecting and updating data

We often want to make selections from our data and only use specific rows from a DataFrame in the analysis. There are multiple ways of selecting subsets of a pandas DataFrame than can be based on e.g. specific index values or using some predefined criteria to make the selection, such as "give me all rows where values in column X are larger than zero". Next, we will go through the most useful tricks for selecting specific rows, columns and individual values.


### Selecting rows and columns

One common way of selecting only specific rows from your DataFrame is done via a concept of **slicing**. Slicing in pandas can be done in a similar manner as with normal Python lists, i.e. you specify index range you want to select inside the square brackets: ``dataframe[start_index:stop_index]``.

Let's select the first five rows and assign them to a variable called `selection`. Here, we will first see how selecting the data works like you would do using normal Python list.
<!-- #endregion -->

```python deletable=true editable=true jupyter={"outputs_hidden": false}
# Select first five rows of dataframe using row index values
selection = data[0:5]
selection
```

<!-- #region deletable=true editable=true -->
Here we have selected the first five rows (index 0-4) using the integer index. Notice that the logic here follows how Python's list slicing (or `range` function) works, i.e. the value on the right side of the colon (here number `5`) tells when to stop, but that value is not taken into the final selection. Hence, the syntax is `start_index:stop_index` (also additional parameter `:step` could be added here to the end). 
<!-- #endregion -->

<!-- #region deletable=true editable=true -->
Doing selections like in the previous example can be done, but there is also a better and more flexible way of selecting data using so called `.loc` label-indexing. As the name implies, `loc` selects data based on axis labels (row and column labels). This does not necesssarily tell much to you at this point, but `loc` makes it possible to conduct more specific selections, such as allowing you to choose which columns are chosen when selecting a subset of rows. It also makes possible to benefit from row labels that are not necessarily sequantial numbers (as with all our examples thus far), but they can represent other objects as well, such as dates or timestamps. Hence, `loc` can become very handy when working with timeseries data (we will learn more about this later). 

Let's test the `loc` label-indexing by selecting temperature values from column `TEMP` using rows 0-5:
<!-- #endregion -->

```python deletable=true editable=true jupyter={"outputs_hidden": false}
# Select temp column values on rows 0-5
selection = data.loc[0:5, 'TEMP']
selection
```

Notice that in this case, we get six rows of data (index 0-5)! This happens because we are now doing the selection based on axis labels instead of normal Python-kind of indexing. It is important to notice the difference between these two approaches, as mixing the two may cause confusion,  incorrect analysis results or bugs in your code, if you do not pay attention. We recommend to use `loc` always when possible (there are specific cases when you want to use other approaches, more about this soon). 

Hence, the basic syntax for `loc` is:
 
 - `.loc[first_included_label:last_included_label, columns]`

By looking at the syntax, you might guess that it is also possible to select multiple columns when using `loc`. Next, we will test this by selecting the `TEMP` and `TEMP_CELSIUS` columns from a set of rows by passing them inside a list.

```python deletable=true editable=true jupyter={"outputs_hidden": false}
# Select columns temp and temp_celsius on rows 0-5
selection = data.loc[0:5, ['TEMP', 'TEMP_CELSIUS']]
selection
```

As a result, we now have a new DataFrame with two columns and 6 rows (i.e. index labels ranging from 0 to 5). 

A good thing to know when doing selections, is that the end result after the selection can be something called a ``view``. In such cases, the selection and the original data may still linked to each other. This happens e.g. if you make a selection like above but return only a single column from the original data. In some situations a change in the original *data* for that specific column can also change the value in the *selection*. Without going into details why and when this happens, this behavior can nevertheless be confusing having unexpected consequences. To avoid this behavior, a good practice to follow is to always make a copy whenever doing selections (i.e. *unlink* the two DataFrames). You can make a copy easily while doing the selection by adding a `.copy()` at the end of the command.    

```python
# Select columns temp and temp_celsius on rows 0-5 and 
# make a copy out of it to ensure they are not linked to each other
selection = data.loc[0:5, ['TEMP', 'TEMP_CELSIUS']].copy()
selection
```

Now we have the exact same data in our end result, but we have ensured that the selection is not linked to the original data anymore. 

To demonstrate what can happen with the view, let's make a selection of a single column from our data, and modify the data a bit to see what consequences might happen if we are not careful.

```python
# Select a column that will be end up being a "view"
temp = selection["TEMP"]
temp
```

Now if we make a change to our original data, i.e. *selection*, it will also influence our values in *temp*:

```python
# Update the first value of the TEMP column
selection.iloc[0,0] = 30.0
selection.head()
```

```python
# Check the values in temp (which we did not touch)
temp
```

As we can see, now the value in our *temp* Series changed from 65.5 to 30.0 although we did not make any change to it directly. The change happened nevertheless because the data objects were still linked to each other. 


**Test your understanding**

Calculate the mean temperature (in Celsius) for the last seven days of June. Do the selection using the row index values.


### Selecting a single row or value

You can also select an individual row from specific position using the `.loc[]` indexing. Here we select all the data values using index 4 (the 5th row):

```python deletable=true editable=true jupyter={"outputs_hidden": false}
# Select one row using index
row = data.loc[4]
row
```

<!-- #region deletable=true editable=true -->
``.loc[]`` indexing returns the values from that position as a ``Series`` where the indices are actually the column names of those variables. Hence, you can access the value of an individual column by referring to its index using following format (both should work):
<!-- #endregion -->

```python deletable=true editable=true jupyter={"outputs_hidden": false}
# Print one attribute from the selected row
row['TEMP']
```

Sometimes it is enough to access a single value in a DataFrame directly. In this case, we can use ``.at`` instead of `loc`.
Let's select the temperature (column `TEMP`) on the first row (index `0`) of our DataFrame.

```python
selection.at[0, "TEMP"]
```

As an output, we got the individual value 65.5. `at` works only when accessing a single value, whereas the `loc` can be used to access both a single or multiple values at the same time. The end result when fetching a single value with `loc` is exactly the same. The difference between the two approaches is minimal, hence we recommend using `loc` in all cases because it is more flexible (`at` is slightly faster but in most cases it does not make a difference). 

```python
selection.loc[0, "TEMP"]
```

### Selecting values based on index positions

As we have learned thus far, `.loc` and `.at` are based on the *axis labels* - the names of columns and rows. For positional based indexing, pandas has an `.iloc` which is based on *integer value* indices. With `.iloc`, it is also possible to refer to the columns based on their index value (i.e. to a positional number of a column in the DataFrame). For example,  `data.iloc[0,0]` would return `20160601` in our example DataFrame which is the value on the first row and first column in the data.
    

```python
# Check the first rows
print(data.head())
print()
print("Value at position (0,0) is", data.iloc[0,0])
```

Hence, the syntax for `iloc` is:

 - `iloc[start_row_position:stop_row_position, start_column_position:stop_column_position]`

By following this syntax, we can access the value on the first row and second column (`TEMP`) by calling:

```python
data.iloc[0,1]
```

It is also possible to get ranges of rows and columns with `iloc`. For example, we could select `YEARMODA` and `TEMP` columns from the first five rows based on their indices (positions) in the data:

```python
# Select rows from positions 0 to 5
# and columns from positions 0 to 2 
selection = data.iloc[0:5:,0:2]
selection
```

A good thing to notice, is that with `iloc`, the behavior in terms of how many rows are returned differs from `loc`. Here, the `0:5` returns 5 rows (following the Python list slicing behavarior), whereas using `loc` would return 6 rows (i.e. also including the row at index 5). 
    
One handy functionality with `iloc` is the ability to fetch data starting from the end of the DataFrame. Hence, it is possible to retrieve the last row in the DataFrame by passing a negative number to the `iloc`, where value -1 corresponds to the last row (or column), -2 corresponds to the second last, and so on. Following this, it is easy to see e.g. what is the ``TEMP_CELSIUS`` value (the last column) of the last row of data.

```python
# Check the value on the last row and last column in the data
data.iloc[-1, -1]
```

<!-- #region deletable=true editable=true -->
### Conditional selections

One really useful feature in pandas is the ability to easily filter and select rows based on a conditional statement.
The following example shows how we check if the Celsius temperature at each row on the `TEMP_CELSIUS`column is higher than 15 degrees.
<!-- #endregion -->

```python
# Check the condition
data['TEMP_CELSIUS'] > 15
```

As a result, we get a Series of booleans, where the value `True` or `False` at each row determines whether our condition was met or not. This kind of Series or numpy.array of boolean values based on some predefined criteria is typically called a ``mask``. We can take advantage of this mask when doing selections with `loc` based on specific criteria. In the following, we will use the same criteria, and store all rows meeting the criteria into a variable `warm_temps` (warm temperatures). We can specify the criteria directly inside the `loc` square brackets:

```python deletable=true editable=true jupyter={"outputs_hidden": false}
# Select rows with temp celsius higher than 15 degrees
warm_temps = data.loc[data['TEMP_CELSIUS'] > 15]
warm_temps
```

<!-- #region deletable=true editable=true -->
It is also possible to combine multiple criteria at the same time. Here, we select temperatures above 15 degrees that were recorded on the second half of June in 2016 (i.e. `YEARMODA >= 20160615`).
Combining multiple criteria can be done with the `&` operator (AND) or the `|` operator (OR). Notice, that it is often useful to separate the different clauses inside the parentheses `()`.
<!-- #endregion -->

```python deletable=true editable=true jupyter={"outputs_hidden": false}
# Select rows with temp celsius higher than 15 degrees from late June 2016
warm_temps = data.loc[(data['TEMP_CELSIUS'] > 15) & (data['YEARMODA'] >= 20160615)]
warm_temps
```

<!-- #region deletable=true editable=true -->
Now we have a subset of our DataFrame with only rows where the `TEMP_CELSIUS` is above 15 and the dates in `YEARMODA` column start from 15th of June. Notice, that the index values (numbers on the left) are still showing the index labels from the original DataFrame. This indicates that our result is really a slice from the original data. 
<!-- #endregion -->

It is possible to **reset** the index using `reset_index()` function which makes the index numbering to start from 0 and increase the index values in a sequantal manner. This is often a useful operation to do, because it makes it easier then to slice the data with `loc` or `iloc`. By default the `reset_index()` would make a new column called `index` to keep track on the previous index which might be useful in some cases but here not, so we can omit that by passing parameter `drop=True`. 

```python deletable=true editable=true jupyter={"outputs_hidden": false}
# Reset index
warm_temps = warm_temps.reset_index(drop=True)
warm_temps
```

As can be seen, now the index values goes from 0 to 12. Resetting the index has now also *unlinked* the ``warm_temps`` DataFrame from the ``data``, meaning that it is not a view anymore but an independent Pandas object. 


When making selections, it is quite typical that pandas might give you warnings if you continue to work with the selected data without resetting the index or taking a copy when you make the selection. To demonstrate this, make the selection again and do a small change for the first value of the ``TEMP_CELSIUS`` column. Here, we can take advantage of the `iloc` which makes it easy to access the first row based based on position 0. 

```python
# Make the selection
warm_temps = data.loc[(data['TEMP_CELSIUS'] > 15) & (data['YEARMODA'] >= 20160615)]

# Now update the first value of the last column (i.e. column position -1) in our selection
warm_temps.iloc[0, -1] = 17.5
```

Because we modified the selection which is a slice from the original data, pandas gives us a warning about a possibly invalid value assignment. In most cases, the warning can be ignored but it is a good practice to always take a copy when doing selections, especially if you continue working with the selection:

```python
# Make the selection and take a copy
warm_temps = data.loc[(data['TEMP_CELSIUS'] > 15) & (data['YEARMODA'] >= 20160615)].copy()

# Now update the first value of the last column (i.e. column position -1) in our selection
warm_temps.iloc[0, -1] = 17.5
```

As we can see, now we did not receive any warnings, and it would be safe to continue working with this selection. 


#### Check your understanding

Find the mean temperatures (in Celsius) for the last seven days of June again. This time you should select the rows based on a condition for the `YEARMODA` column!

```python
# Mean temperature for the last seven days of June (use a conditional statement to select the correct rows):
data['TEMP_CELSIUS'].loc[data['YEARMODA'] >= 20160624].mean()
```

<!-- #region deletable=true editable=true -->
## Dealing with missing data

As you may have noticed by now, we have several missing values for the temperature minimum, maximum, and difference columns (`MIN`, `MAX`, `DIFF`, and `DIFF_MIN`). These missing values are indicated as `NaN` (not-a-number). Having missing data in your datafile is really common situation and typically you want to deal with it somehow. Common procedures to deal with `NaN` values are to either **remove** them from
the DataFrame or **fill** them with some value. In Pandas both of these options are really easy to do.

Let's first start by checking whether our data has NaN values.
<!-- #endregion -->

```python
# Check the data
warm_temps
```

As we can see, the ``MIN`` and ``DIFF`` columns are missing values at index 26. It is also possible to confirm this with pandas by accessing a specific Series attribute called `.hasnans` which can be a handy tool especially when automating some data analysis pipelines. Each Series (i.e. column) in the DataFrame has this attribute and you can use it as follows:

```python
# Check with pandas if MIN column contains NaNs
warm_temps["MIN"].hasnans
```

As a result, you get either True or False, depending on whether the Series contained any NaN values, or not.


Let's now see how we can remove the NoData values (i.e. clean the data) using the `.dropna()` function. Inside the function you can pass a list of column(s) from which the `NaN` values should found using the `subset` parameter.

```python deletable=true editable=true jupyter={"outputs_hidden": false}
# Drop no data values based on the MIN column
warm_temps_clean = warm_temps.dropna(subset=['MIN'])
warm_temps_clean
```

<!-- #region deletable=true editable=true -->
As you can see by looking at the table above (and the change in index values), we now have a DataFrame without the NoData values. By doing this, you naturally loose data (rows) which might not be an optimal solution in some cases.

Hence, pandas also provides an option to fill the NoData with some value using `fillna()` function. Here, we can fill the missing values in the with value -9999. Note that we are not giving the `subset` parameter this time.
<!-- #endregion -->

```python deletable=true editable=true jupyter={"outputs_hidden": false}
warm_temps.fillna(-9999)
```

<!-- #region deletable=true editable=true -->
As a result we now have a DataFrame where all NoData values in the whole DataFrame are filled with the value -9999. If you want to fill NaN values values of only a specific column, you can do that by targeting the `fillna` function to only a specific column (or columns): 
<!-- #endregion -->

```python
# Fill NaN of specific column
warm_temps["MIN"] = warm_temps["MIN"].fillna(-9999)
```

Notice that because we already filled every NaN in the whole DataFrame in the previous step, the command above does not change anything.  

It is important to be aware, that in many cases filling the data with a specific value is dangerous because you end up modifying the actual data, which might affect the results of your analysis. For example, in the case above we would have dramatically changed the temperature difference columns because the -9999 values not an actual temperature difference! Hence, use caution when filling missing values. 
    
In some cases, you might have to fill in no data values for the purposes of saving the data to file in a spesific format. For example, some GIS software don't accept missing values. Always pay attention to potential no data values when reading in data files and doing further analysis.


## Data type conversions

<!-- #region editable=true -->
When doing data analysis, one quite typical operation that needs to be done is to convert values in a column from one datatype to another, such as from floating point to integer. Remember, that we already did data type conversions in Chapter 1 using the built-in Python functions such as `int()` or `str()`.

For values stored in pandas Series, we can use `astype()` method. Next we will continue using the same data as previously, and convert all the temperature values (floats) in column ``TEMP`` to integers.

Let's start by looking our original data:
<!-- #endregion -->

```python
data['TEMP'].head()
```

Now we can easily convert those decimal numbers to integers by calling `astype(int)`:

```python
data['TEMP'].astype(int).head()
```

As we can see the values were converted to integers. However, it is important to be careful with type conversions from floating point values to integers. The conversion simply drops the stuff to the right of the decimal point, so all values are rounded down to the nearest whole number. For example, the second value in our Series (65.8) was truncated to 65 as an integer, when it clearly should be rounded up to 66.

Chaining the round and type conversion functions solves this issue as the `.round(0).astype(int)` command first rounds the values with zero decimals and then converts those values into integers.

```python editable=true jupyter={"outputs_hidden": false}
data['TEMP'].round(0).astype(int).head()
```

As we can see, now the integer values are correctly rounded. 

The `astype` method supports converting between all basic Python data types (`int`, `float`, `str`), but it also knows how to convert between more specific numpy data types, such as `int64`, `int32`, `float64`, `float32` to mention a few (see [^numpydtypes] for a full list). Using the numpy data type can useful if you need to be more specific e.g. how many bits should be reserved for storing the values. For instance, `int64` (i.e. *64-bit integer*) can store integer values ranging between -9223372036854775808 and 9223372036854775807, whereas `int16` can only store values from -32768 to 32767. If passing the "normal" `int` or `float` to the `astype` function, pandas will automatically store 64-bit numeric values. The larger bits you use, the more physical memory is required to store the data. Hence, in some specific cases e.g. when dealing with extremely large datasets, it might be useful to be able to determine that the values in specific columns are stored with lower bits (to save memory). 


## Sorting data

Quite often it is useful to be able to sort your data (descending/ascending) based on values in some column
This can be easily done with Pandas using `sort_values(by='YourColumnName')` -function.

Let's first sort the values on ascending order based on the `TEMP` column:

```python deletable=true editable=true jupyter={"outputs_hidden": false}
# Sort dataframe, ascending
data.sort_values(by='TEMP').head()
```

<!-- #region deletable=true editable=true -->
Of course, it is also possible to sort them in descending order with ``ascending=False`` parameter:

<!-- #endregion -->

```python deletable=true editable=true jupyter={"outputs_hidden": false}
# Sort dataframe, descending
data.sort_values(by='TEMP', ascending=False).head()
```

In some situations, you might need to sort values based on multiple columns simultaneously, which is sometimes called as multi-level sorting. This can be done by passing a list of column names to the `by` parameter. When you sort the data based on multiple columns, sometimes you also might want to sort your data in a way that the first-level sorting happens in ascending order, and the second-level sorting happens in descending order. A typical situation for this kind of sorting could be e.g. when sorting the temperatures first by weekday (Monday, Tuesday, etc.) and then under each weekday ordering the values in descending order that would always show the warmest temperature of specific week first.

Let's modify our data a bit to demonstrate this. We will add a new column that has information about the weekday. The 1st of June 2016 was Wednesday, so we start from that.

```python
# Create a list of weekdays that matches with our data
# The data covers 4 weeks + 2 days (i.e. altogether 30 days)
week_days = ["Wed", "Thu", "Fri", "Sat", "Sun", "Mon", "Tue"]
day_list = week_days*4 + week_days[:2]

# Add the weekdays to our DataFrame
data["WEEKDAY"] = day_list
data.head(10)
```

Now we have a new column with information about the weekday of each row. Next, we can test how to sort the values, so that we order the data by weekday and within each weekday the temperatures are in descending order. You can adjust how the ordering works by passing a list of boolean values to `ascending` parameter.

```python
data.sort_values(by=["WEEKDAY", "TEMP_CELSIUS"], ascending=[True, False]).head(10)
```

As a result the data is now ordered first by weekday (i.e. the same weekday values are grouped) and the within these weekdays the temperature values are always in descending order showing the warmest day first. Ordering data in this manner based on multiple criteria can sometimes be very useful when analyzing your data. 

<!-- #region deletable=true editable=true -->
## Writing data to a file

Lastly, it is of course important to be able to write the data that you have analyzed into your computer. This is really handy in Pandas as it supports many different data formats by default [^pandasio], such as CSV, Excel, JSON, HDF5, Pickle etc.

One of the most typical output formats is CSV file. Function `to_csv()` can be used to easily save your data in CSV format.
Let's first save the data from our `data` DataFrame into a file called `Kumpula_temp_results_June_2016.csv`.
<!-- #endregion -->

```python deletable=true editable=true jupyter={"outputs_hidden": false}
# define output filename
output_fp = "Kumpula_temps_June_2016.csv"

# Save dataframe to csv
data.to_csv(output_fp, sep=',')
```

<!-- #region deletable=true editable=true -->
Now we have the data from our DataFrame saved to a file and this is how it looks using a JupyterLab viewer:
![Text file output](../img/pandas-save-file-1.png)

As we can see, the first column in the datafile contains now the index value of the rows. There are also quite many decimals present in the new columns
that we created. We can deal with these and save the temperature values from `warm_temps` DataFrame without the index and with only 1 decimal in the floating point numbers.

Omitting the index can be with `index=False` parameter. Specifying how many decimals should be written can be done with `float_format` parameter where text `%.1f` defines pandas to use 1 decimals in all columns when writing the data to a file (changing the value 1 to 2 would write 2 decimals etc.)
<!-- #endregion -->

```python deletable=true editable=true jupyter={"outputs_hidden": false}
# define output filename
output_fp2 = "Kumpula_temps_above15_June_2016.csv"

# Save dataframe to csv
warm_temps.to_csv(output_fp2, sep=',', index=False, float_format="%.1f")
```

<!-- #region deletable=true editable=true -->
And this is how the temperature data looks now after the modifications:

![Output after float fomatting](../img/pandas-save-file-2.png)

As a results we have a "cleaner" output file without the index column, and with only 1 decimal for floating point numbers.
<!-- #endregion -->

### Footnotes

[^numpydtypes]: <https://numpy.org/doc/stable/user/basics.types.html>
[^pandasio]: <https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html>

```python

```