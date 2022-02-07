---
title: "Visualizing data with Matplotlib"
teaching: 15
exercises: 15
questions:
- "How can I plot my data?"
- "How can I save my plot for publishing?"
objectives:
- "Plot simple graphs from data."
keypoints:
- "Use the `pyplot` library from `matplotlib` for creating simple visualizations."
- "Many styles of plot are available: see the [Python Graph Gallery](https://python-graph-gallery.com/matplotlib/) for more options."
---
## Visualizing data
The mathematician Richard Hamming once said, "The purpose of computing is insight, not numbers," and
the best way to develop insight is often to visualize data.  Visualization deserves an entire
lecture of its own, but we can explore a few features of Python's `matplotlib` library here.  While
there is no official plotting library, `matplotlib` is the _de facto_ standard.  Let's import it - 

~~~
import matplotlib.pyplot
~~~
{: .language-python}

Everytime we use a function from this library - say the `plot` function we need to pre-pend it with the library name `matplotlib.pyplot`. Typing `matplotlib.pyplot.plot` many times is quite repetative and can lead easily to typo-mistakes. 
Instead we can import the library with a shortened nickname:

~~~
import matplotlib.pyplot as plt
~~~
{: .language-python}

Now each time we want to use the `plot` function we can call it using `plt.plot` instead.

> ## Some IPython Magic
>
> If you're using an IPython / Jupyter notebook,
> you'll need to execute the following command
> in order for your matplotlib images to appear
> in the notebook when `show()` is called:
>
> ~~~
> %matplotlib inline
> ~~~
> {: .language-python}
>
> The `%` indicates an IPython magic function -
> a function that is only valid within the notebook environment.
> Note that you only have to execute this function once per notebook.
{: .callout}

Let's read-in the cleaned UV-Vis data and assign the wavelengths and absorption data to variables

~~~
data = numpy.loadtxt(fname='./data/UVVis-01-cleaned.csv')
wavelengths = data[0,:]
absorption_data = data[1,:]
~~~

Let's take a look at the average absorption data across all wavelengths:

~~~
ave_absorption = numpy.mean(absorption_data, axis=0)
ave_plot = plt.plot(ave_absorption)
plt.show()
~~~
{: .language-python}

![Average Absorption over Wavelength](../fig/01-numpy_01.png)

Here, we have put the average per wavelength across all samples in the variable `ave_absorption`, then
asked `matplotlib.pyplot` (which we've shortened to `plt`) to create and display a line graph of those values.

At the moment the x-axis has no physical significance; it is an integer range from 0 to 1200. 
Instead we can ask `matplotlib.pyplot` to plot a line graph of absorption vs wavelength with labelled axes.

~~~
ave_plot = plt.plot(wavelengths,ave_absorption)
plt.xlabel("wavelength (nm) ")
plt.ylabel("ave. absorption (Arb. units)")
plt.show()
~~~

> ## Arbitary units
>
> When labelling axes it is important to give the units of measure.
> Sometimes we are not so interested in the absolute value of the data,
> but in the relative values - for example, at which wavelength is absorption strongest?
> In this case we can use "arbitrary units" to show a ratio of a quantity in relation to a 
> pre-defined reference measurement.
{: .callout}

![Average Absorption with Labelled Axes](../fig/01-numpy_01b.png)

We are interested in analysing a sub-set of the data, from index 650 to index 800. 
So let's take a slice of the wavelength and data arrays.

~~~
data_slice = absorption_data[:,650:800]
wavelength_slice = wavelengths[650:800]
~~~
{: .language-python} 

We can now plot this sub-set of the absorption data.

~~~
max_plot = plt.plot(wavelength_slice,numpy.mean(data_slice, axis=0))
plt.xlabel("wavelength")
plt.ylabel("ave. absorption")
plt.show()
~~~
{: .language-python}

![Average Value Along Slice of the First Axis](../fig/01-numpy_01c.png)

Let's have a look at two other statistics:

~~~
max_plot = plt.plot(wavelength_slice,numpy.max(data_slice, axis=0))
plt.xlabel("wavelength")
plt.ylabel("max absorption")
plt.show()
~~~
{: .language-python}

![Maximum Value Along Slice of The First Axis](../fig/01-numpy_02.png)

~~~
min_plot = plt.plot(wavelength_slice,numpy.min(data_slice, axis=0))
plt.xlabel("wavelength")
plt.ylabel("min absorption")
plt.show()
~~~
{: .language-python}

![Minimum Value Along Slice of The First Axis](../fig/01-numpy_03.png)

### Grouping plots
You can group similar plots in a single figure using subplots.
This script below uses a number of new commands. The function `matplotlib.pyplot.figure()`
creates a space into which we will place all of our plots. The parameter `figsize`
tells Python how big to make this space. Each subplot is placed into the figure using
its `add_subplot` [method]({{ page.root }}/reference/#method). The `add_subplot` method takes 3
parameters. The first denotes how many total rows of subplots there are, the second parameter
refers to the total number of subplot columns, and the final parameter denotes which subplot
your variable is referencing (left-to-right, top-to-bottom). Each subplot is stored in a
different variable (`axes1`, `axes2`, `axes3`). Once a subplot is created, the axes can
be titled using the `set_xlabel()` command (or `set_ylabel()`).
Here are our three plots side by side:

~~~
import numpy
import matplotlib.pyplot as plt

data = numpy.loadtxt(fname='./data/UVVis-01-cleaned.csv')
wavelengths = data[0,:]
absorption_data = data[1,:]

data_slice = absorption_data[:,650:800]
wavelength_slice = wavelengths[650:800]

fig = plt.figure(figsize=(10.0, 3.0))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('average')
axes1.set_xlabel('wavelength')
axes1.plot(wavelength_slice,numpy.mean(data_slice, axis=0))

axes2.set_ylabel('max')
axes2.set_xlabel('wavelength')
axes2.plot(wavelength_slice,numpy.max(data_slice, axis=0))

axes3.set_ylabel('min')
axes3.set_xlabel('wavelength')
axes3.plot(wavelength_slice,numpy.min(data_slice, axis=0))

fig.tight_layout()

plt.savefig('./group_plot.png')

plt.show()
~~~
{: .language-python}

![The Previous Plots as Subplots](../fig/01-numpy_04.png)

The [call]({{ page.root }}/reference/#function-call) to `loadtxt` reads our data,
and the rest of the program tells the plotting library
how large we want the figure to be,
that we're creating three subplots,
what to draw for each one,
and that we want a tight layout
(If we leave out that call to `fig.tight_layout()`,
the graphs will actually be squeezed together more closely).
The [call]({{ page.root }}/reference/#function-call) to `savefig` saves our figure to the file `group_plot.png`.

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

> ## Line fitting
>
> In the previous chapter we calculated the velocity of a ball and stored it as a Numpy array
> ~~~
> import numpy
>
> g = 9.81
> velocity_array = numpy.zeros(50)
> v_0 = 0
> 
> for index,time in enumerate(numpy.linspace(0,10,50)):
>        velocity_array[index] = v_0 + g*time
> ~~~
> {: .language-python}
>
> We can fit a polynomial to this data using the `numpy.polyfit` function. In this case, we know that is is a first order polynomial (straight line)
> ~~~
> fit = numpy.polyfit(numpy.linspace(0,10,50), velocity_list, 1)
> print(fit)
> ~~~
> {: .language-python}
> 
> What is the gradient and intercept of the straight line fit? Does this make physical sense? 
> Make a scatter plot of velocity vs time. Label the x-axis and y-axis (with units) and give the plot a title.
>
> > ## Solution
> > The gradient is equal to the acceleration of the ball which is given by the acceleration due to gravity. The intercept is the starting velocity of the ball, which in this example is zero.
> > ~~~
> > import matplotlib.pyplot as plt
> >
> > plt.scatter(numpy.linspace(0,10,50),velocity_list)
> > plt.xlabel("Time (s)")
> > plt.ylabel("Velocity (m/s)")
> > plt.title("Velocity of an object accelerated by gravity")
> > ~~~
> > {: .language-python}
> {: .solution}
>
> Use the polyval function to generate and plot velocities over the timeframe 30 to 100 seconds.
> 
> > ## Solution
> > ~~~
> > import matplotlib.pyplot as plt
> >
> > time_range = numpy.linspace(30,100,70)
> > plt.plot(time_range,np.polyval(fit,time_range))
> > plt.xlabel("Time (s)")
> > plt.ylabel("Velocity (m/s)")
> > plt.title("Velocity of an object accelerated by gravity")
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

> ## Error bars and exponential growth
> 
> This question is partly modelled on the a [blog post](https://towardsdatascience.com/modeling-exponential-growth-49a2b6f22e1f). There is also a nice
> [3Blue1Brown video on exponential growth in the context of Covid](https://www.youtube.com/watch?v=Kas0tIxDvrg).
> 
> We have the following (hypothetical) data for the growth in Covid cases at a university over a two-week period
> ~~~
> import numpy as np
> day = np.arange(0,15)
> case_numbers = np.array([2,3,4,8,15,32,65,128,253,512,1025,2049,4090,8191,16387])
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

> ## Plot Scaling
>
> Why do all of our plots stop just short of the upper end of our graph?
>
> > ## Solution
> > Because matplotlib normally sets x and y axes limits to the min and max of our data
> > (depending on data range)
> {: .solution}
>
> If we want to change this, we can use the `set_ylim(min, max)` method of each 'axes',
> for example:
>
> ~~~
> axes3.set_ylim(0,6)
> ~~~
> {: .language-python}
>
> Update your plotting code to automatically set a more appropriate scale.
> (Hint: you can make use of the `max` and `min` methods to help.)
>
> > ## Solution
> > ~~~
> > # One method
> > axes3.set_ylabel('min')
> > axes3.plot(numpy.min(data, axis=0))
> > axes3.set_ylim(0,6)
> > ~~~
> > {: .language-python}
> {: .solution}
>
> > ## Solution
> > ~~~
> > # A more automated approach
> > min_data = numpy.min(data, axis=0)
> > axes3.set_ylabel('min')
> > axes3.plot(min_data)
> > axes3.set_ylim(numpy.min(min_data), numpy.max(min_data) * 1.1)
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}


> ## Make Your Own Plot
>
> Create a plot showing the standard deviation (`numpy.std`)
> of the absorption data for each day across all patients.
>
> > ## Solution
> > ~~~
> > import numpy
> > import matplotlib.pyplot as plt
> >
> > std_plot = plt.plot(numpy.std(data, axis=0))
> > plt.show()
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

> ## Moving Plots Around
>
> Modify the program to display the three plots on top of one another
> instead of side by side.
>
> > ## Solution
> > ~~~
> > import numpy
> > import matplotlib.pyplot as plt
> >
> > data = numpy.loadtxt(fname='./data/UVVis-01-cleaned.csv')
> > wavelengths = data[0,:]
> > absorption_data = data[1,:]
> >
> > # change figsize (swap width and height)
> > fig = plt.figure(figsize=(3.0, 10.0))
> >
> > # change add_subplot (swap first two parameters)
> > axes1 = fig.add_subplot(3, 1, 1)
> > axes2 = fig.add_subplot(3, 1, 2)
> > axes3 = fig.add_subplot(3, 1, 3)
> >
> > axes1.set_ylabel('average')
> > axes1.plot(numpy.mean(absorption_data, axis=0))
> >
> > axes2.set_ylabel('max')
> > axes2.plot(numpy.max(absorption_data, axis=0))
> >
> > axes3.set_ylabel('min')
> > axes3.plot(numpy.min(absorption_data, axis=0))
> >
> > fig.tight_layout()
> >
> > plt.show()
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}
