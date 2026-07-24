class DailyDataHelper:
    def __init__(self, message):
        self.message = message
        print("Helper session started.")

    def show_message(self):
        print("Message in uppercase:", self.message.upper())

    def find_target_sum(self, numbers, target):
        print("\nChecking pairs that add up to", target)

        found = False
        for i, num1 in enumerate(numbers):
            for j, num2 in enumerate(numbers):
                if i < j and num1 + num2 == target:
                    print(f"Index {i} ({num1}) + Index {j} ({num2}) = {target}")
                    found = True

        if not found:
            print("No matching pair found.")

    def __del__(self):
        print("Helper session ended.")


message = input("Enter a message: ")

helper = DailyDataHelper(message)

helper.show_message()

numbers = [2, 7, 11, 15, 5, 3]
target = int(input("Enter target sum: "))

helper.find_target_sum(numbers, target)

del helper
