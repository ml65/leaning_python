# Домашнее задание по теме "Интроспекция"

def introspection_info(obj):
    attributes = {}
    methods = []
    for attr_name in dir(obj):
        attr = getattr(obj, attr_name)
        if (callable(attr)):
            methods.append(attr_name)
        else:
            attributes[attr_name] = type(attr)

    return {
        'type': obj.__class__.__name__,
        'attributes': attributes,
        'methods': methods,
        'module': getattr(obj,"__module__","__main__")
    }

class SomeClass:
    attr1 = 0
    attr2 = "Null"
    attr3 = False
    def __init__(self, attr1, attr2, attr3):
        self.attr1 = attr1

    def some_function(self, obj):
        print(obj.__class__.__name__)


obj_info = introspection_info(42)

print(obj_info)

some_obj = SomeClass(1,"tow", True)

obj_info = introspection_info(some_obj)

print(obj_info)