import re

number_barcodes = int(input())
pattern = r"(^|(?<=\s))@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+($|(?=\s))"
for barcode in range(number_barcodes):
    curr_barcode = input()
    match = re.findall(pattern, curr_barcode)
    if match:
        product_group = ''.join(re.findall("\\d+", curr_barcode))
        if not product_group:
            product_group = "00"
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")
