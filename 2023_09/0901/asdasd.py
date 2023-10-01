for _ in range(16):
    s = list(input())
    # print(s)
    for i in range(len(s)):
        if s[i] == '1':
            s[i] = ':carrot_help:'
        elif s[i] == '3':
            s[i] = ':cat_feed: '
        elif s[i] == '2':
            s[i] = ':happycat: '
        else:
            s[i] = ':blob_cat-dance26:'
    print(*s)