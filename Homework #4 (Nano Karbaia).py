# 1) ციკლის მეშვეობით 3 მომხმარებელს შეაყვანინე ინფორმაცია საკუთარი სახელის, გვარის და ასაკის შესახებ.
# თითოეული მომხმარებლის ინფორმაცია შეინახე ინდივიდუალურ სიაში.
# შემდეგ კი სამივე სია დაამატე საერთო ცარიელ სიას სახელად consumer_info.
# Input_ის მეშვეობით მომხმარებლის ინდექსის შეყვანის შემთხვევაში პროგრამამ უნდა დაბრუნოს არჩეულ
# მომხმარებელზე ინფორმაცია შემდეგნაირად:
# Name: Elene
# Lastname: Khardava
# Age: 21

consumerinfo=[]
i=0
while i<3:
    a=[]
    name=input('\nშეიყვანეთ თქვენი სახელი: ')
    lastname=input('შეიყვანეთ თქვენი გვარი: ')
    age=input('შეიყვანეთ თქვენი ასაკი: ')

    a.append(name)
    a.append(lastname)
    a.append(age)
    consumerinfo.append(a)
    i += 1
while True:
    try:
        index=int(input('\nშეიყვანეთ ინდექსი(0,1,2): '))
        print(f"""
        Name: {consumerinfo[index][0]}
        Lastname: {consumerinfo[index][1]}
        Age: {consumerinfo[index][2]}
        """)
        break
    except:
        print('გთხოვთ, შეიყვანოთ ჩამოთვლილთაგან')


# 2) შექმენი ჩაშენებული სია, რომელშიც იქნება შენახული ცნობილი მსახიობების შესახებ ინფორმაცია.
# მომხმარებელს შემოჰყავს მსახიობის სახელი ან გვარი.
# თუ სიაში მოიძებნა მსახიობი, დაბეჭდე მის შესახებ არსებული ინფორმაცია რეზიუმის სახით.

# პირველი ვარიანტი:

actors=[['Jennifer', 'Lawrence', 33],['Nicole', 'Kidman', 57], ['Angelina', 'Jolie', 49],['Tom', 'Hanks', 68],['Meryl', 'Streep',74],['Leonardo', 'DiCaprio',49]]

a=input('შეიყვანეთ მსახიობის სახელი ან გვარი: ')

f = False
for i in actors:
    if a in i:
        print(f"""
            Name: {i[0]}
            Lastname: {i[1]}
            Age: {i[2]}
            """)
        f = True
if not f:
    print('ეს მსახიობი ვერ მოიძებნა!')

# მეორე ვარიანტი:

actors=[['Jennifer', 'Lawrence', 33],['Nicole', 'Kidman', 57], ['Angelina', 'Jolie', 49],['Tom', 'Hanks', 68],['Meryl', 'Streep',74],['Leonardo', 'DiCaprio',49]]


def find_actor_info(a):
    for b in actors:
        if a in b:
            return b
    return None

actor_name = input('Enter the actor\'s first or last name: ')

actor_info = find_actor_info(actor_name)

if actor_info:
    print(f"Name: {actor_info[0]} {actor_info[1]}, Age: {actor_info[2]}")
else:
    print("ეს მსახიობი ვერ მოიძებნა!")


# 3) შექმენი ფუნქცია რომელიც მიიღებს სიას და
# დააბრუნებს ასევე სიას, თუმცა უნიკალური
# ელემენტებით (გამოიყენე set მონაცემთა ტიპი).


def unique_list(a):
    b=list(set(a))
    return b

c=['a', 'a', 'k', 2, 3, 4, 4, 8, 7, 'l', '9', 9, 1, 2, 5]
print(unique_list(c))


# 4) შექმენი ფუნქცია რომელიც მიიღებს ორ set ტიპის
# მონაცემს, გააერთიანებს მათ, შემდეგ კი გადააქცევს
# tuple ტიპის მონაცემად და დააბრუნებს შედეგს.

def set_to_tuple(a,b):
    c=a.union(b)
    d=tuple(c)
    return d

a = {'a','b', 'c'}
b = {'a', 'b', 'd', 'e', 'k'}
x = set_to_tuple(a, b)

print(x)


# 5) დაწერე პროგრამა, რომელიც შეამოწმებს გადაცემული
# ლექსიკონი არის თუ არა ცარიელი.

def is_dict_empty(a):
    if a:
        return False
    else:
        return True

a={}
b = {1:'n', 2:'k', 3:'d'}

print('ლექსიკონი ცარიელია? ', is_dict_empty(a))
print('ლექსიკონი ცარიელია? ', is_dict_empty(b))

# 6) დაწერე პროგრამა რომელიც სტრიქონისგან ქმნის
# ლექსიკონს.
# დათვალე სტრიქონში კონკრეტული სიმბოლოს
# ოდენობა. მაგალითად პროგრამას გადავეცით
# სტრიქონი: &#39;w3schools&#39; უნდა დააბრუნოს ლექსიკონი:
#
# {'w': 1, '3': 1, 's': 2, 'c': 1, 'h': 1, 'o': 2, 'l': 1}

a='w3schools'
b={}
for i in a:
    b[i]=a.count(i)
print(b)

