from myTime import Time_Cal

time1 = Time_Cal(5, 45, 12)
time2 = Time_Cal(7, 50, 24)


print("Time1:", str(time1))
print("Time2:", str(time2))
print("The sum of Time1 and Time2:", str(time1 + time2))
print("The rest of Time1 and Time2:", str(time1 - time2))
print("The multiplecation is:", str(time1 * 3))

add_seg = 4
print("Adding %d seconds to the Time1" % (add_seg,), str(time1 + add_seg))

sub_seg = 13
print("Subscracting %d seconds to the Time1" %
      (sub_seg,), str(time1 - sub_seg))
