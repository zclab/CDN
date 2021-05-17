
import argparse
import subprocess
from scripts.website_data import GenerateWebsiteData

src_dir = "images"
rep_url = "https://github.com/zclab/cdn/"
img_url = "https://cdn.jsdelivr.net/gh/zclab/cdn/"

parser = argparse.ArgumentParser()
parser.add_argument("--rename_file", action="store_true")
args = parser.parse_args()

if args.rename_file:
    print("---------- Rename all the files -------------")
    from scripts.file_rename import rename_all_files
    rename_all_files(src_dir)

webdata = GenerateWebsiteData(
    src_dir, rep_url, img_url, branch="master")
webdata.generate_all_items_toml(output_file="website/data/items.toml")

subprocess.run("cd website && hugo --minify", shell=True)
