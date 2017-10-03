import csv
f1 = open('tweets.txt','w')
with open("twitDB.csv") as f:
    
    content = csv.reader(f)
    for line in content:
        try:
            ex = line[3][6:-1]
            tweet = " ".join(filter(lambda x:(x[0]!='@'),ex.split()))
            f1.write(tweet+'\n')
            print(tweet)
        except:
            pass

