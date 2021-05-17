
import os
from pathlib import Path


def rename_all_files(src_dir):
    """容易出现覆盖已存在的文件的问题
    """
    for root, dirs, files in os.walk(src_dir):
        count, files = 0, sorted(files)
        for f in files:
            file = Path(root) / f
            if file.suffix in (".png", ".jpg", ".gif", ".ico", ".svg"):
                count += 1
                prefix = str(file.parent).replace("/", "_")
                new_name = str(file.with_name(
                    "{}_{:04d}{}".format(prefix, count, file.suffix)))
                os.rename(str(file), new_name)
