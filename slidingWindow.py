import collections
def longsubstringK(s,k):
    # "ecebcd" k = 2 ece output: 3
    counter = collections.defaultdict(int) # windows
    start,max_len = 0,0

    tmp_count_letter = 0

    for i,each in enumerate(s):

        counter[each] += 1


        while len(counter) > k:
            counter[s[start]] -= 1
            if counter[s[start]] == 0:
                del counter[s[start]]
            start += 1
        max_len = max(max_len, i - start + 1)
    return max_len

print(longsubstringK("ecebcd",2))
