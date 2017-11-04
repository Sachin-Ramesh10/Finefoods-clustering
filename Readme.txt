
download dataset from https://snap.stanford.edu/data/web-FineFoods.html

The Final.py contains synchronous commands to execute the complete list of requirements and generate the results

requirements to run:(in the same folder as that of Final.py)
-stopwords.txt (containing all the stopwords. The stopwords.txt that i have used , has all the stowords with word in each line)
-finefoods.txt (datafile)

execution:
-on executing Final.py, it asks for the input file name, in our case its finefoods.txt

Upon execution, the program ends after producing below files.

Reviews.txt ---- contains reviews/text field of the dataset
Uniquewords.txt ---- contains unique words in all of the reviews
Top500_Freq.csv ---- contains the top 500 unique words ordered(decending) by their frequency among total words
VectorMatrix.csv ---- contains the vectors of top 500 words in particular review. first row is 500 words and 1st column is the review number.
TopClusteredwords.txt ----contains the top 5 words from each of the cluster and its feature value

*******result of my execution is placed in Results folder in submitted zip file*****************
*******Top500_Freq.csv(Problem 7.1)||TopClusteredwords.txt(Problem 7.2)*************************

Internal execution steps:

Selecting review/text
reading only reviews/text field and saving it for further reference

Tokenizing the Review/text
using nltk framework, reviews have been tokenized and saved in a list

removing special characters
using regular expression unwanted characted/symbols are removed converting to lowercase

finding unique words
finding unique words among the total list of words and saving it to the list L

removing stopwords
comparing L with stopwords list and few customized unwanted words list(due to inconsistent spellings and hypelinks) and removing them saving them to list W

finding frequency of top 500
coapring list W with list of words counting their coccurence and choosing top 500 values

creating vector matrix
using the top 500 words each review is compared for the words occurence and vectorized.saved in a matrix form in csv file

creating dataframe of vectors
reading the vectorized csv file and loading the dataframe with the matrix value(tried direct approach but was consuming too much memory)

Starting Clustering
using skikit's kmeans algorithm to cluster the dataframe into 10 clusters

Finding top 5 words from Each clusters
once we have the cluster traversing each clsuter to get top 5 words and its feature value.saving it to txt file