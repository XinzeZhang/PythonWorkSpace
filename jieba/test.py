# encoding=utf-8
from __future__ import print_function, unicode_literals
import sys
# sys.path.append("../")
import jieba
jieba.load_userdict("userdict.txt")
import jieba.posseg as pseg
import jieba.analyse

# jieba.add_word('石墨烯')
# jieba.add_word('凱特琳')
# jieba.del_word('自定义词')

test_sent = (
    "公司开出现金支票，从银行提取现金5000元，以用于零星开支\n"
    '以银行存款支付销售乙商品应负担的运输费87000元'

)
entry = jieba.cut(test_sent, HMM=True)
print(' '.join(entry))

print("=" * 40)

result = pseg.cut(test_sent)

for w in result:
    print(w.word, "/", w.flag, ", ", end=' ')

print("\n" + "=" * 40)

print('=' * 40)
print('3. 关键词提取')
print('-' * 40)
print(' TF-IDF')
print('-' * 40)

s = "以银行存款支付销售乙商品应负担的运输费87000元"
for x, w in jieba.analyse.extract_tags(s, withWeight=True):
    print('%s %s' % (x, w))

print('-' * 40)
print(' TextRank')
print('-' * 40)

for x, w in jieba.analyse.textrank(s, withWeight=True):
    print('%s %s' % (x, w))
