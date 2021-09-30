# Welcome to the contributing guide

Thank you for showing interest in our project. Any contribution you make means a lot to us and will be reflected in the contributors tab on our repostiroy.

This document will give you a detailed overview over how to contribute to our project and have your Pull Request accepted. Please,make sure you have read through thisdocumentation and followed the correct steps before making your first Pull Request in our repository. If you fail to follow the steps mentioned here, it might lead to your Pull Request being declined.


## New contributors guide

See the [README](README.md) to get an overview of the project and find other necessary information. Here are some great resources to get you comfortable with open source contributions:
- [Finding ways to contribute to open source on GitHub](https://docs.github.com/en/get-started/exploring-projects-on-github/finding-ways-to-contribute-to-open-source-on-github)
- [Set up Git](https://docs.github.com/en/get-started/quickstart/set-up-git)
- [GitHub flow](https://docs.github.com/en/get-started/quickstart/github-flow)
- [Collaborating with pull requests](https://docs.github.com/en/github/collaborating-with-pull-requests)


## Linter

We use [black](https://github.com/psf/black) as the autolinter for our project. Make sure you have `black` installed on your local system and have run the linter on your code successfully before making a Pull Request. Our workflow test verifies if your coding has proper linting as per the standards set by `black`, unless our linting workflow passes for your Pull Request, it will not be merged. Read the below section to understand how to use `black` for properly formatting your code.


## Getting Started with Coding

The first thing you need to do is find an issue to work on. Go to Issues and find a suitable issue which you think you can handle and are willing to work on. Make sure you ask the maintainers to have the issue assigned to you before you start working on it.

Ok now that you have your issue assigned to you, it is time to start hacking!

**Step 1:** Fork the repository

**Step 2:** Clone the forked repository to your local machine with `git clone <repository link>`

**Step 3:** Add a remote (upstream) to your fork using: 
```
git remote add upstream https://github.com/GDSC-RCCIIT/General-Purpose-Scripts.git
```

**Step 4:** Synchronize your fork with upstream using the following commands:

```

$ git checkout main

$ git fetch upstream 

$ git merge upstream/main

$ git push origin main

```

**Step 5:** Make a branch with a suitable name relevant to the issue you are working on using `git branch <branch>`

**Step 6:** Switch your working branch from master to the newly created branch with `git checkout <branch>`

**Step 7:** Work on the changes. You can keep track of your branch and staging area using `git status`

**Step 8:** Make sure you run the `black` autolinter before you add your changes to the staging area. `black` can be installed on your local system using `pip install black`, and can be run with `black .` on all the files in your current working directory.

**Step 9:** Add all of the changes you made to the staging area before you commit with `git add .` 

**Step 10:** Commit your changes with a meaningful commit message using `git commit -m "commit message"`

**Step 11:** Finally push your changes to your forked repository using `git push origin <branch>`


## Making your first Pull Request

Once you have finished working on an issue and have pushed the changes to your forked repository, it is time to make your first pull request. Go to your forked repository on GitHub and it should show you an option to `Compare & pull request`. Click the `Compare & pull request` button and it will directly initiate a Pull Request for you, follow the Pull Request template and fill out the necessary information. Once that is done, click the `Create Pull Request` button.

Congratulations! you just created your first Pull Request. Now all you have to do is wait for the maintainers to review your Pull Request before it can be merged.


## Creating an Issue

In case of a bug report, feature request or a script request, you are free to open up an Issue for the maintainers and contributors. Go to the Issues tab and hit the `New Issue` button. Follow the Issue template corresponding to the type of your issue and fill up the required information. Once that is done press the `Submit new issue` button. Our maintainers will look into your issue and have it sorted as soon as possible once you have it submitted.
