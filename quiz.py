def quiz():
    q1 = input("What is 1+1?\na.1 b.11 c.69 d.3\n")
    if str(q1) == "a":
        print("Correct!")
        q2 = input("What does the mitocondria do?\na.Nothing b.Acts like the brain of the cell c.Its the powerhouse of the cell d.Stores protein\n")
        if str(q2) == "c":
            print("Correct!")
            return
        else:
            print("Incorrect!")
            return
    else:
        print("Incorrect!")
        return

quiz()