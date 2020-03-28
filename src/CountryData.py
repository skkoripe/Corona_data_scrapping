

class CountryData():
    def __init__(self,country,total_cases,new_cases,total_deaths,new_deaths,total_recovered,rank):
        self.country=country
        self.total_cases=total_cases
        self.new_cases=new_cases
        self.total_deaths=total_deaths
        self.new_deaths=new_deaths
        self.total_recovered=total_recovered
        self.rank=rank
    
    def serialize(self):
        return {'country' : self.country, 'total_cases' : self.total_cases, 'new_cases' : self.new_cases , 'total_deaths' : self.total_deaths, 'new_deaths' : self.new_deaths , 'total_recovered' : self.total_recovered, 'rank' : self.rank}
