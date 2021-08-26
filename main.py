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
            new_obj = CloudCtx()
            new_obj.retrieve_info(item)
            CloudCtx.add_obj(new_obj)



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
        print("MO contine: {} {} {} {} {}".format(self.name, self.tenant_name, self.description,
                                                  self.name_alias, self.ctx_profile_name))



mo = PathInfo("C:/Users/Adrian23/Desktop/JOB/work - PC/info/exercise.txt")
mo.read_from_path()
mo.create_cloud_ctx_obj()
CloudCtx.LISTA_CLOUD_CTX_OBJ[0].display_info()




