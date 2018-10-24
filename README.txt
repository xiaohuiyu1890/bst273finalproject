1.	List your name and email address.

NAME: Xiaohui Yu
EMAIL: xiaohuiyu@hsph.harvard.edu
URL: https://github.com/xiaohuiyu1890/bst273finalproject.git



2.	Summarize your experience working on the final project. For example, you might approximate how many hours you spent on it and how those hours were distributed. If you found some aspects considerably harder than others, list those here. If there are known problems with your final project script, list those here.

ANSWER: I spent approximately 20 hours on the final project. It took me a long time to find and decide on using seaborn to create a stratified plot. Also, I found it challenging to figure out how to use specific strings in the header as label. 



3.	In a few sentences, describe what your final project script does.

ANSWER: The script generates scatter plots based on columns of data from TSV-format input files. The user can choose input file, the columns for x-axis and y-axis, optional category for stratification, and an optional path to the output file. If not specified, there would be only one stratum and the scatter plot will be saved in the working directory as scatter_plot.png. 



4.	List any modules (outside of the Python standard library) that are required to execute your final project script. You may answer “N/A” if no such modules are required.

ANSWER: argparse, matplotlib.pyplot, pandas, seaborn




5.	Describe your sample INPUT FILE(S). If you are completing a custom final project that does not require an input file, explain that clearly here.

ANSWER: The input file contains TSV-format data. Its top row contains the names of “fields” from the data frame and fields store a particular measurement for a set of observations; Each row after the first contains the measurements for a particular observation. Measurements can be continuous (numbers) or categorical (text labels). Importantly, it is assumed that the data frame is well-formed: i.e. there are no missing values, no text-values in otherwise numerical columns, all columns have the same length, etc.
The famous "Iris" dataset is used as a sample input file, which lists 150 sets of sepal  width, sepal length, petal width, petal length in cm, and their class. The final field (“class”) is a categorical field; the first four fields are all continuous. 



6.	Provide the command used to produce your sample OUTPUT FILE with flags and arguments specified (e.g. “$ python script_name.py arguments”).

ANSWER: 
(optional stratification, optional output path) python scatter.py -x 1 -y 3 -cat 5 iris.tsv -o xiaohuiplot.png
(default no stratification, default output path) python scatter.py -x 1 -y 3 iris.tsv



7.	Describe your sample OUTPUT FILE(S). If you are completing a custom final project that does not produce an output file, capture the STDOUT of the command specified above and include it here (e.g. “$ command > sample_stdout.txt”).

ANSWER: The first sample output file is a png-formatted scatter plot based on the "Iris" dataset. As the title indicates, the scatter plot shows petal width(cm) as y-axis and sepal width (cm) as x-axis, stratified by class. The stratification is color-coded; also, both x-axis and y-axis are labeled using information from the header. As set by user in the command, the scatter plot is saved as xiaohuiyuploy.png in the working directory. 
The second sample output file sets both stratification and output path as default, i.e. no stratification and the scatter plot being saved as scatter_ploy.png in the working directory.  



8.	What was your favorite part of learning to program in BST 273 (i.e. something we should definitely NOT change in future incarnations of the course)?

ANSWER: My favorite part was to practice translating English into coding command in class. I think it was helpful in the long run learning how to approach a question from a programming language's perspective. Also, office hours are incredibly helpful and they are VERY much needed. 



9.	What was your LEAST favorite part of learning to program in BST 273 (i.e. something we should look into changing for future incarnations of the course)?

ANSWER: In the first three classes, we spent about half an hour each practicing and working on problems individually in class; I think that time could have been better spent and we can all practice on our own after class. Also, I think it would be helpful if we could go through a real-life python script for a data analysis project, and see the bigger picture of how Python can be used in data analysis for medical research. 


