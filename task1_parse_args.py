import sys
import os

def parse_args():
    if len(sys.argv) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    input_ext = os.path.splitext(input_file)[1].lower()
    output_ext = os.path.splitext(output_file)[1].lower()

    if input_ext not in ['.xml', '.json', '.yml', '.yaml']:
        print("Unsupported input file format.")
        sys.exit(1)
    
    if output_ext not in ['.xml', '.json', '.yml', '.yaml']:
        print("Unsupported output file format.")
        sys.exit(1)
    
    return input_file, output_file, input_ext, output_ext

if __name__ == "__main__":
    input_file, output_file, input_ext, output_ext = parse_args()
    print(f"Input file: {input_file}, Output file: {output_file}")
