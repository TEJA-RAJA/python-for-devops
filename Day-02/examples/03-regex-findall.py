import re

text = "The quick brown fox"
pattern = r"brown"

match = re.search(pattern, text)
if match:
    print("Pattern found:", match.group())
else:
    print("Pattern not found")
