# coding=utf-8
'''
Created on 2017�?9�?19�?

@author: Administrator
'''


def _combinators(_handle, items, n):
    ''' 抽取下列组合的�?�用结构'''
    if n == 0:
        yield [ ]
    else:
        for i, item in enumerate(items):
            this_one = [item]
            for cc in _combinators(_handle, _handle(items, i), n - 1):
                yield this_one + cc


def permutations(items, n):
    '''取得n个不同的项， 顺序是有意义�?'''

    def skipIthItem(items, i):
        return items[:i] + items[i + 1:]

    return _combinators(skipIthItem, items, n)


def uniqueCombinations(items, n):
    '''取得n个不同的项，顺序无关'''

    def afterIthItem(items, i):
        return items[i + 1:]

    return _combinators(afterIthItem, items, n)


def selections(items, n):
    '''取得n项（不一定要不同），顺序是有意义�?'''

    def keepAllItems(items, i):
        return items

    return _combinators(keepAllItems, items, n)


def selections_unordered(items, n):
    '''取得n项（不一定要不同），顺序是无意义�?'''

    def afterAndIncludeIthItem(items, i):
        return items[i:]

    return _combinators(afterAndIncludeIthItem, items, n)


if __name__ == '__main__':
    print "Permutations of String"
    print map(''.join, permutations('abc', 3))
# 输出�? ['bar', 'bra', 'abr', 'arb', 'rba', 'rab']

    print "Unique Combinations of 2 letters from String"
    print map(''.join, uniqueCombinations('abc', 2))
# 输出: ['ba', 'br', 'ar']

    print "Selections of 2 letters from String"
    print map(''.join, selections('abc', 2))
# 输出�? ['bb', 'ba', 'br', 'ab', 'aa', 'ar', 'rb', 'ra', 'rr']
    print map(''.join, selections_unordered('abc', 2))

