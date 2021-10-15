# second solution
orig_chars = input().strip()
encoded = input().strip()

enc_map = {}
dec_map = {}

n = len(orig_chars)
i = 0
while i < n:
    o = orig_chars[i]
    e = encoded[i]
    enc_map[o] = e
    dec_map[e] = o

    i += 1

orig_text = input().strip()

encoded_orig_text = ""
for c in orig_text:
    encoded_orig_text += enc_map[c]

encoded_text = input().strip()

decoded_text = ""
for c in encoded_text:
    decoded_text += dec_map[c]

print(encoded_orig_text)
print(decoded_text)
