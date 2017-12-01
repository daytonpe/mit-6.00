from string import *

# this is a code file that you can use as a template for submitting your
# solutions


# these are some example strings for use in testing your code

#  target strings

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'

### PROBLEM 1
def countSubStringMatch(target,key):
    # need edge case error states
    i = 0
    for x in  range(0,len(target)):
        if key == target[x:x+len(key)]:
            i = i+1
    return i
# print(countSubStringMatch(target1, 'a'))

def countSubStringMatchRecursive (target, key):
    # need edge case error states
    if len(target)<len(key):
        return 0;
    
    i = 0

    if key == target[0:len(key)]:
        i = i + 1
    newtarget = target[1:len(target)]
    
    return i + countSubStringMatchRecursive(newtarget, key)
# print(countSubStringMatchRecursive(target1, 'a'))



### PROBLEM 2
def subStringMatchExact(target, key):
    # need edge case error states
    arr = ()
    for x in  range(0,len(target)):
        if key == target[x:x+len(key)]:
            # arr.append(x)
            arr = arr + (x, )
    return arr
# print(subStringMatchExact("atgacatgcacaagtatgcat","atgc"))



### PROBLEM 3
### constrainedMatchPair([5, 15],[6, 13, 1], 40)
def constrainedMatchPair(firstMatch,secondMatch,length):
    # print("length: " + str(length))
    arr = ()

    for n in firstMatch:
        for k in secondMatch:
            if (n+length+1 == k):
                # print(n+length+1)
                arr = arr + (k,) #why did they want us to use a tuple not a list?
    return arr


### the following procedure you will use in Problem 3
def subStringMatchOneSub(target,key):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        # print('breaking key',key,'into',key1,key2)
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
        # print('match1',match1)
        # print('match2',match2)
        # print('possible matches for',key1,key2,'start at',filtered)
        # print()
    return allAnswers

        
# print(subStringMatchOneSub("ATGC","ATGTTGACATGCA"))
#subStringMatchOneSub("ATGC",012345678901234")

### PROBLEM 4
def subStringMatchExactlyOneSub(target,key):
    oneSubTuple = subStringMatchOneSub(target,key)
    exactTuple  = subStringMatchExact(target, key)
    print(oneSubTuple)
    print(exactTuple)
    exclusiveOneTuple = ()

    for i in oneSubTuple:
        if i in exactTuple:
            continue
        else:
            exclusiveOneTuple = exclusiveOneTuple + (i, )

    return exclusiveOneTuple






# print(subStringMatchExactlyOneSub("atgacatgatgtcacaatatgcatgcatcatgcgatgccgtctatcgctcgtacgctacgctagcatcgaccagtatgcatgc","atgc"))
            



