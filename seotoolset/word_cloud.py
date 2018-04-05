from .clean_text import *
from wordcloud import WordCloud


def get_keyword_cloud():
    clean_text = get_clean_text("https://ikman.lk")
    wordcloud = WordCloud().generate(clean_text)
    # lower max_font_size
    wordcloud = WordCloud(max_font_size=40).generate(clean_text)
    image = wordcloud.to_image()
    image.show()
