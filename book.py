book = {}
book["tom"] = {
    'name': 'tom',
    'address': '1 park street, ny',
    'phone': 123654789
}
book["bob"] = {
    'name': 'bob',
    'address': '1 green street, ny',
    'phone': 7896443
}

import json
s = json.dumps(book)
with open("c://data//book.txt", "w") as f:
    f.write(s)
