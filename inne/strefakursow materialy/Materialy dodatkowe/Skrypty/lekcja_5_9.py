
import argparse

parser = argparse.ArgumentParser(description='Szukanie wedlug klucza')
parser.add_argument('snippet', help='czesc lub cale slowo')

args = parser.parse_args()
snippet = args.snippet.lower()

words = open('/usr/share/dict/polish').readlines()
print([word.strip() for word in words if snippet in word.lower()])
