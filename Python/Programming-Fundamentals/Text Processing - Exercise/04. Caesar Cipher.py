text = input()

enc_text = [chr(ord(c) + 3) for c in text]

print("".join(enc_text))
