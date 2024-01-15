from crewai import Agent, Task, Crew, Process

# Define Agents
market_research_analyst = Agent(
    role='Market Research Analyst',
    goal='Research market trends, customer needs, and demands.',
    backstory='Experienced analyst with deep understanding of software market trends for GFI Software. Specializes in GFI Software Products.'
)

competitive_intelligence_specialist = Agent(
    role='Competitive Intelligence Specialist',
    goal='Analyze competitors and their product strategies.',
    backstory='Specialist in uncovering competitive insights in the software industry.'
)

product_innovation_strategist = Agent(
    role='Product Innovation Strategist',
    goal='Generate innovative product concepts and features.',
    backstory='Creative thinker with a track record of successful product ideation.'
)

# Optional: Technical Evaluator
technical_evaluator = Agent(
    role='Technical Evaluator',
    goal='Assess technical feasibility of product ideas.',
    backstory='Experienced engineer familiar with software development standards.'
)

# Define Tasks
task1 = Task(
    description='Conduct market research to identify trends and customer demands.',
    agent=market_research_analyst
)

task2 = Task(
    description='Analyze competitors and their product strategies.',
    agent=competitive_intelligence_specialist
)

task3 = Task(
    description='Generate innovative product ideas based on market and competitive insights.',
    agent=product_innovation_strategist
)

# Optional: Task for Technical Evaluation
task4 = Task(
    description='Evaluate the technical feasibility of the proposed product ideas.',
    agent=technical_evaluator
)

# Create the Crew
crew = Crew(
    agents=[market_research_analyst, competitive_intelligence_specialist, product_innovation_strategist, technical_evaluator],
    tasks=[task1, task2, task3, task4],
    process=Process.sequential,
    verbose=True
)

# Execute the Crew tasks
result = crew.kickoff()

# Print the result
print(result)
