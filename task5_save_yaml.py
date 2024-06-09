import yaml

def save_yaml(data, file_path):
    with open(file_path, 'w') as file:
        yaml.dump(data, file, default_flow_style=False)

if __name__ == "__main__":
    data = {"key": "value"}
    output_file = "C:\\Users\\Asus-pc\\Desktop\\Projekt\\output.yml"
    save_yaml(data, output_file)
    print(f"Zapisano do {output_file}")
