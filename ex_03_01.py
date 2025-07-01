sh = input('Enter a Hours: ')
sr = input('Enter a Rate: ')
fh = float(sh)
fr = float(sr)
# print(fh, fr)
if fh > 40:
    # print('Overtime')
    reg = fh * fr
    otp = (fh - 40) * (fr * 0.5)
    # print(reg, otp)
    xp = reg + otp  
else:
    # print('Regular time')  
    xp = fh * fr
print('Pay:', xp)