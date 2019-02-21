---
title: Running your Code as a Python Script
teaching: 10
exercises: 10
questions:
- "How can I export my Jupyter notebook as a Python script?"
- "How do I run a Python script?"
- "How can I pass an argument to my script?"
objectives:
- "Export a Jupyter notebook to a Python script"
- "Run a Python script using the terminal"
- "Write a Python script which takes a command line argument"
keypoints:
- Copy/paste or use the `%%writefile myfile.py` notebook magic to export a single cell
- Use `jupyter nbconvert --to script my_notebook.ipynb` to export a complete notebook 
- Use `python3 script_name.py` to run a script from the terminal
- Import the `sys` module and use `sys.argv` to take a command line argument
---

In the previous lesson we wrote a script for plotting the average, maximum and mean of the absorption.
If you wanted to share this script with other researchers you may want to export this code cell as a plain text file. You can then send the file in an email or - even better - publish it on a website like [Github](https://github.com) or [Gitlab](https://gitlab.com). Plain text can be easier to version control than Jupyter Notebooks, although there are a growing number of tools (example [nbdime](https://github.com/jupyter/nbdime)) which are designed to make the version control of Jupyter Notebooks easier.

To convert the code in your Jupyter Notebook cell into a plain text `.py` file there are two options:

- Option one:
	- copy the code cell
	- open a text editor
	- paste the code into your text editor
	- save with a `.py` extension

- Option two:
	- Use the [Jupyter Magic](https://ipython.readthedocs.io/en/stable/interactive/magics.html) command `%%writefile myfile.py` in your code block

Let's use option two.

~~~
%%writefile absorption_plots.py

import numpy
import matplotlib.pyplot

data = numpy.loadtxt(fname='UVVis-01-cleaned.csv', delimiter=',')
wavelengths = pandas.read_csv("./data/UVVis-01.csv",usecols=[0],header=None).to_numpy()

data_slice = data[:,650:800]
wavelength_slice = wavelengths[650:800]

fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('average')
axes1.plot(wavelength_slice,numpy.mean(data_slice, axis=0))

axes2.set_ylabel('max')
axes2.plot(wavelength_slice,numpy.max(data_slice, axis=0))

axes3.set_ylabel('min')
axes3.plot(wavelength_slice,numpy.min(data_slice, axis=0))

fig.tight_layout()

matplotlib.pyplot.savefig('./group_plot.png')

matplotlib.pyplot.show()
~~~
{: .language-python}

> ## Exporting a complete Notebook
>
> If you want to export all the code in a Jupyter Notebook
> you'll need to execute the following command
> from the terminal.
>
> ~~~
> jupyter nbconvert --to script my_notebook.ipynb
> ~~~
> {: .language-python}
>
> This uses the [nbconvert tool](https://github.com/jupyter/nbconvert).
> 
{: .callout}

We can now run the script in a terminal to generate the plot. Note that the cleaned and un-cleaned data files will need to be in the same folder as your python script.

~~~
python3 absorption_plots.py
~~~
{: .language-bash}

At the moment our 

~~~
import sys
import numpy
import matplotlib.pyplot

data = numpy.loadtxt(fname=sys.argv[0], delimiter=',')
wavelengths = pandas.read_csv(sys.argv[1],usecols=[0],header=None).to_numpy()

data_slice = data[:,650:800]
wavelength_slice = wavelengths[650:800]

fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('average')
axes1.plot(wavelength_slice,numpy.mean(data_slice, axis=0))

axes2.set_ylabel('max')
axes2.plot(wavelength_slice,numpy.max(data_slice, axis=0))

axes3.set_ylabel('min')
axes3.plot(wavelength_slice,numpy.min(data_slice, axis=0))

fig.tight_layout()

matplotlib.pyplot.savefig('./group_plot.png')

matplotlib.pyplot.show()
~~~
{: .language-python}

To take a command line argument