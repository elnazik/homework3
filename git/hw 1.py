obj='a'

print(type(obj))

def a(b):
    print(b)

class SuperHero(object):
    name= 'people'

    def __init__(self,name,nickname,superpower,health_points,catchprase):
        self.name=name
        self.nickname=nickname
        self.superpower=superpower
        self.health_points=health_points
        self.catchprase=catchprase


    def sayname(self):
        print(self.name, self.nickname, self.superpower, self.health_points, self.catchprase)

    def __str__(self):
        return f'{self.name},{self.nickname},{self.superpower},{self.health_points},{self.catchprase}'

    def __len__(self):
        return len(self.name, self.nickname, self.catchprase, self.health_points, self.superpower)


people= SuperHero('Peter Parker', 'spidermen', ' stamina', 99, 'With Great Power Comes Great Responsibility')
people2=SuperHero('Diana', 'Wonder Woman', 'ability to fly.', 999, 'i fight')
print(people.name, people.nickname, people.superpower, people.health_points*2, people.catchprase)
print(people2.name, people2.nickname, people2.superpower, people2.health_points*2, people2.catchprase)



