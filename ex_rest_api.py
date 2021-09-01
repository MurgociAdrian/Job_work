import requests
import unittest
import random



class TestClass(unittest.TestCase):


   LIST_JOKE_TYPES = ["general", "programming", "knock-knock"]


   def setUp(self):

      r = requests.get(ReadFromAPI.STRING_API_URL)
      r.raise_for_status()


   def test_all_joke_types(self):

      for joke_type in TestClass.LIST_JOKE_TYPES:
         json_data = ReadFromAPI.get_10_random_jokes_by_type(joke_type)
         for i in range(len(json_data)):
            self.assertEqual(json_data[i]["type"], joke_type, '''The joke nr {} is not of type {}'''.format(i, joke_type))


   def test_10_count_jokes(self):

      joke_type = random.choice(TestClass.LIST_JOKE_TYPES)
      json_data = ReadFromAPI.get_10_random_jokes_by_type(joke_type)

      self.assertEqual(len(json_data), 10,
                       '''Error! The nr of jokes received is {} and should be 10'''.format(len(json_data)))


   def test_10_same_type(self):

      type_count = TestClass.get_nr_of_same_joke_types(ReadFromAPI.get_ten_random_jokes_1())

      self.assertNotEqual(type_count, 10, '''Error! All joke types are the same for all 10 jokes''')


   def test_10_count_and_same_type(self):

      json_data = ReadFromAPI.get_ten_random_jokes_1()
      type_count = TestClass.get_nr_of_same_joke_types(json_data)

      self.assertEqual(len(json_data), 10,
                       '''Error! The nr of jokes received is {} and should be 10'''.format(len(json_data)))

      self.assertNotEqual(type_count, 10, '''Error! All joke types are the same for all 10 jokes''')


   def test_a_post_call(self):

      dict_joke = {"id": 388, "type": "programming", "setup": "test", "punchline": "test1"}

      self.assertEqual(ReadFromAPI.make_a_post_call(dict_joke), 404, '''Error!''')


   @staticmethod
   def get_nr_of_same_joke_types(json_data):

      list_types = [item["type"] for item in json_data]

      return list_types.count(list_types[0])



class ReadFromAPI:


   STRING_API_URL = "https://official-joke-api.appspot.com"


   @staticmethod
   def make_request(string_url_param, bool_print, parity):

      r = requests.get(ReadFromAPI.STRING_API_URL + string_url_param)
      print(r.status_code, end = '\n')
      
      if bool_print is True:
         ReadFromAPI.print_user_friendly(r.json(), parity)
         print(" ")
          
      return r.json()


   @staticmethod
   def make_a_post_call(dict_joke):

      r = requests.post(ReadFromAPI.STRING_API_URL + "/jokes/ten", data = dict_joke)
      return r.status_code


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


   @staticmethod
   def get_random_joke_1(bool_print = False, parity = None):

      return ReadFromAPI.make_request("/random_joke", bool_print, parity)


   @staticmethod
   def get_random_joke_2(bool_print = False, parity = None):

      return ReadFromAPI.make_request("/jokes/random", bool_print, parity)


   @staticmethod
   def get_ten_random_jokes_1(bool_print = False, parity = None):

      return ReadFromAPI.make_request("/random_ten", bool_print, parity)


   @staticmethod
   def get_ten_random_jokes_2(bool_print = False, parity = None):

      return ReadFromAPI.make_request("/jokes/ten", bool_print, parity)


   @staticmethod
   def get_random_programming_joke(bool_print = False, parity = None):

      return ReadFromAPI.make_request("/jokes/programming/random", bool_print, parity)


   @staticmethod
   def get_10_random_programming_jokes(bool_print = False, parity = None):

      return ReadFromAPI.make_request("/jokes/programming/ten", bool_print, parity)


   @staticmethod
   def get_10_random_jokes_by_type(joke_type, bool_print = False, parity = None):

      return ReadFromAPI.make_request("/jokes/" + joke_type + "/ten", bool_print, parity)



if __name__ == "__main__":
   unittest.main()
   # ReadFromAPI.get_random_joke_1(True, "even")
   # ReadFromAPI.get_ten_random_jokes_2(True, "odd")
   # ReadFromAPI.get_10_random_jokes_by_type("knock-knock", True, "even")
