class ObjList:
    """ Класс ObjList. """
    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.__data = data

    def get_next(self):
        """ Получает значение приватного атрибута __next. """
        return self.__next

    def get_prev(self):
        """ Получает значение приватного атрибута __prev. """
        return self.__prev

    def get_data(self):
        """ Получает значение приватного атрибута __data. """
        return self.__data

    def set_next(self, obj):
        """ Устанавливает новое значение приватного атрибута __data. """
        self.__next = obj

    def set_prev(self, obj):
        """ Устанавливает новое значение приватного атрибута __data. """
        self.__prev = obj

    def set_data(self, data):
        """ Устанавливает новое значение приватного атрибута __data. """
        self.__data = data


class LinkedList:
    """ Класс, представляющий связный список. """
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        """ Добавляет новый объект obj в конец связного списка. """
        if self.head is None:
            self.head = obj
            self.tail = obj
        else:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
            self.tail = obj

    def remove_obj(self):
        """ Удаляет последний объект из связного списка. """
        if self.tail == self.head:
            self.head = None
            self.tail = None
        else:
            prev_obj = self.tail.get_prev()
            prev_obj.set_next(None)
            self.tail = prev_obj

    def get_data(self):
        """ Получает список строк свойства __data всех объектов связного списка. """
        data_list = []
        obj = self.head
        while obj:
            data_list.append(obj.get_data())
            obj = obj.get_next()
        return data_list


# Пример запуска программы
# ob1 = ObjList('data1')
# ob2 = ObjList('data2')
# ob3 = ObjList('data3')

# lst = LinkedList()

# lst.add_obj(ob1)
# lst.add_obj(ob2)
# lst.add_obj(ob3)
#
# res = lst.get_data()
# print(res)

# lst.remove_obj()
# res = lst.get_data()
# print(res)

# lst.remove_obj()
# res = lst.get_data()
# print(res)
