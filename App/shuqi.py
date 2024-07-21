from backends.utils import getSoup
from backends.book import Chapter

info = {
    "framework" : "selenium",
    "browser" : "edge",
    "driver" : None
}

temp_dict = {}

def get_every_chapter(bookurl:str):
    soup = getSoup(bookurl,info['driver'],0.6)
    bookname = soup.select("span.bname")[0].text.replace("\n","")
    bookname = bookname.split(" ")[0]
    temp_dict['bookname'] = bookname
    chapters = []
    for item in soup.select("td a"):
        chapters.append(
            Chapter(
                chapter_link = 'https://shuqi.com'+item['href'],
                chapter_name = item.text.replace("\n","").replace("\r","")
            )
        )
    return chapters

def get_chapter_content(chapter:Chapter):
    soup = getSoup(chapter.chapter_link,info['driver'],0.7)
    
    #判断是否会员
    #if len(soup.select("div.js-toBuy")) != 0:
     #   return
    
    contents = ''
    for p in soup.select("p.chapter-p"):
        contents = contents + (p.text+'\n')
    contents = "\n" + chapter.chapter_name   + contents
    return contents

def writedown(chapterTitle:str,text:str):
    with open(f"./data/《{temp_dict['bookname']}》.txt","a+",encoding='utf-8') as f:
        f.write(chapterTitle+"\n")
        f.write(text+"\n\n")
        f.flush()

    