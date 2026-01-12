import re


def extract_title(markdown):
    match = re.search(r"^# .*$", markdown, flags=re.MULTILINE)
    if not match:
        raise Exception("No h1 Header")
    else:
        return markdown[match.start() + 1 : match.end()].strip()
