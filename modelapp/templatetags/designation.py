from django import template

register = template.Library()

def desig(value, arg):
    des = value.split('&')
    if arg == 'first':
        return des[0]
    elif arg == 'second':
        return des[1]
    



register.filter('desig' , desig)