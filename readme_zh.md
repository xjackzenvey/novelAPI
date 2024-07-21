>注意：本项目仅作为学习交流用途，请勿滥用！

## NovelAPI：高效的，可拓展的小说下载API框架
 #
#### 调用方式：
`GET 127.0.0.1:19999/novel?platform=插件名?bookurl=书籍地址`
##
#### 启动方式：
* 在windows下：
`pip install -r requirements.txt`
`./start.cmd`
*在linux下：
`尚未测试，预计使用gunicorn服务器启动API.`

##
#### 关于插件：
插件的编写很简单。你只需要实现以下函数：

* `get_every_chapter(bookurl:str) -> list[backends.book.Chapter]`
* `get_chapter_content(chapter:backends.book.Chapter) -> str`
* `writedown(text:str) -> None`

和一个结构：
* `info = {}`

具体可查看我写的插件(插件在App文件夹内存储，动态加载)。