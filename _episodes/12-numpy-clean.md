---
title: "Cleaning data with Numpy"
teaching: 15
exercises: 15
questions:
- "How can I import and clean data in Python?"
objectives:
- "Read tabular data from a file into a program using `NumPy`."
- "Remove unwanted data columns"
- "Swap row and column data (transpose)"
- "Save data to a file"
keypoints:
- "Use the `NumPy` library to work with tabular data in Python"
- "The `loadtxt` function is used to read in .csv data"
- "The `loadtxt` function has several keywords which can simplify data parsing"
- "The `array` object has a `transpose` method which will transpose rows and columns"
- "The `savetxt` functions is used to write the data to a file"
---

~~~
import numpy 
~~~
{: .language-python}

Importing a library is like getting a piece of lab equipment out of a storage locker and setting it
up on the bench. Libraries provide additional functionality to the basic Python package, much like
a new piece of equipment adds functionality to a lab space. Just like in the lab, importing too
many libraries can sometimes complicate and slow down your programs - so we only import what we
need for each program. Once we've imported the library, we can ask the library to read our data
file for us:

~~~
numpy.loadtxt("./notebooks/UVVis-01.csv",delimiter=",")
~~~
{: .language-python}

The expression `numpy.loadtxt(...)` is a [function call]({{ page.root }}/reference/#function-call)
that asks Python to run the [function]({{ page.root }}/reference/#function) `loadtxt` which
belongs to the `numpy` library. This [dotted notation]({{ page.root }}/reference/#dotted-notation)
is used everywhere in Python: the thing that appears before the dot contains the thing that
appears after.

As an example, John Smith is the John that belongs to the Smith family.
We could use the dot notation to write his name `smith.john`,
just as `loadtxt` is a function that belongs to the `numpy` library.

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

`numpy.loadtxt` has two [arguments]({{ page.root }}/reference/#argument): the name of the file we want to read and the delimiter which separates data values in the file.
This data we have read in is from a UV-Vis experiment. 
The rows are the data for each wavelength,
and the columns are the individual samples.
We will also analyse the data using the `numpy` Python library, but before we do this we must clean up the data. There are two things we would like to do:

* Delete the repeated wavelength columns
* Transpose the data (swap rows and columns; so each row corresponds to a different sample)

We are able to do all the first two things on this list with the following command:

~~~
numpy.loadtxt("./notebooks/UVVis-01.csv",delimiter=",",usecols=[0,1,3,5,7,9,11,13,15,17,19])
~~~
{: .language-python}

`numpy.loadtxt` now has two keywords: the `delimiter` keyword and the `usecols` keyword which specifies the columns to read in.

Our call to `numpy.loadtxt` read our file
but didn't save the data in memory.
To do that,
we need to assign the array to a variable. Just as we can assign a single value to a variable, we
can also assign an array of values to a variable using the same syntax.  Let's re-run
`numpy.loadtxt` and save the returned data:

~~~
data = numpy.loadtxt("./notebooks/UVVis-01.csv",delimiter=",",usecols=[0,1,3,5,7,9,11,13,15,17,19])
~~~
{: .language-python}

This statement doesn't produce any output because we've assigned the output to the variable `data`.
If we want to check that the data have been loaded,
we can print the variable's value:

~~~
print(data)
~~~
{: .language-python}

~~~~
[[ 1.50000000e+03  4.47125000e-04 -3.66223800e-03 ...  1.20771340e-02
   3.98183100e-03  4.21040200e-03]
 [ 1.49900000e+03  6.55591000e-04 -3.49741500e-03 ...  1.22769590e-02
   4.22229500e-03  4.36906300e-03]
 [ 1.49800000e+03  8.64056000e-04 -3.34321500e-03 ...  1.24000520e-02
   4.32843200e-03  4.38802100e-03]
 ...
 [ 2.02000000e+02  1.00000000e+01 -1.22419536e-01 ...  3.11538220e-02
  -1.33138746e-01  8.95578190e-02]
 [ 2.01000000e+02  1.29667747e+00 -7.07442700e-03 ...  1.53292596e-01
  -6.67433520e-02  8.41182170e-02]
 [ 2.00000000e+02  1.66669679e+00 -1.82473719e-01 ... -2.67419547e-01
   1.55003861e-01  1.43565789e-01]]
~~~~
{: .output}

Now that the data is in memory,
we can manipulateit.
First,
let's ask what [type]({{ page.root }}/reference/#type) of thing `data` refers to:

~~~
print(type(data))
~~~
{: .language-python}

~~~
<class 'numpy.ndarray'>
~~~
{: .output}

The output tells us that `data` currently refers to
a n-dimensional array, the functionality for which is provided by the `numpy` library.

> ## Data Type
>
> An array is a central data structure of the NumPy library. 
> columns of potentially different types. An array is a grid of values that can be indexed in various ways.
> The elements are all of the same type, referred to as the array dtype.
{: .callout}

We can now use the `transpose` method to swap the rows and columns of `data`, and assign this to the variable `data`.

~~~
data = data.transpose()
print(data)
~~~
{: .language-python}

~~~
[[ 1.50000000e+03  1.49900000e+03  1.49800000e+03 ...  2.02000000e+02
   2.01000000e+02  2.00000000e+02]
 [ 4.47125000e-04  6.55591000e-04  8.64056000e-04 ...  1.00000000e+01
   1.29667747e+00  1.66669679e+00]
 [-3.66223800e-03 -3.49741500e-03 -3.34321500e-03 ... -1.22419536e-01
  -7.07442700e-03 -1.82473719e-01]
 ...
 [ 1.20771340e-02  1.22769590e-02  1.24000520e-02 ...  3.11538220e-02
   1.53292596e-01 -2.67419547e-01]
 [ 3.98183100e-03  4.22229500e-03  4.32843200e-03 ... -1.33138746e-01
  -6.67433520e-02  1.55003861e-01]
 [ 4.21040200e-03  4.36906300e-03  4.38802100e-03 ...  8.95578190e-02
   8.41182170e-02  1.43565789e-01]]
~~~
{: .output}

The final thing left to do is print our cleaned dataset to a file for analysing later. To do this we can use the `savetxt` function:

~~~
np.savetxt("./notebooks/UVVis-01-cleaned.csv",data)
~~~
{: .language-python}


