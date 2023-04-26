import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help="filename of the file to be decoded")

args = parser.parse_args()

def decode_Caesar_cipher(s, n):
    alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) + n) % len(alpha)]
    print(text)


filename = args.file
opened_file = open(filename)
encoded_text = opened_file.read()
opened_file.close()

decode_Caesar_cipher(encoded_text, -13)
