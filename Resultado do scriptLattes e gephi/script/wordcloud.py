import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from wordcloud import WordCloud, STOPWORDS


def createCloud(separated_titles):
        for i, data in enumerate(separated_titles):
            stopwords = STOPWORDS.union({"RT"})
            text = " ".join([j.text for j in data])
            wordcloud = WordCloud( background_color='white', stopwords=stopwords, max_words=200, max_font_size=40)
            wordcloud.generate(text)
            fig = plt.figure(1)
            plt.imshow(wordcloud)
            plt.axis('off')
            fig.savefig("wordcloud/wordcloud{}.png".format(i), dpi=900)
