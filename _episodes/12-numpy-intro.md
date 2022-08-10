---
title: "Storing data in Numpy arrays"
teaching: 20
exercises: 25
questions:
- "What is a Numpy array and when is it useful?"
- "How can I import and clean data in Python?"
objectives:
- "Read tabular data from a file into a program using `NumPy`"
- "Describe the key features and use-cases of a Numpy n-dimensional array"
- "Clean data for easier file parsing"
- "Save data to a file"
- "Create Numpy arrays"
- "Create an automatic counter within a FOR loop"
- "Iterate through 1d and 2d Numpy arrays"
keypoints:
- "Use the `NumPy` library to work with numerical data in Python"
- "The `loadtxt` function is used to read in .csv data"
- "Built-in Python functions can be used to read file headings"
- "To save the data to memory we can assign it to a variable"
- "An array is a central data structure of the NumPy library"
- "Extra information about an array are stored as attributes"
- "The `savetxt` function is used to write data to a file"
- "`numpy.linspace` generates evenly spaced numbers over a given interval"
- "The `enumerate` function allows us to have an automatic counter within a `for` loop"
---

## Use the `NumPy` library to work with numerical data in Python

In this tutorial we will use Numpy to read in experimental data.
In order to load this data, we need to access
([import]({{ page.root }}/reference/#import) in Python terminology) a library called
[NumPy](http://docs.scipy.org/doc/numpy/ "NumPy Documentation").  In general you should use this
library if you want to do fancy things with numbers, especially if you have matrices or arrays.  We
can import NumPy using:

~~~
import numpy 
~~~
{: .language-python}

> ## Numpy or Pandas?
>
> Another common Python package for working with 2-dimensional tabular data is Pandas.
> If you have heterogeneous data - columns with different data-types (strings and floats for example) - Pandas might be a good choice.
> If you are applying mathematical operations to multi-dimensional arrays, Numpy is a good choice. NumPy typically consumes less memory than Pandas, but this only becomes noticeable for very large arrays.
> For this relatively small 2-dimensional table of floats, either will work well.
{: .callout}


> ## Scientists Dislike Typing
>
> We will always use the syntax `import numpy` to import NumPy.
> However, in order to save typing, it is
> [often suggested](http://www.scipy.org/getting-started.html#an-example-script)
> to make a shortcut like so: `import numpy as np`.
> If you ever see Python code online using a NumPy function with `np`
> (for example, `np.loadtxt(...)`), it's because they've used this shortcut.
> When working with other people, it is important to agree on a convention of how common libraries
> are imported.
{: .callout}


## The `loadtxt` function is used to read in .csv data

To load the data file we can use the expression `numpy.loadtxt(...)`. This is a [function call]({{ page.root }}/reference/#function-call)
that asks Python to run the [function]({{ page.root }}/reference/#function) `loadtxt` which
belongs to the `numpy` library.

~~~
numpy.loadtxt("./data/transmittance.csv",delimiter=",",skiprows=1)
~~~
{: .language-python}

Since we haven't told the notebook to do anything else with the function's output,
the notebook displays it.
In this case,
that output is the data we just loaded.
By default,
only a few rows and columns are shown
(with `...` to omit elements when displaying big arrays).
Also note that, to save space, Python displays numbers as `1.` instead of `1.0`
when there's nothing after the decimal point.

`numpy.loadtxt` has three [arguments]({{ page.root }}/reference/#argument): the name of the file we want to read, the delimiter which separates data values in the file and the number of rows to skip when reading the file. The first row contains column names, and so we ask Numpy to skip this.


### What is the meaning of this data?

This data we have read in is transmittance data from a UV-Vis experiment. When light interacts with a medium some of it will be transmitted, reflected or absorbed. Transmittance is the intensity of the transmitted radiation leaving the medium, normalised by the intensity of the radiation entering the medium. As such it is usually expressed as a percentage. 
The rows contain the data for each wavelength,
and the columns contain the data for different materials.

## Built-in Python functions can be used to read file headings

To read in the column headings we can use Python:

~~~
f = open("./data/transmittance.csv")
header = f.readline()
header
~~~
{: .language-python}

~~~
'\ufeffWavelength (nm),Transmittance ITO (%),Transmittance CdS (%),Transmittance Si (%),Transmittance GaAs (%)\n'
~~~
{: .output}

Note that in the code below we are *not* using the Numpy library - just built-in Python functions.
There are some rogue unicode characters that are a relic from the excel file that originally held this data.
To remove these characters we can specify the `encoding` keyword - an internet search of `\ufeff` suggested this solution.
The internet search bar is a useful friend when programming!

~~~
f = open("./data/transmittance.csv", encoding='utf-8-sig')
header = f.readline()
header
~~~
{: .language-python}

~~~
'Wavelength (nm),Transmittance ITO (%),Transmittance CdS (%),Transmittance Si (%),Transmittance GaAs (%)\n'
~~~
{: .output}

We can now see that the first heading corresponds to Wavelength, the second to ITO transmittance, the third to CdS transmittance and so on. Note that the `\n` denotes a newline character - it is not unicode.

## To save the data to memory we can assign it to a variable

Note that our call to `numpy.loadtxt` read our file
but didn't save the data in memory.
To do that,
we need to assign the array to a variable. Just as we can assign a single value to a variable, we
can also assign an array of values to a variable using the same syntax.  Let's re-run
`numpy.loadtxt` and save the returned data:

~~~
numpy.loadtxt("./data/transmittance.csv",delimiter=",",skiprows=1)
~~~
{: .language-python}

This statement doesn't produce any output because we've assigned the output to the variable `data`.
If we want to check that the data have been loaded,
we can print the variable's value:

~~~
print(data)
~~~
{: .language-python

## An array is a central data structure of the NumPy library

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

An array is a central data structure of the NumPy library. 
columns of potentially different types. An array is a grid of values that can be indexed in various ways.
The elements are all of the same type, referred to as the array dtype.

> ## Arrays vs lists
>
> You may wonder why we care about Numpy arrays, when we already have Python lists.
> A NumPy array holds on a single type of data, whilst lists can hold elements of different types.
> This makes NumPy more efficient in memory usage.
> It also makes it quicker to iterate through a NumPy array and manipulate elements in the array.
> Arrays are more suited to mathematical tasks as the operations are element-by-element. 
> For example, what happens when we multiply a list by a integer? 
> Is this what we would expect to see when working with vectors?
{: .callout}

The `type` function tells us that
a variable is a NumPy array but won't tell you the type of
thing inside the array.
To find out the type
of the data contained in the NumPy array we can print the `dtype` attribute.

~~~
print(data.dtype)
~~~
{: .language-python}

~~~
'float64'
~~~
{: .output}

This tells us that the NumPy array's elements are
[floating-point numbers]({{ page.root }}/reference/#floating-point number).

## Extra information about an array are stored as attributes

When we
created the variable `data` to store our absorption data, we didn't just create the array; we also
created information about the array, called attributes. This extra information describes `data` in the same way an adjective describes a noun.

For example, `data.shape` is an attribute of `data` which describes the dimensions of `data`. 

~~~
print(data.shape)
~~~
{: .language-python}

~~~
(148, 5)
~~~
{: .output}

The output tells us that the `data` array variable contains 11 rows and 1301 columns. 

Note that we use the same
dotted notation for the attributes of variables that we use for the functions in libraries because
they have the same part-and-whole relationship.

## The `savetxt` function is used to write data to a file

If we want to save a file with clean header data (without the unicode) we can use the NumPy `savetxt` function:

~~~
numpy.savetxt('./data/transmittance_cleaned.csv',data,header=header)
~~~
{: .language-python}

Now when we read this in we do not need to specify the unicode encoding, as the unicode is no longer there!

~~~
f = open("./data/transmittance_cleaned.csv")
header = f.readline()
header
~~~
{: .language-python}

~~~
'% Wavelength (nm),Transmittance ITO (%),Transmittance CdS (%),Transmittance Si (%),Transmittance GaAs (%)\n'
~~~
{: .output}

Note that Numpy has inserted a `%` at the start of the header line to indicate that it is a comment and should be ignored. Numpy has also written the file without commas separating each data value. As a result, we can read in this cleaned data file with a single numpy argument:

~~~
numpy.loadtxt("./data/transmittance.csv")
~~~
{: .language-python}

## Create an array for storing data yet-to-be-generated using `numpy.zeros`

In the previous example we imported data from a file as a Numpy array. However it may be that we want to create a Numpy array which stores calculation data that is generated within the code itself.
For example, we may want to calculate the velocity of a ball at 50 points in time between 0 and 10 seconds inclusive. First we create an empty Numpy array with the correct dimensions

~~~
velocity_array = numpy.zeros(50) # empty array to hold calculated values
~~~
{: .language-python}

## Use `numpy.linspace` to generate evenly spaced numbers over a given interval.

To specify the times at which we take measurements of the ball speed we can use the `numpy.linspace` function. This will generate an array with 50 elements, each of which is evenly spaced between 0 and 10 (inclusive).

~~~
times = numpy.linspace(0,10,50) # times between 0 and 10s
~~~
{: .language-python}

## The `enumerate` function allows us to have an automatic counter within a `for` loop

Enumerate is a Python built-in function. It allows us to have an automatic counter within a `for` loop. The best way to understand `enumerate` is to see it in action.

~~~
for index, value in enumerate([10,20,30]):
    print("index is: ", index)
    print("value is: ", value)
~~~
{: .language-python}

~~~
index is: 0
value is: 10
index is: 1
value is: 20
index is: 2
value is: 30
~~~
{: .output}

We can use `enumerate` to index the velocity array as we iterate through the `for` loop.

~~~
velocity_array = numpy.zeros(50) # empty array to hold calculated values

for index,time in enumerate(times): 
       velocity_array[index] = v_0 + g*time
~~~
{: .language-python}

Finally, we can use `numpy.around` to round the calculated velocities to 2 decimal places.

~~~
numpy.around(velocity_list, decimals=2) 
~~~
{: .language-python}

Although this approach generates the correct velocity values, we can use [Numpy operations] to write more readable code in fewer lines. This will be explored further in the following question.

> ## Creating two-dimensional Numpy arrays
>
> Create a two-dimensional velocity with 4 rows and 5000 columns. Each row corresponds to a different starting 
> velocity value 
> (-10,0,10,20 m/s) and each column corresponds to an evenly spaced point in time (between 0 and 100 seconds 
> inclusive). Use two nested for loops to iterate through the array and populate each element with the corresponding 
> velocity for that particular starting velocity and time.
>
> > ## Solution
> >
> > ~~~
> > import numpy
> >
> > g = 9.81 # acceleration due to gravity in m/s^2
> > v_0_array = numpy.array([-10,0,10,20]) # starting velocities in m/s
> > times = numpy.linspace(0,100,5000) # times between 0 and 10s
> > velocity_array = numpy.zeros((4,5000)) # empty array to hold calculated values
> >
> > for i, v_0 in enumerate(v_0_array):
> >  for j,time in enumerate(times): 
> >       velocity_array[i,j] = v_0 + g*time
> > ~~~
> > {: .python}
> {: .solution}
>
> For loops can be computationally inefficient. To speed up this calculation we can make use of vectorized 
> operations in Numpy. Use [Numpy operations](https://numpy.org/doc/stable/user/quickstart.html#basic-operations) and [broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html) to re-write this code so it executes faster. To measure the
> execution 
> time you can use the 
> [`%%timeit` Jupyter magic command](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-timeit).
>
> > ## Solution
> >
> > ~~~
> > import numpy
> >
> > g = 9.81 # acceleration due to gravity in m/s^2
> > v_0 = numpy.array([[-10,0,10,20]]).transpose() # starting velocities in m/s
> > times = numpy.array([numpy.linspace(0,100,5000)]) # times between 0 and 10s
> > velocity_array = v_0 + g*times
> > ~~~
> > {: .python}
> {: .solution}
> 
> Note that the `v_0` array in the example code above is transposed to allow 
> [Numpy broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html) between
> two differently shaped arrays
{: .challenge}

> ## Python round vs Numpy round.
>
> Why will the following code produce an error?
> 
> ~~~
> import numpy
> import math
> 
> x = numpy.array([2,6,7])
> print(math.sqrt(x))
> ~~~
> {: .python}
>
> > ## Solution
> >
> > This code will produce an error because `math.sqrt` can only take the square root of python scalars 
> > (integers or floats) - it can't take a Numpy array as an argument. 
> > To find the square root of elements in an array we must use `Numpy.sqrt`. 
> > Numpy takes the square root 
> > [element-wise](https://scipy-lectures.org/intro/numpy /operations.html#elementwise-operations).
> > 
> {: .solution}
{: .challenge}
