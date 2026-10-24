class Solution:
    def topKFrequent(self, nums, k) :
        seen = {}
        # key : value => 2 : 4
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num]  = 1
                
        # print(seen)
        # print(seen.items())
        sorted_item = sorted(seen.items() , reverse=True , key= lambda x : x[1])
        # print(sorted_item)
        
        top_k = []
        for i in range(k):
            top_k.append(sorted_item[i][0])
        # print(top_k)
        return top_k
            
            

sol = Solution()
top_k = sol.topKFrequent([1,2,2,3,3,3] , 2)
print(top_k)
        