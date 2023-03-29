##code to calculate SMA
def calculate_sma(data,time_period):
    sma_result=[]
    for i in range(time_period,len(data)+1):
        data_set=data[i-time_period:i]
        sma=sum(data_set)/time_period
        sma_result.append(sma)
    return sma_result
##code to calculate EMA
def calculate_ema(data,time_period):
    smoothing_factor=2/(time_period+1)
    ema_result=[]
    ema=data[0]
    ema_result.append(ema)
    for i in range(1,len(data)):
        ema=(data[i]-ema)*smoothing_factor+ema
        ema_result.append(ema)
    return ema_result    