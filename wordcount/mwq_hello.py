import jieba, os

rootdir = "D:\\devfiles\\countfile"


def count(file):
    txt = open(file, "r", encoding="utf-8").read()
    words = jieba.lcut(txt)
    counts = {}
    for word in words:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    for i in range(15):
        word, count = items[i]
        print("{0:<10}{1:<5}".format(word, count))


filelist = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
for i in range(0, len(filelist)):
    path = os.path.join(rootdir, filelist[i])
    if os.path.isfile(path):
        print("*******" + path + "*********")
        count(path)
