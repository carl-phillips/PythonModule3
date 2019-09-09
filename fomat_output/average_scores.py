def average(score1, score2, score3):
    return (int(score1) + int(score2) + int(score3)) / 3


def main():
    fname = input("Your first name: ")
    lname = input("Your last name: ")
    age = input("Your age: ")
    score1 = input("First score: ")
    score2 = input("Second score: ")
    score3 = input("Third score: ")
    avg = average(score1, score2, score3)
    print(fname + ' ' + lname + ', your average score is: ' + str(avg));


main()
