from pdf2image import convert_from_path

pages = convert_from_path(r'C:\Users\Sushil\Documents\Study\Python\SampleFiles\BasePdf.pdf',500,poppler_path=r'C:\Users\Sushil\Documents\Study\Python\AdditionalLib\Release-23.01.0-0\poppler-23.01.0\Library\bin')
for page in pages:
    page.save(r"C:\Users\Sushil\Documents\Study\Python\SampleFiles\BaseImg.jpg", "JPEG")
    break