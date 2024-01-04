import glob
import os
import shutil
import json
import re

try:
    os.mkdir("./processed")
except OSError:
    print("'./processed' directory already exists")

receipts = [f for f in glob.glob('./receipts/receipt-[0-9]*.json') if re.match('./receipts/receipt-[0-9]*[02468].json', f)]
subtotal = 0.0

for path in receipts:
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    destination = path.replace('receipts','processed')
    shutil.move(path, destination)
    print(f"moved '{path}' to '{destination}'")

print("Receipt subtotal: $%.2f" % subtotal)
