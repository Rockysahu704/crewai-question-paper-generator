from crewai import Agent
from config.llm import llm

question_creator = Agent(
    role="School Teacher",
    goal="Generate exam questions based on subject and marks",
    backstory="An experienced teacher who creates balanced exam papers.",
    llm=llm,
    verbose=True
)

difficulty_checker = Agent(
    role="Exam Moderator",
    goal="Ensure questions match difficulty level",
    backstory="Maintains exam standards.",
    llm=llm,
    verbose=True
)

formatter = Agent(
    role="Paper Formatter",
    goal="Format the question paper professionally",
    backstory="Creates structured exam papers.",
    llm=llm,
    verbose=True
)