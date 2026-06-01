nomes = None

def nomecatchoro():
    dog = 'nyx' 
    global nomes
    nomes = dog
    return dog

def meunome(dog):
    ric = 'Ricardo'
    print(dog)
    print(nomes)
    return ric

nomecatchoro()
meunome(nomecatchoro)


