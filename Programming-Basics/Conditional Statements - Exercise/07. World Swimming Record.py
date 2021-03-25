record = float(input())
large = float(input())
time = float(input())
total_time = large * time
time_after = round(large // 15)
time_after_r = time_after * 12.5
total = total_time + time_after_r
if total < record:
    print(f" Yes, he succeeded! The new world record is {total:.2f} seconds.")
elif total >= record:
    no = abs(total - record)
    print(f"No, he failed! He was {no:.2f} seconds slower.")

