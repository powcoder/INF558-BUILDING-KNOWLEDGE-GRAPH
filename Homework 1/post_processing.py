https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
import logging
import sys, ujson

from bs4 import BeautifulSoup
from pathlib import Path


def deserialize_jl(input_file):
    with open(input_file, "r") as f:
        return [ujson.loads(s) for s in f]


def serialize_jl(records, output_file):
    with open(output_file, "w") as f:
        for record in records:
            f.write(ujson.dumps(record))
            f.write("\n")


def get_essential_information(cdr):
    html = cdr["raw_content"]
    bs4_elem = BeautifulSoup(html, 'html.parser')
    main_content = bs4_elem.select_one("div.region-content")

    new_cdr = {k: v for k, v in cdr.items() if k != "raw_content"}
    new_cdr["raw_content"] = str(main_content)
    return new_cdr


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Error: missing path to cdr file!")
        exit(1)

    cdr_file = sys.argv[1]
    if not Path(cdr_file).exists():
        print("Error: path of cdr file does not exist!")
        exit(1)

    try:
        web_pages = deserialize_jl(cdr_file)
    except Exception as e:
        print("Error: invalid cdr file!")
        logging.exception(e)
        exit(1)

    new_pages = []
    for i, page in enumerate(web_pages):
        try:
            new_pages.append(get_essential_information(page))
        except:
            print(f"Your web_page at index {i} is invalid!")
            raise

        print(f"\rProcess: ({i}/{len(web_pages)})...", end="", flush=True)

    serialize_jl(new_pages, cdr_file + ".processed")
