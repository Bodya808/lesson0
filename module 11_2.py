def introspection_info(obj):
    result = {
        'Тип объекта': type(obj).__name__,
        'Атрибуты объекта': dir(obj),
        'Методы объекта': [method for method in dir(type(obj)) if callable(getattr(type(obj), method))],
        'Модуль, к которому принадлежит класс объекта': obj.__class__.__module__
    }
    return result



number_info = introspection_info(42)
print(number_info)
