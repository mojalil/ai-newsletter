from datetime import datetime
from crewai import Task


class AINewsLetterTasks():
    def fetch_news_task(self, agent):
        return Task(
            description=f'Fetch top Venture Capital news stories from the past 24 hours. The current time is {datetime.now()}.',
            agent=agent,
            async_execution=True,
            expected_output="""A list of top Venture Capital news story titles, URLs, and a brief summary for each story from the past 24 hours. 
                Example Output: 
                [
                    {  'title': 'Venture Capital Firm invests $100M in AI Startup', 
                    'url': 'https://example.com/story1', 
                    'summary': 'A large splash in venture today when  ...'
                    }, 
                    {{...}}
                ]
            """
        )
    
    def analyze_news_task(self, agent, context):
        return Task(
            description='Analyze each news story and ensure there are at least 5 well-formatted articles',
            agent=agent,
            async_execution=True,
            context=context,
            expected_output="""A markdown-formatted analysis for each news story, including a rundown, detailed bullet points, 
                and a "Why it matters" section. There should be at least 5 articles, each following the proper format.
                Example Output: 
                '## Venture Capital firm takes spotlight by investing $100M \n\n
                **The Rundown:
                ** 100M invested into AI startup made a splash in today ...\n\n
                **The details:**\n\n
                - Sequoia Capital poured 100M into AI assistants in this year alone...\n\n
                **Why it matters:** While AI-related investments have been rampant over the last year, this shows there is still a huge appitite to fund various AI companies.\n\n'
            """
        )
    
    def compile_newsletter_task(self, agent, context, callback_function):
        return Task(
            description='Compile the newsletter',
            agent=agent,
            context=context,
            expected_output="""A complete newsletter in markdown format, with a consistent style and layout.
                Example Output: 
                '# Top stories in Venture Capital today today:\\n\\n
                - Venture Capital firm takes spotlight by investing $100M\\n
                - Altman seeks TRILLIONS for global AI chip initiative\\n\\n

                ## Venture Capital firm takes spotlight by investing $100M\\n\\n
                **The Rundown:** AI made a splash in this year\'s Super Bowl commercials...\\n\\n
                **The details:**...\\n\\n
                **Why it matters::**...\\n\\n
                ## Altman seeks TRILLIONS for global AI chip initiative\\n\\n
                **The Rundown:** OpenAI CEO Sam Altman is reportedly angling to raise TRILLIONS of dollars...\\n\\n'
                **The details:**...\\n\\n
                **Why it matters::**...\\n\\n
            """,
            callback=callback_function
        )