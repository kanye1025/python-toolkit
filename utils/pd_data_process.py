import pandas as pd
def supplement_missing(df,field_keys,value_defaults):
    df_out = pd.DataFrame({"__key__":[True]})

    for field,keys in field_keys.items():
        df_key = pd.DataFrame({field:keys})
        df_key["__key__"] = True
        df_out = pd.merge(df_out,df_key,on=["__key__"],how='outer')

    df_out  = pd.merge(df_out,df,on=list(field_keys.keys()),how='left')
    df_out.drop(columns=['__key__'],inplace=True)
    for field,default_value in value_defaults.items():
        df_out[field].fillna(default_value,inplace=True)
    return df_out