import xmltodict

def save_xml(data, file_path):
    with open(file_path, 'w') as file:
        file.write(xmltodict.unparse(data, pretty=True))

if __name__ == "__main__":
    data = {"key": "value"}
    output_file = "C:\\Users\\Asus-pc\\Desktop\\Projekt\\output.xml"
    save_xml(data, output_file)
    print(f"Zapisano do {output_file}")
