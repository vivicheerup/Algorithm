#V10
class Solution:
    def removedupString(self,s):
        # nlogn
        #s = sorted(s) if the input is disordered
        slist = [i for i in s]

        idx_n = 0
        for i in range(len(slist)):
            if i == len(slist)-1 or slist[i+1] != slist[i]:
                slist[idx_n] = slist[i]
                idx_n += 1
            else:
                continue


        print(''.join(str(i) for i in slist[:idx_n]))

    def StringCompression(self,s):

        b = 0
        idx_n = 0
        count = 1
        res = ""

        for i in range(len(s)):

            if i == len(s)-1 or s[i+1] != s[i]:
                res += str(count) + s[i]
                count = 1
                b = i + 1

            else:
                count = i - b + 2
        print(res)

    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        # if len(list1) > len(list2):
        #     self.findRestaurant(list2,list1)
        import sys
        restaurant = {name: i for i, name in enumerate(list1)}
        min_s = sys.maxsize
        res = []
        for j in range(len(list2)):
            if list2[j] in restaurant:

                temp_s = restaurant[list2[j]] + j

                if temp_s < min_s:
                    min_s = temp_s
                    idx = restaurant[list2[j]]
                    res = [list1[idx]]

                elif temp_s == min_s:
                    idx = restaurant[list2[j]]
                    res.append(list1[idx])

        return res

s = Solution()
a = "adheeeekee"
s.StringCompression(a)

#s.removedupString(a)


s = "aaabbcc" # 3a2b2c