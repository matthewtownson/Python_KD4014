---
title: "Retrieving data from Numpy arrays"
teaching: 15
exercises: 15
questions:
- "How can I select data from a NumPy array?"
objectives:
- "Index a two-dimensional NumPy array."
- "Select columns from a two-dimensional NumPy array."
keypoints:
- "All the indexing and slicing that we've used on lists and strings also works on arrays."
- "Use `array[x, y]` to select a single element from a 2D array"
- "Use `data[:,x]` to select a column"
---

## All the indexing and slicing that we've used on lists and strings also works on arrays.

In an earlier tutorial we have seen how to slice and index a one-dimensional Python list. 
Selecting data from our a multi-dimensional NumPy array is similar, but now we must provide indices or slices for each axis.

## Use `array[x, y]` to select a single element from a 2D array

To select a single element from our two dimensional array we must provide two indices: 
one which selects the row, and one which selects the column.

For example, to select single values in the array:

~~~
print('first value in data:', data[0, 0])
~~~
{: .language-python}

~~~
first value in data: 300
~~~
{: .output}

~~~
print('middle value in data:', absorption_data[50, 2])
~~~
{: .language-python}

~~~
middle value in data: 0.06
~~~
{: .output}

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

## Use `data[:,x]` to select a column
However we are more likely to want to work with particular rows or columns of our data. For this we need to combine slicing and indexing.

The first column of the data contains the wavelengths. We can select this section of the data array and assign it to a variable `wavelengths` using the following command:

~~~
wavelengths = data[:,0]
~~~
{: .language-python}

~~~
print(wavelengths)
~~~
{: .language-python}

~~~
array([300., 301., 302., 303., 304., 305., 306., 307., 308., 309., 310.,
       311., 312., 313., 314., 315., 316., 317., 318., 319., 320., 321.,
       322., 323., 324., 325., 326., 327., 328., 329., 330., 331., 332.,
       333., 334., 335., 336., 337., 338., 339., 340., 341., 342., 343.,
       344., 345., 346., 347., 348., 349., 350., 351., 352., 353., 354.,
       355., 356., 357., 358., 359., 360., 361., 362., 363., 364., 365.,
       366., 367., 368., 369., 370., 371., 372., 373., 374., 375., 376.,
       377., 378., 379., 380., 381., 382., 383., 384., 385., 386., 387.,
       388., 389., 390., 391., 392., 393., 394., 395., 396., 397., 398.,
       399., 400., 401., 402., 403., 404., 405., 406., 407., 408., 409.,
       410., 411., 412., 413., 414., 415., 416., 417., 418., 419., 420.,
       421., 422., 423., 424., 425., 426., 427., 428., 429., 430., 431.,
       432., 433., 434., 435., 436., 437., 438., 439., 440., 441., 442.,
       443., 444., 445., 446., 447.])
~~~
{: .output}

We have to specify two indices/slices (separated by a comma) as this is a two dimensional array (with rows and columns). 
The first slice selects all rows, the second index selects the zeroth column. 

Look carefully at the slice `[:]` - we have not specified a lower or upper bound. If we don't include the lower
bound, Python uses 0 by default; if we don't include the upper, the slice runs to the end of the
axis, and if we don't include either (i.e., if we just use ':' on its own), the slice includes
everything. 

The second column contains the data for the ITO (Indium Tin Oxide). To select this data and assign it to a new variable we can use a similar command, but now selecting the first column:

~~~
ITO_transmittance = data[:,1]
~~~
{: .language-python}

We can then repeat this for the other materials:

~~~
CdS_transmittance = data[:,1]
Si_transmittance = data[:,2]
GaAs_transmittance = data[:,3]
~~~
{: .language-python}

> ## Selecting a row
>
> Can you work out how to select a row of a two-dimensional array?
> 
> > If `A` is the two dimensional array, `A[0,:]` will select the first row. 
> > This can be shortened to `A[0]`, as the row is the primary axis.
> > {: .solution}
{: .challenge}

> ## Slicing and Stacking Arrays
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
