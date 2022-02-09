---
layout: page
title: "Setup"
permalink: /setup/
root: ..
---

To participate in the Python workshop you will need access to the software described below.
In addition, you will need an up-to-date web browser.

## Installing Python Using Anaconda

[Python][python] is a popular language for scientific computing, and great for
general-purpose programming as well. Installing all of its scientific packages
individually can be a bit difficult, however, so we recommend the all-in-one
installer [Anaconda][anaconda].

Regardless of how you choose to install it, please make sure you install Python
version 3.x (e.g., 3.4 is fine). Also, please set up your python environment at 
in advance of the workshop.  

### Windows - [Video tutorial][video-windows]

1. Open [https://www.anaconda.com/download][continuum-windows]
   with your web browser.

2. Download the Python 3 installer for Windows.

3. Double-click the executable and install Python 3 using _MOST_ of the
   default settings, the only exception is to check **Add Anaconda to my PATH environment variable**.

### Mac OS X - [Video tutorial][video-mac]

1. Open [https://www.anaconda.com/download][continuum-mac]
   with your web browser.

2. Download the Python 3 installer for OS X.

3. Install Python 3 using all of the defaults for installation.

## Getting the Data

To obtain the data we will be using, download the file 
[transmittance.csv]({{page.root}}/data/transmittance.csv).

## Starting Python

We will teach Python using the [Jupyter notebook][jupyter], a 
programming environment that runs in a web browser. Jupyter requires a reasonably 
up-to-date browser, preferably a current version of Chrome, Safari, or Firefox 
(note that Internet Explorer version 9 and below are *not* supported). If you 
installed Python using Anaconda, Jupyter should already be on your system. If 
you did not use Anaconda, use the Python package manager pip
(see the [Jupyter website][jupyter-install] for details.)

## Check that jupyter notebook is installed

To start the notebook, open a terminal or git bash and type the command:

~~~
$ jupyter notebook
~~~
{: .bash}

To start the Python interpreter without the notebook, open a terminal 
or Git Bash and type the command:

~~~
$ python
~~~
{: .bash}

## Binder as an alternative

As a (not so great) alternative you can complete the tutorials in this course using the Binder service running through a web browser. Simply click on the "launch binder" button here: [https://github.com/lucydot/empty_binder](https://github.com/lucydot/empty_binder), wait a while whilst the virtual environment is created, and then click on `Python 3` under Notebook.

Why is this a not-so-great alternative? Well firstly, the binder will time-out after a period of inactivity (about 15 minutes) and so you risk losing your work! Secondly, your work cannot be stored on Binder - so you will have to download if you would like to keep a copy. Thirdly, you cannot upload your work - so you have to start from scratch each time you use it. But still, if you cannot access Jupyter Notebook any other way - this is an option that requires only a web browser and internet connection.

[anaconda]: https://www.anaconda.com/
[continuum-mac]: https://www.anaconda.com/download/#macos
[continuum-linux]: https://www.anaconda.com/download/#linux
[continuum-windows]: https://www.anaconda.com/download/#windows
[jupyter]: http://jupyter.org/
[jupyter-install]: http://jupyter.readthedocs.io/en/latest/install.html#optional-for-experienced-python-developers-installing-jupyter-with-pip
[python]: https://python.org
[video-mac]: https://www.youtube.com/watch?v=TcSAln46u9U
[video-windows]: https://www.youtube.com/watch?v=xxQ0mzZ8UvA




  
