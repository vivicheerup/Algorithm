# you have a list which contains xy coordinate you can pick up stone in the condition that only the row or column also
# has stone
#  **
#  *****
#  ***
# how many stone you can pick up in total (as much as you can)
# [1,2],[2,3],[5,6],[2,5][2,4]
#
class Solution:
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        total_count = 0

        visited = []
        for each in stones:
            if each not in visited:
                cnt = self.dfsfindStoneconnected(each[0], each[1], visited, stones)
                total_count += cnt

        return total_count

    def dfsfindStoneconnected(self, x, y, visited, stones):

        visited.append([x, y])
        cn1, cn2 = 0, 0
        for each in stones:
            if each not in visited:
                if x == each[0]:
                    cn1 = 1 + self.dfsfindStoneconnected(each[0], each[1], visited, stones)

                if y == each[1]:
                    cn2 = 1 + self.dfsfindStoneconnected(each[0], each[1], visited, stones)

        return cn2 + cn1

    def unionsolution(self,stones):
        # stones is a litst of coordinate
        root = [-1]*100
        for each in stones:
            pos = each[0]


    def find(self,root,x):
        while root[x] != -1:
            x = root[x]

        return x



stones = [[275,136],[213,121],[216,275],[58,17],[103,291],[11,255],
          [120,80],[180,11],[141,197],[298,53],[262,87],[290,202],
          [297,71],[122,52],[0,271],[49,291],[234,103],[81,35],
          [292,120],[230,123],[45,180],[16,205],[49,177],[98,7],
          [159,295],[284,43],[19,67],[115,144],[55,139],[269,68],
          [95,207],[266,178],[206,154],[290,44],[282,241],[211,256],
          [150,116],[276,240],[242,35],[101,101],[94,23],[93,171],[88,67],
          [134,141],[282,10],[181,10],[59,9],[261,186],[182,84],[171,17],
          [220,171],[239,52],[202,70],[91,275],[0,135],[27,93],[114,93],[111,109],
          [274,147],[232,39],[122,176],[74,23],[192,118],[39,219],[282,226],
          [207,134],[127,205],[14,96],[140,125],[137,69],[116,47],[271,15],
          [52,112],[160,59],[60,96],[260,14],[183,258],[43,263],[58,254],[218,267],
          [262,213],[217,175],[96,9],[210,1],[176,234],[103,58],[18,98],[129,228],[254,43],
          [5,20],[74,97],[54,263],[159,117],[261,221],[163,249],[205,2],[226,137],[299,197],
          [295,59],[288,240],[187,197],[276,223],[169,19],[161,21],[166,203],[28,23],[93,95],
          [44,89],[77,133],[216,239],[288,204],[279,188],[204,255],[60,84],[247,32],[15,39],
          [31,153],[93,121],[221,164],[281,291],[56,53],[267,269],[153,11],[198,203],[56,27],
          [5,39],[217,102],[171,195],[241,250],[36,44],[176,271],[294,150],[219,20],[162,238],
          [86,20],[182,57],[168,63],[249,173],[293,116],[175,157],[89,225],[189,155],[100,19],
          [263,140],[36,88],[119,104],[185,108],[26,222],[251,171],[71,124],[29,186],[77,204],
          [20,118],[228,241],[202,281],[200,233],[129,159],[293,154],[137,36],[72,49],[85,148],
          [13,148],[295,29],[174,296],[243,40],[137,14],[278,280],[226,201],[91,277],[68,167],
          [161,228],[98,298],[27,62],[12,247],[57,278],[172,72],[159,235],[177,294],[209,170],
          [146,197],[77,197],[174,59],[66,22],[172,267],[287,99],[234,92],[72,179],[230,67],[192,58],
          [25,31],[158,23],[242,133],[221,298],[109,16],[202,79],[299,250],[11,270],[292,255],[239,37],
          [92,102],[281,74],[140,2],[146,173],[235,153],[62,224],[299,59],[89,6],[195,254],[125,97],
          [142,129],[26,202],[248,77],[125,251],[239,112],[30,280],[132,171],[185,74],[275,104],[192,27],
          [165,135],[240,5],[285,104],[117,98],[7,173],[167,142],[133,152],[123,173],
          [120,25],[48,80],[113,87],[36,31],[111,283],[165,37],[193,170],[100,243],[196,174],
          [44,214],[96,241],[90,30],[139,20],[128,31],[68,127],[79,241],[247,88],[264,4],
          [163,121],[120,221],[75,66],[241,267],[149,61],[93,11],[60,271],[100,195],[286,254],
          [113,237],[73,193],[37,133],[173,278],[257,184],[137,33],[270,6],[162,78],[190,264],
          [98,138],[156,85],[250,255],[175,114],[230,81],[250,229],[103,234],[257,90],[131,158],
          [43,288],[142,44],[273,278],[178,291],[22,0],[99,248],[127,75],[20,258],[290,117],
          [99,267],[119,212],[137,286],[149,152],[208,143],[121,8],[122,189],[164,137],[40,121],
          [200,46],[106,286],[233,36],[77,250],[283,271],[49,128],[233,42],[207,285],[280,216],
          [46,34],[134,209],[199,66],[43,144],[153,61],[273,51],[101,106],[93,29],[128,57],[184,198],
          [142,89],[254,183],[24,122],[128,198],[265,255],[298,87],[0,227],[135,238],[257,279],[71,268],
          [208,291],[18,68],[130,119],[211,249],[269,114],[212,166],[0,63],[74,26],[234,247],[20,50],
          [91,258],[270,106],[115,19],[80,223],[245,36],[221,216],[37,122],[148,271],[85,33],[138,201],
          [91,32],[113,115],[94,47],[9,1],[88,295],[278,134],[213,93],[104,62],[276,60],[147,234],
          [99,49],[175,144],[229,296],[133,14],[108,20],[39,239],[249,146],[198,188],[290,53],[288,45],
          [137,145],[102,26],[9,185],[271,250],[283,64],[70,232],[124,253],[94,169],[257,132],[180,128],
          [285,246],[207,92],[246,253],[106,29],[148,14],[256,129],[280,190],[201,91],[179,83],[288,198],
          [19,71],[26,22],[149,285],[250,63],[245,265],[126,159],[220,192],[211,288],[93,66],[24,130],
          [259,184],[86,87],[190,227],[213,98],[218,149],[297,279],[5,118],[25,206],[224,223],[40,198],
          [8,276],[24,117],[228,198],[262,124],[101,172],[153,70],[104,286],[27,266],[178,70],[180,211],
          [72,27],[145,187],[39,296],[193,233],[17,274],[165,63],[80,97],[25,173],[94,113],[104,208],[292,160],
          [15,76],[161,18],[36,199],[193,227],[181,0],[259,109],[280,230],[145,128],[93,53],[81,152],[265,100],
          [134,27],[58,115],[44,135],[4,235],[203,208],[182,194],[289,217],[167,238],[14,269],[131,299],
          [231,196],[149,265],[250,43],[125,3],[161,235],[264,164],[161,98],[71,110],[194,270],[155,20],
          [138,100],[99,97],[7,24],[13,69],[244,224],[24,67],[131,270],[148,146],[151,167],[124,222],
          [236,77],[285,21],[208,149],[123,30],[185,296],[152,106],[19,179],[52,183],[65,153],[130,255],
          [172,58],[119,278],[191,165],[245,296],[1,47],[269,166],[134,217],[102,24],[100,120],[216,257],
          [55,59],[194,229],[181,18],[208,231],[1,137],[145,114],[256,205],[140,71],[292,17],[185,57],
          [173,132],[256,10],[221,141],[266,267],[283,2],[63,6],[37,31],[48,293],[250,61],[7,205],[239,138],
          [65,146],[179,194],[116,42],[93,239],[254,33],[122,212],[119,129],[242,91],[101,109],[129,132],
          [100,77],[253,247],[52,113],[118,289],[228,166],[260,285],[11,7],[117,180],[114,278],[172,288],
          [106,167],[268,154],[8,233],[193,179],[219,261],[133,289],[186,13],[161,254],[85,88],[127,129],
          [225,181],[79,22],[1,57],[176,164],[71,204],[131,114],[93,130],[109,176],[228,152],[286,54],[97,94],
          [199,150],[35,37],[74,72],[115,211],[102,70],[256,24],[227,286],[111,171],[178,275],[292,299],
          [200,248],[248,170],[208,58],[93,199],[8,77],[224,282],[120,135],[96,278],[40,85],[24,185],[17,247],
          [46,41],[210,62],[167,14],[207,151],[294,189],[90,285],[88,89],[202,225],[57,3],[200,171],[32,290],
          [35,239],[186,53],[125,274],[230,157],[272,225],[264,222],[148,105],[182,253],[173,31],[270,232],
          [181,280],[86,247],[161,121],[105,111],[134,6],[209,158],[141,16],[67,8],[190,252],[132,279],[37,207],
          [109,200],[268,48],[143,46],[282,230],[32,147],[187,139],[153,208],[110,144],[185,63],[96,57],[230,148],
          [85,236],[171,141],[138,150],[261,166],[219,210],[55,157],[93,74],[232,42],[80,193],[118,114],[249,129],
          [297,37],[224,253],[213,249],[264,291],[125,13],[178,14],[213,227],[288,262],[175,61],[66,185],
          [85,18],[74,41],[28,216],[223,125],[238,275],[62,290],[255,112],[152,122],[168,52],[136,297],
          [139,129],[193,92],[92,103],[239,222],[23,79],[44,258],[82,77],[18,39],[184,230],[245,290],
          [0,274],[169,253],[79,264],[106,97],[133,118],[267,178],[146,94],[174,200],[83,168],[247,243],
          [171,106],[242,163],[141,228],[103,120],[148,114],[270,32],[42,90],[174,285],[11,59],[112,38],
          [180,204],[184,135],[196,175],[84,212],[198,191],[47,219],[269,70],[293,217],[39,273],[292,34],
          [113,176],[68,276],[230,46],[163,120],[81,243],[266,7],[23,168],[154,41],[230,185],[288,266],
          [175,41],[208,115],[113,283],[134,143],[31,95],[293,158],[70,234],[71,47],[95,171],[270,196],
          [166,193],[237,197],[191,219],[101,53],[75,14],[191,62],[18,244],[178,33],[174,107],[73,256],
          [138,88],[49,96],[96,148],[220,118],[172,197],[69,153],[21,255],[1,92],[89,271],[97,64],[290,273],
          [92,56],[127,297],[266,262],[92,175],[293,122],[114,124],[26,16],[41,88],[20,206],[83,232],[103,213],
          [83,71],[153,147],[142,275],[152,184],[177,40],[61,89],[256,156],[285,35],[70,229],[99,121],[5,48],
          [104,117],[172,262],[40,266],[297,94],[269,48],[119,172],[170,0],[33,129],[7,36],[87,30],[278,278],
          [12,45],[141,38],[46,211],[100,12],[249,257],[194,217],[209,23],[228,190],[46,157]]
s = Solution()
print(s.removeStones(stones))