from fpdf import FPDF

def generate_pdf(title, content):
    pdf = FPDF()
    pdf.add_page()
    
    # Set font and add title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, title, 0, 1, 'C')  # 'C' for center alignment
    
    # Set font for content
    pdf.set_font("Arial", size=12)
    
    for item in content:
        question = item['question']
        answer = item['answer']
        
        # Display question
        pdf.set_fill_color(220, 220, 220)  # light gray background for questions
        pdf.multi_cell(0, 10, question, 0, 'L', 1)  # 'L' for left alignment, 1 for filling the cell with the fill color
        
        # Display answer
        pdf.multi_cell(0, 10, answer)
        pdf.ln(5)  # space between Q&A pairs
    
    pdf.output("answer.pdf")

# Example Usage:
content = [
    {"question": "a. What is the capital of France?", "answer": "Answer: Paris."},
    {"question": "b. Which planet is known as the Red Planet?", "answer": "Answer: Mars."}
]

course_code = "13.012"
problem = "3"
title = f"Course Code: {course_code}, Problem {problem}"
generate_pdf(title, content)
