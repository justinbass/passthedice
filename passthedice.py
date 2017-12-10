#!/usr/bin/python

from argparse import ArgumentParser
from math import ceil, log
from random import randint

def crange(a,b):
    """Character range, inclusive from chr(a) to chr(b)"""
    return ''.join([chr(i) for i in xrange(a,b+1)])

def without(s, w):
    """Remove all in str w from string s"""
    l = list(s)
    for i in w:
        l.remove(i)
    return "".join(l)

def listToNum(l, base):
    """Convert list of numbers into a number with base 'base'"""
    num = 0
    for i,val in enumerate(l):
        num += val * (base ** i)
    return num

def numToList(n, base, length):
    """Convert number into a list of numbers, length l, base 'base'"""
    l = list()
    for i in xrange(length):
        l.append(n % base)
        n /= base
    return l

r09 = crange(48,57)
raz = crange(97,122)
rAF = crange(65,70)
rAZ = crange(65,90)

Currencies = {
    'bitcoin': (r09 + rAF, 64),
    'ethereum': (r09 + raz, 64),
    'litecoin': (r09 + rAF, 64),
    'iota': (rAZ + '9', 81),
    'hex': (r09 + rAF, 64)}

parser = ArgumentParser(description=
    'Turn dice rolls into cryptocurrency private keys')

parser.add_argument('-c', '--currency', default='hex',
    choices = Currencies.keys(),
    help='Cryptocurrency to generate for')
parser.add_argument('-d', '--diceMax', type=int, default=6,
    help='Maximum number of a given dice roll')
parser.add_argument('-m', '--diceMin', type=int, default=1,
    help='Minimum number of a given dice roll')
parser.add_argument('-r', '--random', action='store_true',
    help='Generate random numbers rather than inputting them.')

args = parser.parse_args()

if args.diceMin < 0:
    print "Minimum dice roll must be greater than 0"

if args.diceMax <= args.diceMin:
    print "Maximum dice roll must be larger than minimum dice roll"

currencyMapping = Currencies[args.currency][0]
outLen = Currencies[args.currency][1]

inMin = args.diceMin
inBase = args.diceMax

inMax = inBase - inMin + 1
outBase = len(currencyMapping)

inLen = int(ceil(log(outBase ** outLen, inBase)))

inputRolls = list()

if args.random:
    inputRolls = [int(randint(inMin, inMax)) for i in xrange(inLen)]
else:
    print 'Please enter in dice-rolls between %d and %d' % (inMin, inMax)

while len(inputRolls) < inLen:
    rollsRemain = inLen - len(inputRolls)
    print 'Need %d more rolls' % rollsRemain
    s = raw_input()
    nums = map(int, s.split())
    validNums = [i for i in nums if i >= inMin and i <= inMax]

    invalidNums = [str(i) for i in nums if i < inMin or i > inMax]
    if invalidNums:
        print 'Invalid numbers, ignoring: ' + ' '.join(invalidNums)

    inputRolls.extend(validNums)

intermediate = listToNum(inputRolls, inBase)
outList = numToList(intermediate, outBase, outLen)

outVals = ''.join([currencyMapping[i-inMin] for i in outList])

print "Private key: " + outVals
