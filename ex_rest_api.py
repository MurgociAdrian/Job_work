import requests



class ReadFromAPI:


   def __init__(self):

      self.json_obj = None


   @staticmethod
   def make_request(string_url_param, *args):

      r = requests.get("https://official-joke-api.appspot.com" + string_url_param)
      if not args:
         ReadFromAPI.print_user_friendly(r.json())
      else:
         ReadFromAPI.print_user_friendly(r.json(), args[0])
      print(" ")
      return r.json()


   @staticmethod
   def print_user_friendly(json_data, *args):

      if args:
         parity = args[0]
      else:
         parity = 0

      if type(json_data) is list:
         for i in range(len(json_data)):
            ReadFromAPI.print_method(json_data[i], parity)

      elif type(json_data) is dict:
         ReadFromAPI.print_method(json_data, parity)

      else:
         print("Unknown data type of json file.")


   @staticmethod
   def print_method(processed_json_data, *args):

      if ((args[0] == "even" and int(processed_json_data["id"]) % 2 == 0)
         or (args[0] == "odd" and int(processed_json_data["id"]) % 2 != 0)
         or args[0] == 0):

         print("setup: {}\npunchline: {}\n".format(processed_json_data["setup"], processed_json_data["punchline"]))


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


   def get_10_random_jokes_by_id_parity(self, parity):

      self.json_obj = ReadFromAPI.make_request("/random_ten", parity)




s = ReadFromAPI()
s.get_random_joke_2()
s.get_10_random_jokes_by_id_parity("even")
s.get_10_random_jokes_by_id_parity("odd")
