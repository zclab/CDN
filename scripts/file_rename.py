
import os
import re
from pathlib import Path


def rename_all_files(src_dir, *suffixes):

    for root, dirs, files in os.walk(src_dir):
        root_path = Path(root).resolve()
        prefix = root_path.parts[-1]

        pat, pated_files, unpated_files = r"^%s_\d{3}$" % prefix, [], []
        for f in files:
            if Path(f).suffix in suffixes:
                if re.match(pat, Path(f).stem):
                    pated_files.append(f)
                else:
                    unpated_files.append(f)

        count = len(pated_files) + 1
        for f in unpated_files:
            file = root_path / f
            if file.suffix in suffixes:
                os.rename(file, file.with_name(
                    "{}_{:03d}{}".format(prefix, count, file.suffix)))
                count += 1
