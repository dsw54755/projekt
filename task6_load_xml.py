import xmltodict

def load_xml(file_path):
    with open(file_path, 'r') as file:
        return xmltodict.parse(file.read())

if __name__ == "__main__":
    input_file = "C:\\Users\\Asus-pc\\Desktop\\Projekt\\input.xml"
    data = load_xml(input_file)
    print(data)
