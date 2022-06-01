id_pasw = {}
id_name = {}
id_phone = {}
id_salary = {}
id_status = {}
id_dep = {}
item_price = {}
id_item = {}
id_complain = {}
id_achievements = {}
deps = ["CLOTHING", "COSMETICS", "FURNITURE", "GARDENING", "GROCERIES", "HOUSEWARE", "TOILETRIES"]


class shop(object):
    number_of_workers = 0
    line1 = []
    line2 = []
    line3 = []


class Person(shop):
    ID = 0

    def __init__(self, status):
        self.status = status
        print("Enter {}'s full name:".format(self.status))
        self.name = input().upper()

        while True:
            pass
            try:
                print("Enter {}'s age:".format(self.status))
                self.age = int(input())
            except Exception as e:
                print("ERROR!", e)
            else:
                if self.age > 0:
                    break
                else:
                    print("ERROR!\nAge must be more than 0")

        while True:
            print("Enter {}'s phone number:".format(self.status))
            self.phone = '+998' + input("+998")
            if len(self.phone) == 13: break
            print("IMPROPER PHONE NUMBER FORMAT")


class Assistant(Person):

    def add(self):
        Person.ID += 1
        self.id = Person.ID
        print("SELECT {}'s working department:".format(self.status))
        count = 1
        for dep in deps:
            print('{}. {}'.format(count, dep))
            count += 1
        while True:
            try:
                ch = int(input("YOUR CHOICE: "))
            except Exception as e:
                print("ERROR!\n", e)
            else:
                if len(deps) >= ch:
                    self.dep = deps[ch - 1]
                    break
                else:
                    print("WRONG INPUT.\nTRY AGAIN.")
                    continue
        while True:
            try:
                print("Enter {}'s salary:".format(self.status))
                self.sal = float(input())
            except Exception as e:
                print("ERROR!", e)
            else:
                if self.sal > 0:
                    break
                else:
                    print("ERROR!\nSalary must be positive number")
        Person.number_of_workers += 1
        id_name[self.id] = self.name
        id_phone[self.id] = self.phone
        id_salary[self.id] = self.sal
        id_status[self.id] = self.status
        id_dep[self.id] = self.dep
        print("Your LOGIN and ID is:", self.id)
        self.pasw = pasw(self.id)
        id_pasw[self.id] = self.pasw
        id_achievements[self.id] = 0
        id_complain[self.id] = 0


class Cashier(Person):
    def add(self):
        Person.ID += 1
        self.id = Person.ID
        id_complain[self.id] = 0
        while True:
            try:
                print("Enter {}'s salary:".format(self.status))
                self.sal = float(input())
            except Exception as e:
                print("ERROR!\n", e)
            else:
                if self.sal > 0:
                    break
                else:
                    print("ERROR!\nSalary must be positive number")
        Person.number_of_workers += 1
        while True:
            try:
                print("Number of the line:")
                self.dep = int(input())
            except Exception as e:
                print("ERROR!\n", e)
            else:
                if self.dep >= 1 and self.dep <= 3:
                    break
                else:
                    print("ERROR!\nNumber must be between 1 and 3")
        id_name[self.id] = self.name
        id_phone[self.id] = self.phone
        id_salary[self.id] = self.sal
        id_dep[self.id] = self.dep
        id_status[self.id] = self.status
        print("Your LOGIN and ID is:", self.id)
        self.pasw = pasw(self.id)
        id_pasw[self.id] = self.pasw
        id_achievements[self.id] = 0


class Manager(Person):

    def add(self):
        while True:
            try:
                print("Enter {}'s salary:".format(self.status))
                self.sal = float(input())
            except Exception as e:
                print("ERROR!\n", e)
            else:
                if self.sal > 0:
                    break
                else:
                    print("ERROR!\nSalary must be positive number")
        Person.number_of_workers += 1
        self.dep = "WHOLE STORE"
        Person.ID += 1
        self.id = Person.ID
        self.pasw = pasw(self.id)
        id_complain[self.id] = 0
        id_pasw[self.id] = self.pasw
        id_name[self.id] = self.name
        id_phone[self.id] = self.phone
        id_salary[self.id] = self.sal
        id_dep[self.id] = self.dep
        id_status[self.id] = self.status
        id_achievements[self.id] = 'NONE'


class Customer(Person):
    def add(self):
        Person.ID += 1
        self.id = Person.ID
        print("Your LOGIN and ID is:", self.id)
        self.pasw = pasw(self.id)
        id_pasw[self.id] = self.pasw
        id_name[self.id] = self.name
        id_phone[self.id] = self.phone
        id_status[self.id] = self.status
        id_complain[self.id] = 0
        id_dep[self.id] = "NONE"
        id_salary[self.id] = 0
        id_achievements[self.id] = 0


class Item(shop):
    ID = 0

    def __init__(self):
        self.name = str(input("Insert product's name:\n")).upper()
        while True:
            try:
                self.price = int(input("Insert {}'s price:\n".format(self.name)))
            except Exception as e:
                print("ERROR!\n", e)
            else:
                if self.price > 0:
                    break
                else:
                    print("Price cannot be a negative number")
        item_price[self.name] = self.price
        Item.ID += 1
        self.id = Item.ID
        id_item[self.id] = self.name


def menu():
    print("MAIN MENU")
    print("1. Log in")
    print("2. Register")
    print("3. QUIT")
    while True:
        ch = int(input("CHOOSE YOUR OPTION: "))
        if (ch <= 3 and ch >= 1):
            break
        else:
            print("Wrong input.\nChoose between 1 and 4")
            continue
    if ch == 1:
        Auth()
    elif ch == 2:
        Register()
    elif ch == 3:
        exit(0)


def Register():
    print("WHO ARE YOU?")
    print("1. CUSTOMER")
    print("2. MANAGER")
    print("3. ASSISTANT")
    print("4. CASHIER")
    print("5. MAIN MENU")
    while True:
        try:
            ch = int(input("CHOOSE YOUR OPTION: "))
        except Exception as e:
            print("ERROR!\n", e)
        else:
            if (ch <= 5 and ch >= 1):
                break
            else:
                print("Wrong input.\nChoose between 1 and 5")
    if ch == 1:
        add_Customer()
        menu()
    elif ch == 2:
        add_Manager()
        menu()
    elif ch == 3:
        add_Assistant()
        menu()
    elif ch == 4:
        add_Cashier()
        menu()
    elif ch == 5:
        menu()


def Auth():
    print("Insert '0' in order to go back to main menu")
    print("Insert your ID number:")
    id = int(input())
    if id == 0:
        menu()
    if id in id_pasw:
        print("Insert your password:")
        pasw = input()
        if pasw == 0:
            menu()
        elif pasw == id_pasw[id]:
            if id_status[id] == "Assistant":
                Assistant_menu(id)
            elif id_status[id] == "Cashier":
                Cashier_menu(id)
            elif id_status[id] == "Customer":
                Customer_menu(id)
            elif id_status[id] == "Manager":
                Manager_menu(id)
        else:
            print("WRONG PASSWORD.")
            Auth()
    else:
        print("AUTHENTICATION FAILED.")
        print("UNKNOWN ID.")
        print("PLEASE TRY AGAIN.")
        Auth()


def pasw(id):
    print("Insert new password for your id number (" + str(id) + '):\n(Note, it cannot be "0")')
    pasw = input()
    while (pasw == "" and pasw == '0'):
        print("WRONG INPUT.\nTRY AGAIN.\n")
        pasw = input()
    return pasw


def new_pasw(id):
    print("Insert old password for your id number (" + str(id) + '):')
    p = input()
    if p == id_pasw[id]:
        pasw(id)
    if p == "" or p == '0':
        print("WRONG INPUT.\nTRY AGAIN.")
        new_pasw(id)


def Assistant_menu(worker_id):
    print("ASSISTANT MENU")
    print("1. ADD NEW PRODUCT")
    print("2. CHANGE A PRICE OF A PRODUCT")
    print("3. REMOVE PRODUCT")
    print("4. QUIT THE JOB")
    print("5. CHANGE THE PASSWORD")
    print("6. CHANGE DEPARTMENT")
    print("7. MAIN MENU")
    while True:
        try:
            ch = int(input("CHOOSE YOUR OPTION: "))
        except Exception as e:
            print("ERROR!\n", e)
        else:
            if (ch <= 7 and ch >= 1):
                break
            else:
                print("Wrong input.\nChoose between 1 and 7")
    if ch == 1:
        add_item(worker_id)
    elif ch == 2:
        change_price(worker_id)
    elif ch == 3:
        remove_item(worker_id)
    elif ch == 4:
        quit(worker_id)
    elif ch == 5:
        new_pasw(worker_id)
    elif ch == 6:
        change_dep(worker_id)
    elif ch == 7:
        menu()
    print("Do you have other operations to complete?\n1. YES\n2. NO")
    while True:
        try:
            ch = int(input("CHOOSE YOUR OPTION: "))
        except Exception as e:
            print("ERROR!\n", e)
        else:
            if (ch == 2 or ch == 1):
                break
            else:
                print("Wrong input.\nChoose 1 or 2")
    if ch == 1:
        Assistant_menu(worker_id)
    else:
        menu()


def Cashier_menu(worker_id):
    print("CASHIER MENU")
    print("1. CHANGE THE LINE")
    print("2. CHANGE THE PASSWORD")
    print("3. QUIT THE JOB")
    print("4. MAIN MENU")
    while True:
        try:
            ch = int(input("CHOOSE YOUR OPTION: "))
        except Exception as e:
            print("ERROR!\n", e)
        else:
            if (ch <= 4 and ch >= 1):
                break
            else:
                print("Wrong input.\nChoose between 1 and 4")
    if ch == 1:
        change_dep(worker_id)
    elif ch == 2:
        new_pasw(worker_id)
    elif ch == 3:
        quit(worker_id)
    elif ch == 4:
        menu()
    print("Do you have other operations to complete?\n1. YES\n2. NO")
    while True:
        try:
            ch = int(input("CHOOSE YOUR OPTION: "))
        except Exception as e:
            print("ERROR!\n", e)
        else:
            if (ch == 2 or ch == 1):
                break
            else:
                print("Wrong input.\nChoose 1 or 2")
    if ch == 1:
        Cashier_menu(worker_id)
    else:
        menu()


def Manager_menu(worker_id):
    print("MANAGER MENU")
    print("1. RAISE SALARY")
    print("2. CHANGE THE PASSWORD")
    print("3. FIRE WORKER")
    print("4. WORKERS' INFO")
    print("5. WHO IS CURRENTLY IN THE STORE")
    print("6. MAIN MENU")
    while True:
        try:
            ch = int(input("CHOOSE YOUR OPTION: "))
        except Exception as e:
            print("ERROR!\n", e)
        else:
            if (ch <= 6 and ch >= 1):
                break
            else:
                print("Wrong input.\nChoose between 1 and 6")
    if ch == 1:
        raise_salary()
    elif ch == 2:
        new_pasw(worker_id)
    elif ch == 3:
        fire_worker()
    elif ch == 4:
        workers_list()
    elif ch == 5:
        list()
    elif ch == 6:
        menu()

    print("Do you have other operations to complete?\n1. YES\n2. NO")
    while True:
        try:
            ch = int(input("CHOOSE YOUR OPTION: "))
        except Exception as e:
            print("ERROR!\n", e)
        else:
            if (ch == 2 or ch == 1):
                break
            else:
                print("Wrong input.\nChoose 1 or 2")
    if ch == 1:
        Manager_menu(worker_id)
    else:
        menu()


def Customer_menu(id):
    print("CUSTOMER MENU")
    print("1. BUY PRODUCTS")
    print("2. COMPLAIN")
    print("3. CHANGE PASSWORD")
    print("4. QUIT THE STORE")
    print("5. MAIN MENU")
    while True:
        try:
            ch = int(input("CHOOSE YOUR OPTION: "))
        except Exception as e:
            print("ERROR!\n", e)
        else:
            if (ch <= 5 and ch >= 1):
                break
            else:
                print("Wrong input.\nChoose between 1 and 5")
    if ch == 1:
        buy(id)
    elif ch == 2:
        complain(id)
    elif ch == 3:
        new_pasw(id)
    elif ch == 4:
        quit(id)
    elif ch == 5:
        menu()
    print("Do you have other operations to complete?\n1. YES\n2. NO")
    while True:
        try:
            ch = int(input("CHOOSE YOUR OPTION: "))
        except Exception as e:
            print("ERROR!\n", e)
        else:
            if (ch == 2 or ch == 1):
                break
            else:
                print("Wrong input.\nChoose 1 or 2")
    if ch == 1:
        Customer_menu(id)
    else:
        quit(id)


def raise_salary():
    workers_list()
    while True:
        id = int(input("Insert worker's ID, whose salary you want to raise:\n"))
        if id not in id_name:
            continue
        else:
            break

    while True:
        try:
            print("Insert this", id_status[id] + "'s salary raise (+x%):")
            r = int(input())
        except Exception as e:
            print("ERROR!", e)
        else:
            break

    id_salary[id] += id_salary[id] * r / 100
    print(id_status[id] + "'s salary after increase:\n", id_salary[id], sep='')


def list():
    print("-" * 57)
    print("-" * 57)
    print("||{:^6}||{:^15}||{:^28}||".format("ID", "NAME", "PHONE NUMBER"))
    for i in id_name:
        print("-" * 57)
        print("-" * 57)
        print("||{:^6}||{:^15}||{:^28}||".format(i, id_name[i], id_phone[i]))
    print("-" * 57)
    print("-" * 57)


def workers_list():
    print("-" * 124)
    print("-" * 124)
    print("||{:^6}||{:^15}||{:^28}||{:^9}||{:^15}||{:^6}||{:^15}||{:^12}||".format("ID", "NAME", "PHONE NUMBER",
                                                                                   "WORKS AS", "DEPARTMENT/LINE",
                                                                                   "SALARY", "№ OF COMPLAINTS",
                                                                                   "ACHIEVEMENTS"))
    for i in id_name:
        if id_status[i] != "Customer":
            print("-" * 124)
            print("-" * 124)
            print("||{:^6}||{:^15}||{:^28}||{:^9}||{:^15}||{:^6}||{:^15}||{:^12}||".format(i, id_name[i], id_phone[i],
                                                                                           id_status[i], id_dep[i],
                                                                                           id_salary[i], id_complain[i],
                                                                                           id_achievements[i]))
    print("-" * 124)
    print("-" * 124)


def items_list():
    print('-' * 25)
    print('-' * 25)
    print("||{:^3}||{:^9}||{:^5}||".format("ID", "PRODUCT", "PRICE"))
    for id in id_item:
        print('-' * 25)
        print('-' * 25)
        print("||{:^3}||{:^9}||{:^5}||".format(id, id_item[id], item_price[id_item[id]]))
    print('-' * 25)
    print('-' * 25)


def add_Customer():
    p1 = Customer("Customer")
    p1.add()
    print(p1.status, "was successfully added")


def add_Assistant():
    p1 = Assistant('Assistant')
    p1.add()
    print(p1.status, "was successfully added")


def add_Cashier():
    p1 = Cashier('Cashier')
    p1.add()
    print(p1.status, "was successfully added")


def add_Manager():
    p1 = Manager('Manager')
    p1.add()
    print(p1.status, "was successfully added")


def fire_worker():
    workers_list()
    while True:
        id = int(input("Insert worker's ID, who you want to fire:\n"))
        if id not in id_name:
            print("NO WORKER WITH SUCH ID.\nTRY AGAIN.")
            continue
        else:
            print(id_name[id], "with ID", id, "was successfully deleted")
            id_name.pop(id)
            id_dep.pop(id)
            id_phone.pop(id)
            id_salary.pop(id)
            id_status.pop(id)
            id_pasw.pop(id)
            id_achievements.pop(id)
            id_complain.pop(id)
            break


def complain(id):
    workers_list()
    while True:
        id = int(input("Insert worker's ID, who you want to complaint to:\n"))
        if id not in id_name and id_status[id] != "Customer":
            print("NO WORKER WITH SUCH ID.\nTRY AGAIN.")
            continue
        else:
            print("YOU HAVE COMPLAINED SUCCESSFULLY ON THE WORKER WITH ID", id)
            id_complain[id] += 1
            break


def quit(worker_id):
    id_name.pop(worker_id)
    id_pasw.pop(worker_id)
    id_dep.pop(worker_id)
    id_phone.pop(worker_id)
    id_salary.pop(worker_id)
    id_status.pop(worker_id)
    id_achievements.pop(worker_id)
    id_complain.pop(worker_id)
    menu()


def add_item(worker_id):
    p1 = Item()
    print("Product", p1.name, 'for', p1.price, 'was successfully added')
    id_achievements[worker_id] += 1


def remove_item(worker_id):
    items_list()
    print("Please insert the ID of the product that you want to remove:")
    id = int(input())
    if id in id_item:
        print(id_item[id], 'for', item_price[id_item[id]], "was successfully removed")
        item_price.pop(id_item[id])
        id_item.pop(id)
        id_achievements[worker_id] += 1
    else:
        print("No such item in the list.\nTry again.")
        remove_item(worker_id)


def change_price(worker_id):
    items_list()
    print("Please insert the ID of the product, which's price is needed to be changed:")
    id = int(input())
    if id in id_item:
        print("Insert new price:")
        price = int(input())
        item_price[id_item[id]] = price
        print(id_item[id], 'for', item_price[id_item[id]], "was successfully changed")
        id_achievements[worker_id] += 1
    else:
        print("No such item in the list.\nTry again.")
        remove_item(worker_id)


def buy(cust_id):
    items_list()
    lst = []
    print("Please insert the ID of the product that you want to add in your basket:")
    while True:
        id = (input())
        if id.upper() == "SAVE":
            break
        else:
            id = int(id)
        if id in id_item:
            print(id_item[id], 'for', item_price[id_item[id]], "was successfully added.")
            id_achievements[cust_id] += 1
            print("If you have selected all the necessary goods then insert 'SAVE'.")
            lst.append(id)
        else:
            print("No such item in the list.\nTry again.")
    select_line(cust_id, lst)


def select_line(cust_id, lst):
    print("Please select the line in which you want to be served:")
    lines = []
    for id in id_dep:
        if id_status[id] == "Cashier":
            print("LINE №", id_dep[id], sep='')
            lines.append(id_dep[id])
    print("Number of the line:")
    while True:
        try:
            line_no = int(input())
        except Exception as e:
            print("ERROR!\n", e)
        else:
            if line_no not in lines:
                print("ERROR!\nTHERE IS NO SUCH LINE IN AVAILABLE")
            else:
                break
    payment(cust_id, lst, line_no)


def payment(cust_id, lst, line_no):
    tot = 0
    print("___RECIEPT___")
    for i in lst:
        print('*', id_item[i], '-', item_price[id_item[i]])
        tot += item_price[id_item[i]]
    print("TOTAL:", tot)
    print("Cashier:", end=' ')
    for k in id_dep:
        if id_dep[k] == line_no:
            print(id_name[k])
            id_achievements[k]+=1
    print("Thank you for your purchase,", id_name[cust_id])


def change_dep(worker_id):
    if id_status[worker_id] == "Cashier":
        print("AVAILABLE LINES:")
        count = 0
        for line in id_dep:
            if line == id_dep[worker_id]:
                continue
            print("LINE №", line, sep='')
            count += 1
        if count == 0:
            print("ALL LINES FROM 1 TO 3 ARE AVAILABLE")
        while True:
            ch = int(input("PREFERRED LINE №"))
            if ch <= 3 and ch >= 1:
                break
            else:
                print("WRONG INPUT.\nTRY AGAIN.")
        for worker_id2 in id_dep:
            if id_dep[worker_id2] == ch:
                temp = id_dep[worker_id]
                id_dep[worker_id] = id_dep[worker_id2]
                id_dep[worker_id2] = temp
    else:
        print("SELECT DEPARTMENT THAT YOU WANT TO MOVE TO:")
        count = 1
        avail = []
        for dep in deps:
            avail.append(dep)
            print('{}. {}'.format(count, dep))
        while True:
            try:
                ch = int(input("YOUR CHOICE: "))
            except Exception as e:
                print("ERROR!\n", e)
            else:
                if len(avail) >= ch:
                    id_dep[worker_id] = avail[ch - 1]
                    break
                else:
                    print("WRONG INPUT.\nTRY AGAIN.")
                    continue
    print("CHANGES HAVE BEEN APPLIED SUCCESSFULLY")


menu()
