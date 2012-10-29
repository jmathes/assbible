import os
import re
from pprint import pprint

bibledir = os.path.join(os.path.dirname(__file__), "bible")

asslines = {}
asscounts = {}

ass_re = re.compile(r"\b[Aa][Ss][Ss]\b")
assert ass_re.search("ass")
assert ass_re.search("Ass")
assert ass_re.search("aSS")
assert ass_re.search("aSS")
assert ass_re.search(" ass ")
assert ass_re.search("dumb ass")
assert ass_re.search("Rejoice greatly, O daughter of Zion; shout, O daughter of Jerusalem: behold, thy King cometh unto thee: he is just, and having salvation; lowly, and riding upon an ass, and upon a colt the foal of an ass.")
assert not ass_re.search("dick")
assert not ass_re.search("pass")
assert not ass_re.search("assyria")

for bookfile in os.listdir(bibledir):
    with open(os.path.join(bibledir, bookfile), 'rb') as book:
        bookname = book.readline()
        asscounts[bookname] = 0
        line = "asdf"
        while line != "":
            line = book.readline()
            if not ass_re.search(line):
                continue
            asscounts[bookname] += 1
            niceline = line.replace("\n", "")
            niceline = niceline.replace("\r", "")
            asslines[bookname[:-2] + " " + niceline[:niceline.find(" ") - 1]] = niceline[niceline.find(" ") + 1:]


pprint(asslines)
# pprint(asscounts)
