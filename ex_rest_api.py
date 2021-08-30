import requests



class ReadFromAPI:


   def __init__(self):

      self.json_obj = None


   @staticmethod
   def print_user_friendly(json_data):

      if type(json_data) is list:
         for i in range(len(json_data)):
            ReadFromAPI.print_method(json_data[i])

      elif type(json_data) is dict:
         ReadFromAPI.print_method(json_data)

      else:
         print("Unknown data type of json file.")


   @staticmethod
   def print_method(processed_json_data):

      for key, value in processed_json_data.items():
         if key == "setup" or key == "punchline":
            print("{}: {}".format(key, value))
      print(" ")


   def endpoint1(self):

      r = requests.get('https://official-joke-api.appspot.com/random_joke')
      self.json_obj = r.json()
      ReadFromAPI.print_user_friendly(self.json_obj)


   def endpoint1(self):

      r = requests.get('https://official-joke-api.appspot.com/jokes/random')
      self.json_obj = r.json()
      ReadFromAPI.print_user_friendly(self.json_obj)


   def endpoint2(self):

      r = requests.get('https://official-joke-api.appspot.com/random_ten')
      self.json_obj = r.json()
      ReadFromAPI.print_user_friendly(self.json_obj)


   def endpoint3(self):

      r = requests.get('https://official-joke-api.appspot.com/jokes/ten')
      self.json_obj = r.json()
      ReadFromAPI.print_user_friendly(self.json_obj)


   def endpoint4(self):

      r = requests.get('https://official-joke-api.appspot.com/random_joke')
      self.json_obj = r.json()
      ReadFromAPI.print_user_friendly(self.json_obj)


   def endpoint5(self):

      r = requests.get('https://official-joke-api.appspot.com/jokes/programming/random')
      self.json_obj = r.json()
      ReadFromAPI.print_user_friendly(self.json_obj)


   def endpoint6(self):

      r = requests.get('https://official-joke-api.appspot.com/jokes/programming/ten')
      self.json_obj = r.json()
      ReadFromAPI.print_user_friendly(self.json_obj)




s = ReadFromAPI()
s.endpoint1()
s.endpoint6()



