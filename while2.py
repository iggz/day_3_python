# Prompt user over and over and over again
# but if they say "bye" three times
# just exit the program

# Set our bye_count to zero, no one has said anything yet...

bye_count = 0

while bye_count < 3:
    # Initial condition is set to True
    should_run = True

    # Use that condition as part of the 'while'
    while should_run:
        user_input = input("What? ")
        print("%s" % (user_input))
        if user_input == "bye":
            should_run = False

            # Reassigning buy_count using its previous value
            bye_count = bye_count + 1
        print(bye_count)