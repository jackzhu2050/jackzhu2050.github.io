import os
import re
import shutil

ROOT = os.path.abspath(os.path.dirname(__file__))


def proc(f: str):
    with open(f, 'r+') as fh:
        cont = fh.read()
        fh.seek(0)
        extra = """Author: Jack Zhu
date: {}
comments: True""".format('-'.join(os.path.basename(f).split('-')[:3]))
        cont = re.sub(r"category: (.*)", extra, cont)
        cont = re.sub(
            r'tags: (.*)',
            lambda x: 'tags: [' + ', '.join(x.group(1).split()) + ']', cont)
        cont = re.sub(r'!\[(.*)\]\(/assets(.*)\)', r'![\1](\2)', cont)
        fh.write(cont)


def get_images(f):
    with open(f) as fh:
        cont = fh.read()
        images = re.findall(r'!\[.*\]\(/assets/images/(.*)\)', cont)
        return images


def migrate(names):
    from_path = os.path.join(ROOT, "../towerjoo.github.com")
    posts_dir = os.path.join(from_path, "_posts")
    images_dir = os.path.join(from_path, "assets/images")
    for name in names:
        pfrom = os.path.join(posts_dir, name)
        images = get_images(pfrom)
        for image in images:
            shutil.move(os.path.join(images_dir, image),
                        os.path.join(ROOT, "images", image))
        pto = os.path.join(ROOT, "_posts/", os.path.basename(pfrom))
        shutil.move(pfrom, pto)
        proc(pto)
        print(f"{pfrom} has been migrated to {pto}")


if __name__ == "__main__":
    names = [
        "2019-12-22-educated.md",
        "2019-03-11-For-Whom-the-Bell-Tolls.md",
        "2019-02-12-random-thoughts.md",
        "2019-02-08-wild-swan.md",
        "2018-12-31-perks-of-being-a-wallflower.md",
        "2018-12-16-humanity.md",
        "2018-07-30-new-office.md",
        "2018-07-23-its-too-hot.md",
        "2018-07-16-goodbye-worldcup.md",
        "2018-07-08-god-of-medicine.md",
        "2018-07-01-world-cup-again.md",
        "2018-06-24-world-cup-russia.md",
        "2018-06-10-github-ms-blockchain.md",
        "2018-06-03-eos.md",
        "2017-08-25-life_and_death_in_shanghai.md",
        "2017-09-02-HK_trip.md",
        "2017-10-16-read-original-language-book.md",
        "2018-04-15-self-reflection.md",
        "2018-04-22-marathon-13k.md",
        "2018-04-29-stay-put.md",
        "2018-05-06-books.md",
        "2018-05-14-sick-and-novel.md",
        "2018-05-21-yc-startup.md",
        "2018-05-28-reading-as-career.md",
    ]
    migrate(names)