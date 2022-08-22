def convert_seconds(seconds):
    hour=seconds//3600
    minute= (seconds- hour*3600)//60
    remaining_second= seconds-minute*60- hour*3600
    return hour, minute, remaining_second

hours, minutes, seconds= convert_seconds(19800)
print(hours, minutes, seconds)