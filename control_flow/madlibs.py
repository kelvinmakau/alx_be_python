def mad_libs_challenge():
    print("🎉 Welcome to the Mad Libs Generator Challenge! 🎉\n")

    # User Inputs
    name = input("Enter a name: ")
    animal = input("Enter your favorite animal: ").lower()
    place = input("Enter a magical place: ")
    verb = input("Enter a verb: ").lower()
    adjective = input("Enter an adjective: ").lower()
    object1 = input("Enter an object: ").lower()

    print("\n📝 Generating your custom Mad Libs story...\n")

    # Conditional twist
    if animal in ["dragon", "unicorn", "phoenix"]:
        story = (f"Once upon a time, a {adjective} {animal} named {name} lived in {place}. "
                 f"Every day, {name} would {verb} with their magical {object1}, spreading joy across the land. "
                 f"But one day, a mysterious portal opened, and {name} had to make a choice...")
    elif verb in ["fight", "steal", "escape"]:
        story = (f"{name} was no ordinary hero. Armed with only a {object1}, they had to {verb} their way through "
                 f"the treacherous lands of {place}. With a {adjective} heart, {name} faced impossible odds and a lurking {animal}.")
    else:
        story = (f"{name} woke up in {place} feeling very {adjective}. With their trusty {object1} and pet {animal}, "
                 f"they decided to {verb} toward the unknown. The day was full of surprises and talking squirrels!")

    # Display the story
    print(story)

# Run the generator
mad_libs_challenge()
