#Program No.9 Increment inside the range condition
#break statement -> to stop the control immediately
line = int(input("How many lines? "))
for counter in range(1,line+1,2):
    print(f"This is line {counter}")
    if counter == 10: #Tới đây nó sẽ break
        #continue
        break

print()
input("Press return to continue ...")

while True:
    user_input = input("Nhập vào một số nguyên: ")
    if user_input.isdigit():
        # Nếu chuỗi chỉ chứa số, thoát khỏi vòng lặp và xử lý tiếp.
        break
    else:
        print("Hãy nhập một số nguyên hợp lệ!")
