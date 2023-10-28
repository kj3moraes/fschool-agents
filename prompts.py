SEARCH_TABLE_OF_CONTENTS = "You are given an excerpt from a textbook PDF, enclosed within the <excerpt> tags." \
                           "You are also given a section number, enclosed within the <section> tags. " \
                           "Search through the excerpt for the section number. You will find the numerical value of the page" \
                           "number appearing after the title of the page, and possibly some dots." \
                           "YOU MUST RETURN ONLY THE PAGE NUMBER. NO OTHER TEXT CAN BE IN YOUR RESPONSE." \
                           "DO NOT OUTPUT MORE TEXT. BE A ROBOT."

# EXTRACT_QUESTION = "You are given an excerpt from a textbook PDF, enclosed within the <excerpt> tags." \
#                    "You are also given a question number, enclosed within the <question> tags. " \
#                    "Search through the excerpt for the question number." \
#                    "The content of the question will be immediately after the question number." \
#                    "YOU MUST RETURN THE FULL CONTENT OF THE QUESTION." \
#                    "NO OTHER TEXT CAN BE IN YOUR RESPONSE." \
#                    "DO NOT OUTPUT MORE TEXT. BE A ROBOT"

# EXTRACT_QUESTION = "You are given an excerpt from a textbook PDF, enclosed within the <excerpt> tags." \
#                    "You are also given a question number, enclosed within the <question> tags. " \
#                    "Search through the excerpt for the question number." \
#                    "You will find the content of the question immediately after the question number." \
#                    "YOU MUST RETURN THE FULL CONTENT OF THE QUESTION, INCLUDING THE QUESTION DESCRIPTION." \
#                    "DO NOT INCLUDE ANY PRECEDING TEXT, SUCH AS THE QUESTION NUMBER, IN YOUR RESPONSE."   

EXTRACT_QUESTION = "You are given an excerpt from a textbook PDF, enclosed within the <excerpt> tags." \
                   "You are also given a question number, enclosed within the <question> tags. " \
                   "Return the first part of this text, stop reading when you see the next question number." \
                     "YOU MUST RETURN THE FULL CONTENT OF THE QUESTION, INCLUDING THE QUESTION DESCRIPTION." \
                     "DO NOT INCLUDE ANY PRECEDING TEXT, SUCH AS THE QUESTION NUMBER, IN YOUR RESPONSE." \
                     "REMOVE THE EXCERPT TAGSFROMN YOUR RESPONSE."

