import fitz  # PyMuPDF

def readfile(filename):
    '''read and return file content'''
    try:
        with fitz.open(filename) as doc:
            text = ""
            for page in doc:
                text += page.get_text()
            return text
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error: An error occurred while reading '{filename}': {e}")
        return None
def count_words(text):
    '''count and return number of words in text'''
    if text is None:
        return 0
    words = text.split()
    return len(words)
import re 
def count_words_no_punctuation(text):
    '''count and return number of words in text, ignoring punctuation'''
    if text is None:
        return 0
    clean_words = re.sub(r'[^a-zA-Z\s]', ' ', text)
    words = clean_words.split()
    #dont cpunt empty words as words
    words = [word for word in words if word]
    return len(words)
def count_lines(text):
    """count and return number of lines in text"""
    if text is None:
        return 0
    lines = text.splitlines()
    while lines and not lines[-1].strip():
        lines.pop()
    return len(lines)
def display_results(filename, word_count, word_count_no_punctuation, line_count):
    '''display results in a formatted way'''
    print(f"File: {filename}")
    print(f"Total Words: {word_count}")
    print(f"Total Words (No Punctuation): {word_count_no_punctuation}")
    print(f"Total Lines: {line_count}")


def save_to_csv(data, output_file="results.csv"):
    import csv
    import os
    # a for append, adds new roe to results instead of override
    with open(output_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Filename", "Word Count", "Word Count (No Punctuation)", "Line Count"])
        for row in data:
            writer.writerow(row)
def analyze_pdf(filename):
    '''main function to analyze pdf text'''
    print(f"Analyzing '{filename}'...")
    text = readfile(filename)
    if text is None:
        return
    word_count = count_words(text)
    word_count_no_punctuation = count_words_no_punctuation(text)
    line_count = count_lines(text)
    display_results(filename, word_count, word_count_no_punctuation, line_count)
    save_to_csv([[filename, word_count, word_count_no_punctuation, line_count]], output_file="results.csv")
import sys
def main():
    '''entry point with CLI andaling'''
    print(" "*50)
    print ("PDF Text Analysis Tool")
    print(" "*50)

    if len(sys.argv) > 1:
        filename = sys.argv[1]
        analyze_pdf(filename)
    else:   
        print("Usage: python reading_pdf.py <filename>")
        filename = input("Enter the filename to analyze: ").strip()
        if filename:
            analyze_pdf(filename)
if __name__ == "__main__":
    main()