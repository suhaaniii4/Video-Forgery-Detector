import gdown
import zipfile

file_id = "19LILW_YEJ3Q3HpzhB3mvk56u97JhO_oP"

url = f"https://drive.google.com/uc?id={file_id}"

gdown.download(url, "dataset.zip", quiet=False)

with zipfile.ZipFile("dataset.zip", "r") as zip_ref:
    zip_ref.extractall(".")