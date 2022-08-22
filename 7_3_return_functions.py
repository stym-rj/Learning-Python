def seconds(hour, minute, seconds):
    sec=(hour*3600)+ (minute*60) + seconds
    return sec

time_a=seconds(5, 30, 50)
time_b=seconds(1, 10, 40)

sum= time_a+time_b

print(sum)