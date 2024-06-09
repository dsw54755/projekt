import sys
import os
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QMessageBox

def convert(input_file, output_file, input_ext, output_ext):
    # Przykładowa funkcja konwersji, tutaj dodaj logikę konwersji między formatami
    pass

class ConverterThread(threading.Thread):
    def __init__(self, input_file, output_file, input_ext, output_ext):
        threading.Thread.__init__(self)
        self.input_file = input_file
        self.output_file = output_file
        self.input_ext = input_ext
        self.output_ext = output_ext

    def run(self):
        convert(self.input_file, self.output_file, self.input_ext, self.output_ext)

class ConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Konwerter')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.load_button = QPushButton('Wczytaj plik', self)
        self.load_button.clicked.connect(self.load_file)
        layout.addWidget(self.load_button)

        self.save_button = QPushButton('Zapisz plik', self)
        self.save_button.clicked.connect(self.save_file)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def load_file(self):
        options = QFileDialog.Options()
        file, _ = QFileDialog.getOpenFileName(self, "Otwórz plik", "", "Wszystkie pliki (*);;XML Files (*.xml);;JSON Files (*.json);;YAML Files (*.yml *.yaml)", options=options)
        if file:
            self.input_file = file
            self.input_ext = os.path.splitext(file)[1].lower()
            QMessageBox.information(self, "Wybrany plik", f"Wybrany plik: {file}")

    def save_file(self):
        options = QFileDialog.Options()
        file, _ = QFileDialog.getSaveFileName(self, "Zapisz plik", "C:\\Users\\Asus-pc\\Desktop\\Projekt\\output.json", "Wszystkie pliki (*);;XML Files (*.xml);;JSON Files (*.json);;YAML Files (*.yml *.yaml)", options=options)
        if file:
            self.output_file = file
            self.output_ext = os.path.splitext(file)[1].lower()
            self.thread = ConverterThread(self.input_file, self.output_file, self.input_ext, self.output_ext)
            self.thread.start()
            self.thread.join()
            QMessageBox.information(self, "Zapisany plik", f"Zapisany plik: {file}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    converter = ConverterApp()
    converter.show()
    sys.exit(app.exec_())
