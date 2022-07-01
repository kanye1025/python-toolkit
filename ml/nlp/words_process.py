import  jieba

def cut_with_stop_words(sent,stop_words):
    ret = []
    for w in jieba.cut(sent):
        if w not in stop_words:
            ret.append(w)
    return ret