
import subprocess
from scripts.website_data import GenerateWebsiteData

src_dir = "cdn"
rep_url = "https://github.com/zclab/cdn/"
img_url = "https://cdn.jsdelivr.net/gh/zclab/cdn/"


webdata = GenerateWebsiteData(
    src_dir, rep_url, img_url, branch="master")
webdata.generate_all_items_toml(output_file="website/data/items.toml")

subprocess.run("cd website && hugo --minify", shell=True)
