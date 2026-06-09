# Creating a Clean Python Environment with uv
curl -LsSf https://astral.sh/uv/install.sh | sh 


### Create a virtual environment with Python 3.11
uv venv --python 3.11

### Activate it
source .venv/bin/activate  

# Libraries

## install libraries
uv pip install pdfplumber pymupdf pypdf -q



To run:

Python practice_analyzer.py /Users/leahpolonsky/Desktop/practice1.pdf

Or interactive mode: Python  practice_analyzer.py

Created a result.csv file with the table to output to googlesheets

To delete that file:
 Python delete_csv.py “filename to delete”
