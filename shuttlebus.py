from datetime import datetime, timedelta

n = int(input())
t = int(input())
m = int(input())

timetable = list(
    map(str, input().replace('“', '').replace('”', '').replace('[', '').replace(']', '').replace(' ', '').split(',')))
crew_arrive_list = [datetime.strptime(date, '%H:%M') for date in timetable]
crew_boarding_dic = {}
crew_last_boarding_date = None
start_boarding_date = datetime.strptime('09:00', '%H:%M')

for i in range(n):
    if i != 0:
        first = start_boarding_date + timedelta(minutes=(i - 1) * t)
    else:
        first = datetime.strptime('00:00', '%H:%M')
    last_boarding_date = start_boarding_date + timedelta(minutes=i * t)
    for arrive_date in sorted(crew_arrive_list):
        if (arrive_date - last_boarding_date).total_seconds() <= 0 < (arrive_date - first).total_seconds():
            crew_last_boarding_date = last_boarding_date
            if last_boarding_date in crew_boarding_dic:
                crew_boarding_dic[last_boarding_date] += 1
            else:
                crew_boarding_dic[last_boarding_date] = 1

if crew_last_boarding_date is None or crew_boarding_dic[crew_last_boarding_date] < m:
    con_boarding_time = (start_boarding_date + timedelta(minutes=(n - 1) * t)).strftime('%H:%M')
else:
    con_boarding_time = (sorted(crew_arrive_list)
                         [sum(crew_boarding_dic.values()) - crew_boarding_dic[crew_last_boarding_date] + m - 1] 
                         + timedelta(minutes=-1)).strftime('%H:%M')

print(con_boarding_time)
