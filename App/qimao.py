from backends.book import Chapter
import requests
from bs4 import BeautifulSoup
import json

info = {
    "framework" : None
}

temp_dict = {}

headers = {
    'referer' : 'https://www.qimao.com/',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
    #'Cookie' : 'Hm_lvt_1b6d0fc94c391c78c2fbeda715896432=1720423642; HMACCOUNT=F46C1CE6CF3C029C; sajssdk_2015_cross_new_user=1; _csrf-frontend=f136e650783ca09b3115a9cc897aa8c853c88145a85e9030b89193baf2e7396ea%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%22Ncmk5PPlEf8P2SGKk0htTyM5Wq54u8Jx%22%3B%7D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22190913d754f9fd-059ea82365c4954-4c657b58-2073600-190913d7550cab%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkwOTEzZDc1NGY5ZmQtMDU5ZWE4MjM2NWM0OTU0LTRjNjU3YjU4LTIwNzM2MDAtMTkwOTEzZDc1NTBjYWIifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%22190913d754f9fd-059ea82365c4954-4c657b58-2073600-190913d7550cab%22%7D; acw_tc=76b20fe717204316162197635e7656a088d5a32f1d33f8170cc3f07dd1bdf8; Hm_lpvt_1b6d0fc94c391c78c2fbeda715896432=1720431745',
    'If-None-Natch':'',
    'If-Modified-Since':''
}

def get_book_name(index_url:str):
    soup = BeautifulSoup(requests.get(index_url).content)
    return soup.select("div.title span.txt")[0].text

def generate_bookid(bookurl:str):
    if bookurl[-1] == '/':
        return bookurl.split("/")[-2]
    else:
        return bookurl.split("/")[-1]

def get_every_chapter(bookurl:str):
    book_id = generate_bookid(bookurl)
    temp_dict['bookname'] = get_book_name(bookurl)
    get_url = f'https://www.qimao.com/api/book/chapter-list?book_id={book_id}'
    chapter_data = json.loads(requests.get(get_url).content.decode())['data']['chapters']
    chapters = []
    i=0
    for item in chapter_data:
        chapter_info = Chapter(
            chapter_link = f'https://www.qimao.com/shuku/{book_id}-{item["id"]}',
            chapter_name = item['title']
        )       
        chapters.append(chapter_info)
    return chapters

def get_chapter_content(chapter:Chapter):
    
    content = requests.get(chapter.chapter_link,headers).content
    soup = BeautifulSoup(content)
    
    print("下载："+chapter.chapter_link)
    texts = ''
    for p in soup.select('div.article p'):
        texts+=("    "+p.text+"\n")
    return texts

def writedown(chapterTitle:str,text:str):
    with open(f"./data/《{temp_dict['bookname']}》.txt","a+",encoding='utf-8') as f:
        f.write(chapterTitle+"\n")
        f.write(text+"\n\n")
        f.flush()



