from flask import render_template
from . import main
from ..requests import get_news

# @main.route("/")
# def index():
#     # title = "welcome home"
   
#     return render_template("index.html")
    
# @main.route("/category/<string:category>")  
# def categories(category):
#     mydata = get_news(category)

#     return render_template("categories.html",data=mydata)


