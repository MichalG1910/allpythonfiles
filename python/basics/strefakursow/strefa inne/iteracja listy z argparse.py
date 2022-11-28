import argparse
parser = argparse.ArgumentParser(description = "Szukanie według klucza")
parser.add_argument("snippet", help = "część lub całe słowo")

args = parser.parse_args()
snippet = args.snippet.lower()

words = open("d:\\python\\basics\\inne\\slowa.txt").readlines()
print([word.strip() for word in words if snippet in word.lower()])

words = open("d:\\python\\basics\\inne\\analizatekstu.txt")
wo = words.read()
z = "the"
ile = wo.count(z)
print("{0} - {1}".format(z, ile))
