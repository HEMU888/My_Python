
string=""
for x in range(1,10):
	string=""
	for y in range(1,x+1):
		if str(y) == "1":
			string = string + (str(y) + "*" + str(x) + "=" + str(x*y))
		else:
		    string = string + "\t" + (str(y) + "*" + str(x) + "=" + str(x*y))
	print(string)
squares=[value**2 for value in range(1,11)]
print(squares)
print(squares[-2:])

alien_0 = {'color':'green', 'points':5}
print(alien_0['color'])
print(alien_0['points'])

user_0 = {
	'username':'efermi',
	'first':'enrico',
	'last':'fermi',
}

for key, value in user_0.items():
	print("\nKey:" + key);
	print("\nValue:" + value)

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10, 'x':10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
	print(alien)
#message=input("Tell me:")
#print(message)

def describe_pet(pet_name, animal_type='dog'):
	"""显示宠物的信息"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')
