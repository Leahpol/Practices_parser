## Creating a Clean Python Environment with uv
curl -LsSf https://astral.sh/uv/install.sh | sh 


# Create a virtual environment with Python 3.11
uv venv --python 3.11

# Activate it
source .venv/bin/activate  

## Libraries

# install libraries
uv pip install pdfplumber pymupdf pypdf -q