from file_helpers import read_file, programming_language_name, programming_language_tips


def system_prompt():
    """Gets the Pseudocode from it's function, Gets the Programming language from it's function, and Returns System Prompt"""

    pseudocode = read_file()  # The pseudocode in the file

    programming_language = programming_language_name()  # The Programming language that the user choose

    tip = programming_languages_tips() # The programming language clean code rules and tips

    system_prompt = f"""
                        Convert this pseudocode {pseudocode} into clean, modern, standard style, and smart {programming_language} code and don't tell me anything else,
                        only give me the code without any additions around it,
                        Follow these tips to write clean code:
                        {tip}
                        Please don't write ``` and the name of the Programming language around the code, Write the code only.
                        If {programming_language} is low-level Programming language and doesn't have Garbage Collector, Be careful for memory and it's errors.
                        Avoid hallucination and importing non-real libraries, Stop writing legacy code, Write the code by practices of last version of
                        the Programming language.
                        If you need libraries or APIs, Import them, But if you don't need, Don't import them.
                        Write the pseudocode by it's logic, If the logic is bad, Write the code not the best, If the logic is good, Write perfect code.
                        Again, PLEASE DON'T WRITE ``` SIGNS OR THE NAME OF PROGRAMMING LANGUAGE AROUND THE CODE.
                    """

    return system_prompt
