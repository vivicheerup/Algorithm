# dfs practice
def similarityword(word1,word2,pairs):
    if len(word1) != len(word2):
        return False

    for i in range(len(word1)):
        if word1[i] == word2[i]:
            continue
        elif word2[i] in dfscheck(pairs,word1[i],[],[]):
            continue
        else:
            return False

    return True


def dfscheck(pairs,start_word,res,visited):

    for each in pairs:
        if start_word in each and each not in visited:
            tmp = ""
            if each[0] != start_word:
                tmp = each[0]
            if each[1] != start_word:
                tmp = each[1]
            #print(tmp)
            res.append(tmp)
            visited.append(each)
            #print(res)
            dfscheck(pairs,tmp,res,visited)
    return res




