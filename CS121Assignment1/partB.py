import sys

def tokenize(file):
    import re
    f = open(file, 'r')
    string = f.read()
    list = re.compile('\W').split(string.lower())
    return list

def intersect(file1, file2):
    list1 = tokenize(file1)
    list2 = tokenize(file2)
    # time complexity = BEST: O(min(len(s), len(t)) WORST: O(len(s) * len(t))
    common = list(set(list1) & set(list2))
    common.remove('')
    print(str(len(common)))

if len(sys.argv) < 2:
    print("Please specify the file")
    sys.exit(0)

intersect(sys.argv[1], sys.argv[2])







