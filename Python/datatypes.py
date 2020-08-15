import numpy as np

start_usage = baywheels.memory_usage().sum() / 1024**2
print("Memory usage of baywheels dataframe is :",start_usage," MB")

#for col in ['duration_sec','start_station_latitude', 'start_station_longitude', 'end_station_latitude', 'end_station_longitude']:

    #datetime:
    try:
        df[col] = pd.to_datetime(df[col])
    except ValueError:
        pass

    #bool:
    if (df[col].unique() == ['True', 'False']).all() | (df[col].unique() == [1,0]).all():
        df[col] = df[col].astype(np.bool_)

    #category:
    if (df[col].nunique() / df.shape[0]) <= 0.2:
        df[col] = df[col].astype('category')

    IsInt = False
    mx = baywheels[col].max()
    mn = baywheels[col].min()
            
    if IsInt:
         if mn >= 0:
            if mx < 255:
                baywheels[col] = baywheels[col].astype(np.uint8)
            elif mx < 65535:
                baywheels[col] = baywheels[col].astype(np.uint16)
            elif mx < 4294967295:
                baywheels[col] = baywheels[col].astype(np.uint32)
            else:
                baywheels[col] = baywheels[col].astype(np.uint64)
        else:
            if mn > np.iinfo(np.int8).min and mx < np.iinfo(np.int8).max:
                baywheels[col] = baywheels[col].astype(np.int8)
            elif mn > np.iinfo(np.int16).min and mx < np.iinfo(np.int16).max:
                baywheels[col] = baywheels[col].astype(np.int16)
            elif mn > np.iinfo(np.int32).min and mx < np.iinfo(np.int32).max:
                baywheels[col] = baywheels[col].astype(np.int32)
            elif mn > np.iinfo(np.int64).min and mx < np.iinfo(np.int64).max:
                baywheels[col] = baywheels[col].astype(np.int64)    
    else:
        baywheels[col] = baywheels[col].astype(np.float32)

#################################################################################

# the main function:
import numpy as np
def reduce_mem_usage(props):
    start_mem_usg = props.memory_usage().sum() / 1024**2 
    print("Memory usage of properties dataframe is :",start_mem_usg," MB")
    NAlist = [] # Keeps track of columns that have missing values filled in. 
    for col in props.columns:
        if props[col].dtype != object:  # Exclude strings
            
            # Print current column type
            print("******************************")
            print("Column: ",col)
            print("dtype before: ",props[col].dtype)
            
            # make variables for Int, max and min
            IsInt = False
            mx = props[col].max()
            mn = props[col].min()
            
            # Integer does not support NA, therefore, NA needs to be filled
            if not np.isfinite(props[col]).all(): 
                NAlist.append(col)
                props[col].fillna(mn-1,inplace=True)  
                   
            # test if column can be converted to an integer
            asint = props[col].fillna(0).astype(np.int64)
            result = (props[col] - asint)
            result = result.sum()
            if result > -0.01 and result < 0.01:
                IsInt = True

            
            # Make Integer/unsigned Integer datatypes
            if IsInt:
                if mn >= 0:
                    if mx < 255:
                        props[col] = props[col].astype(np.uint8)
                    elif mx < 65535:
                        props[col] = props[col].astype(np.uint16)
                    elif mx < 4294967295:
                        props[col] = props[col].astype(np.uint32)
                    else:
                        props[col] = props[col].astype(np.uint64)
                else:
                    if mn > np.iinfo(np.int8).min and mx < np.iinfo(np.int8).max:
                        props[col] = props[col].astype(np.int8)
                    elif mn > np.iinfo(np.int16).min and mx < np.iinfo(np.int16).max:
                        props[col] = props[col].astype(np.int16)
                    elif mn > np.iinfo(np.int32).min and mx < np.iinfo(np.int32).max:
                        props[col] = props[col].astype(np.int32)
                    elif mn > np.iinfo(np.int64).min and mx < np.iinfo(np.int64).max:
                        props[col] = props[col].astype(np.int64)    
            
            # Make float datatypes 32 bit
            else:
                props[col] = props[col].astype(np.float32)
            
            # Print new column type
            print("dtype after: ",props[col].dtype)
            print("******************************")
    
    # Print final result
    print("___MEMORY USAGE AFTER COMPLETION:___")
    mem_usg = props.memory_usage().sum() / 1024**2 
    print("Memory usage is: ",mem_usg," MB")
    print("This is ",100*mem_usg/start_mem_usg,"% of the initial size")
    return props, NAlist


#