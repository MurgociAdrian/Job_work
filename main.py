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

            new_ctx_obj.add_reference_to_health_inst(new_health_obj)



class CloudCtx():


    NR_OF_CLOUD_CTX_OBJ_CREATED = 0
    LISTA_CLOUD_CTX_OBJ = []


    def __init__(self):

        self.name = " "
        self.tenant_name = " "
        self.description = " "
        self.name_alias = " "
        self.ctx_profile_name = " "
        self.reference_to_health_inst = None


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


    def add_reference_to_health_inst(self, health_obj):

        self.reference_to_health_inst = health_obj


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

        i = 0
        while nr_max_obj > 0:
            obj = CloudCtx.LISTA_CLOUD_CTX_OBJ[i]
            nr_max_obj -= 1
            i += 1
            print("hcloudCtx MO have: {} {} {} {} {}  + displayed_health: {}".format(obj.name, obj.tenant_name, obj.description, obj.name_alias,
                                                                                         obj.ctx_profile_name, obj.reference_to_health_inst.displayed_health))



    @classmethod
    def display_obj_in_order_by_cur_health(cls):

        list_cloud_ctx_obj_to_print = CloudCtx.LISTA_CLOUD_CTX_OBJ.copy()

        for i, item1 in enumerate(CloudCtx.LISTA_CLOUD_CTX_OBJ):
            for j, item2 in enumerate(CloudCtx.LISTA_CLOUD_CTX_OBJ):
                if (int(item1.reference_to_health_inst.current_health) > int(item2.reference_to_health_inst.current_health)) and (i<j):
                    aux = list_cloud_ctx_obj_to_print[i]
                    list_cloud_ctx_obj_to_print[i] = list_cloud_ctx_obj_to_print[j]
                    list_cloud_ctx_obj_to_print[j] = aux

        print(list_cloud_ctx_obj_to_print)

        # # VERIFICARE (ok)
        # for obj in list_cloud_ctx_obj_to_print:
        #     print(obj.reference_to_health_inst.current_health)



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




mo = PathInfo("C:/Users/Adrian23/Desktop/JOB/work - PC/info/exercise.txt")
mo.read_from_path()

mo.create_CloudCtx_and_HealthInst_obj()

#CloudCtx.display_specific_info(3)
#print(CloudCtx.NR_OF_CLOUD_CTX_OBJ_CREATED)
#CloudCtx.display_obj_in_order_by_cur_health()

CloudCtx.LISTA_CLOUD_CTX_OBJ[0].display_info()
HealthInst.LISTA_HEALTH_OBJ[0].display_info()

# d = {"Tim": "18", "Charlie":12, "Tiffany":22, "Robert":25}
# d.update
# print(a)