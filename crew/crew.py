from crewai import Crew
from agents.agents import question_creator, difficulty_checker, formatter
from tasks.tasks import create_tasks

def run_crew(subject, class_name):
    tasks = create_tasks(subject, class_name)

    crew = Crew(
        agents=[question_creator, difficulty_checker, formatter],
        tasks=tasks,
        verbose=True
    )

    result = crew.kickoff()
    return result