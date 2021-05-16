
import os
from pathlib import Path


def get_item_toml(*item):
    return """[[items]]\ntitle = "{}"\nimage = "{}"\nthumb = "{}"\nalt= "{}"\ndescription = "{}"\nurl = "{}"\n\n""".format(*item)


class GenerateWebsiteData:

    def __init__(self, src_dir, rep_url, img_url, branch="main") -> None:
        self.src_dir = src_dir
        self.rep_url = rep_url
        self.img_url = img_url
        self.branch = branch

    def format_item(self, file):
        """get required information from file

        Args:
            file (Path): Path to the file

        Returns:
            tuple: title, image, thumb, alt, description, url
        """
        image = self.img_url + str(file)
        url = self.rep_url + "blob/{}/{}/".format(self.branch, file)

        return file.name, image, image, file.name, image, url

    def generate_all_items_toml(self, *suffix, output_file):

        suffix = (".png", ".jpg") if not(suffix) else suffix

        all_items = []
        for root, dirs, files in os.walk(self.src_dir):
            for f in files:
                file = Path(root) / f
                if Path(file).suffix in suffix:
                    all_items.append(self.format_item(Path(file)))

        all_items = sorted(all_items, key=lambda x: x[0])
        with open(output_file, 'w') as f:
            for item in all_items:
                f.write(get_item_toml(*item))
