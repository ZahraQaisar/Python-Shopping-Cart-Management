cart = []
prod = {
        "laptop": {
                    'price' : 999.99,
                    'Quantity' : 10},
        "wireless mouse": {
                    'price' : 25.49,
                    'Quantity' : 10},
        "bluetooth headphones":  {
                    'price' : 79.99,
                    'Quantity' : 10},
        "usb flash drive": {
                    'price' : 15.99,
                    'Quantity' : 10},
        "keyboard": {
                    'price' : 45.00,
                    'Quantity' : 10}}

class Cart:
    def __init__(self):
        pass
    
    def add_items(self, user_input):
        self.user_input = user_input
        if self.user_input in prod.keys():
            if prod[self.user_input]['Quantity'] > 0:
                cart.append(self.user_input)
                prod[self.user_input]['Quantity'] = prod[self.user_input]['Quantity'] - 1
            else:
                print(f'Sorry! {self.user_input} Not Available.')
        elif self.user_input == 'r' or self.user_input == 'c' or self.user_input == 'q':
            print("Proceeded!")
        else:
            print('Invalid Input!')
        print('CART:',cart)
    
    def remove_items(self, remove_prod):
        self.remove_prod = remove_prod
        if self.remove_prod in cart:
            cart.remove(self.remove_prod)
            if self.remove_prod in prod.keys():
                current = prod[self.remove_prod]['Quantity']
                updated = current + 1
                # print(updated)
                prod[remove_prod].update({'Quantity': updated})
        print('CART:', cart)  
        
    def quantity(self):
        print("Products:-")
        for keys, val in prod.items():
            print(keys, ':', prod[keys]['Quantity'])
    
    def total_price(self):
        count_lp, count_kb, count_wm, count_bh, count_fd = 0, 0, 0, 0, 0
        num = len(cart)
        
        for x in cart:
            if x == 'laptop':
                count_lp += 1
            if x == 'keyboard':
                count_kb += 1
            if x == 'wireless mouse':
                count_wm += 1
            if x == 'bluetooth headphones':
                count_bh += 1
            if x == 'usb flash drive':
                count_fd += 1
        
        total_lp = count_lp * prod['laptop']['price']
        total_kb = count_kb * prod['keyboard']['price']
        total_wm = count_wm * prod['wireless mouse']['price']
        total_bh = count_bh * prod['bluetooth headphones']['price']
        total_fd = count_fd * prod['usb flash drive']['price']

        total_cost = total_lp + total_kb + total_wm + total_fd + total_bh
        
        print("BILL:-")
        print('------------------------')
        print("Laptop(s)           ",':', count_lp, '| Price: ', total_lp)
        print("Keyboad(s)          ",':', count_kb, '| Price: ', total_kb)
        print("wireless mouse(s)   ",':', count_wm, '| Price: ', total_wm)
        print("bluetooth headphones",':', count_bh, '| Price: ', total_bh)
        print("usb flash drive(s)  ",':', count_fd, '| Price: ', total_fd)
        print('------------------------')
        print("Total Products:", num)
        print("Total cost:", total_cost)
        print("=== Thank You! ===")

print("Products:-")
for key, val in prod.items():
    print(' ',key)
    for key, val in val.items():
        print('     ',key, ':', val)

user_input = []
cont = True
while(cont):
    user_input = input('''
                => Q to Quit
                => R to Remove Product
                => C for Cost
                => P for Products(quanity)
                Enter (product to add in cart) or (Q/R/C/P):''')
    user_input = user_input.lower()
    c = Cart()
    c.add_items(user_input)

    if user_input == 'q':
        cont = False
        
    elif len(cart) > 0 and user_input == 'r':
        remove_prod = input("Product to remove:")
        remove_prod = remove_prod.lower()
        c.remove_items(remove_prod)

    elif len(cart) <= 0 and user_input == 'r':
        print("No items in the cart!")
        
    elif len(cart) > 0 and user_input == 'c':
        c.total_price()
        
    elif user_input == 'p':
        c.quantity()
        