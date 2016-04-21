import random

#Establish the stats
strength=random.randrange(3,18)
dexterity=random.randrange(3,18)
constitution=random.randrange(3,18)
intelligence=random.randrange(3,18)
wisdom=random.randrange(3,18)
charisma=random.randrange(3,18)

print('Strength: ', strength , '\t\tDexterity: ' , dexterity , '\nConstitution: ',constitution,'\tIntelligence: ',intelligence,'\nWisdom: ',wisdom,'\t\tCharisma: ',charisma)

#Work out the total
stattotal=[strength,dexterity,wisdom,constitution,intelligence,wisdom,charisma]

print('\nTotal Value: ',sum(stattotal))
