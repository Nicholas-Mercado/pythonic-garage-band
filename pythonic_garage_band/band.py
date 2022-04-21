
    
class Band:
    
    def __init__(self, name="unknown", members="unknown"):
        self.name = name
        self.members = members  
    

class Musician:
    def __init__(self, name="unknown"):
        self.name = name



class Guitarist(Musician):
    def __init__(self, name="unknown"):
        self.name = name

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def __str__(self):
        return f"My name is {self.name} and I play guitar"


class Bassist(Musician):
    
    def __init__(self, name="unknown"):
        self.name = name
    
    def __str__(self):
        return f"My name is {self.name} and I play bass"
    
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"


class Drummer(Musician):
    def __init__(self, name="unknown"):
        self.name = name

    def __str__(self, name="unknown"):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"


nirvana = Band("Nirvana", [])
