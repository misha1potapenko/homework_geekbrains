duration = int(input('Введите количество секунд: '))

if duration < 60:
    print(str(duration) + ' сек')
if duration >= 60 and duration < 3600:
    min = duration // 60
    sec = duration % 60
    print(str(min) + ' мин ' + str(sec) + ' сек')
if duration >= 3600 and duration < 86400:
    hour = duration // 3600
    duration = duration - hour * 3600
    min = duration  // 60
    sec = duration % 60
    print(str(hour) + ' час ' + str(min) + ' мин ' + str(sec) + ' сек')
if duration >= 86400:
    day = duration // 86400
    duration = duration - day * 86400
    hour = duration // 3600
    duration = duration - hour * 3600
    min = duration // 60
    sec = duration % 60
    print(str(day) + ' дн ' + str(hour) + ' час ' + str(min) + ' мин ' + str(sec) + ' сек')
