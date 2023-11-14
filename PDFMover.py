import os
import shutil


class PDFMover:
    def __init__(self, source, target):
        self.source = source
        self.target = target

    def list_files(self, path_type):
        if path_type == 'source':
            return [file for file in os.listdir(self.source) if '.pdf' in file]
        elif path_type == 'target':
            return [file for file in os.listdir(self.target) if '.pdf' in file]

    def check_target(self):
        missing_books = []
        for file in self.list_files('source'):
            if file not in self.list_files('target'):
                missing_books.append(file)

        return missing_books

    def move_files(self):
        for file in self.check_target():
            shutil.move(f"{self.source}\\{file}", f"{self.target}\\{file}")


