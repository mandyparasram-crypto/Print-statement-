Amount = int(input("Please enter amount for Withdrawal"))

note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10

print("notes of 100 rupes", note_1)
print("notes of  50 rupes", note_2)
print("notes of  10 rupes", note_3)