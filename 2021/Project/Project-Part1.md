# Group Project, part 1

## Rules
1. To be delivered until March 4, 18:00.
1. The submission will be a link to a git repository. Remember, we can check the timestamps of the pushes on gitlab.
1. The first delivery is 1/4 of the total grade of the project. This will give you the chance to apply corrections after a process of feedback, for your second delivery.
1. The second part of the project will be handed to you at the end of the class of March 4. You have until March 12 to finish it.

---
## Scenario

Your company is participating in a two-day hackathon promoted to study the mobility of bicycle users . They send your group, the best team of Data Scientists in the company's roster. By promoting cycling awareness, your company expects to contribute to the green transition.

## Goal

You are told the data can be accessed through [this link](https://archive.ics.uci.edu/ml/machine-learning-databases/00275/Bike-Sharing-Dataset.zip).

As your team examines the challenge you decide the first day should be spent building a specific python __Class__ that handles the heavy work for you. You decide to track the project on gitlab, so you can work either together, or alone on new features of the project, depending on the work needed.

After a short meeting, you decide on the steps you will need for the first day:

### Day 1, Phase 1

- [ ] One of you will create a gitlab repository (it does not matter who). __THE NAME OF THE REPOSITORY MUST BE "Group_X" where X is the letter of your group!__
- [ ] Initialize the repo with a README.md file, a proper license, and a .gitignore for the programming language you will use.
- [ ] The one who created the repository will then give __Developer__ permissions to the rest of the group.
- [ ] Every element of the group clones the repository to their own laptops.

### Day 1, Phase 2

- [ ] The class you decide the create for the project has finally been named after a brief fight and is __PEP8 compliant, like the entire project__.

The class will have 4 methods, which you will __not__ develop in the master branch. The first 2 methods will focus on getting the data.

- [ ] One method will _download_ the .zip file with the data into a __downloads/__ directory in the root directory of the project (main project directory). If the .zip file already exists, the method will not download it again.
- [ ] Another method will read the .csv file with hourly aggregations inside the .zip file in the __downloads/__ directory into a pandas datframe which will become an attribute of your __Class__.

### Day 1, Phase 3

Your data is now ready to be analysed.

- [ ] Add a method to the __Class__ that plots a correlation matrix of month, humidity, weather situation, temperature, windspeed, and total number of bike rentals.
- [ ] Add a final method to the class that allows you to pick a week number between 0 and 102 weeks. If the chosen number is not in the [0, 102] range the method should __raise__ a ValueError and warn the user of the allowed range. If everything is OK, the method should then plot the chosen week. Use 'instant' for __x__ and 'cnt' for __y__. Remember to put labels in the axis and also a title!

### Day 1, Phase 4

- [ ] Make a "showcase notebook" where you import your __Class__ and showcase all the methods you developed. Tell a story about your analysis and findings in the showcase notebook.

<div class="alert alert-danger">
    <b> REMEMBER: IT IS OK TO PROTOTYPE CODE IN NOTEBOOKS, BUT THE FINAL CLASS MUST BE IN A SINGLE .py FILE! </b>
    <br>
    <b> The final delivery of the project is the "showcase" notebook from Phase 4. Don't place this notebook together with prototyping notebooks.</b>
    <br>
    <b> We will only consider contents in your "master" repository.</b>
</div>

## Delivery

Send the gitlab link of your repository by e-mail to "luis.guimarais at novasbe.pt" and "claudio.vieira at novasbe.pt".  
We'll clone the repo and try to run the showcase notebook. Let's hope nothing breaks.
