from pprint import pprint


class Introspection:
    def __init__(self, value):
        self.value = value

    def my_method(self):
        return self.value


def introspection_info(obj):
    obj_type = type(obj).__name__

    obj_module = getattr(obj, '__module__', None)

    attributes = dir(obj)

    methods = [attr for attr in attributes if callable(getattr(obj, attr))]

    non_methods = [attr for attr in attributes if not callable(getattr(obj, attr))]

    info = {
        'type': obj_type,
        'attributes': non_methods,
        'methods': methods,
        'module': obj_module
    }

    return info


number_info = introspection_info(42)
pprint(number_info)

my_object = Introspection(10)

object_info = introspection_info(my_object)
pprint(object_info)
