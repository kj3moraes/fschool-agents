from datetime import datetime

from pydantic import BaseModel, PositiveInt



pdf_data = """
18.443 Problem Set 3 Spring 2015
Statistics for Applications
Due Date: 2/27/2015
prior to 3:00pm

Problems from John A. Rice, Third Edition. [Chapter.Section.Problem]

1. Problem 8.10.21.

2. Problem 8.10.45. A Random walk Model for Chromatin
Only parts (a) through (g). See R script file “Rproject3.script4.Chromatin.r” in Rproject3. You can edit this file for your answers; turn in hard-copy of an html file compiled by creating a “notebook” from the script (press the button on the script window that looks like a notebook). Circle/highlight your answers on the hard-copy.

3. Problem 8.10.51 Double Exponential (Laplace) Distribution

4. Problem 8.10.58 Gene Frequencies of Haptoglobin Type See R Script file “Rproject3.script1.multinomial.simulation.r” in Rproject3. You can edit this file for your answers; turn in hard-copy of an html file compiled by creating a “notebook” from the script (press the button on the script window that looks like a notebook). Circle/highlight your answers on the hard-copy.

1

MIT OpenCourseWare
http://ocw.mit.edu

18.443 Statistics for Applications
Spring 2015

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

"""

class ProblemSet(BaseModel):
    # data: {
    #     textbook_name: str
    #     textbook_author: str
    # }
    # problem_chapter_section_and_problem: dict[str, str]  


external_data = {
    'id': 123,
    'signup_ts': '2019-06-01 12:22',  
    'tastes': {
        'wine': 9,
        b'cheese': 7,  
        'cabbage': '1',  
    },
}

problemSet = ProblemSet(pdf_data)
print(problemSet)
print(problemSet.model_dump())  