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
%%writefile transmittance_plots.py

import numpy
import matplotlib.pyplot as plt

numpy.loadtxt("./data/transmittance_cleaned.csv")
wavelengths = data[:,0]
ITO_transmittance = data[:,1]
CdS_transmittance = data[:,2]
Si_transmittance = data[:,3]
GaAs_transmittance = data[:,4]

fig = plt.figure(figsize=(10.0, 10.0))

axes1 = fig.add_subplot(2, 2, 1)
axes2 = fig.add_subplot(2, 2, 2)
axes3 = fig.add_subplot(2, 2, 3)
axes4 = fig.add_subplot(2, 2, 4)

axes1.plot(wavelengths,ITO_transmittance)
axes1.set_ylabel("Transmittance (%)")
axes1.set_title("ITO")

axes2.plot(wavelengths,CdS_transmittance)
axes2.set_title("CdS")
axes2.sharey(axes1)

axes3 .plot(wavelengths,Si_transmittance)
axes3.set_xlabel("wavelength (nm) ")
axes3.set_ylabel("Transmittance (%)")
axes3.set_title("Si")

axes4.plot(wavelengths,GaAs_transmittance)
axes4.set_xlabel("wavelength (nm) ")
axes4.set_title("GaAs")
axes4.sharey(axes3)

fig.tight_layout()

plt.savefig('./group_transmittance.png')

plt.show()
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
>
> This uses the [nbconvert tool](https://github.com/jupyter/nbconvert).
> 
{: .callout}

We can now run the script in a terminal to generate the plot. Note that the transmittance data file will need to be in a  sub-folder called `data`.

~~~
python3 transmittance_plots.py
~~~
{: .language-bash}

The data file that is read in by the script are currently hard coded - they cannot be changed without changing the code itself. Instead, we can import the `sys` library which allows us to provide command line arguments specifying the filenames for our data. The first command line argument is accessed with the variable `sys.argv[1]` , the second command line argument is accessed with the `sys.argv[2]` argument and so on. We can adapt the `transmittance_plots.py` script as follows:

~~~
import sys
import numpy
import matplotlib.pyplot as plt

numpy.loadtxt(sys.argv[1])
wavelengths = data[:,0]
ITO_transmittance = data[:,1]
CdS_transmittance = data[:,2]
Si_transmittance = data[:,3]
GaAs_transmittance = data[:,4]

fig = plt.figure(figsize=(10.0, 10.0))

axes1 = fig.add_subplot(2, 2, 1)
axes2 = fig.add_subplot(2, 2, 2)
axes3 = fig.add_subplot(2, 2, 3)
axes4 = fig.add_subplot(2, 2, 4)

axes1.plot(wavelengths,ITO_transmittance)
axes1.set_ylabel("Transmittance (%)")
axes1.set_title("ITO")

axes2.plot(wavelengths,CdS_transmittance)
axes2.set_title("CdS")
axes2.sharey(axes1)

axes3 .plot(wavelengths,Si_transmittance)
axes3.set_xlabel("wavelength (nm) ")
axes3.set_ylabel("Transmittance (%)")
axes3.set_title("Si")

axes4.plot(wavelengths,GaAs_transmittance)
axes4.set_xlabel("wavelength (nm) ")
axes4.set_title("GaAs")
axes4.sharey(axes3)

fig.tight_layout()

plt.savefig(sys.argv[2])

plt.show()
~~~
{: .language-python}

In this example `sys.argv[1]` should correspond to the cleaned data file, and `sys.argv[2]` should correspond to the name you would like to give the resulting plot. 

~~~
python3 absorption_plots.py ./data/transmittance_cleaned.csv ./transmittance_plot_scr.png
~~~
{: .language-bash}
