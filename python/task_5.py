# task_1
import datetime
# def write_journal_entries():
#     f = open("journal.txt", 'a')
#     current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     while True:
#              journal_entries = str(input("Enter your journal entry (or type 'exit' to stop): "))
#              f.write(f"[{current_time}] {journal_entries}\n")
#              if journal_entries.lower() == 'exit':
#                 print("Exiting journal log.")
#                 break
#     print(f"Entry logged at {current_time}")
#     f.close()
# write_journal_entries()

# task_2
# def journal_entries():
#     with open("journal.txt", 'r') as file:
#         for line in file:
#             print(line)
# journal_entries()

# task 3
# write_journal_entries()

# task 4
def read_journal_entries():
    try:
        # Open the journal.txt file in read mode
        with open("journal.txt", 'r') as file:
            count_line = 0  # To count the number of entries (lines)
            count_word = 0  # To count the total number of words

            # Iterate over each line in the file
            for line in file:
                count_line += 1  # Increment line count for each entry
                count_word += len(line.split())  # Increment word count by splitting the line into words

        # Print the total number of entries and words
        print(f"Total number of entries: {count_line}")
        print(f"Total number of words: {count_word}")

    except FileNotFoundError:
        print("No journal file found. Please create entries first.")

# Call the function to read the journal entries and count lines and words
read_journal_entries()
