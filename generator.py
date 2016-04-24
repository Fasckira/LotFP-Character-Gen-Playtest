import random

#First we need to check to see if we can generate a playable character
stattotal = 1
while stattotal < 55 :

	strength=random.randrange(3,19)
	dexterity=random.randrange(3,19)
	constitution=random.randrange(3,19)
	intelligence=random.randrange(3,19)
	wisdom=random.randrange(3,19)
	charisma=random.randrange(3,19)

	stattotal=strength+dexterity+wisdom+constitution+intelligence+wisdom+charisma

print('\nCongratulations, your character is playable with a total score of', stattotal)
print('\nStrength: ', strength , '\t\tDexterity: ' , dexterity , '\nConstitution: ',constitution,'\tIntelligence: ',intelligence,'\nWisdom: ',wisdom,'\t\tCharisma: ',charisma)

#Lets pick a class now
characterclass=['Fighter','Magic User','Specialist']
chosenclass=random.choice(characterclass)
print('\nYour class is',chosenclass)

#Time to work out the HP
if constitution <= 4 :
	hp = random.randrange(1,5)
elif constitution <= 8 :
	hp = random.randrange(1,7)
elif constitution <= 12 :
	hp = random.randrange(1,9)
elif constitution <= 16 :
	hp = random.randrange(1,11)
else :
	hp = random.randrange(1,13)

print('\nYour HP is',hp)

#Lets do the Save vs Magical Effects
if charisma <= 4 :
	vsmagic = '2d6'
elif charisma <= 8 :
	vsmagic = '3d6'
elif charisma <= 12 : 
	vsmagic = '4d6'
elif charisma <= 16 :
	vsmagic = '5d6'
else :
	vsmagic = '6d6'

print('\nYour Saving Throw Vs Magical Effects is',vsmagic)

#And now the Save Vs Non Magical Effects
if wisdom <= 4 :
	vsnonmagic = '2d6'
elif wisdom <= 8 :
	vsnonmagic = '3d6'
elif wisdom <= 12 :
	vsnonmagic = '4d6'
elif wisdom <= 16 :
	vsnonmagic = '5d6'
else :
	vsnonmagic = '6d6'

print ('Your Saving Throw vs Non Magical Effects is',vsnonmagic)

#Time for initiative
if dexterity <= 4 :
	initiative = '1d4'
elif dexterity <= 8 :
	initiative = '1d6'
elif dexterity <= 12 :
	initiative = '1d8'
elif dexterity <= 16 : 
	initiative = '1d10'
else :
	initiative = '1d12'

print ('Your initiative is',initiative)

#Encumberance Check
if strength <= 4 :
	encumberance = '3'
elif strength <= 8 :
	encumberance = '4'
elif strength <= 12 :
	encumberance = '5'
elif strength <= 16 :
	encumberance = '6'
else :
	encumberance = '7'

print (encumberance,'items equal one encumberance point for you.')

#Skills - this section is a mess and doesn't work
skills=['Architecture','Bushcraft','Climb','Languages','Leadership','Luck','Medicine','Seamanship','Search','Sleight of Hand','Tinkering','Stealth']

if intelligence <= 4 :
	print('You are an unskilled peasant.')
if intelligence <= 8 :
	threeskill = random.choice(skills)
	print('You have a +3 in',threeskill)
if intelligence <= 12 :
	threeskill = random.choice(skills)
	twoskill = random.choice(skills)
	print('You have a +3 in',threeskill,'and a +2 in',twoskill)
if intelligence <= 16 :
	threeskill = random.choice(skills)
	twoskill = random.choice(skills)
	print('You have a +3 in',threeskill,'and a +2 in',twoskill)
else :
	print('Stuff')

