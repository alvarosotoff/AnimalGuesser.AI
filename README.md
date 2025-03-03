# **Animal Quiz - README**

## Summary
**Animal Quiz** is an interactive Python application that uses a series of yes/no questions to identify an animal. Built with Tkinter, the program progressively filters a dataset of animals based on user responses. If no match is found, users can contribute by adding their animal to improve the database. This project is part of the **Building AI course project**.

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

This here it's just because the bot checking the summarys in the READMEs doesn't find my Summary so I have to copy the given one down here.
<!-- This is the markdown template for the final project of the Building AI course, 
created by Reaktor Innovations and University of Helsinki. 
Copy the template, paste it to your GitHub README and edit! -->

# Project Title

Final project for the Building AI course

## Summary

Describe briefly in 2-3 sentences what your project is about. About 250 characters is a nice length! 


## Background

Which problems does your idea solve? How common or frequent is this problem? What is your personal motivation? Why is this topic important or interesting?

This is how you make a list, if you need one:
* problem 1
* problem 2
* etc.


## How is it used?

Describe the process of using the solution. In what kind situations is the solution needed (environment, time, etc.)? Who are the users, what kinds of needs should be taken into account?

Images will make your README look nice!
Once you upload an image to your repository, you can link link to it like this (replace the URL with file path, if you've uploaded an image to Github.)
![Cat](https://upload.wikimedia.org/wikipedia/commons/5/5e/Sleeping_cat_on_her_back.jpg)

If you need to resize images, you have to use an HTML tag, like this:
<img src="https://upload.wikimedia.org/wikipedia/commons/5/5e/Sleeping_cat_on_her_back.jpg" width="300">

This is how you create code examples:
```
def main():
   countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
   pop = [5615000, 5439000, 324000, 5080000, 9609000]   # not actually needed in this exercise...
   fishers = [1891, 2652, 3800, 11611, 1757]

   totPop = sum(pop)
   totFish = sum(fishers)

   # write your solution here

   for i in range(len(countries)):
      print("%s %.2f%%" % (countries[i], 100.0))    # current just prints 100%

main()
```


## Data sources and AI methods
Where does your data come from? Do you collect it yourself or do you use data collected by someone else?
If you need to use links, here's an example:
[Twitter API](https://developer.twitter.com/en/docs)

| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |

## Challenges

What does your project _not_ solve? Which limitations and ethical considerations should be taken into account when deploying a solution like this?

## What next?

How could your project grow and become something even more? What kind of skills, what kind of assistance would you  need to move on? 


## Acknowledgments

* list here the sources of inspiration 
* do not use code, images, data etc. from others without permission
* when you have permission to use other people's materials, always mention the original creator and the open source / Creative Commons licence they've used
  <br>For example: [Sleeping Cat on Her Back by Umberto Salvagnin](https://commons.wikimedia.org/wiki/File:Sleeping_cat_on_her_back.jpg#filelinks) / [CC BY 2.0](https://creativecommons.org/licenses/by/2.0)
* etc
