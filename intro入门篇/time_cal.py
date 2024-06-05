with open('contents.md', 'r') as file:
    total_minutes = 0
    for line in file:
        if ':' in line:
            minutes, seconds = map(int, line.strip().split(':'))
            total_minutes += minutes + seconds / 60

hours = int(total_minutes // 60)
minutes = int(total_minutes % 60)
print(f"Total time: {hours}:{minutes:02d}")
