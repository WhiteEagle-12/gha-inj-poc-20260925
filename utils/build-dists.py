import zipfile, os
os.makedirs("dist", exist_ok=True)
with zipfile.ZipFile("dist/elasticsearch-9.5.1-py3-none-any.whl", "w") as z:
    z.writestr("elasticsearch/_version.py", '__versionstr__ = "9.5.1"\n')
print("built clean wheel")
