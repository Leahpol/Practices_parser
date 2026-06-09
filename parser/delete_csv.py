import os
def main(output_file="results.csv"):
    if os.path.exists(output_file):
        os.remove(output_file)
if __name__ == "__main__":
    main()