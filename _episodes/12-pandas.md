---
title: "Cleaning data with Pandas"
teaching: 15
exercises: 15
questions:
- "How can I import and clean tabular data in Python?"
objectives:
- "Read tabular data from a file into a program using `pandas`."
- "Remove unwanted data columns"
- "Swap row and column data (transpose)"
keypoints:
- "Use the `pandas` library to work with tabular data in Python"
- "The `read_csv` function is used to read in .csv data"
- "The `read_csv` function has several keywords which can simplify data parsing"
- "The `dataframe` object has a `transpose` method which will transpose rows and columns"
- "The `dataframe` object has a `to_csv` method which will write the dataframe to a file"
---

~~~
import pandas
~~~
{: .language-python}

Importing a library is like getting a piece of lab equipment out of a storage locker and setting it
up on the bench. Libraries provide additional functionality to the basic Python package, much like
a new piece of equipment adds functionality to a lab space. Just like in the lab, importing too
many libraries can sometimes complicate and slow down your programs - so we only import what we
need for each program. Once we've imported the library, we can ask the library to read our data
file for us:

~~~
pandas.read_csv("./data/UVVis-01.csv")
~~~
{: .language-python}

The expression `pandas.read_csv(...)` is a [function call]({{ page.root }}/reference/#function-call)
that asks Python to run the [function]({{ page.root }}/reference/#function) `read_csv` which
belongs to the `pandas` library. This [dotted notation]({{ page.root }}/reference/#dotted-notation)
is used everywhere in Python: the thing that appears before the dot contains the thing that
appears after.

As an example, John Smith is the John that belongs to the Smith family.
We could use the dot notation to write his name `smith.john`,
just as `read_csv` is a function that belongs to the `pandas` library.

Since we haven't told it to do anything else with the function's output,
the notebook displays it.
In this case,
that output is the data we just loaded.
By default,
only a few rows and columns are shown
(with `...` to omit elements when displaying big arrays).
To save space,
Python displays numbers as `1.` instead of `1.0`
when there's nothing interesting after the decimal point.

`pandas.read_csv` has one [argument]({{ page.root }}/reference/#argument): the name of the file we want to read.
This data we have read in is from a UV-Vis experiment. 
We will analyse the data using the `numpy` Python library, but before we do this we must clean up the dataframe. There are three things we would like to do:

* Delete the repeated wavelength columns
* Set the correct column headings (numpy has automatically set the first row of data as the column headings)
* Transpose the data (swap rows and columns; so each row corresponds to a different sample)

We are able to do all the first two things on this list with the following command:

~~~
pandas.read_csv("./data/UVVis-01.csv",usecols=[1,3,5,7,9,11,13,15,17,19],header=None)
~~~
{: .language-python}

`pandas.read_csv` now has two [parameters]({{ page.root }}/reference/#parameter): the `usecols` keyword which specifies the columns to read in and the `header` keyword which, when we set to `False`, tells the `read_csv` function that there is no heading data in the file and that the headers should be set to an integer range. 

Our call to `pandas.read_csv` read our file
but didn't save the data in memory.
To do that,
we need to assign the array to a variable. Just as we can assign a single value to a variable, we
can also assign an array of values to a variable using the same syntax.  Let's re-run
`pandas.read_csv` and save the returned data:

~~~
data = pandas.read_csv("./data/UVVis-01.csv",usecols=[1,3,5,7,9,11,13,15,17,19],header=None)
~~~
{: .language-python}

This statement doesn't produce any output because we've assigned the output to the variable `data`.
If we want to check that the data have been loaded,
we can print the variable's value:

~~~
print(data)
~~~
{: .language-python}

~~~
~~~
{: .output}

Now that the data are in memory,
we can manipulate them.
First,
let's ask what [type]({{ page.root }}/reference/#type) of thing `data` refers to:

~~~
print(type(data))
~~~
{: .language-python}

~~~
<class 'pandas.DataFrame'>
~~~
{: .output}

The output tells us that `data` currently refers to
an pandas DataFrame, the functionality for which is provided by the `pandas` library.

> ## Data Type
>
> A Pandas DataFrame is a two-dimensional labeled data structure with 
> columns of potentially different types.
{: .callout}

The `transpose` method swaps the rows and columns of the resulting `dataframe`.
