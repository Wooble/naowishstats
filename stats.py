import csv
import collections

def main():
    with open("livelog.txt") as livelog:
        r = csv.reader(livelog, delimiter=':')
        c = collections.Counter()
        for line in r:
            if line[-1].startswith("message=wished for"):
                wish = line[-1].replace('message=wished for "', '')[0:-1]
                c[wish] += 1
    for wish in c.most_common():
        print wish
        

if __name__ == "__main__":
    main()
