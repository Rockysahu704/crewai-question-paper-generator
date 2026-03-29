from crew.crew import run_crew

if __name__ == "__main__":
    subject = input("Enter subject: ")
    class_name = input("Enter class: ")

    result = run_crew(subject, class_name)

    print("\n===== FINAL QUESTION PAPER =====\n")
    print(result)