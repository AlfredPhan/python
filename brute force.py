#Program for Brute force Hacking of Caesar Algorithm
message = "UDYMTS"
#message = "UDZ WKLV VLGH" #encrypted message
Letters = "ABCDEFGHIJKLMNOPQRTUVWXYZ"
for key in range(len(Letters)):
    translated = ''
    for ch in message:
        if ch in Letters:
            num = Letters.find(ch) #to find the array position
            num = num - key #formula for fiding the shift values
            if num < 0:
                num = num + len(Letters)
            translated = translated + Letters[num]
        else:
            translated = translated + ch
    print("Hacking key is %s: %s" % (key,translated))
