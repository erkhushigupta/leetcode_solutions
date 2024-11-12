class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        ret=[0]*len(queries)
        items.sort()
        for i in range(1,len(items)):
            items[i][1]=max(items[i-1][1],items[i][1])
        lst=[(queries[i],i) for i in range(len(queries))]
        lst.sort()
        idx=0
        last=0
        for q,i in lst:
            while idx<len(items) and items[idx][0]<=q:
                last=items[idx][1]
                idx+=1
            ret[i]=last
        return ret