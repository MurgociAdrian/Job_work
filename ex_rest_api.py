import requests
import unittest



class TestClass(unittest.TestCase):


   def test_joke_type(self):
      r = ReadFromAPI()
      joke_type = "general"   # tipuri: knock-knock, general, programming
      r.store_10_random_jokes_by_type(joke_type)
      for i in range(len(r.json_obj)):
         self.assertEqual(r.json_obj[i]["type"], joke_type, '''The joke nr {} is not of type {}'''.format(i, joke_type))



class ReadFromAPI:


   def __init__(self):

      self.json_obj = None


   @staticmethod
   def make_request(string_url_param, parity):

      r = requests.get("https://official-joke-api.appspot.com" + string_url_param)
      ReadFromAPI.print_user_friendly(r.json(), parity)
      print(" ")
      return r.json()


   @staticmethod
   def print_user_friendly(json_data, parity):

      if type(json_data) is list:
         for i in range(len(json_data)):
            ReadFromAPI.print_method(json_data[i], parity)

      elif type(json_data) is dict:
         ReadFromAPI.print_method(json_data, parity)

      else:
         print("Unknown data type of json file.")


   @staticmethod
   def print_method(processed_json_data, parity):

      if ((parity == "even" and int(processed_json_data["id"]) % 2 == 0)
         or (parity == "odd" and int(processed_json_data["id"]) % 2 != 0)
         or parity is None):

         print("setup: {}\npunchline: {}\n".format(processed_json_data["setup"], processed_json_data["punchline"]))


   def get_random_joke_1(self, parity):

      self.json_obj = ReadFromAPI.make_request("/random_joke", parity)


   def get_random_joke_2(self, parity):

      self.json_obj = ReadFromAPI.make_request("/jokes/random", parity)


   def get_ten_random_jokes_1(self, parity):

      self.json_obj = ReadFromAPI.make_request("/random_ten", parity)


   def get_ten_random_jokes_2(self, parity):

      self.json_obj = ReadFromAPI.make_request("/jokes/ten", parity)


   def get_random_programming_joke(self, parity):

      self.json_obj = ReadFromAPI.make_request("/jokes/programming/random", parity)


   def get_10_random_programming_jokes(self, parity):

      self.json_obj = ReadFromAPI.make_request("/jokes/programming/ten", parity)


   def store_10_random_jokes_by_type(self, joke_type):

      r = requests.get("https://official-joke-api.appspot.com/jokes/" + joke_type + "/ten")
      self.json_obj = r.json()



if __name__ == "__main__":
   unittest.main()