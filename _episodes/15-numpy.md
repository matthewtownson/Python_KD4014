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

In earlier tutorials we have read-in and plotted our raw transmittance spectroscopy data. 
In this tutorial we will analyse this data to calculate the band gap of each material. For our analysis we will make use of a number of functions in the Numpy library: `numpy.polyfit`, `numpy.polyval` and `numpy.roots`.
We will also use Numpy array operations to calculate the reflectance of each material.

### Digging a little deeper into transmittance spectroscopy

![Schematic for transmittance spectroscopy](../fig/trasmittance_schematic.png)

The schematic above is taken from the Lab script for course KD5081 at Northumbria University.

The optical transmittance spectrum of a semiconductor yields information on the energy band structure of the semiconductor. In particular if the frequency of the radiation $\nu$ is such that $E_g<h\nu$ where $E_g$ is the energy bandgap of the semiconductor then each photon absorbed creates an electron-hole pair and there is weak transmittance. If however $E_g>h\nu$ then the electron-hole pair cannot be generated and there is usually strong transmittance in this region. Thus by measuring the position of the transmittance edge, one can determine the energy bandgap of the material using the equation
$$ E_g = h\nu = \frac{hc}{\lambda_0} $$

It is, however, often difficult to locate the absorption edge precisely as it may be “smeared out” over a wide wavelength range. A simple criterion that suffices in this case is to take the point which is obtained by extrapolating the transmission curves. This requires a straight line fitting to the data, which will be our first analysis task.

First we will slice our ITO transmittance data and visualise it to find the linear region. For example, the following slice generates a region that looks roughly linear.

~~~
plt.plot(wavelengths[50:111],ITO_transmittance[50:111],label='ITO')
~~~
{: .language-python}

![](./fig/analysis_1.png)

We have done this manually, and "by eye", but there are ways  - beyond the scope of this course - to automate this process and reduce role of human judgement. For example, see [this answer](https://stackoverflow.com/a/13728059) on the very useful site Stack Overflow.

## Fit a polynomial function to data using the `numpy.polyfit` function

We can fit a polynomial to this data slice using the `numpy.polyfit` function. This function uses a [least-squares method](https://www.youtube.com/watch?v=P8hT5nDai6A) to perform the fitting. In this case, we know that is is a first order polynomial (straight line) - but note that least squares methods (and the polyfit function) can be used to fit higher order polynomials.

~~~
fit=numpy.polyfit(wavelengths[50:111],ITO_transmittance[50:111], 1)
print(fit)
~~~
{: .language-python}

~~~
array([   0.79366912, -275.85006769])
~~~
{: .output}
 
The `polyfit` function returns two values. From the function documentation (`numpy.polyfit?`) we can see that these are the polynomial coefficients with the highest power returned first. As this is a linear fit, the first value is the gradient of the line and the second value is the intercept on the x-axis.

We can overlay the fit on our dataset to verify that our fit is sensible. To do this we first evaluate this fit using the `numpy.polyval` function for a number of points along the x-axis.

~~~
fit_val = numpy.polyval(fit,np.linspace(350,410,1000)))
~~~
{: .language-python}

~~~
array([-6.00256795e+00, -5.94695550e+00, -5.89134305e+00, ...
~~~
{: .output}

This generates an array of y values.

We then plot the experimental data and our fit alongside each other. As there are now multiple plot lines we also include a legend.

~~~
plt.plot(wavelengths,ITO_transmittance,label='experimental data')
plt.plot(np.linspace(340,410,1000),fit_val,label='least squares fit')
plt.legend()
plt.title("ITO transmittance")
~~~
{: .language-python}

![](./fig/analysis_2.png)

This looks sensible! To calculate the band gap energy of our material we need to calculate the point at which the fit intercepts with the x-axis. As our fit is linear, this point corresponds to the one and only root of our polynomial equation. To find the root(s) of a polynomial equation we can use the `numpy.roots` function.

~~~
numpy.roots(fit)
~~~
{: .language-python}

~~~
array([347.56306101])
~~~
{: .output}

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



> ## Error bars and exponential growth
> 
> This question is partly modelled on the a [blog post](https://towardsdatascience.com/modeling-exponential-growth-49a2b6f22e1f). There is also a nice
> [3Blue1Brown video on exponential growth in the context of Covid](https://www.youtube.com/watch?v=Kas0tIxDvrg).
> 
> We have the following (hypothetical) data for the growth in Covid cases at a university over a two-week period
> ~~~
> import numpy as np
> day = np.arange(0,15)
> case_numbers = np.array([3,4,8,15,32,65,128,253,512,1025,2049,4090,8191,16387])
> ~~~
> {: .language-python}
> 
> An administrator realises that some test results may have been filed a day late or a day early. This makes the error bar on the case numbers +/- 200.
> Using the `matplotlib.pyplot.errorbar` function with the `yerr` keyword argument plot the case number data with error bars. Label your axes and title the plot.
> 
> > ## Solution
> > ~~~
> > import matplotlib.pyplot as plt
> > 
> > plt.errorbar(day,case_numbers,yerr=200)
> > plt.xlabel("Time (days)")
> > plt.ylabel("Case numbers")
> > plt.title("Covid case numbers over time")
> > ~~~
> > {: .language-python}
> {: .solution}
> 
> By taking a logarithm of the data, fit a straight line to the case number data and predict the exponential growth factor. 
> 
> > ## Solution
> > From scanning the blog post we can see that the growth factor is the base of the exponential.
> > Assuming the growth is exponential, to generate a straight-(ish) line we first need to take a logarithm of the case values data.
> > We can then fit a straight line to this to calculate the logarithm of the growth factor. 
> > ~~~
> > log_growth_factor, log_starting_case_number = np.polyfit(day,np.log(case_numbers),1)
> > growth_factor = np.exp(log_growth_factor)
> > ~~~
> > {: .language-python}
> {: .solution}
> 
> From inspecting the data, does the calculated growth factor make sense? 
> 
> > ## Solution
> > The data roughly doubles each day. The calculated growth factor is 1.94, which is reassuringly close to 2. 
> {: .solution}
{: .challenge}

> ## Encapsulation
>
> If you want to repeat the same analysis step(s) a number of times you may want to write a function.
> Fill in the blanks to create a function that takes a single filename, containing comma separated values, as an argument,
> loads the data in the file named by the argument,
> and returns the minimum value in that data.
>
> ~~~
> import numpy
>
> def min_in_data(....):
>     data = ....
>     return ....
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


