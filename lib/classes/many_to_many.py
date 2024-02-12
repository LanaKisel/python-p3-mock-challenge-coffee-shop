from statistics import mean
class Coffee:
    all = []
    def __init__(self, name):
        self.name = name
        Coffee.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and not hasattr(self, "name") and len(name)>=3:
            self._name = name

        
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list({order.customer for order in self.orders()})
    
    def num_orders(self):
        coffee_ordered = [order.coffee for order in self.orders()]
        return coffee_ordered.count(self)


    def average_price(self):
        coffee_price = [order.price for order in self.orders()]
        if len(coffee_price):
            return mean(coffee_price) 
        else:
            return 0
        # for order in self.orders():
        #     total += order.price
        # average = total / self.num_orders()    
        # return average      

class Customer:
    all = []
    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name        
        
    def orders(self):
        return list({order for order in Order.all if order.customer == self})
    
    def coffees(self):
        return list({order.coffee for order in self.orders()})
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self._price = price
        Order.all.append(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer =customer    
    
    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee= coffee

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if isinstance(price, float) and not hasattr(self, "price") and 1.0 <= price.value <= 10.0:
            self._price = price   
