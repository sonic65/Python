import os


print(os.path.abspath("."))
file_path = (os.path.dirname(os.path.abspath(".") + "/config.ini")
print(file_path)