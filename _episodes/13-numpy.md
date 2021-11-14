---
title: "Analysing data with NumPy"
teaching: 15
exercises: 15
questions:
- "How can I import and analyse tabular data files in Python?"
objectives:
- "Read tabular data from a file into a program using `numpy`."
- "Select individual values and subsections from data."
- "Perform operations on arrays of data."
keypoints:
- "Use the `numpy` library to work with arrays in Python."
- "The expression `array.shape` gives the shape of an array."
- "Use `array[x, y]` to select a single element from a 2D array."
- "Array indices start at 0, not 1."
- "All the indexing and slicing that we've used on lists and strings also works on arrays."
- "Use `low:high` to specify a `slice` that includes indices from `low` to `high-1`."
- "Use `numpy.mean(array)`, `numpy.max(array)`, and `numpy.min(array)` to calculate simple statistics."
- "Use `numpy.mean(array, axis=0)` or `numpy.mean(array, axis=1)` to calculate statistics across the specified axis."
---
## Loading data into Python
In order to load our inflammation data, we need to access
([import]({{ page.root }}/reference/#import) in Python terminology) a library called
[NumPy](http://docs.scipy.org/doc/numpy/ "NumPy Documentation").  In general you should use this
library if you want to do fancy things with numbers, especially if you have matrices or arrays.  We
can import NumPy using:

First lets import the numpy library, and ask the library to read our cleaned data
file for us:

~~~
import numpy
numpy.loadtxt(fname='./data/UVVis-01-cleaned.csv')
~~~
{: .language-python}

~~~
array([[ 1.50000000e+03,  1.49900000e+03,  1.49800000e+03, ...,
         2.02000000e+02,  2.01000000e+02,  2.00000000e+02],
       [ 4.47125000e-04,  6.55591000e-04,  8.64056000e-04, ...,
         1.00000000e+01,  1.29667747e+00,  1.66669679e+00],
       [-3.66223800e-03, -3.49741500e-03, -3.34321500e-03, ...,
        -1.22419536e-01, -7.07442700e-03, -1.82473719e-01],
       ...,
       [ 1.20771340e-02,  1.22769590e-02,  1.24000520e-02, ...,
         3.11538220e-02,  1.53292596e-01, -2.67419547e-01],
       [ 3.98183100e-03,  4.22229500e-03,  4.32843200e-03, ...,
        -1.33138746e-01, -6.67433520e-02,  1.55003861e-01],
       [ 4.21040200e-03,  4.36906300e-03,  4.38802100e-03, ...,
         8.95578190e-02,  8.41182170e-02,  1.43565789e-01]])
~~~
{: .output}

The expression `numpy.loadtxt(...)` is a [function call]({{ page.root }}/reference/#function-call)
that asks Python to run the [function]({{ page.root }}/reference/#function) `loadtxt` which
belongs to the `numpy` library. 

Let's re-run
`numpy.loadtxt` and save the returned data:

~~~
data = numpy.loadtxt(fname='./data/UVVis-01-cleaned.csv')
~~~
{: .language-python}

Remember, this statement doesn't produce any output because we've assigned the output to the variable `data`.
If we want to check that the data have been loaded,
we can print the variable's value:

~~~
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

Remember that the rows are the individual samples, and the columns
are the absorption at each wavelength.

> ## Data Type
>
> A Numpy array contains one or more elements
> of the same type. The `type` function will only tell you that
> a variable is a NumPy array but won't tell you the type of
> thing inside the array.
> We can find out the type
> of the data contained in the NumPy array.
>
> ~~~
> print(data.dtype)
> ~~~
> {: .language-python}
>
> ~~~
> 'float64'
> ~~~
> {: .output}
>
> This tells us that the NumPy array's elements are
> [floating-point numbers]({{ page.root }}/reference/#floating-point number).
{: .callout}

With the following command, we can see the array's [shape]({{ page.root }}/reference/#shape):

~~~
print(data.shape)
~~~
{: .language-python}

~~~
(11, 1301)
~~~
{: .output}

The output tells us that the `data` array variable contains 11 rows and 1301 columns. When we
created the variable `data` to store our absorption data, we didn't just create the array; we also
created information about the array, called [members]({{ page.root }}/reference/#member) or
attributes. This extra information describes `data` in the same way an adjective describes a noun.
`data.shape` is an attribute of `data` which describes the dimensions of `data`. We use the same
dotted notation for the attributes of variables that we use for the functions in libraries because
they have the same part-and-whole relationship.

## Slicing and indexing data

The first row of the data contains the wavelengths. We can select this section of the data array  and assign it to a variable `wavelengths` using the following command:

~~~
wavelengths = data[0,0:1302]
~~~
{: .language-python}

~~~
print(wavelengths)
~~~
{: .language-python}

~~~
[1500. 1499. 1498. ...  202.  201.  200.]
~~~
{: .output}

We have to specify two indices/slices (separated by a comma) as this is a two dimensional array (with rows and columns). The first index 0 selects the first row only. The [slice]({{ page.root }}/reference/#slice) `0:1302` means "Start at index 0 and go up to but not including index 1302". As there are 1301 elements in each row, this slice is equivalent to selecting every element in that row.

However we do not need to select and upper and lower bound for this slice. If we don't include the lower
bound, Python uses 0 by default; if we don't include the upper, the slice runs to the end of the
axis, and if we don't include either (i.e., if we just use ':' on its own), the slice includes
everything. 

This makes `data[0,0:1302]` exactly equal to `data[0,:]` for this example.

All other rows contains the absorption data. We can select this section of the data array and assign it to a variable `absorption_data` using the following similar command:

~~~
absorption_data = data[1:,:]
~~~
{: .language-python}

~~~
print(absorption_data)
~~~
{: .language-python}

~~~
[[ 4.47125000e-04  6.55591000e-04  8.64056000e-04 ...  1.00000000e+01
   1.29667747e+00  1.66669679e+00]
 [-3.66223800e-03 -3.49741500e-03 -3.34321500e-03 ... -1.22419536e-01
  -7.07442700e-03 -1.82473719e-01]
 [ 2.23267300e-03  2.29731000e-03  2.47505900e-03 ...  3.31975669e-01
   3.77199233e-01  3.53418890e-02]
 ...
 [ 1.20771340e-02  1.22769590e-02  1.24000520e-02 ...  3.11538220e-02
   1.53292596e-01 -2.67419547e-01]
 [ 3.98183100e-03  4.22229500e-03  4.32843200e-03 ... -1.33138746e-01
  -6.67433520e-02  1.55003861e-01]
 [ 4.21040200e-03  4.36906300e-03  4.38802100e-03 ...  8.95578190e-02
   8.41182170e-02  1.43565789e-01]]

~~~
{: .output}

The first slice `1:` means "start at index (row) 1 and go to the end of the array" . The second [slice]({{ page.root }}/reference/#slice) `:` means, "start at index (column) 0 and go to the end of the array" or "select all elements in the row".

If we want to get a single number from the array, we must provide an
[index]({{ page.root }}/reference/#index) in square brackets after the variable name, just as we
do in math when referring to an element of a matrix.  Our absorption data has two dimensions, so
we will need to use two indices to refer to one specific value:

~~~
print('first value in data:', absorption_data[0, 0])
~~~
{: .language-python}

~~~
first value in data: 0.000447125
~~~
{: .output}

~~~
print('middle value in data:', absorption_data[5, 600])
~~~
{: .language-python}

~~~
middle value in data: 0.05236074
~~~
{: .output}

## Indexing from zero

The expression `data[5, 600]` accesses the element at row 5, column 600. While this expression may
not surprise you,
 `data[0, 0]` might.
Programming languages like Fortran, MATLAB and R start counting at 1
because that's what human beings have done for thousands of years.
Languages in the C family (including C++, Java, Perl, and Python) count from 0
because it represents an offset from the first value in the array (the second
value is offset by one index from the first value). This is closer to the way
that computers represent arrays (if you are interested in the historical
reasons behind counting indices from zero, you can read
[Mike Hoye's blog post](http://exple.tive.org/blarg/2013/10/22/citation-needed/)).
As a result,
if we have an M×N array in Python,
its indices go from 0 to M-1 on the first axis
and 0 to N-1 on the second.
It takes a bit of getting used to,
but one way to remember the rule is that
the index is how many steps we have to take from the start to get the item we want.

![Zero Index](../fig/python-zero-index.png)

> ## In the Corner
>
> What may also surprise you is that when Python displays an array,
> it shows the element with index `[0, 0]` in the upper left corner
> rather than the lower left.
> This is consistent with the way mathematicians draw matrices
> but different from the Cartesian coordinates.
> The indices are (row, column) instead of (column, row) for the same reason,
> which can be confusing when plotting data.
{: .callout}

## Numpy array operations

Arrays also know how to perform common mathematical operations on their values.  The simplest
operations with data are arithmetic: addition, subtraction, multiplication, and division.  When you
do such operations on arrays, the operation is done element-by-element.  Thus:

~~~
doubledata = absorption_data * 2.0
~~~
{: .language-python}

will create a new array `doubledata`
each element of which is twice the value of the corresponding element in `data`:

~~~
print('original:')
print(data[:3, 36:])
print('doubledata:')
print(doubledata[:3, 36:])
~~~
{: .language-python}

~~~
original:
[[ 7.95187800e-03  8.16034400e-03  8.36880900e-03 ...  1.00000000e+01
   1.29667747e+00  1.66669679e+00]
 [-2.69293800e-03 -2.44559000e-03 -2.69407000e-03 ... -1.22419536e-01
  -7.07442700e-03 -1.82473719e-01]
 [ 3.43972300e-03  3.70568000e-03  3.41978900e-03 ...  3.31975669e-01
   3.77199233e-01  3.53418890e-02]]
doubledata:
[[ 1.59037560e-02  1.63206880e-02  1.67376180e-02 ...  2.00000000e+01
   2.59335494e+00  3.33339357e+00]
 [-5.38587600e-03 -4.89118000e-03 -5.38814000e-03 ... -2.44839072e-01
  -1.41488540e-02 -3.64947438e-01]
 [ 6.87944600e-03  7.41136000e-03  6.83957800e-03 ...  6.63951338e-01
   7.54398466e-01  7.06837780e-02]]
~~~
{: .output}

If, instead of taking an array and doing arithmetic with a single value (as above), you did the
arithmetic operation with another array of the same shape, the operation will be done on
corresponding elements of the two arrays.  Thus:

~~~
tripledata = doubledata + absorption_data
~~~
{: .language-python}

will give you an array where `tripledata[0,0]` will equal `doubledata[0,0]` plus `absorption_data[0,0]`,
and so on for all other elements of the arrays.

~~~
print('tripledata:')
print(tripledata[:3, 36:])
~~~
{: .language-python}

~~~
tripledata:
[[ 2.38556340e-02  2.44810320e-02  2.51064270e-02 ...  3.00000000e+01
   3.89003241e+00  5.00009036e+00]
 [-8.07881400e-03 -7.33677000e-03 -8.08221000e-03 ... -3.67258608e-01
  -2.12232810e-02 -5.47421157e-01]
 [ 1.03191690e-02  1.11170400e-02  1.02593670e-02 ...  9.95927007e-01
   1.13159770e+00  1.06025667e-01]]
~~~
{: .output}

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

Often, we want to do more than add, subtract, multiply, and divide array elements.  NumPy knows how
to do more complex operations, too.  If we want to find the average absorption for all samples across all wavelengths, for example, we can ask NumPy to compute `data`'s mean value:

~~~
print(numpy.mean(absorption_data))
~~~
{: .language-python}

~~~
0.0814548568076864
~~~
{: .output}

`mean` is a [function]({{ page.root }}/reference/#function) that takes
an array as an [argument]({{ page.root }}/reference/#argument).

> ## Not All Functions Have Input
>
> Generally, a function uses inputs to produce outputs.
> However, some functions produce outputs without
> needing any input. For example, checking the current time
> doesn't require any input.
>
> ~~~
> import time
> print(time.ctime())
> ~~~
> {: .language-python}
>
> ~~~
> 'Sat Mar 26 13:07:33 2016'
> ~~~
> {: .output}
>
> For functions that don't take in any arguments,
> we still need parentheses (`()`)
> to tell Python to go and do something for us.
{: .callout}

NumPy has lots of useful functions that take an array as input.
Let's use three of those functions to get some descriptive values about the dataset.
We'll also use multiple assignment,
a convenient Python feature that will enable us to do this all in one line.

~~~
maxval, minval, stdval = numpy.max(absorption_data), numpy.min(absorption_data), numpy.std(absorption_data)

print('maximum absorption:', maxval)
print('minimum absorption:', minval)
print('standard deviation:', stdval)
~~~
{: .language-python}

Here we've assigned the return value from `numpy.max(absorption_data)` to the variable `maxval`, the value
from `numpy.min(absorption_data)` to `minval`, and so on.

~~~
maximum absorption: 10.0
minimum absorption: -1.036568046
standard deviation: 0.24849228257073133
~~~
{: .output}

> ## Mystery Functions in IPython
>
> How did we know what functions NumPy has and how to use them?
> If you are working in the IPython/Jupyter Notebook, there is an easy way to find out.
> If you type the name of something followed by a dot, then you can use tab completion
> (e.g. type `numpy.` and then press tab)
> to see a list of all functions and attributes that you can use. After selecting one, you
> can also add a question mark (e.g. `numpy.cumprod?`), and IPython will return an
> explanation of the method! This is the same as doing `help(numpy.cumprod)`.
{: .callout}

When analyzing data, though,
we often want to look at variations in statistical values,
such as the maximum absorption per sample
or the average absorption per wavelength.
One way to do this is to create a new temporary array of the data we want,
then ask it to do the calculation:

~~~
sample_0 = absorption_data[0, :] # 0 on the first axis (rows), everything on the second (columns)
print('maximum absorption for sample 0:', sample_0.max())
~~~
{: .language-python}

~~~
maximum absorption for sample 0: 10.0
~~~
{: .output}

Everything in a line of code following the '#' symbol is a
[comment]({{ page.root }}/reference/#comment) that is ignored by Python.
Comments allow programmers to leave explanatory notes for other
programmers or their future selves.

We don't actually need to store the row in a variable of its own.
Instead, we can combine the selection and the function call:

~~~
print('maximum absorption for sample 2:', numpy.max(absorption_data[2, :]))
~~~
{: .language-python}

~~~
maximum absorption for sample 2: 0.37719923299999997
~~~
{: .output}

What if we need the maximum absorption for each patient over all wavelengths (as in the
next diagram on the left) or the average for each wavelength (as in the
diagram on the right)? As the diagram below shows, we want to perform the
operation across an axis:

![Operations Across Axes](../fig/python-operations-across-axes.png)

To support this functionality,
most array functions allow us to specify the axis we want to work on.
If we ask for the average across axis 0 (rows in our 2D example),
we get:

~~~
print(numpy.mean(absorption_data, axis=0))
~~~
{: .language-python}

~~~
[0.00556981 0.00575402 0.00588247 ... 1.07087656 0.34124763 0.27600167]
~~~
{: .output}

As a quick check,
we can ask this array what its shape is:

~~~
print(numpy.mean(absorption_data, axis=0).shape)
~~~
{: .language-python}

~~~
(1301,)
~~~
{: .output}

The expression `(1301,)` tells us we have an N×1 vector,
so this is the average absorption per day for all samples.
If we average across axis 1 (columns in our 2D example), we get:

~~~
print(numpy.mean(absorption_data, axis=1))
~~~
{: .language-python}

~~~
[0.13104075 0.02947129 0.02323768 0.08578812 0.07745822 0.10012283
 0.10339795 0.09871813 0.08216419 0.08314941]
~~~
{: .output}

which is the average absorption per sample across all wavelengths.


> ## Creating Numpy arrays
>
> In the examples above we imported data from a file as a Numpy array. However there are other ways to create a Numpy array.
> For example, the following code creates an array filled with zeros and then populates it with the velocity of a ball at a sequence of evenly spaced times between 0 and 10 seconds.
> 
> ~~~
> import numpy
>
> g = 6.67408e-11 # gravitational constant
> velocity_list = numpy.zeros(50)
> v_0 = 0 # starting velocity
> 
> for index,time in enumerate(numpy.linspace(0,10,50)):
>        velocity_list[index] = v_0 + g*time
> ~~~
> {: .python}
>
> What does `numpy.linspace` generate? What is the `enumerate` function?
> Using the numpy `round` function, round all of the velocity values to two decimal places
>
> > ## Solution
> >
> > ~~~
> > numpy.round(velocity_list, decimals=2) 
> > ~~~
> {: .python}
> {: .solution}
{: .challenge}

> ## Pandas vs Numpy
>
> Another common Python library for handling data is the `Pandas` python package. 
> The core object in `Pandas` is called a `dataframe`. 
> A dataframe is two-dimensional and is designed to hold tabular data.
> In contrast to Numpy n-dimensional arrays, the columns of a dataframe can hold different
> types of data. For example, one column can hold strings, and another column can hold integers.
> In which contexts might Pandas be a more useful library than Numpy (and vice-verca)?
> > ## Solution
> >
> > The NumPy module works well with numerical data whilst Pandas is more suited to tabular data of different types
> > (including strings). 
> > NumPy provides a multi-dimensional array (a Pandas dataframe has a maximum of two dimensions).
> > If memory is a limiting factor, NumPy typically consumes less memory than Pandas.
> {: .solution}
{: .challenge}


> ## Encapsulation
>
> Fill in the blanks to create a function that takes a single filename, containing comma separated values, as an argument,
> loads the data in the file named by the argument,
> and returns the minimum value in that data.
>
> ~~~
> import numpy
>
> def min_in_data(____):
>     data = ____
>     return ____
> ~~~
> {: .python}
> > ## Solution
> >
> > ~~~
> > import numpy
> > 
> > def min_in_data(filename):
> >     data = numpy.loadtxt(fname=filename, delimiter=',')
> >     return data.min()
> > ~~~
> {: .python}
> {: .solution}
{: .challenge}

> ## Stacking Arrays
>
> Arrays can be concatenated and stacked on top of one another,
> using NumPy's `vstack` and `hstack` functions for vertical and horizontal stacking, respectively.
>
> ~~~
> import numpy
>
> A = numpy.array([[1,2,3], [4,5,6], [7, 8, 9]])
> print('A = ')
> print(A)
>
> B = numpy.hstack([A, A])
> print('B = ')
> print(B)
>
> C = numpy.vstack([A, A])
> print('C = ')
> print(C)
> ~~~
> {: .language-python}
>
> ~~~
> A =
> [[1 2 3]
>  [4 5 6]
>  [7 8 9]]
> B =
> [[1 2 3 1 2 3]
>  [4 5 6 4 5 6]
>  [7 8 9 7 8 9]]
> C =
> [[1 2 3]
>  [4 5 6]
>  [7 8 9]
>  [1 2 3]
>  [4 5 6]
>  [7 8 9]]
> ~~~
> {: .output}
>
> Write some additional code that slices the first and last columns of `A`,
> and stacks them into a 3x2 array.
> Make sure to `print` the results to verify your solution.
>
> > ## Solution
> >
> > A 'gotcha' with array indexing is that singleton dimensions
> > are dropped by default. That means `A[:, 0]` is a one dimensional
> > array, which won't stack as desired. To preserve singleton dimensions,
> > the index itself can be a slice or array. For example, `A[:, :1]` returns
> > a two dimensional array with one singleton dimension (i.e. a column
> > vector).
> >
> > ~~~
> > D = numpy.hstack((A[:, :1], A[:, -1:]))
> > print('D = ')
> > print(D)
> > ~~~
> > {: .language-python}
> >
> > ~~~
> > D =
> > [[1 3]
> >  [4 6]
> >  [7 9]]
> > ~~~
> > {: .output}
> {: .solution}
>
> > ## Solution
> >
> > An alternative way to achieve the same result is to use Numpy's
> > delete function to remove the second column of A.
> >
> > ~~~
> > D = numpy.delete(A, 1, 1)
> > print('D = ')
> > print(D)
> > ~~~
> > {: .language-python}
> >
> > ~~~
> > D =
> > [[1 3]
> >  [4 6]
> >  [7 9]]
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}
