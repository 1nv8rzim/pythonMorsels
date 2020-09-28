import os
from pathlib import Path
from tempfile import TemporaryDirectory


class cd:
    def __init__(self, sub_dir=None):
        self.sub_dir = sub_dir

    def __enter__(self):
        self.original_dir = Path.cwd()
        self.temp_dir = TemporaryDirectory() if self.sub_dir is None else None
        self.new_dir = self.temp_dir.name if self.sub_dir is None else self.original_dir.joinpath(
            self.sub_dir)
        os.chdir(self.new_dir)
        self.current = self.new_dir
        self.previous = self.original_dir
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.original_dir)
        if self.sub_dir is None:
            self.temp_dir.cleanup()
