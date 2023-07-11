from pyresparser import ResumeParser

path="OmkarResume.pdf"
data = ResumeParser(path).get_extracted_data()
print(data)
