class Item:
    
    def __init__(self, name, price, category):
        self._name = name
        self._category = category
        if price <= 0:
            raise ValueError(f"Invalid value for price, got {price}")
        self._price = price
    
    @property
    def name(self):
        return self._name
        
    @property
    def price(self):
        return self._price
        
    @property
    def category(self):
        return self._category
    
    def __str__(self):
        return f'{self._name}@{self._price}-{self._category}'

class Query:
    
    def __init__(self, field, operation, value):
        operation_list = ['IN', 'EQ', 'GT', 'GTE','LT', 'LTE','STARTS_WITH', 'ENDS_WITH','CONTAINS']
        self._field = field
        self._value = value
           
        if  operation not in operation_list:
            raise ValueError(f'Invalid value for operation, got {operation}')
        
        self._operation = operation
            
    @property    
    def field(self):
        return self._field
        
    @property    
    def operation(self):
        return self._operation
        
    @property    
    def value(self):
        return self._value
        
    def __str__(self):
        return f'{self._field} {self._operation} {self._value}'
        
class Store:
    
    def __init__(self):
        self.items = []
        
    def __str__(self):
        if len(self.items) != 0:
            return '\n'.join(map(str, self.items))
        else:
            return 'No items'
            
    def add_item(self, item):
        self.items.append(item)
    
    def count(self):
        return len(self.items)
    
    def filter(self, query):
        filter_items = Store()
        
        for item in self.items:
            value = getattr(item, query.field)
            
            if query.operation == "EQ" and value == query.value:
                filter_items.add_item(item)
                
            elif query.operation == "GT" and value > query.value:
                filter_items.add_item(item)
                
            elif query.operation == "GTE" and value >= query.value:
                filter_items.add_item(item)
                
            elif query.operation == "LT" and value < query.value:
                filter_items.add_item(item)
            
            elif query.operation == "LTE" and value <= query.value:
                filter_items.add_item(item)
                
            elif query.operation == "STARTS_WITH" and value.startswith(query.value):
                filter_items.add_item(item)
                
            elif query.operation == "ENDS_WITH" and value.endswith(query.value):
                filter_items.add_item(item)
                
            elif query.operation == "CONTAINS" and value.__contains__(query.value):
                filter_items.add_item(item)
                
            elif query.operation == "IN" and value in query.value:
                filter_items.add_item(item)
        
        return filter_items
        
    def exclude(self, query):
        excluded_filtered_items = Store()
        included_filtered_items = self.filter(query)
        
        for i in self.items:
            if i not in included_filtered_items.items:
                excluded_filtered_items.add_item(i)
        return excluded_filtered_items