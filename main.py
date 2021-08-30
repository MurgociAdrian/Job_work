import argparse
import json
from datetime import datetime



if __name__ == "__main__":

        parser = argparse.ArgumentParser()
        parser.add_argument("path", help = "Give the json file path")
        args = parser.parse_args()

        with open(args.path, "r") as read_file:
            all_data = json.load(read_file)

        obj_list = all_data["imdata"]



def create_cloudctx_and_healthinst_obj(nr_max_obj, obj_list_name):

    while nr_max_obj > 0:

        item = obj_list_name[CloudCtx.NR_OF_CLOUD_CTX_OBJ_CREATED]
        CloudCtx.NR_OF_CLOUD_CTX_OBJ_CREATED += 1
        nr_max_obj -= 1

        hcloud_ctx_atrib = item["hcloudCtx"]["attributes"]
        health_atrib = item["hcloudCtx"]["children"]

        new_ctx_obj = CloudCtx()
        new_health_obj = HealthInst()

        new_ctx_obj.retrieve_info(hcloud_ctx_atrib)
        CloudCtx.add_obj(new_ctx_obj)

        new_health_obj.retrieve_info(health_atrib)
        HealthInst.add_obj(new_health_obj)

        new_ctx_obj.add_reference_to_health_inst(new_health_obj)



class CloudCtx:


    NR_OF_CLOUD_CTX_OBJ_CREATED = 0
    LIST_CLOUD_CTX_OBJ = []


    def __init__(self):

        self.name = " "
        self.tenant_name = " "
        self.description = " "
        self.name_alias = " "
        self.ctx_profile_name = " "
        self.last_modified = datetime(1900, 1, 1)
        self.reference_to_health_inst = None


    def __repr__(self):

        return """CloudCtx -> name: {}  tenant_name: {}  description: {}  name_alias: {}  ctx_profile_name: {} 
                  last_modif: {}  displayed_health: {} \n""".format(self.name, self.tenant_name, self.description,
                                                                    self.name_alias, self.ctx_profile_name,
                                                                    self.last_modified,
                                                                    self.reference_to_health_inst.displayed_health)


    @classmethod
    def add_obj(cls, ctx_obj):

       cls.LIST_CLOUD_CTX_OBJ.append(ctx_obj)


    def retrieve_info(self, hcloud_atrib_dict):

        self.name = CloudCtx.verify_empty(hcloud_atrib_dict, "name")
        self.tenant_name = CloudCtx.verify_empty(hcloud_atrib_dict, "tenantName")
        self.description = CloudCtx.verify_empty(hcloud_atrib_dict, "description")
        self.name_alias = CloudCtx.verify_empty(hcloud_atrib_dict, "nameAlias")
        self.ctx_profile_name = CloudCtx.verify_empty(hcloud_atrib_dict, "ctxProfileName")
        self.last_modified = (datetime.fromisoformat(hcloud_atrib_dict["modTs"][:19])).strftime("%d-%m-%Y %H:%M:%S %p")


    def add_reference_to_health_inst(self, health_obj):

        self.reference_to_health_inst = health_obj


    @staticmethod
    def verify_empty(hcloud_atrib_dict, atrib_name):

        if hcloud_atrib_dict[atrib_name] == "":
            return "-"
        else:
            return hcloud_atrib_dict[atrib_name]


    @classmethod
    def display_obj_in_order_by_cur_health(cls):

        list_cloud_ctx_obj_to_print = CloudCtx.LIST_CLOUD_CTX_OBJ.copy()
        list_cloud_ctx_obj_to_print.sort(key=lambda x: int(x.reference_to_health_inst.current_health))

        print(list_cloud_ctx_obj_to_print)


    @classmethod
    def display_obj_by_last_modify(cls):

        list_cloud_ctx_obj_to_print = CloudCtx.LIST_CLOUD_CTX_OBJ.copy()
        list_cloud_ctx_obj_to_print.sort(key=lambda x: datetime.strptime(x.last_modified,'%d-%m-%Y %H:%M:%S %p'), reverse = True)

        print(list_cloud_ctx_obj_to_print)



class HealthInst():


    LIST_HEALTH_OBJ = []


    def __init__(self):

        self.current_health = " "
        self.max_sev = " "
        self.displayed_health = " "


    def __repr__(self):

        return """healthInst -> cur: {}  maxSev: {}  disp_health: {}
               """.format(self.current_health, self.max_sev, self.displayed_health)


    @classmethod
    def add_obj(cls, health_obj):

        cls.LIST_HEALTH_OBJ.append(health_obj)


    def retrieve_info(self, health_val):

        if not health_val:
            self.current_health = "0"
            self.displayed_health = "Unhealthy"
        else:
            dict_atrib_health = health_val[0]["healthInst"]["attributes"]
            self.current_health = dict_atrib_health["cur"]
            self.max_sev = dict_atrib_health["maxSev"]

            if self.current_health == "100":
                self.displayed_health = "Healthy"
            elif int(self.current_health) < 100:
                self.displayed_health = "Unhealthy"
            else:
                self.displayed_health = "Error!"




create_cloudctx_and_healthinst_obj(3, obj_list)
create_cloudctx_and_healthinst_obj(2, obj_list)

#CloudCtx.display_obj_by_last_modify()

print(CloudCtx.LIST_CLOUD_CTX_OBJ)
print(HealthInst.LIST_HEALTH_OBJ)