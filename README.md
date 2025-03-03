# **Animal Quiz - README**

## Summary
**Animal Quiz** is an interactive Python application that uses a series of yes/no questions to identify an animal. Built with Tkinter, the program progressively filters a dataset of animals based on user responses. If no match is found, users can contribute by adding their animal to improve the database.

## Project Description
**Animal Quiz** is a Python application built with Tkinter that attempts to identify an animal based on user responses to a series of yes/no questions. The program filters a dataset of animals and refines its guess with additional questions if necessary. If no match is found, users can provide the name of their animal to help improve the database.

## Features
- **Interactive quiz:** Users answer a set of predefined questions to identify an animal.
- **Multiple-choice answers:** Options include "Yes," "No," and "Don't Know" for greater flexibility.
- **Animal filtering:** The system progressively narrows down potential matches based on user responses.
- **Answer review:** Users can modify their answers before finalizing the guess.
- **Additional questions:** If the initial set of questions is insufficient, more questions are asked.
- **Graphical user interface:** Built with Tkinter for ease of use.

## Technologies Used
- Python
- Tkinter (for the graphical user interface)
- Pillow (for image handling)
- CSV (for storing animal data)
- Random (for selecting animals when unsure)

## Installation & Setup

### Prerequisites
Ensure you have Python installed on your system.

### Steps to Install and Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/animal-quiz.git
   cd animal-quiz
   ```
2. Install dependencies:
   ```bash
   pip install pillow
   ```
3. Run the application:
   ```bash
   python animal_quiz.py
   ```

## File Structure
- `animal_quiz.py` - Main application script
- `animals.csv` - Database of animals and their characteristics
- `Perry.png` - Easter egg image
- `Platypus.png` - Standard platypus image

## License
This project is licensed under the **MIT License** with an additional attribution requirement.

### Permissions
You are free to:
- Use, modify, and distribute the code for personal or commercial purposes.
- Include this project as part of your own work.

### Conditions
- **Attribution Required:** Any person or organization that uses, modifies, distributes, or sells this software **must provide clear credit to the original author, Álvaro Fernández Flórez (alvarosotoff)**. This includes:
  - Mentioning **Álvaro Fernández Flórez** in any public distribution.
  - Keeping this README file or including a similar notice referencing the original source.
  - Clearly stating that the project is based on this work if modified or integrated into another project.
- The original copyright notice must always be included.

### Limitations
This software is provided "as is," without warranty of any kind. The author is not responsible for any issues arising from its use.

