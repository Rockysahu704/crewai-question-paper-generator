from crewai import Task
from agents.agents import question_creator, difficulty_checker, formatter

def create_tasks(subject, class_name):
    
    generate_questions = Task(
        description=f"""
        Generate a question paper for Class {class_name} {subject}.

        Include:
        - 5 questions of 2 marks
        - 5 questions of 4 marks
        - 3 questions of 10 marks
        """,
        agent=question_creator,
        expected_output="List of questions categorized by marks"
    )

    validate_questions = Task(
        description=f"""
        Review the {subject} questions for Class {class_name}.

        Ensure difficulty levels:
        - 2 marks = short
        - 4 marks = medium
        - 10 marks = long
        """,
        agent=difficulty_checker,
        expected_output="Validated questions"
    )

    format_paper = Task(
        description=f"""
        Format the {subject} question paper for Class {class_name}
        into clean exam format with sections A, B, C.
        """,
        agent=formatter,
        expected_output="Final formatted question paper"
    )

    return [generate_questions, validate_questions, format_paper]