import re

file_path = './dataset/the-verdict.txt'
with open(file_path, "r",encoding='utf-8') as f:
    raw_text = f.read()
# print(raw_text[:99])
# print(len(raw_text))

words = re.split(r'([,.?_!"()\']|--|\s)',raw_text)
# 标点被识别为空格，去除空格
words =  [word.strip() for word in words if word.strip()]
# 将字符转换为set类型，并进行排序
all_words = sorted(set(words))
print(all_words[:50])
vocabulary = {token: index for index, token in enumerate(all_words)}