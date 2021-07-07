#Elijah Jedkins PSID: 1786452
def get_age():
    age = int(input())
    if (age >= 18 and age <= 75):
        return age
    else:
        # Raised exception for invalid ages
        raise ValueError("Invalid age.")


def fat_burning_heart_rate(age):
    # Will return the fat burning heart rate depending on the age given.
    return ((70 / 100) * (220 - age))

    return heart_rate


if __name__ == "__main__":

    try:
        age = get_age()
        # Will print out the age and the calculated fat burning heart rate
        print("Fat burning heart rate for a", age, "year-old:", fat_burning_heart_rate(age), "bpm")
    except ValueError as ag:

        print(ag.args[0])
        # If the age is not in the range the statement below is printed
        print("Could not calculate heart rate info.\n")

