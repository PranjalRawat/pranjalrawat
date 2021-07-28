from django import template

register = template.Library()


def stars(value,arg):
    li=[]
    if arg == 'full':
        a = value//2
        for i in range(a):
            li.append(1)
        return li
    elif arg == 'half':
        if value%2!=0:
            li.append(1)
        return li
    elif arg == 'none':
        a = (10-value)//2
        for i in range(a):
            li.append(1)
        return li

register.filter('stars' , stars)
