---
title: "Variables and Assignment"
teaching: 15
exercises: 15
questions:
- "How can I store data in programs?"
objectives:
- "Write programs that assign scalar values to variables and perform calculations with those values."
- "Correctly trace value changes in programs that use scalar assignment."
keypoints:
- "Use variables to store values."
- "Use `print` to display values."
- "Variables persist between cells."
- "Variables must be created before they are used."
- "Variables can be used in calculations."
- "Python is case-sensitive."
- "Use meaningful variable names."
---
## Use variables to store values.

*   Variables are names for values.
*   In Python the `=` symbol assigns the value on the right to the name on the left.
*   The variable is created when a value is assigned to it.
*   Here, Python assigns an age to a variable `age`
    and a name in quotes to a variable `first_name`.

~~~
age = 42
first_name = 'Ahmed'
~~~
{: .python}

*   Variable names
    * can **only** contain letters, digits, and underscore `_` (typically used to separate words in long variable names)
    * cannot start with a digit
*   Variable names that start with underscores like `__alistairs_real_age` have a special meaning
    so we won't do that until we understand the convention.

## Use `print` to display values.

*   Python has a built-in function called `print` that prints things as text.
*   Call the function (i.e., tell Python to run it) by using its name.
*   Provide values to the function (i.e., the things to print) in parentheses.
*   To add a string to the printout, wrap the string in single or double quotes.
*   The values passed to the function are called 'arguments'

~~~
print(first_name, 'is', age, 'years old')
~~~
{: .python}
~~~
Ahmed is 42 years old
~~~
{: .output}

*   `print` automatically puts a single space between items to separate them.
*   And wraps around to a new line at the end.

## Variables must be created before they are used.

*   If a variable doesn't exist yet, or if the name has been mis-spelled,
    Python reports an error.
    *   Unlike some languages, which "guess" a default value.

~~~
print(last_name)
~~~
{: .python}
~~~
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-1-c1fbb4e96102> in <module>()
----> 1 print(last_name)

NameError: name 'last_name' is not defined
~~~
{: .error}

*   The last line of an error message is usually the most informative.
*   We will look at error messages in detail [later]({{ page.root }}/15-scope/#reading-error-messages).

> ## Variables Persist Between Cells
>
> Be aware that it is the order of **execution** of cells that is important in a Jupyter notebook, not the order
> in which they appear. Python will remember **all** the code that was run previously, including any variables you have
> defined, irrespective of the order in the notebook. Therefore if you define variables lower down the notebook and then
> (re)run cells further up, those defined further down will still be present. As an example, create 2 cells with the
> following content, in this order:
>
> ~~~
> print(myval)
> ~~~
> {: .python}
>
> ~~~
> myval = 1
> ~~~
> {: .python}
>
> If you execute this in order, the first cell will give an error. However, if you run the first cell **after** the second
> cell it will print out ‘1’. To prevent confusion, it can be helpful to use the `Kernel` -> `Restart & Run All` option which
> clears the interpreter and runs everything from a clean slate going top to bottom.
{: .callout}

## Variables can be used in calculations.

*   We can use variables in calculations just as if they were values.
    *   Remember, we assigned 42 to `age` a few lines ago.

~~~
age = age + 3
print('Age in three years:', age)
~~~
{: .python}
~~~
Age in three years: 45
~~~
{: .output}



## Python is case-sensitive.

*   Python thinks that upper- and lower-case letters are different,
    so `Name` and `name` are different variables.
*   There are conventions for using upper-case letters at the start of variable names so we will use lower-case letters for now.

## Use meaningful variable names.

*   Python doesn't care what you call variables as long as they obey the rules
    (alphanumeric characters and the underscore).

~~~
flabadab = 42
ewr_422_yY = 'Ahmed'
print(ewr_422_yY, 'is', flabadab, 'years old')
~~~
{: .python}

*   Use meaningful variable names to help other people understand what the program does.
*   The most important "other person" is your future self.

> ## Swapping Values
>
> Fill the table showing the values of the variables in this program
> **after** each statement is executed.
>
> ~~~
> # Command  # Value of x   # Value of y   # Value of swap #
> x = 1.0    #              #              #               #
> y = 3.0    #              #              #               #
> swap = x   #              #              #               #
> x = y      #              #              #               #
> y = swap   #              #              #               #
> ~~~
> {: .python}
> > ## Solution
> >
> > ~~~
> > # Command  # Value of x   # Value of y   # Value of swap #
> > x = 1.0    # 1.0          # not defined  # not defined   #
> > y = 3.0    # 1.0          # 3.0          # not defined   #
> > swap = x   # 1.0          # 3.0          # 1.0           #
> > x = y      # 3.0          # 3.0          # 1.0           #
> > y = swap   # 3.0          # 1.0          # 1.0           #
> > ~~~
> > {: .output}
> > 
> > These three lines exchange the values in `x` and `y` using the `swap`
> > variable for temporary storage. This is a fairly common programming idiom.
>{: .solution}
{: .challenge}

> ## Predicting Values
>
> What is the final value of `position` in the program below?
> (Try to predict the value without running the program,
> then check your prediction.)
>
> ~~~
> initial = 'left'
> position = initial
> initial = 'right'
> ~~~
> {: .python}
> > ## Solution
> >
> > ~~~
> > 'left'
> > ~~~
> > {: .output}
> >
>> The `initial` variable is assigned the value 'left'.
> > In the second line, the `position` variable also receives
>> the string value 'left'. In third line, the `initial` variable is given the
>> value 'right', but the `position` variable retains its string value
>> of 'left'.
>{: .solution}
{: .challenge}



> ## Choosing a Name
>
> Which is a better variable name, `m`, `min`, or `minutes`?
> Why?
> Hint: think about which code you would rather inherit
> from someone who is leaving the lab:
>
> 1. `ts = m * 60 + s`
> 2. `tot_sec = min * 60 + sec`
> 3. `total_seconds = minutes * 60 + seconds`
>
> > ## Solution
> >
> > `minutes` is better because `min` might mean something like "minimum"
> > (and actually does in Python, but we haven't seen that yet).
> {: .solution}
{: .challenge}

