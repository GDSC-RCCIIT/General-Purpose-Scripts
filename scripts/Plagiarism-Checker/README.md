## Check Plagiarism between Two Texts

[![](https://img.shields.io/badge/Made_with-Python-red?style=for-the-badge&logo=python)](https://www.python.org/)
[![](https://img.shields.io/badge/Made_with-Scikit_Learn-blue?style=for-the-badge&logo=scikit-learn)](https://scikit-learn.org/)

### About
A Python script to check the Plagiarism based on Similarity Scores between Two Texts.

### Setup

* Install Python3 from [here](https://www.python.org/)
* Open Windows Command Prompt.
* Clone the repository
```bash
  git clone https://github.com/GDSC-RCCIIT/General-Purpose-Scripts.git
  ```
* Navigate inside the ```scripts/Plagiarism-Checker``` directory.
* Run this command
```bash
  pip install -r requirements.txt
  ```
* Now open the ```data.csv``` file.
* In the ```text1``` column and the ```text2``` column, add the Two Texts for which you want to find the Plagiarism (Similarity) Score.
* Now we are good to go.

Run using Python:
```bash
  python check_plagiarism.py
  ```

* An ```output.csv``` will be generated with an additional column named ```"similarity"``` that has the Plagiarism (Similarity) scores between the Two texts in that Row.
