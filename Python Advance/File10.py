#format function

company = ['ford', 'tesla', 'maruti', 'hyundai', 'honda']

state = ['is okay', 'is sexy', 'is good', 'is cool', 'cannot afford']

""" for i in range(len(company)):
    states = 'company like {1} has this {0} state from users.' #it will reverse state to company
    print(states.format(company[i], state[i]))
 """
#join function

print(' and '.join(company))
print(' and '.join(state))