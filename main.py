import json
import yaml
import xmltodict
import sys
import os

def convert(input_file, output_file):
    input_ext = os.path.splitext(input_file)[1].lower()
    output_ext = os.path.splitext(output_file)[1].lower()

    with open(input_file, 'r') as file:
        if input_ext == '.json':
            data = json.load(file)
        elif input_ext in ['.yml', '.yaml']:
            data = yaml.safe_load(file)
        elif input_ext == '.xml':
            data = xmltodict.parse(file.read())
        else:
            raise ValueError("Zły format wejściowy")

    with open(output_file, 'w') as file:
        if output_ext == '.json':
            json.dump(data, file, indent=4)
        elif output_ext in ['.yml', '.yaml']:
            yaml.dump(data, file, default_flow_style=False)
        elif output_ext == '.xml':
            file.write(xmltodict.unparse(data, pretty=True))
        else:
            raise ValueError("Zły format wyjściowy")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Użycie: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert(input_file, output_file)
    print(f"Przekonwertowano {input_file} do {output_file}")
