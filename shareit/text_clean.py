# -*- coding: utf-8 -*-
"""
@author: Abrams
"""
import logging,re
import sys
import nltk


class Cleaner():
    
    def __init__(self):
        URL = r'https?://[-_.?&~;+=/#0-9A-Za-z]{1,2076}'
        MAIL = r'[-_.0-9A-Za-z]{1,64}@[-_0-9A-Za-z]{1,255}[-_.0-9A-Za-z]{1,255}'
        DATE_1 = r'\d{4}[-/]\d{2}[-/]\d{2}'
        DATE_2 = r'\d{2}[-/]\d{2}[-/]\d{4}'
        DATE_3 = r'\d{2}[-/]\d{2}'
        special_1 = r'-+'
        special_2 = r'_+'
        punctuation = r"""#$%&!"'()*+,./:;<=>?@[\]^><`{|}~·…▬►●═▮◄■▶。，—"""
        PUN=r'[{}]+'.format(punctuation)
        # PUN2='\W+'
        self.methods=[URL,MAIL,DATE_1,DATE_2,DATE_3,special_1,special_2,PUN]
        self.stop_words=set()

    def _filter_emoj(self,text,punctuation_flag=False):
        try:
            if (sys.version_info < (3, 0)):
                text = text.decode('utf8')
        except:
            logging.error('text.decode utf8 error {}'.format(text))
        try:
            # Wide UCS-4 build
            emjoj_re = re.compile(u'['
                                  u'\U0001F300-\U0001F64F'
                                  u'\U0001F680-\U0001F6FF'
                                  u'\u2600-\u2B55'
                                  u'\u23cf'
                                  u'\u23e9'
                                  u'\u231a'
                                  u'\u3030'
                                  u'\ufe0f'
                                  u"\U0001F600-\U0001F64F"  # emoticons
                                  u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                  u'\U00010000-\U0010ffff'
                                  u'\U0001F1E0-\U0001F1FF'  # flags (iOS)
                                  u'\U00002702-\U000027B0]+',
                                  re.UNICODE)
        except:
            # print(e)
            # # Narrow UCS-2 build
            emjoj_re = re.compile(u'('
                                  u'\ud83c[\udf00-\udfff]|'
                                  u'\ud83d[\udc00-\ude4f]|'
                                  u'\uD83D[\uDE80-\uDEFF]|'
                                  u"(\ud83d[\ude00-\ude4f])|"  # emoticon
                                  u'[\u2600-\u2B55]|'
                                  u'[\u23cf]|'
                                  u'[\u1f918]|'
                                  u'[\u1f004]|'
                                  u'[\u23e9]|'
                                  u'[\u231a]|'
                                  u'[\u3030]|'
                                  u'[\ufe0f]|'
                                  u'\uD83D[\uDE00-\uDE4F]|'
                                  u'\uD83C[\uDDE0-\uDDFF]|'
                                  u'[\u2702-\u27B0]|'
                                  u'\uD83D[\uDC00-\uDDFF])+',
                                  re.UNICODE)
        # texts = str(emjoj_re.sub(' ', text))
        # texts = ' '.join([t for t in texts.split(' ') if t != ' ' and t != ''])
        try:
            if punctuation_flag:
                texts = str(emjoj_re.sub(',', text))
            else:
                texts = str(emjoj_re.sub(' ', text))
            texts = ' '.join([t for t in texts.split(' ') if t != ' ' and t != ''])
            # print(texts)
        except:
            # print(e)
            # print(text)
            return text
        
        # print(texts)
        return texts  # 替换字符串中的Emoji
    

    def return_clean_text_nrsw(self,line):
        line=self._filter_emoj(line.strip().lower(),punctuation_flag=False)
        line=line.replace('\n',' ').replace('\r',' ').replace('\t',' ')
        methods=self.methods
        for method in methods:
            line=re.sub(method,' ',line)
        line=nltk.word_tokenize(line)
        res=[]
        for token in line:
            if token.isdigit() or len(token)==1:
                continue
            res.append(token)
        return ' '.join(res)


    def return_text_sp(self,line):
        line=self._filter_emoj(line.strip().lower(),punctuation_flag=True)
        line=line.replace('\n',' ').replace('\r',' ').replace('\t',' ')
        methods=self.methods[:-3]
        for method in methods:
            line=re.sub(method,' ',line)
        line=nltk.word_tokenize(line)
        res=[]
        for token in line:
            if token.isdigit() or len(token)==1 or token in self.stop_words:
                continue
            res.append(token)
        return ' '.join(res)


