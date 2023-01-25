class school:
    def __init__(self, name, address, theme):
        self.name = name
        self.address = address
        self.theme = theme
    
class person2:
    def __init__(self, name, age, country, school):
        self.name = name
        self.age = age
        self.country = country
        self.school = school


school_eco = school('Nova', 'Carcavelos', 'Business')    

sam = person2('Sam', 24, 'Atlantis', school_eco)

sam.school
