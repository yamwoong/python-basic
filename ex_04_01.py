def computepay(hours, rate):
    if hours > 40:
        reg = rate * hours
        otp = (hours - 40) * (rate * 0.5)
        pay = reg + otp
    else: 
        pay = hours * rate
    return pay

sh = input('Enter a Hours: ')
sr = input('Enter a Rate: ')
fh = float(sh)
fr = float(sr)

xp = computepay(fh, fr)

print('Pay:', xp)