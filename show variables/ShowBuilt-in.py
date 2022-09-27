import builtins
import pprint

print('Show global variables:')
pprint.pprint(globals())
print('Show local variables:')
pprint.pprint(locals())

print('Show built-in variables:')
pprint.pprint(dir(builtins))
