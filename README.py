from SoftwareDeveloper import UserProfile

class Information:
   def __init__(self):
      self.name = 'Julieta Collado'
      self.age = '26 years old'
      self.from = 'Buenos Aires, Argentina'
      self.residence = 'Copenhagen, Denmark'
      self.hobbies = 'Travel, coding, cooking, strolls'
      self.contact = 'julietacollado98@hotmail.com'
      self.linkedIn = 'Julieta Marina Collado'
      self.spokenLanguages = 'English, Spanish, Italian'
      

  def skills(self, languages, tools, frameworks,ai_skills):
      if languages:
         return ["Python", "JavaScript", "HTML", "CSS"]
      elif tools:
         return ["Git", "Docker", "VSCode", "PyCharm"]
      elif frameworks:
          return ["PyTorch", "Flask", "Django", "TensorFlow"]
      elif ai_skills:
         return [ "Machine Learning", "Deep Learning", "Neural Networks", "Computer Vision", "Natural Language Processing", "PyTorch", "TensorFlow", "keras", "Scikit-learn"] 
     
  
