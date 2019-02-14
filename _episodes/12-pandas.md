---
title: "Cleaning data with Pandas"
teaching: 15
exercises: 15
questions:
- "How can I import and clean tabular data in Python?"
objectives:
- "Read tabular data from a file into a program using `pandas`."
- "Remove unwanted data columns"
- "Swap row and column data (transpose)"
keypoints:
- "Use the `pandas` library to work with tabular data in Python"
- "The `read_csv` function is used to read in .csv data"
- "The `read_csv` function has several keywords which can simplify data parsing"
- "The `dataframe` object has a `transpose` method which will transpose rows and columns"
- "The `dataframe` object has a `to_csv` method which will write the dataframe to a file"
---


df = pd.read_csv("./data/UVVis-01.csv",usecols=[1,3,5,7,9,11,13,15,17,19],header=None)

df = df.transpose()

df.to_csv("./data/UVVis-01-adapted.csv",header=False,index=False)