from flask import Flask,request,make_response
from backends.utils import setupSelenium
from importlib import import_module      #dynamicall import novel plugins

app = Flask(__name__,static_folder="./data",static_url_path="/static")

@app.route("/novel")
def downloadNovel():
    _platform = request.args.get("platform")
    bookurl = request.args.get("bookurl")

    #check the arguments
    #if the arguments is illegal,return the http-status 400 and the error message below.
    if _platform == None or bookurl == None:
        return make_response({
            "code" : -1,
            "errmsg" : "illegal arguments."
        },400)
    
    #if we cannot import the plugin,we return 404.
    try:
        plugin = import_module("App."+_platform)
    except Exception as e:
        return make_response({
            "code" : -1,
            "errmsg" : "not support the platform"
        },404)
    
    '''
      #there are several steps to spider a novel.
      #first,get the information of each chapter
      #then,get the content of a chapter according to the link.
            in the case we could write them to a file using the mode "a+"
    '''
    try:
        if plugin.info['framework'] == 'selenium':
            plugin.info['driver'] = setupSelenium(
                browser = plugin.info['browser'],
                driver_path = "./driver.exe"                        #the browserDriver's path
            )

    except Exception as e:
        return make_response({
            "code" : -2,
            "errmsg" : "initialize the plugin error: "+str(e)
        },500)
    

    #now Let's go for it!

    '''
      #first we should call the function "get_every_chapter" which is expected to:
            ACCEPT the argument "bookurl:str"
            RETURN a list[backends.book.chapter]
    '''
    try:
        chapters = plugin.get_every_chapter(bookurl)
    except Exception as e:
        return make_response({
            "code" : -3,
            "errmsg" : "fail to spider chapters: " + str(e) 
        },500)
    
    '''
      #then it comes to step into "get_chapter_content". It should:
            ACCEPT the argument "chapter:backend.book.chapter"
            RETURN a single string "chapterContent"

      #Never to forget that you should write a function named "writedown" to keep the texts.It will:
            ACCEPT the argument chapter_tile:str,text:str
            RETURN none
        :::to write yourself's data,create a temp dict in your plugin.
    '''
    try:
        for chap in chapters:
            _content = plugin.get_chapter_content(chap)
            plugin.writedown(chap.chapter_name,_content)

    except Exception as e:
        return make_response({
            "code" : -3,
            "errmsg" : "fail to spider the chapter contents: "+str(e)
        },500)
    

    return {
        "code" : 0,
        "errmsg" : ""
    }