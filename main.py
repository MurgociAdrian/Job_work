import json



class PathInfo():


    def __init__(self, path_name):

        self.path_name = path_name


    def read_from_path(self):

        with open(self.path_name, "r") as read_file:
            self.all_data = json.load(read_file)

        self.lista_obj = self.all_data["imdata"]


    def create_cloud_ctx_obj(self):

        for item in self.lista_obj:
            new_ctx_obj = CloudCtx()
            new_ctx_obj.retrieve_info(item)
            CloudCtx.add_obj(new_ctx_obj)


    def create_healt_inst_obj(self):

        for item in self.lista_obj:
            health_atrib = item["hcloudCtx"]["children"][0]
            new_health_obj = HealthInst()
            HealthInst.retrieve_info(new_health_obj, health_atrib)
            HealthInst.add_obj(new_health_obj)



class CloudCtx():


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

        print("hcloudCtx MO contine: {} {} {} {} {}".format(self.name, self.tenant_name, self.description,
                                                  self.name_alias, self.ctx_profile_name))



class HealthInst():


    LISTA_HEALTH_OBJ = []


    def __init__(self):

        self.current_health = " "
        self.max_sev = " "


    @classmethod
    def add_obj(cls, health_obj):

        cls.LISTA_HEALTH_OBJ.append(health_obj)


    def retrieve_info(self, health_val):

        self.current_health = health_val["healthInst"]["attributes"]["cur"]
        self.max_sev = health_val["healthInst"]["attributes"]["maxSev"]


    def displayed_health(self):

        if self.current_health == "100":
            print("Healthy")
        elif int(self.current_health) < 100:
            print("Unhealthy")
        else:
            print("Error! cur_health is >100 or negative")


    def display_info(self):

        print("healthInst MO contine: {} {}".format(self.current_health, self.max_sev))




mo = PathInfo("C:/Users/Adrian23/Desktop/JOB/work - PC/info/exercise.txt")
mo.read_from_path()
mo.create_cloud_ctx_obj()
CloudCtx.LISTA_CLOUD_CTX_OBJ[3].display_info()

mo.create_healt_inst_obj()
HealthInst.LISTA_HEALTH_OBJ[3].display_info()
HealthInst.LISTA_HEALTH_OBJ[3].displayed_health()



