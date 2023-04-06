import jieba
with open("comment.txt","r",encoding="utf-8") as f:
    text = f.read()
comment_words = jieba.lcut(text)
comment_dict = {}
for word in comment_words:
    if len(word) == 1:
        continue
    else:
        comment_dict[word] = comment_dict.get(word,0) + 1
sort_list = sorted(comment_dict.items(),key=lambda x:x[1],reverse=True)
for i in range(15):
    word,count = sort_list[i]
    print(f"{word:^10}{count:^10}")
