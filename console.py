import json
from random import choice

# Pick random quote from source
with open("./quotes.json") as f:
    q = json.loads(f.read())
result = choice(q)

# Define results
quote = result['Quote']
author = result['Author']
source = result['Source']

# Output quote result
print("")
if source:
	print('"' + quote + '".' + "\n- " + author + ", " + source)
elif not source:
	print('"' + quote + '".' + "\n- " + author)