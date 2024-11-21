def count_heat_waves(temperatures):
    heat_wave_count = 0
    consecutive_days = 0
    for temp in temperatures:
        if temp > 30:
            consecutive_days += 1
            if consecutive_days == 3:  
                heat_wave_count += 1
        else:
            consecutive_days = 0  # Reset 
    return heat_wave_count

def find_longest_cold_streak(temperatures):
    longest_streak = 0
    current_streak = 0
    for temp in temperatures:
        if temp < 15:
            current_streak += 1
            longest_streak = max(longest_streak, current_streak)
        else:
            current_streak = 0  # Reset 
    return longest_streak

def calculate_average_temperature(temperatures):
    return sum(temperatures) / len(temperatures)

def main():
    # Step 1: Input  temperatures
    temp_input = input("Enter temperatures for each day separated by space: ")
    temperatures = list(map(int, temp_input.split()))
    
    # Step 2: Analyze  data
    heat_wave_count = count_heat_waves(temperatures)
    longest_cold_streak = find_longest_cold_streak(temperatures)
    average_temperature = calculate_average_temperature(temperatures)
    
    # Step 3: Display results
    print(f"Number of heat waves: {heat_wave_count}")
    print(f"Longest cold streak: {longest_cold_streak} days")
    print(f"Average temperature: {average_temperature:.2f}°C")

# Run the program
if __name__ == "__main__":
    main()
