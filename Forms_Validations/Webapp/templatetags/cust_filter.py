from django import template
register = template.Library()

# def custchars5(value):
#     result = value[0:6]
#     return result
# register.filter('c5',custchars5)

# """user defined"""
# def custchars5(value,n):
#     result = value[0:n]
#     return result
# register.filter('cn',custchars5)

"""pre defined"""
@register.filter(name='cn')
def custchars5(value,n):
    # n = int(input("enter filter data"))
    result = value[0:n]
    return result
# register.filter('cn',custchars5)