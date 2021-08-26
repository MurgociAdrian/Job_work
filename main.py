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

        self.name = mo_val["hcloudCtx"]["attributes"]["name"]
        self.tenant_name = mo_val["hcloudCtx"]["attributes"]["tenantName"]
        self.description = mo_val["hcloudCtx"]["attributes"]["description"]
        self.name_alias = mo_val["hcloudCtx"]["attributes"]["nameAlias"]
        self.ctx_profile_name = mo_val["hcloudCtx"]["attributes"]["ctxProfileName"]

        for atrib in vars(self):
            if self.? == "": # and (not atrib.startswith('__')):
               self.? = "-"


    def display_info(self):
        print("MO contine: {} {} {} {} {}".format(self.name, self.tenant_name, self.description,
                                                  self.name_alias, self.ctx_profile_name))



mo = PathInfo("C:/Users/Adrian23/Desktop/JOB/work - PC/info/exercise.txt")
mo.read_from_path()
mo.create_cloud_ctx_obj()
CloudCtx.LISTA_CLOUD_CTX_OBJ[0].display_info()




