from SoftwareDeveloper import JulietaCollado

class Information:
   def __init__(self):
      self.name = 'Julieta Collado'
      self.age = '25 years old'
      self.from = 'Buenos Aires, Argentina'
      self.residence = 'Sweden'
      self.hobbies = 'Travel, coding, go for walks'
      self.contact = 'julietacollado98@hotmail.com'
      self.linkedIn = 'Julieta Marina Colberg Collado'
      self.spokenLanguages = 'English, Spanish, Italian'
      

  def skills(self, languages, databases, frameworks):
      if languages:
         return ["Python", "JavaScript", "HTML", "CSS"]
      elif databases:
         return ["SQLite", "MySQL"]
      elif frameworks:
          return ["Flask", "Cypress", "Playwright", "Django"]
     
  
