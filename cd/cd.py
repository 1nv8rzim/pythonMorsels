import os


class cd:
    def __init__(self, subdir):
        self.subdir = subdir

    def __enter__(self):
        self.original_dir = os.getcwd()
        os.chdir(self.subdir)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.original_dir)
