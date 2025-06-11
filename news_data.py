from newspaper import Article

def get_news_article(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.title + " " + article.text

news_text_us = get_news_article("https://www.thetimes.co.uk/article/india-constituency-reform-babies-seats-south-f3ck8d8l0")
print("BBC News (US):")
print(news_text_us[:500]) 
