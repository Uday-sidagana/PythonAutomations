import re

import fitz #pyMuPdf
import PIL.Image #pillow
import io



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

#--------------------------------
pdf = fitz.open("Confidential.pdf")
counter =1
for i in range(len(pdf)):
   page = pdf[i]
   images = page.get_images
   for image in images(page):
      first_img= pdf.extract_image(image[0])
      print(first_img)
      image_data = first_img["image"]

      img = PIL.Image.open(io.BytesIO(image_data))
      extension = first_img["ext"]
      img.save(f"image{counter}.{extension}")
      
      counter +=1





      
      


