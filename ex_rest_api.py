import requests
import unittest
import random



class TestClass(unittest.TestCase):


   LIST_JOKE_TYPES = ["general", "programming", "knock-knock"]


   def test_all_joke_type(self):

      r = ReadFromAPI()

      for joke_type in TestClass.LIST_JOKE_TYPES:
         r.get_10_random_jokes_by_type(None, joke_type, None)
         for i in range(len(r.json_obj)):
            self.assertEqual(r.json_obj[i]["type"], joke_type,
                             '''The joke nr {} is not of type {}'''.format(i, joke_type))


   def test_10_count_jokes(self):

      r = ReadFromAPI()
      joke_type = random.choice(TestClass.LIST_JOKE_TYPES)
      r.get_10_random_jokes_by_type(None, joke_type, None)

      self.assertEqual(len(r.json_obj), 10,
                       '''Error! The nr of jokes received is {} and should be 10'''.format(len(r.json_obj)))


   def test_10_same_type(self):

      r = ReadFromAPI()
      r.get_ten_random_jokes_1(None, None)

      list_types = []
      for i in range(len(r.json_obj)):
         list_types.append(r.json_obj[i]["type"])
      type_count = list_types.count(list_types[0])
      self.assertNotEqual(type_count, 10, '''Error! All joke types are the same for all 10 jokes''')



class ReadFromAPI:


   def __init__(self):

      self.json_obj = None


   @staticmethod
   def make_request(string_url_param, parity, bool_print):

      r = requests.get("https://official-joke-api.appspot.com" + string_url_param)
      if bool_print:
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


   def get_random_joke_1(self, parity, bool_print):

      self.json_obj = ReadFromAPI.make_request("/random_joke", parity, bool_print)


   def get_random_joke_2(self, parity, bool_print):

      self.json_obj = ReadFromAPI.make_request("/jokes/random", parity, bool_print)


   def get_ten_random_jokes_1(self, parity, bool_print):

      self.json_obj = ReadFromAPI.make_request("/random_ten", parity, bool_print)


   def get_ten_random_jokes_2(self, parity, bool_print):

      self.json_obj = ReadFromAPI.make_request("/jokes/ten", parity, bool_print)


   def get_random_programming_joke(self, parity, bool_print):

      self.json_obj = ReadFromAPI.make_request("/jokes/programming/random", parity, bool_print)


   def get_10_random_programming_jokes(self, parity, bool_print):

      self.json_obj = ReadFromAPI.make_request("/jokes/programming/ten", parity, bool_print)


   def get_10_random_jokes_by_type(self, parity, joke_type, bool_print):

    self.json_obj = ReadFromAPI.make_request("/jokes/" + joke_type + "/ten", parity, bool_print)



if __name__ == "__main__":
   unittest.main()