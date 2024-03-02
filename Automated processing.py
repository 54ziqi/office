import wordcloud
import chardet
import matplotlib.pyplot as plt


# 自动检测文本文件的编码
def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']


# 创建一个 WordCloud 对象
wordcloud = wordcloud.WordCloud()

# 设置 WordCloud 对象的参数
wordcloud.width = 500
wordcloud.height = 500
wordcloud.max_words = 100
wordcloud.background_color = 'white'

# 加载字体文件（词云文字库.ttf）
font_path = 'MiSans VF.ttf'  # 请确保这是正确的路径
wordcloud.font_path = font_path  # 设置字体的路径

# 加载文本数据
file_path = 'data.txt'
encoding = detect_encoding(file_path)
with open(file_path, 'rb') as f:
    text = f.read().decode(encoding)

# 将逗号分隔的文本转换为单词列表
word_list = text.split(',')

# 将单词列表转换为字符串
text = ' '.join(word_list)

# 生成词云
wordcloud.generate(text)

# 使用 matplotlib 显示词云图片（可选，仅为了检查）
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # 不显示坐标轴
plt.show()

# 保存词云图片（如果您还没有显示它的话）
wordcloud.to_file('wordcloud.png')
