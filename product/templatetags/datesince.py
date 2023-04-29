from django import template
from datetime import datetime, date

register = template.Library()

@register.filter
def datesince(d):
    now = date.today()
    t = now - d
    if d == now:
        return 'today'
    elif t.days == 1:
        return 'yesterday'
    elif t.days > 1 and t.days < 8:
        return f"{t.days} days"
    elif t.days > 7:
        return f"{t.days // 7} weeks" 
    

"""
{{ comment.pub_date | datesince }}

"""


# str = "idrak mp3; vahid mp4; sadiq mp5"

# def design(t):
#     if ";" in t:
#         t = t.replace(";", "\n")
#     return t 

# print(design(str)) 

@register.filter
def design(str):
    if ";" in str:
        str = str.replace(';', ' - ')
    return str


