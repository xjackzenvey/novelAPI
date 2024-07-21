[简体中文](readme_zh.md)

>Warnning: The project can only used for learning.Don't abuse it!

## NovelAPI：extensive efficient framework for downloading novels for website
 #
#### The way to call it：
`GET 127.0.0.1:19999/novel?platform=<Plugin name>?bookurl=<book url>`
##
#### The way to launch：
* for Microsoft Windows：
`pip install -r requirements.txt`
`./start.cmd`
* for Linux：
`Not test yet.Gunicorn server is expected in the future.`

##
#### About the plugin：
It is easy to make a plugin.What you should do is to write the functions below：

* `get_every_chapter(bookurl:str) -> list[backends.book.Chapter]`
* `get_chapter_content(chapter:backends.book.Chapter) -> str`
* `writedown(text:str) -> None`

and a struct(a dict in fact)：
* `info = {}`

you can look into my plugin to see how they work.(The plugin is stored at App Folder and they'll be loaded dynamically)