# Implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. 
# If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. 
# And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, 
# it’s time for breakfast.

# breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00.

def main():
    time = input("What time is it? ")
    convert(time)
           
def convert(time):
    hours, minutes = time.split(":")
    minutes = round(int(minutes) * 1/6)
    time = float(hours + "." + str(minutes))
    if 7.0 <= time <= 8.0:
        print("brakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time.")

if __name__ == "__main__":
    main()

main()
