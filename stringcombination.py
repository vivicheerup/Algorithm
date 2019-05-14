class Solution:
    def combination(self,str,b,m):
        stack = []
        if m == 0:
            return
        if b >=len(str):
            return
        stack.append(str[b])
        self.combination(str,b+1,m-1)
        stack.pop()
        self.combination(str,b+1,m)

    def permutation(self,nums):
        def dfs(Nums,subList):
            if len(subList) == len(Nums):
                res.append(subList[:])
            for m in Nums:
                if m in subList:
                    continue
                subList.append(m)
                dfs(Nums,subList)
                subList.remove(m)

        res = []
        sub = []
        dfs(nums,sub)
        return self.res
    A = [1,2,3,4]
    permutation(A)





