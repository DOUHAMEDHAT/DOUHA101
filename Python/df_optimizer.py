def optimizer(dataframe):
    start_memory = dataframe.memory_usage().sum() / 1024**2 
    print("Memory usage of dataframe is :",start_memory," MB")
    
    dataframe.drop_duplicates()
    
    start_frame = pd.DataFrame(columns=['column_name', 'start_type', 'start_usage_MB'])
    end_frame = pd.DataFrame(columns=['column_name', 'end_type', 'end_usage_MB'])

    for col in dataframe.columns:
        start_frame = start_frame.append({
            'column_name': dataframe[col].name, 
            'start_type': dataframe[col].dtype.name,
            'start_usage_MB': (dataframe.memory_usage()[col]/(1024**2))
        } ,ignore_index=True)
            
        if (list(dataframe[col].unique()) == ['True', 'False']) or (list(dataframe[col].unique()) == [1,0]):
            dataframe[col] = dataframe[col].astype('bool')
        elif dataframe[col].dtype == object:
            try:
                if pd.api.types.is_datetime64_any_dtype(pd.to_datetime(dataframe[col])):        
                    dt = pd.to_datetime(dataframe[col])
                    if (dt.dt.floor('d') == dt).all():
                        dataframe[col] = pd.to_datetime(dataframe[col], utc=False)
                    else:
                        dataframe[col] = pd.to_datetime(dataframe[col], utc=True)
            except:                            
                if dataframe[col].nunique() != dataframe[col].count():
                    dataframe[col] = dataframe[col].astype('category')
                else:
                    dataframe[col] = dataframe[col].astype('object')
        elif dataframe[col].dtype != object:
            if dataframe[col].astype('float64').all():
                result = (dataframe[col] - dataframe[col].fillna(0).astype(np.int64))
                result = result.sum()
                if result > -0.01 and result < 0.01:
                    mx = dataframe[col].max()
                    mn = dataframe[col].min()
                    if mn >= 0:
                        if mx < 255:
                            dataframe[col] = dataframe[col].astype(np.uint8)
                        elif mx < 65535:
                            dataframe[col] = dataframe[col].astype(np.uint16)
                        elif mx < 4294967295:
                            dataframe[col] = dataframe[col].astype(np.uint32)
                        else:
                            dataframe[col] = dataframe[col].astype(np.uint64)
                    else:
                        if mn > np.iinfo(np.int8).min and mx < np.iinfo(np.int8).max:
                            dataframe[col] = dataframe[col].astype(np.int8)
                        elif mn > np.iinfo(np.int16).min and mx < np.iinfo(np.int16).max:
                            dataframe[col] = dataframe[col].astype(np.int16)
                        elif mn > np.iinfo(np.int32).min and mx < np.iinfo(np.int32).max:
                            dataframe[col] = dataframe[col].astype(np.int32)
                        elif mn > np.iinfo(np.int64).min and mx < np.iinfo(np.int64).max:
                            dataframe[col] = dataframe[col].astype(np.int64)
                else:
                    mxf = dataframe[col].max()
                    mnf = dataframe[col].min()
                    if mnf > np.finfo(np.float16).min and mxf < np.finfo(np.float16).max:
                        dataframe[col] = dataframe[col].astype(np.float16)
                    elif mnf > np.finfo(np.float32).min and mxf < np.finfo(np.float32).max:
                        dataframe[col] = dataframe[col].astype(np.float32)
                    else:
                        dataframe[col] = dataframe[col].astype(np.float64)
        end_frame = end_frame.append({
            'column_name': dataframe[col].name, 
            'end_type': dataframe[col].dtype.name,
            'end_usage_MB': (dataframe.memory_usage()[col]/(1024**2))
        } ,ignore_index=True)              
    
    
    frame = start_frame.merge(end_frame, how='left')
    frame['%optimization'] = round(((frame['start_usage_MB'] - frame['end_usage_MB'])/frame['start_usage_MB'])*100.00,2)
    
    print("___MEMORY USAGE AFTER MODIFICATION:___")
    end_memory = dataframe.memory_usage().sum() / 1024**2 
    print("Memory usage is: ",end_memory," MB")
    print("This is ",100*end_memory/start_memory,"% of the initial size")
    print("The summary of dataframe optimization:")
    return frame
