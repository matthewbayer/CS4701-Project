# CS4701-Project


## dataset
The complete dataset used for training both the Markov model and the GPT-2 finetuning. Each file is the complete data for the specified class.

## Markov Model
#### **Dependencies**
Numpy

### marovorder.py
The main file for the markov model.

### generate.py
Generates a single questions using the complete training set.\
Run using this command in terminal:\
`python3 generate.py`\
The number below the generated question displays the number of times the markov model had to randomly select a transition.

4 parameters that can be adjusted:

##### CHAR
Switch for character or word based markov model\
True for character, False for word

##### ORDER
Higher order markov model\
ORDER >= 1

##### SMOOTH
Laplace smoothing factor\
SMOOTH >= 0\
Should not be larger than 0.00001

##### TEXT
Input text for generation\
None to select a random state from the training set\
If CHAR, then number of characters in TEXT >= ORDER\
If not CHAR, then number of words in TEXT >= ORDER

### trainval.py
Generates a question for each question in the test set using the start of the question as the input.\
Recommending using this command in terminal:\
`time python3 trainval.py > outfile`\
The output would be truncated in the terminal, so this command writes to a file so it's easier to read. This command takes around 90 seconds to execute, so the `time` command is used to make sure there are no abnormalities.\
Each segment, delimited by a line of equal signs, contains the question ID, the original question, the generated question, and the number of times the markov model had to randomly select a transition.\
At the end, there's a Numpy array where the first column is the ID for the question and the second column is how many words overlap. Then, statistical information is also added for convenience.

The same parameters can be adjusted plus two additional parameters:

##### SPLIT
The percentage of the total dataset to be used as the training set. 1 - SPLIT is used as the test set for text generation.\
When SPLIT = 0.9, 550 questions are generated.

##### START
How many words or characters from the test question is used as the input text.\
START >= ORDER

## GPT-2
### CS_4701_GPT2_Script.ipynb
Should be run using Google Colab.\
The script will not run without manual upload of the dataset .py files.

### outputs/finetuned.py
Generated text using GPT-2 after finetuning as a Python list of strings.

### outputs/standard_gpt2.py
Generated text using GPT-2 without finetuning as a Python list of strings.

## outputs/test_set.py
The test set used for text generation.

## Other files

### piazza_scrapy.py
Unsuccessful attempt at web scraping Piazza. Not needed at all as dataset was manually collected.
#### **Dependencies**
BeautifulSoup

### examples, rating, results, sample
Various examples of generated text and output using markov model

### datatset_histogram.ipynb
Used to generate the histograms seen in final report
#### **Dependencies**
matplotlib
