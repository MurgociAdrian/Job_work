import requests
import unittest
import random



class TestClass(unittest.TestCase):


   LIST_JOKE_TYPES = ["general", "programming", "knock-knock"]


   def setUp(self):

      r = requests.get(ReadFromAPI.STRING_URL)
      r.raise_for_status()


   def test_all_joke_types(self):

      r = ReadFromAPI()

      for joke_type in TestClass.LIST_JOKE_TYPES:
         r.get_10_random_jokes_by_type(joke_type)
         for i in range(len(r.json_obj)):
            self.assertEqual(r.json_obj[i]["type"], joke_type,
                             '''The joke nr {} is not of type {}'''.format(i, joke_type))


   def test_10_count_jokes(self):

      r = ReadFromAPI()
      joke_type = random.choice(TestClass.LIST_JOKE_TYPES)
      r.get_10_random_jokes_by_type(joke_type)

      self.assertEqual(len(r.json_obj), 10,
                       '''Error! The nr of jokes received is {} and should be 10'''.format(len(r.json_obj)))


   def test_10_same_type(self):

      r = ReadFromAPI()
      r.get_ten_random_jokes_1()

      type_count = TestClass.get_nr_of_same_joke_types(r.json_obj)

      self.assertNotEqual(type_count, 10, '''Error! All joke types are the same for all 10 jokes''')


   def test_10_count_and_same_type(self):

      r = ReadFromAPI()
      r.get_ten_random_jokes_1()

      type_count = TestClass.get_nr_of_same_joke_types(r.json_obj)

      self.assertEqual(len(r.json_obj), 10,
                       '''Error! The nr of jokes received is {} and should be 10'''.format(len(r.json_obj)))

      self.assertNotEqual(type_count, 10, '''Error! All joke types are the same for all 10 jokes''')


   def test_a_post_call(self):

      dict_joke = {"id": 388, "type": "programming", "setup": "test", "punchline": "test1"}

      r = requests.post("https://official-joke-api.appspot.com/jokes/ten", data = dict_joke)

      r.raise_for_status()


   @staticmethod
   def get_nr_of_same_joke_types(json_data):

      list_types = []
      for i in range(len(json_data)):
         list_types.append(json_data[i]["type"])

      return list_types.count(list_types[0])



class ReadFromAPI:


   STRING_URL = "https://official-joke-api.appspot.com"


   def __init__(self):

      self.json_obj = None
      self.response_obj = None


   @classmethod
   def store_url(cls, string_url_param):

      ReadFromAPI.STRING_URL = "https://official-joke-api.appspot.com" + string_url_param


   @staticmethod
   def make_request(string_url_param, *tuple_print_parity):

      r = requests.get("https://official-joke-api.appspot.com" + string_url_param)
      ReadFromAPI.store_url(string_url_param)
      print(r.status_code, end = '\n')
      
      if tuple_print_parity[0]:
         if tuple_print_parity[0][0][0] is True:
            if len(tuple_print_parity[0][0]) == 1:
               ReadFromAPI.print_user_friendly(r.json(), None)
            else:
               ReadFromAPI.print_user_friendly(r.json(), tuple_print_parity[0][0][1])
         print(" ")
          
      return r.json(), r


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


   def get_random_joke_1(self, *tuple_print_parity):

      (self.json_obj, self.response_obj) = ReadFromAPI.make_request("/random_joke", tuple_print_parity)


   def get_random_joke_2(self, *tuple_print_parity):

      (self.json_obj, self.response_obj) = ReadFromAPI.make_request("/jokes/random", tuple_print_parity)


   def get_ten_random_jokes_1(self, *tuple_print_parity):

      (self.json_obj, self.response_obj) = ReadFromAPI.make_request("/random_ten", tuple_print_parity)


   def get_ten_random_jokes_2(self, *tuple_print_parity):

      (self.json_obj, self.response_obj) = ReadFromAPI.make_request("/jokes/ten", tuple_print_parity)


   def get_random_programming_joke(self, *tuple_print_parity):

      (self.json_obj, self.response_obj) = ReadFromAPI.make_request("/jokes/programming/random", tuple_print_parity)


   def get_10_random_programming_jokes(self, *tuple_print_parity):

      (self.json_obj, self.response_obj) = ReadFromAPI.make_request("/jokes/programming/ten", tuple_print_parity)


   def get_10_random_jokes_by_type(self, joke_type, *tuple_print_parity):

      (self.json_obj, self.response_obj) = ReadFromAPI.make_request("/jokes/" + joke_type + "/ten", tuple_print_parity)



if __name__ == "__main__":
   unittest.main()
   # s = ReadFromAPI()
   # s.get_random_joke_2((True, "even"))
   # s.get_ten_random_jokes_1()
   # s.get_ten_random_jokes_1((True, "odd"))
   # s.get_random_joke_1((True, ))