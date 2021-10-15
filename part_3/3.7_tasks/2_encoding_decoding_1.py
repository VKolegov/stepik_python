# first solution

orig_chars = input().strip()
encoded = input().strip()

orig_text = input().strip()

encoded_orig_text = ""
for c in orig_text:
    i = orig_chars.index(c)
    encoded_orig_text += encoded[i]

encoded_text = input().strip()

decoded_text = ""
for c in encoded_text:
    i = encoded.index(c)
    decoded_text += orig_chars[i]

print(encoded_orig_text)
print(decoded_text)
