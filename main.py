import json



class PathInfo():


    def __init__(self, path_name):

        self.path_name = path_name

    def read_from_path(self):

        with open(self.path_name, "r") as read_file:
            self.all_data = json.load(read_file)

        self.lista_obj = self.all_data["imdata"]
        # self.nr_obj = int(self.all_data["totalCount"])

    def create_cloud_ctx_obj(self):

        for item in self.lista_obj:
            cloud_ctx_obj = CloudCtx.retrieve_info(item)
            CloudCtx.add_obj(cloud_ctx_obj)



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


    @classmethod
    def retrieve_info(cls, mo_val):

        lista_atrib = ["name", "tenantName", "description", "nameAlias", "ctxProfileName"]
        lista_info = []
        dict_atrib = (mo_val["hcloudCtx"])["attributes"]
        for name in lista_atrib:
            if dict_atrib[name] == "":
                lista_info.append("-")
            else:
                lista_info.append(dict_atrib[name])

        new_obj = CloudCtx()

        new_obj.name = lista_info[0]
        new_obj.tenant_name = lista_info[1]
        new_obj.description = lista_info[2]
        new_obj.name_alias = lista_info[3]
        new_obj.ctx_profile_name = lista_info[4]

        return new_obj


    @classmethod
    def display_info(cls, name_obj):
        print("MO contine: {} {} {} {} {}".format(name_obj.name, name_obj.tenant_name, name_obj.description,
                                                  name_obj.name_alias, name_obj.ctx_profile_name))



mo = PathInfo("C:/Users/Adrian23/Desktop/JOB/work - PC/info/exercise.txt")
mo.read_from_path()
mo.create_cloud_ctx_obj()
CloudCtx.display_info(CloudCtx.LISTA_CLOUD_CTX_OBJ[0])



#print(CloudCtx.LISTA_CLOUD_CTX_OBJ, end='\n')
#print(repr(CloudCtx.LISTA_CLOUD_CTX_OBJ[0]))




