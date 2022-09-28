class Developer:
    def __init__(self, fName,lName, lang):
        self.fName = fName
        self.lName =lName
        self.__language = lang

    def coding(self):
        return "I am coding"
    def set_language(self, newlang):
        self.__language = newlang


dev1=Developer("Mariya","Smith")
dev2=Developer("Anna", "Boleyn")
dev1.__language ="Python"
dev2.__language = "Java"