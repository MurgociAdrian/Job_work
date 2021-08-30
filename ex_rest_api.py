import requests



class ReadFromAPI:


   def __init__(self):

      self.json_obj = None


   @staticmethod
   def make_request(string_url_param):

      r = requests.get("https://official-joke-api.appspot.com" + string_url_param)
      ReadFromAPI.print_user_friendly(r.json())
      return r.json()


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


   def get_random_joke_1(self):

      self.json_obj = ReadFromAPI.make_request("/random_joke")


   def get_random_joke_2(self):

      self.json_obj = ReadFromAPI.make_request("/jokes/random")


   def get_ten_random_jokes_1(self):

      self.json_obj = ReadFromAPI.make_request("/random_ten")


   def get_ten_random_jokes_2(self):

      self.json_obj = ReadFromAPI.make_request("/random_joke")


   def get_random_programming_joke(self):

      self.json_obj = ReadFromAPI.make_request("/jokes/programming/random")


   def get_10_random_programming_jokes(self):

      self.json_obj = ReadFromAPI.make_request("/jokes/programming/ten")




s = ReadFromAPI()
s.get_10_random_programming_jokes()
s.get_ten_random_jokes_1()
s.get_random_joke_2()
s.get_random_joke_2()


