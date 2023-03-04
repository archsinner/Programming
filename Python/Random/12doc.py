def main():
    # Create a list of 12 days of christmas
    days = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]
    # Create a list of gifts
    gifts = ["a partridge in a pear tree", "two turtle doves", "three french hens", "four calling birds", "five golden rings", "six geese a laying", "seven swans a swimming", "eight maids a milking", "nine ladies dancing", "ten lords a leaping", "eleven pipers piping", "twelve drummers drumming"]
    # Print the lyrics
    for i in range(len(days)):
        print("On the", days[i], "day of Christmas my true love gave to me:")
        for j in range(i, -1, -1):
            print(gifts[j])
        print()

# Call the main function
main()



    

