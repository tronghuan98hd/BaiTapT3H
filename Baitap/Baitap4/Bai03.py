days_in_month = [(31, "Jan"), (28, "Feb"), (31, "Mar"),
                 (30, "Apr"), (31, "May"), (30, "Jun"),
                 (31, "Jul"), (31, "Aug"), (30, "Sep"),
                 (31, "Dec"), (30, "Oct"), (31, "Nov")]
input_ = 10;
if input_ not in range(1,12):
    print("mời bạn nhập lại")
else:
    print(days_in_month[input_ - 1])

#(31, 'Dec')
