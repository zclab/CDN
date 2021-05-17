
import os
from pathlib import Path


class FileRename:

    def __init__(self, src_dir) -> None:
        self.src_dir = src_dir

    def rename_all_files(self, *suffix):
        suffix = (".png", ".jpg", ".svg", ".ico") if not(suffix) else suffix

        for root, dirs, files in os.walk(self.src_dir):
            for f in files:
                file = Path(root) / f
                if file.suffix in suffix:
                    new_name = Path(root) / "_".join(file.parts)
                    os.rename(file, new_name)
