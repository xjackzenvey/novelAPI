from bs4 import BeautifulSoup
from backends.utils import getHtml
from backends.book import Chapter

info = {
    "framework" : "selenium",
    "browser" : "edge",
    "driver" : None
}

temp_dict = {}

def get_every_chapter(bookurl : str):
    html = getHtml(bookurl,info['driver'],0.6)
    soup = BeautifulSoup(html,features='lxml')
    chapters = []
    temp_dict['bookname'] = soup.select("h1")[0].text
    for chap in soup.select("a.chapter-name"):
        chapters.append(Chapter(
            chapter_link = "https://"+chap['href'],
            chapter_name = chap.text
        ))
    return chapters


def get_chapter_content(chapter:Chapter):
    chapter_url = chapter.chapter_link
    html = getHtml(chapter_url,info["driver"],0.6)
    soup = BeautifulSoup(html,features='lxml')
    chapter_content = ''
    for p in soup.select("main p"):
        p_content = p.text.replace("\n","")
        chapter_content += (p_content+"\n")
    return chapter_content


def writedown(chapterTitle:str,text:str):
    with open(f"./data/《{temp_dict['bookname']}》.txt","a+",encoding='utf-8') as f:
        f.write(chapterTitle+"\n")
        f.write(text+"\n\n")
        f.flush()