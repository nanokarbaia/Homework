#1. დაწერე პროგრამა რომელიც გეკითხება ჯერ სახელს, შემდეგ გვარს და ინფორმაციის მიღების შემდეგ ტერმინალში ბეჭდავს ერთმანეთის გვერდით.
# George Abramia

Name=input('Please, enter your name: ')
LastName=input('Please, enter your last name: ')
print('Name, Last name: ', Name, LastName)

# 2. დაწერე პროგრამა რომელიც ითხოვს ორ რიცხვს, პირველი რიცხვი აჰყავს მეორის ხარისხში და შედეგი იბეჭდება ტერმინალში.

a=int(input('Please, enter the number: '))
b=int(input('Please, enter the number: '))
print(a**b)

# 3. დაწერე პროგრამა რომელიც გეკითხება სახელს, გვარს, ასაკს და ქალაქს და ბეჭდავს ინფორმაციას შემდეგი სახით:
# Name: Lia
# Surname: Kebadze
# Age: 20
# City: Tbilisi

name=input('Please, enter your name: ')
surname=input('Please, enter your surname: ')
age=input('Please, enter your age: ')
city=input('Please, enter the city you live in: ')

print(f"""
Name: {name}
Surname: {surname}
Age: {age}
City: {city}
""")


# 4. დაწერე პროგრამა, რომელიც გთხოვს შეიყვანო ნებისმიერი სამი სხვადასხვა ხილის დასახელება ცალცალკე. რეზულტატი კი იბეჭდება შემდეგი სახით:
# Apple//Peach%%Orange

f1=input('Please, enter the fruit: ')
f2=input('Please, enter the fruit: ')
f3=input('Please, enter the fruit: ')

print(f1+'//'+f2+'%%'+f3)


# 5. დაწერე პროგრამა, რომელიც გთხოვს შეიყვანო ტექსტი, დათვლის მასში არსებული სიმბოლოების რაოდენობას და გამოიტანს შედეგს შემდეგნაირად:
# Number of symbols: 50

text=input('Please, enter the text: ')

print(len(text))





