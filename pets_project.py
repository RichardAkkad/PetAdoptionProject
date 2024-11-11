import datetime


class Pet:
    comp_pet_list = []
    count = 0

    def __init__(self, pet, id_no, sex, breed, age, hair_colour, nuted, set_price_4_pet, disability, adopted,
                 last_checkup=None, arrival_time=None):
        self.pet = pet
        self.id_no = id_no
        self.sex = sex
        self.breed = breed
        self.age = age
        self.hair_colour = hair_colour
        self.nuted = nuted
        self.set_price_4_pet = set_price_4_pet
        self.disability = disability
        self.adopted = adopted
        self.last_checkup = last_checkup
        self.arrival_time = arrival_time

        Pet.comp_pet_list.append((self))
        Pet.count_pets()

    @classmethod
    def no_of_Pets(cls):
        return cls.count

    @classmethod
    def count_pets(cls):
        cls.count += 1

    def Description(self):
        return f" I am a {self.sex} and age {self.age}"

    def actual_price(self):
        return self.Price_adjustment_age() + self.price_adjustment_nuted() + self.set_price_4_pet + self.price_disability()

    def Price_adjustment_age(self):
        if 1 <= self.age <= 3:
            age_price_adj_2 = 0
            age_price_adj_2 += 100
            return age_price_adj_2
        return 0

    def price_adjustment_nuted(self):
        if self.nuted:
            nuted_price_adj = 0
            nuted_price_adj += 150
            return nuted_price_adj
        return 0

    def price_disability(self):
        if self.disability and self.set_price_4_pet > 300:
            disability_price_adj = 0
            disability_price_adj -= 150
            return disability_price_adj
        return 0

    def __repr__(self):
        return f"id={self.id_no},sex={self.sex},breed={self.breed},age={self.age},hair_colour={self.hair_colour}"


class Cat(Pet):

    def __init__(self):

        self.cat_list = []
        self.cat_result_list = []

    def Append_cat(self, cat):
        self.cat_list.append(cat)

    def cat_price_4_search(self):
        while True:
            amount = input("please enter the price range or q and enter to quit: ")
            if 0 < len(amount) <= 4 and amount.isdigit():
                amount = int(amount)
                self.cat_result_list = self.Cat_Result(amount)
                break
            elif amount.isdigit():
                print("please try a different range of numbers")
            elif amount=="q":
                quit()
            else:
                print("can only except numerals")


    def Cat_Result(self, amount):
        for animal in self.cat_list:
            if animal.actual_price() <= amount and not animal.adopted:  # "actual.price()" is a method call from the "pet class" that we are using and can use it because of "Cat(pet)" and same for dog, we basicly have 2 method calls for this method in parent class
                self.cat_result_list.append((animal.arrival_time, animal.id_no, animal.sex, animal.breed, animal.nuted,animal.actual_price()))
        return self.cat_result_list

    def return_cat_result(self):  # you call this function
        return self.cat_result_list


class Dog(Pet):

    def __init__(self):

        self.list = []
        self.result_list = []

    def Append(self, dog):
        self.list.append(dog)

    def price_4_search(self):  # you call this function and this function needs to be used before function "return_result" on line 48
        while True:
            amount = input("please enter the price range or press q and enter to quit: ")
            if 0 <= len(amount) <= 4 and amount.isdigit():
                amount = int(amount)
                self.result_list = self.Result(amount)  # just updates "self.result_list" onyl and then if we want to print "self.result_list" we can from line 138
                break  # also note that self.result_list changes everytime we do a new query
            elif amount.isdigit():
                print("please try a different range of numbers")
            elif amount=="q":
                quit()
            else:
                print("can only except numerals")



    def Result(self, amount):
        for animal in self.list:
            if animal.actual_price() <= amount and not animal.adopted:
                self.result_list.append((animal.arrival_time, animal.id_no, animal.sex, animal.breed, animal.nuted,animal.actual_price()))
        return self.result_list

    def return_result(self):  # you call this function
        return self.result_list


class Main(Pet):

    def __init__(self):
        self.total_pet_list = Pet.comp_pet_list

    def id_check(self):
        while True:
            check_id = input("please enter a id number if you require details of a pet or press q and enter to quit: ")
            if check_id=="q": # remember enter just returns "" so "q"+"" =="q"
                return
            elif check_id.isdigit():
                 check_id = int(check_id)
                 for pet in self.total_pet_list:
                    if pet.id_no == check_id:
                        return pet
                 print("id number not recognised")
            else:
                print("must be numerals only!")




    def make_payment(self, chosen_pet):
        while True:
            payment = input("does the customer want to purchase this pet? or press q and enter to quit ").lower()
            if payment == "yes" and not chosen_pet.adopted:
                chosen_pet.adopted = True  # total_pet_list.remove(chosen_pet)  # 1)if we used "enumerate" in the purchase method and used the index and returned that index from the enumerate then  "self.list.remove(self.list[i])"
                return f"the payment is now done and we have now marked this pet on our system as adopted"  # f"we have removed the pet {chosen_pet} from our database"  # we cant return list[i] because its been remnoved so you are returning another instance in the list that would of come after that instance in the list
                # 2)looks like any "output" can be put in the brackets "{ }" doesnt have to be a assigned variable
                # 3)also because we are returning a instance then in order to see the info from the attribute you have to use the "__repr__" method which we did
            elif payment == "yes" and chosen_pet.adopted:
                print("this pet has already been adopted sorry!")
            elif payment=="no" or payment=="q":
                return
            print("did recognise your response")

    def remove(self,chosen_pet):#self is used as "self.total_pet_list" instance  and the other instance is "chosen_pet"
        while True:
            reason=input("do you want to remove this pet? or press q and enter to quit ").lower()
            if reason == "yes" and not chosen_pet.adopted:
                self.total_pet_list.remove(chosen_pet)
                return f"we have removed the pet {chosen_pet} from our system"
            elif reason == "yes" and chosen_pet.adopted:
                return "pet showing on our system as adopted we cannot remove this pet from our system"
            elif reason == "no" or reason == "q":
                return
            print("did recognise your response")



    def pet_check_up(self):
        while True:
            check = input("would you like to check the pets that are due a check up? or press q and enter to quit?: ").lower()
            if check == "no" or check== "q":
                return
            elif check == "yes":
                return [(pet.id_no, pet.last_checkup) for pet in self.total_pet_list if
                        datetime.date.today() - pet.last_checkup > datetime.timedelta(days=365)]
            print("did not recognise your response!")


    def avg_pet_time_arrival(self):
        while True:

            check_avg = input("would you like to check average arrival time? or press q and enter to quit").lower()
            if check_avg == "no" or check_avg=="q":
                return
            elif check_avg == "yes":
                time_list = [pet.arrival_time.hour for pet in self.total_pet_list]
                return f"The average arrival time of a pet is {round(sum(time_list) / len(time_list))}"
            print("did not recognise your response!")



d1 = Pet("dog", 2212, "male", "dachshund", 1, "brown", True, 850, True, False, datetime.date(2022, 10, 11),
         datetime.time(12, 10, 52))
d2 = Pet("dog", 1855, "male", "greyhound", 6, "grey", True, 1050, True, False, datetime.date(2024, 2, 11),
         datetime.time(9, 11, 2))
d3 = Pet("dog", 1032, "female", "rottweiler", 4, "grey", False, 469, True, False, datetime.date(2023, 10, 11),
         datetime.time(12, 00, 2))
d4 = Pet("dog", 3678, "female", "british_bulldog ", 1, "grey", True, 1050, False, False, datetime.date(2023, 11, 11),
         datetime.time(10, 33, 5))
d5 = Pet("dog", 1891, "male", "greyhound", 7, "black", True, 550, True, False, datetime.date(2022, 9, 11),
         datetime.time(13, 10, 14))
d6 = Pet("dog", 3312, "female", "yorkshire_terrier", 2, "brown", False, 400, True, False, datetime.date(2023, 10, 1),
         datetime.time(9, 10, 40))
d7 = Pet("dog", 7132, "female", "poodle", 5, "white", False, 850, True, True, datetime.date(2024, 1, 10),
         datetime.time(12, 1, 3))

c1 = Pet("cat", 2198, "female", "siamese", 3, "brown", True, 450, True, False, datetime.date(2023, 9, 3),
         datetime.time(11, 14, 54))
c2 = Pet("cat", 5112, "female", "british shorthair", 2, "dark grey", False, 450, True, False, datetime.date(2024, 3, 7),
         datetime.time(14, 5, 52))
c3 = Pet("cat", 6198, "female", "siamese", 3, "white", True, 500, True, True, datetime.date(2023, 3, 3),
         datetime.time(10, 14, 50))
c4 = Pet("cat", 4512, "female", "british shorthair", 1, "dark grey", False, 450, True, True, datetime.date(2022, 3, 2),
         datetime.time(14, 2, 22))
c5 = Pet("cat", 2358, "female", "siamese", 4, "brown", True, 450, False, False, datetime.date(2023, 10, 3),
         datetime.time(9, 14, 54))
c6 = Pet("cat", 1122, "female", "siamese", 5, "grey", False, 440, True, False, datetime.date(2023, 12, 6),
         datetime.time(16, 5, 22))

# print(Pet.comp_pet_list[0])#even though the instances are displayed using "repr" becuase we appended them using "comp_pet_list"( which is a class attribute)we can elements by their index


s1 = Dog()
s1.Append(d1)
s1.Append(d2)
s1.Append(d3)
s1.Append(d4)
s1.Append(d5)
s1.Append(d6)
s1.Append(d7)

g1 = Cat()
g1.Append_cat(c1)
g1.Append_cat(c2)
g1.Append_cat(c3)
g1.Append_cat(c4)
g1.Append_cat(c5)
g1.Append_cat(c6)

# print(Pet("dog",2212,"male", "dachshund", 1, "brown",True,850,datetime.date(2022,10,11),datetime.time(12,10,52)).pet)#useful to know thats its same as d1.pet which is dog

m1 = Main()


def set_return():
    while True:
        query = input("are you a employee or customer? ").lower()
        if query == "customer":

                while True:
                    pet_type = input("are you interested in a cat or a dog or press q and enter to quit? ").lower()
                    if pet_type == "q":
                        quit()
                    elif pet_type == "dog":
                        s1.price_4_search()
                        for instance in s1.return_result():# this will return a list the "s1.return_result()" part here
                            print(", ".join(str(x) for x in instance))
                        break
                    elif pet_type == "cat":
                        g1.cat_price_4_search()
                        for instance in g1.return_cat_result():
                            print(", ".join(str(x) for x in instance))
                        break
                    else:
                        print("your input is not valid please try again!")
                        continue
                while True:
                    next_query = input("is there anything else you would like to check or press q and enter to quit? ").lower()
                    if next_query == "q":
                        quit()
                    elif next_query == "yes":
                        break
                    elif next_query == "no":
                        quit()
                    else:
                        print("your input is not valid please try again")
                        continue
        elif query == "employee":

                while True:
                    employee_query = input("please enter what you would like to check or press q and enter to quit: ").lower()
                    if not  employee_query:
                        print("you input is not valid please try again!")

                    elif employee_query == "q":
                        quit()

                    elif employee_query.startswith("id") or employee_query.endswith("ion"):
                        print(m1.id_check())
                        break
                    elif employee_query.startswith("p" or "pa"):
                        chosen_pet = m1.id_check()#chosen_pet is a instance
                        print(m1.make_payment(chosen_pet))
                        break
                    elif employee_query.startswith("re"):
                        chosen_pet = m1.id_check()  # chosen_pet is a instance
                        print(m1.remove(chosen_pet))
                        break

                    elif employee_query.startswith("ch") or employee_query.endswith("up"):
                            check =m1.pet_check_up()
                            for instance in check: #if put "m1.pet_check_up()" instead of check  it will call function "pet_check_up" again because m1.check_up is a call that will call the function while the "check" variable will not
                                    print(", ".join(str(x) for x in instance))
                            break
                    elif employee_query.startswith("arr" or "ti" or "av"):
                            print(m1.avg_pet_time_arrival())
                            break

                    else:
                        print("your input is not valid please try again")
                        continue

                while True:
                    next_query = input("is there anything else you would like to check or press q and enter to quit? ").lower()
                    if next_query == "q":
                        quit()
                    elif next_query == "yes":
                        break
                    elif next_query == "no":
                        quit()
                    else:
                        print("your input is not valid please try again")
                        continue
        else:
            print("did not recognise that input please try again")
            continue


set_return()








