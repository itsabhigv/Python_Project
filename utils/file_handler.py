import csv

class FileHandler:
    def read_file(self, file_path):
        with open(file_path, "r") as file:
            return file.read()

    def read_csv(self, file_path):
        data = {}
        with open(file_path, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                reg = row["VARIANT_REG"].replace(" ", "")
                data[reg] = row
        return data
