# [[(1100, 1150), (1530, 1620)], [], [(1100, 1150)], [], [(1100, 1150), (1530, 1620)], []]
# [['Helen C White', 'E-Hall'], [], ['Helen C White'], [], ['Helen C White', 'E-Hall'], []]
# [['LEC 069', 'DIS 001'], [], ['LEC 069'], [], ['LEC 069', 'DIS 001'], []]

times = [[(1100, 1150), (1530, 1620)], [], [(1100, 1150)], [], [(1100, 1150), (1530, 1620)], []]

times_1d  = [item for sub_list in times for item in sub_list]
print(times_1d)
#startTime = min(times))

print(startTime)