def day_number(date):
       month, day = map(int, date.split("-"))
       days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30,31]
       total = sum(days[:month - 1]) + day
       return total

arriveAlice = input("Alice arrival (MM-DD): ")
leaveAlice = input("Alice departure (MM-DD): ")
arriveBob = input("Bob arrival (MM-DD): ")
leaveBob = input("Bob departure (MM-DD): ")

start = max(day_number(arriveAlice), day_number(arriveBob))
end = min(day_number(leaveAlice), day_number(leaveBob))

print(max(0, end - start + 1))