def pyramid(n, step = 1): #Recursion
    if step > n: #Base Case มีไว้หยุดการทำงาน ไม่ให้เกิด Recursion ไม่รู้จบ
        return ""
    return "  " * (n - step) + (str(step - 1) + " ") * (2 * step - 1) + "\n" + pyramid(n, step + 1)
    
#ค่าที่เปลี่ยนแปลงได้คือ step n ไม่เพิ่ม เพราะฉะนั้นแต่ละขั้นให้คิดโดยการเพิ่มหรีอลด step
#ตอนคิด "  " * (n - step) + (str(step - 1) + " ") * (2 * step - 1) + จะต้องคำนึงถึงบรรทัดแรกก่อน
inp = input("Enter number: ")
print(pyramid(int(inp)))
# Examples
# Input: 3
#       0
#     1 1 1
#   2 2 2 2 2