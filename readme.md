>注意：本项目仅作为学习交流用途，请勿滥用！

## NovelAPI：extensive efficient framework for downloading novels for website
 #
#### The way to call it：
`GET 127.0.0.1:19999/novel?platform=插件名?bookurl=书籍地址`
##
#### The way to launch：
* for Microsoft Windows：
`pip install -r requirements.txt`
`./start.cmd`
* for Linux：
`尚未测试，预计使用gunicorn服务器启动API.`

##
#### About the plugin：
It is easy to make a plugin.What you should do is to write the functions below：

* `get_every_chapter(bookurl:str) -> list[backends.book.Chapter]`
* `get_chapter_content(chapter:backends.book.Chapter) -> str`
* `writedown(text:str) -> None`

and a struct(a dict in fact)：
* `info = {}`

you can look into my plugin to see how they work.(The plugin is stored at App Folder and they'll be loaded dynamically)