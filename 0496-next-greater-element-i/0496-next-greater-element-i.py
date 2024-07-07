class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        n_next_greater={}
        stack=[]
        for num in nums2:
            while stack and stack[-1]<num:
                                                  
                n_next_greater[stack.pop()]=num
            stack.append(num)
        return[n_next_greater.get(num,-1) for num in nums1]
        
   


#coding 

        