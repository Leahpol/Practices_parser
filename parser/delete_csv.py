import os
import sys
def main(output_file):
    """delete the csv file if it exists to start fresh"""
    if os.path.exists(output_file):
        os.remove(output_file)
if __name__ == "__main__":
    if len(sys.argv) > 1:
        main (sys.argv[1])