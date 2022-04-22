

class Band():
    instances = []
    def __init__(self, name, members):

        self.name = name
        self.members = members
        Band.instances.append(self)
    def play_solos(self):
        solo_list = []
        for member in self.members:
            solo_list.append(member.play_solo())
        return solo_list
    
    @classmethod
    def to_list(cls):
       return cls.instances

    def __repr__(self):
        pass

    def __str__(self):
        return self.name


class Musician:
    def __init__(self, name="unknown"):
        self.name = name


class Guitarist(Musician):
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "face melting guitar solo"


class Bassist(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        return "bass"

    def play_solo(self):
        return "bom bom buh bom"


class Drummer(Musician):
    def __str__(self, name="unknown"):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "rattle boom crash"


nirvana = Band("Nirvana", [])
