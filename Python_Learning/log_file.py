import datetime


# Function to write a log entry

def write_log(file_path, message):

    """function that appends logs with timestamp"""
    try:
        with open(file_path, "a") as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestamp}+{message}\n")
        print(f"log: {message}")
    except Exception as e:
        print(f"error written log: {e}")

def read_log(file_path):
    """function that reads content from a file"""
    try:
        with open(file_path, "r") as file:
             print(f"\n..... log..............")

             for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("file does not exist / 404")

    except Exception as e:
        print(f"error written log: {e}")

if __name__== "__main__":
    log_file = "docs.txt"
    while True:
        print("\n log manager")
        print("1 Write log entry")
        print("2 Read all log entry")
        print("3 Exit")

        choice = input("Pick an option:")
        if choice == "1":
            log_message = input("Enter your log message:")
            write_log(log_file, log_message)
        elif choice == "2":
            read_log(log_file)
        elif choice == "3":
            print("Goodbye")
            break
        else:
            print("Invalid choice")
        

   