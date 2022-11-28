import random
import json

count = 10
words = [word.strip() for word in open('/usr/share/dict/polish').readlines()]

for id in range(count):
    amount = random.uniform(1.0, 1500)
    content = {
            'topic': random.choice(words),
            'value': "%.2f" % amount
            }
    with open(f'./receipts/receipt-{id}.json','w') as f:
        json.dump(content, f)
