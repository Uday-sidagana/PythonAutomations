import re

from pdfminer.high_level import extract_text, extract_pages

text = extract_text("Confidential.pdf")


pattern = re.compile(r"(?i)\bP\w*\b")
pattern2= re.compile(r"[a-zA-Z]+,{1}\s{1}")
matches = pattern.findall(text)
matches2 = pattern2.findall(text)

#To only get words from pattern2 and remove "," and space
for i in matches2:
   print(i[:-2])

'''print(matches)
print(matches2)
'''