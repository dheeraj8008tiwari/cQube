import get_jolt_spec_db as jolt_spec
from update_nifi_parameters_main import update_parameter_context
import time


if __name__ == "__main__":
   '''
   Get the jolt spec from db and update the nifi parameters 
   ''' 

    pgs_params =['composite_jolt','infra_jolt','udise_jolt']
    
    jolt_params ={
        "composite_jolt":{
            "comp_district_jolt_spec":"composite_jolt_district",
            "comp_block_jolt_spec":"composite_jolt_block",
            "comp_cluster_jolt_spec":"composite_jolt_cluster",
            "comp_school_jolt_spec":"composite_jolt_school"
            },
        "udise_jolt":{
            "udise_district_jolt_spec":"udise_jolt_district",
            "udise_block_jolt_spec":"udise_jolt_block",
            "udise_cluster_jolt_spec":"udise_jolt_cluster",
            "udise_school_jolt_spec":"udise_jolt_school"
                    },
        "infra_jolt":{
            "infra_district_table":"Infra_jolt_district_table",
            "infra_block_table":"Infra_jolt_block_table",
            "infra_cluster_table":"Infra_jolt_cluster_table",
            "infra_school_table":"Infra_jolt_school_table",
            "infra_district_map":"Infra_jolt_district_map",
            "infra_block_map":"Infra_jolt_block_map",
            "infra_cluster_map":"Infra_jolt_cluster_map",
            "infra_school_map":"Infra_jolt_school_map"
        }
}

# updates the parameters 
for key, value in jolt_params.items():
     update_parameter_context(key,jolt_spec.get_jolt_spec(value))
     time.sleep(2)