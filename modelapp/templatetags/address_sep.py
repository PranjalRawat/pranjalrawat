from django import template

register = template.Library()

def address(value, arg):
    add = value.split(',')
    if arg == 'name':
        return add[0]
    elif arg == 'city':
        return add[1]
    elif arg == 'pincode':
        return add[2]
    elif arg == 'country':
        return add[3]
    elif arg == 'mobile':
        return add[4]
    elif arg == 'email':
        return add[5]



register.filter('address' , address)