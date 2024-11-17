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
def count_entries_and_words():
        with open('journal.txt', 'r') as file:
            entries = file.readlines()
            
            num_entries = len(entries)
            
            num_words = sum(len(line.split()) for line in entries)
            
            print(f"Total number of entries: {num_entries}")
            print(f"Total number of words: {num_words}")
    
count_entries_and_words()
