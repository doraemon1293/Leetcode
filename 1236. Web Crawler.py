# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
# class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """
import collections
import re
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:

        def in_same_host(a,b):
            m1 = re.match(r"^http://([\w.]+)/?.*$", a)
            m2 = re.match(r"^http://([\w.]+)/?.*$", a)
            return m1.group(1)==m2.group(1)

        visited=set()
        q=collections.deque()
        q.append(startUrl)
        visited.add(startUrl)
        ans=[]
        while q:
            start=q.popleft()
            ans.append(start)
            for url in htmlParser.getUrls(start):
                if url not in visited and in_same_host(url,start):
                    visited.add(url)
                    q.append(url)
        return ans
