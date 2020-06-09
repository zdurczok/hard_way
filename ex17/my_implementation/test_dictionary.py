from my_dictionary import Dictionary

# create a mapping of state to abbreviation
states = Dictionary()
states.set('Oregon', 'OR')
states.set('Florida', 'FL')
states.set('California', 'CA')
states.set('New York', 'NY')
states.set('Michigan', 'MI')

# create a basic set of states and some cities in them
cities = Dictionary()
cities.set('CA', 'San Francisco')
cities.set('MI', 'Detroit')
cities.set('FL', 'Jacksonville')

# add some more cities
cities.set('NY', 'New York')
cities.set('OR', 'Portland')

# print(out some cities
print('-' * 10)
print("NY State has: %s" % cities.get('NY'))
print("OR State has: %s" % cities.get('OR'))

# print(some states
print('-' * 10)
print("Michigan's abbreviation is: %s" % states.get('Michigan'))
print("Florida's abbreviation is: %s" % states.get('Florida'))

# do it by using the state then cities dict
print('-' * 10)

print("Michigan has: %s" % cities.get(states.get('Michigan')))
print("Florida has: %s" % cities.get(states.get('Florida')))

# print(every state abbreviation
print('-' * 10)
states.print_list()

# print(every city in state
print('-' * 10)
cities.print_list()

print('-' * 10)
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

#  adding test_delete() to Zeds tests

def test_delete():
    airplanes = Dictionary()
    airplanes.set('262', 'Me')
    airplanes.set('234', 'Arado')
    airplanes.set('190d', 'Fw')
    assert airplanes.get('262') == 'Me'
    airplanes.delete('262')
    assert airplanes.get('262') == None
    airplanes.delete('234')
    assert airplanes.get('234') == None

test_delete()
