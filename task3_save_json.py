import json

def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    data = {"key": "value"}
    output_file = "path/to/output.json"
    save_json(data, output_file)
    print(f"Zapisano do {output_file}")
