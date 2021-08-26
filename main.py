import json



class PathInfo():


    def __init__(self, path_name):

        self.path_name = path_name


    def read_from_path(self):

        with open(self.path_name, "r") as read_file:
            self.all_data = json.load(read_file)

        self.lista_obj = self.all_data["imdata"]


    def create_CloudCtx_and_HealthInst_obj(self):

        for item in self.lista_obj:
            health_atrib = item["hcloudCtx"]["children"][0]

            new_ctx_obj = CloudCtx()
            new_health_obj = HealthInst()

            new_ctx_obj.retrieve_info(item)
            CloudCtx.add_obj(new_ctx_obj)

            HealthInst.retrieve_info(new_health_obj, health_atrib)
            HealthInst.add_obj(new_health_obj)

            CloudCtx.REFERENCE_TO_HEALTH_INST.update({new_ctx_obj: new_health_obj})



class CloudCtx():


    NR_OF_CLOUD_CTX_OBJ_CREATED = 0
    REFERENCE_TO_HEALTH_INST = dict()
    LISTA_CLOUD_CTX_OBJ = []


    def __init__(self):

        self.name = " "
        self.tenant_name = " "
        self.description = " "
        self.name_alias = " "
        self.ctx_profile_name = " "


    @classmethod
    def add_obj(cls, ctx_obj):

       cls.LISTA_CLOUD_CTX_OBJ.append(ctx_obj)
       cls.NR_OF_CLOUD_CTX_OBJ_CREATED += 1


    def retrieve_info(self, mo_val):

        self.name = CloudCtx.verify_empty(mo_val, "name")
        self.tenant_name = CloudCtx.verify_empty(mo_val, "tenantName")
        self.description = CloudCtx.verify_empty(mo_val, "description")
        self.name_alias = CloudCtx.verify_empty(mo_val, "nameAlias")
        self.ctx_profile_name = CloudCtx.verify_empty(mo_val, "ctxProfileName")


    @staticmethod
    def verify_empty(mo_val, atrib_name):

        if mo_val["hcloudCtx"]["attributes"][atrib_name] == "":
            return "-"
        else:
            return mo_val["hcloudCtx"]["attributes"][atrib_name]


    def display_info(self):

        print("hcloudCtx MO contains: {} {} {} {} {}".format(self.name, self.tenant_name, self.description,
                                                             self.name_alias, self.ctx_profile_name))


    @classmethod
    def display_specific_info(cls, nr_max_obj):

        counter = 0
        for key,value in CloudCtx.REFERENCE_TO_HEALTH_INST.items():
            if counter < nr_max_obj:
                counter += 1
                print("hcloudCtx MO have: {} {} {} {} {}  + displayed_health: {}".format(key.name, key.tenant_name,
                                                                                        key.description, key.name_alias,
                                                                                        key.ctx_profile_name,
                                                                                        value.displayed_health))
            else:
                break


    @classmethod
    def display_obj_in_order_by_cur_health(cls):

        list_with_cloud_ctx_obj = list(CloudCtx.REFERENCE_TO_HEALTH_INST.keys())
        list_with_health_obj = list(CloudCtx.REFERENCE_TO_HEALTH_INST.values())

        list_cloud_ctx_obj_to_print = list_with_cloud_ctx_obj.copy()
        list_health_obj_to_print = list_with_health_obj.copy()
        dict_to_print = dict()

        for i, item1 in enumerate(list_with_health_obj):
            for j, item2 in enumerate(list_with_health_obj):
                if (int(item1.current_health) > int(item2.current_health)) and (i<j):
                    aux = list_health_obj_to_print[i]
                    list_health_obj_to_print[i] = list_health_obj_to_print[j]
                    list_health_obj_to_print[j] = aux

                    aux = list_cloud_ctx_obj_to_print[i]
                    list_cloud_ctx_obj_to_print[i] = list_cloud_ctx_obj_to_print[j]
                    list_cloud_ctx_obj_to_print[j] = aux

        for i in range(len(list_cloud_ctx_obj_to_print)):
            dict_to_print.update({list_cloud_ctx_obj_to_print[i]: list_health_obj_to_print[i]})

        print(dict_to_print)    # verificat, e ok



class HealthInst():


    LISTA_HEALTH_OBJ = []


    def __init__(self):

        self.current_health = " "
        self.max_sev = " "
        self.displayed_health = " "


    @classmethod
    def add_obj(cls, health_obj):

        cls.LISTA_HEALTH_OBJ.append(health_obj)


    def retrieve_info(self, health_val):

        self.current_health = health_val["healthInst"]["attributes"]["cur"]
        self.max_sev = health_val["healthInst"]["attributes"]["maxSev"]

        if self.current_health == "100":
            self.displayed_health = "Healthy"
        elif int(self.current_health) < 100:
            self.displayed_health = "Unhealthy"
        else:
            self.displayed_health = "Error!"


    def display_info(self):

        print("healthInst MO contains: {} {} {}".format(self.current_health, self.max_sev, self.displayed_health))




mo = PathInfo("C:/Users/agmurgoci/Desktop/info/exercise.txt")
mo.read_from_path()

mo.create_CloudCtx_and_HealthInst_obj()

# CloudCtx.display_specific_info(3)
# print(CloudCtx.NR_OF_CLOUD_CTX_OBJ_CREATED)
CloudCtx.display_obj_in_order_by_cur_health()

# CloudCtx.LISTA_CLOUD_CTX_OBJ[0].display_info()
# HealthInst.LISTA_HEALTH_OBJ[0].display_info()
#
# print(CloudCtx.REFERENCE_TO_HEALTH_INST)

# d = {"Tim": "18", "Charlie":12, "Tiffany":22, "Robert":25}
# d.update
# print(a)