
# Node

class Node(object):
    def __init__(self, conteined_object  =  None, next  =  None):
        self.conteined_object  =  conteined_object
        self.next  =  next


# MyQueue

class MyQueue(object):
    def __init__(self, head   =   None):
        self.head  =  Node(conteined_object  =  head, next  =  None)
        self.end_of_queue  =  self.head

    def add(self, element):
        """
        add an item to the end of the queue
        """
        if self.head.conteined_object  ==   None:
            self.head.conteined_object  =  element
        else:
            self.end_of_queue.next  =  Node(element,None)
            self.end_of_queue  =  self.end_of_queue.next


    def remove(self):
        """
        remove an item from the beginning of the queue
        """
        if self.head   ==    self.end_of_queue:
            self.head  =  Node()
            self.end_of_queue  =  self.head
        else:
            self.head  =  self.head.next


    def clear(self):
        """
        clear the queue
        """
        self.__init__()

    def to_list(self):
        """
        convert a queue to a list
        """
        result_array  =  []
        current_element  =  self.head
        while current_element.next !=   None:
            result_array.append(current_element.conteined_object)
            current_element  =  current_element.next
        if current_element.conteined_object !=  None: result_array.append(current_element.conteined_object)
        return result_array


# Country

class Country(object):
    def __init__(self, name: str, capital: str, population: int):
        self.name  =  name
        self.capital  =  capital
        self.population  =  population

    def __str__(self):
        return f"Country - {self.name}; Capital - {self.capital}; Population - {self.population}"



# Conditions

if __name__  ==   "__main__":
    int_array  =  [1,0,7,4,12,6, 10]
    Country_array  =  [
    Country('Russia', "Moscow", 12692400),
    Country('France', 'Paris', 2148000),
    Country('UK', 'London', 8982000)
    ]
    int_queue  =  MyQueue()
    Country_queue  =  MyQueue()
    for i in int_array:
        int_queue.add(i)

    for i in Country_array:
        Country_queue.add(i)

    print(int_queue.to_list())
    print([str(c) for c in Country_queue.to_list()])