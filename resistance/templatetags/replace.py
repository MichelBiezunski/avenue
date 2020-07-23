# Source: https://gist.github.com/derek-schaefer/3834979

from django.template import Library, Node, Variable, VariableDoesNotExist, TemplateSyntaxError

register = Library()

def get_var(v, context):
    try:
        return v.resolve(context)
    except VariableDoesNotExist:
        return v.var

class ReplaceNode(Node):

    def __init__(self, s, old, new):
        self.s = Variable(s)
        self.old = Variable(old)
        self.new = Variable(new)

    def render(self, context):
        s = str(get_var(self.s, context))
        old = str(get_var(self.old, context))
        new = str(get_var(self.new,  context))
        return s.replace(old, new)

# @register.tag
# def replace(parser, token):
#     args = token.split_contents()[1:]
#     if len(args) != 3:
#         raise TemplateSyntaxError('%r tag requires a string, an old value and a new value' % token.contents.split()[0])
#     return ReplaceNode(*args)
