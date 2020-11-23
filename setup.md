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
   default settings. The only exception is to check the 
   **Make Anaconda the default Python** option.

### Mac OS X - [Video tutorial][video-mac]

1. Open [https://www.anaconda.com/download][continuum-mac]
   with your web browser.

2. Download the Python 3 installer for OS X.

3. Install Python 3 using all of the defaults for installation.

### Linux

Note that the following installation steps require you to work from the shell. 
If you run into any difficulties, please request help before the workshop begins.

1.  Open [https://www.anaconda.com/download][continuum-linux] with your web browser.

2.  Download the Python 3 installer for Linux.

3.  Install Python 3 using all of the defaults for installation.

    a.  Open a terminal window.

    b.  Navigate to the folder where you downloaded the installer

    c.  Type

    ~~~
    $ bash Anaconda3-
    ~~~
    {: .bash}

    and press tab.  The name of the file you just downloaded should appear.

    d.  Press enter.

    e.  Follow the text-only prompts.  When the license agreement appears (a colon
        will be present at the bottom of the screen) hold the down arrow until the 
        bottom of the text. Type `yes` and press enter to approve the license. Press 
        enter again to approve the default location for the files. Type `yes` and 
        press enter to prepend Anaconda to your `PATH` (this makes the Anaconda 
        distribution the default Python).
        
        
## Installing Bash

Bash is a commonly-used shell that gives you the power to do simple tasks more quickly.

### Windows - [video tutorial](https://www.youtube.com/watch?v=339AEqk9c-8)

1. Download the Git for Windows [installer](https://git-for-windows.github.io/)

2. Run the installer and follow the steps below:
    
    a) Click on "Next" four times (two times if you've previously
                installed Git).  You don't need to change anything
                in the Information, location, components, and start menu screens.
 
    b) Select “Use the nano editor by default” and click on “Next”.

    c) Keep "Use Git from the command line and..." selected and click on "Next".
                If you forgot to do this programs that you need for the workshop will not work properly.
                If this happens rerun the installer and select the appropriate option.
                
    d) Click on "Next"
    
    e) Keep "Checkout Windows-style, commit Unix-style line endings" selected and click on "Next".

    f) Select "Use Windows' default console window" and click on "Next".
    
    g) Click on "Install"
    
    h) Click on "Finish"

3. If your "HOME" environment variable is not set (or you don't know what this is):

   a) Open command prompt (Open Start Menu then type <code>cmd</code> and press [Enter])

   b) Type the following line into the command prompt window exactly as shown:
     `setx HOME "%USERPROFILE%"`

   c) Press [Enter], you should see `SUCCESS: Specified value was saved.`
  
  d) Quit command prompt by typing `exit` then pressing [Enter]

This will provide you with both Git and Bash in the Git Bash program.


### macOS

 The default shell in all versions of macOS is Bash, so no
        need to install anything.  You access Bash from the Terminal
        (found in
        `/Applications/Utilities`).
       
See the Git installation <a href="https://www.youtube.com/watch?v=9LQhwETCdwY ">video tutorial</a>
        for an example on how to open the Terminal.
        You may want to keep
        Terminal in your dock for this workshop.

### Linux

The default shell is usually Bash, but if your
        machine is set up differently you can run it by opening a
        terminal and typing `bash`.  There is no need to
        install anything.


## Getting the Data

To obtain the data we will be using, download the file 
[UVVis-01.csv]({{page.root}}/data/UVVis-01.csv).
In order to follow the presented material, you should launch a Jupyter 
notebook in the root directory (see [Starting Python](#Starting-Python)).

## Starting Python

We will teach Python using the [Jupyter notebook][jupyter], a 
programming environment that runs in a web browser. Jupyter requires a reasonably 
up-to-date browser, preferably a current version of Chrome, Safari, or Firefox 
(note that Internet Explorer version 9 and below are *not* supported). If you 
installed Python using Anaconda, Jupyter should already be on your system. If 
you did not use Anaconda, use the Python package manager pip
(see the [Jupyter website][jupyter-install] for details.)

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

[anaconda]: https://www.anaconda.com/
[continuum-mac]: https://www.anaconda.com/download/#macos
[continuum-linux]: https://www.anaconda.com/download/#linux
[continuum-windows]: https://www.anaconda.com/download/#windows
[jupyter]: http://jupyter.org/
[jupyter-install]: http://jupyter.readthedocs.io/en/latest/install.html#optional-for-experienced-python-developers-installing-jupyter-with-pip
[python]: https://python.org
[video-mac]: https://www.youtube.com/watch?v=TcSAln46u9U
[video-windows]: https://www.youtube.com/watch?v=xxQ0mzZ8UvA




  
