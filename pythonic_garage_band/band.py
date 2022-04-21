
class Band():
    pass

class Musician():
    pass

class Guitarist():
    
    def __init__(self, name='unknown'):
        self.name = name
        
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"    

    def __str__(self):
        return f"My name is {self.name} and I play guitar"
    

class Bassist():
    pass

class Drummer():
    
    def __init__(self, name='unknown'):
        self.name = name
        
    def __str__(self, name='unknown'):
        return f"My name is {self.name} and I play drums"
    
    # def test_drummer_str():
    # sheila = Drummer("Sheila E.")
    # actual = str(sheila)
    # expected = "My name is Sheila E. and I play drums"
    # assert actual == expected


