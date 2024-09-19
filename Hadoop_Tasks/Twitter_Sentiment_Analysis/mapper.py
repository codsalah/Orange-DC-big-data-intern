import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split(',', 3)
    if len(fields) == 4:
        tweet_id = fields[0]
        category = fields[1]
        sentiment = fields[2]
        tweet_content = fields[3]
        
        print(f"{tweet_id}\t{sentiment}")
