import yaml
import sys

def load_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
        return data
    except yaml.YAMLError:
        print("zły plik yaml.")
        sys.exit(1)

if __name__ == "__main__":
    input_file = "C:\\Users\\Asus-pc\\Desktop\\Projekt\\input.yml"
    data = load_yaml(input_file)
    print(data)
