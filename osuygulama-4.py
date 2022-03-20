import os
try:
    os.mkdir("elma")
except FileExistsError:
    print("Böyle bir dosya vardır")