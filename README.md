# BMI500 Homework (Lecture11)

newicd.py is python 3.6 program that first finds the number of 1-1, 1-many mappings and also no mappings in 10->9 GEMs (ICD10 to 9), then tries to se

To run the code, run the following command:

```python newicd.py path1 path2```

Where path1 is the path1 to '2018_I10gem.txt' file and path2 is the path to 'Q1-Q3-ICD-9-CM.txt' file added to the repository. 

For instance, if the '2018_I10gem.txt' file is in the same folder as the python code, the path1 is : './2018_I10gem.txt' and path2 is './Q1-Q3-ICD-9-CM.txt' and you need to run the following command:

```python newicd.py ./2018_I10gem.txt ./Q1-Q3-ICD-9-CM.txt```

The code writes the output in a text file named: "Output.txt", where the first column is the ICD10 code, the second column is the ICD9 code, and the third column shows the highest frequecy among the corresponding codes of a single icd10 code, in the california state icd9 codes.


