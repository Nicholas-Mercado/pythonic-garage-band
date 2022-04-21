class Band:
    def __init__(self, name="unknown", members="unknown"):
        self.name = name
        self.members = members


class Musician:
    def __init__(self, name="unknown"):
        self.name = name

    def get_instrument(self):
        return "guitar"


class Guitarist(Musician):
    def __init__(self, name="unknown"):
        self.name = name

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def get_instrument(self):
        return "guitar"


class Bassist(Musician):
    def __init__(self, name="unknown"):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        return "bass"


class Drummer(Musician):
    def __init__(self, name="unknown"):
        self.name = name

    def __str__(self, name="unknown"):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return "drums"


nirvana = Band("Nirvana", [])
