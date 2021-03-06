# coding=utf-8
'''
Created on 2017å¹?9æ?19æ?

@author: Administrator
'''


def _combinators(_handle, items, n):
    ''' æ½åä¸åç»åçé?ç¨ç»æ'''
    if n == 0:
        yield [ ]
    else:
        for i, item in enumerate(items):
            this_one = [item]
            for cc in _combinators(_handle, _handle(items, i), n - 1):
                yield this_one + cc


def permutations(items, n):
    '''åå¾nä¸ªä¸åçé¡¹ï¼ é¡ºåºæ¯ææä¹ç?'''

    def skipIthItem(items, i):
        return items[:i] + items[i + 1:]

    return _combinators(skipIthItem, items, n)


def uniqueCombinations(items, n):
    '''åå¾nä¸ªä¸åçé¡¹ï¼é¡ºåºæ å³'''

    def afterIthItem(items, i):
        return items[i + 1:]

    return _combinators(afterIthItem, items, n)


def selections(items, n):
    '''åå¾né¡¹ï¼ä¸ä¸å®è¦ä¸åï¼ï¼é¡ºåºæ¯ææä¹ç?'''

    def keepAllItems(items, i):
        return items

    return _combinators(keepAllItems, items, n)


def selections_unordered(items, n):
    '''åå¾né¡¹ï¼ä¸ä¸å®è¦ä¸åï¼ï¼é¡ºåºæ¯æ æä¹ç?'''

    def afterAndIncludeIthItem(items, i):
        return items[i:]

    return _combinators(afterAndIncludeIthItem, items, n)


if __name__ == '__main__':
    print "Permutations of String"
    print map(''.join, permutations('abc', 3))
# è¾åºï¼? ['bar', 'bra', 'abr', 'arb', 'rba', 'rab']

    print "Unique Combinations of 2 letters from String"
    print map(''.join, uniqueCombinations('abc', 2))
# è¾åº: ['ba', 'br', 'ar']

    print "Selections of 2 letters from String"
    print map(''.join, selections('abc', 2))
# è¾åºï¼? ['bb', 'ba', 'br', 'ab', 'aa', 'ar', 'rb', 'ra', 'rr']
    print map(''.join, selections_unordered('abc', 2))

