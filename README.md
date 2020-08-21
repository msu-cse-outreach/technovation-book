# technovation-book

A RunestoneInteractive textbook for use with MSU's Technovation computer science outreach program.

Created by [Andrew McDonald](mailto:mcdon499@msu.edu),
[Hannah Striebel](mailto:striebe5@msu.edu),
[Zosha Korzecke](mailto:korzeck3@msu.edu),
[Sarah Swann](mailto:swannsar@msu.edu) with the
help of advisors [Dr. Laura Dillon](https://www.egr.msu.edu/people/profile/ldillon)
and [Teresa Isela Vandersloot](https://www.egr.msu.edu/people/profile/iselava1).

## Installation

To set up a working environment and contribute to the Runestone textbook, follow 
these steps:

1. Ensure you have Git and Python (version >= 3.6) installed, and have created a GitHub account.

1. Clone this repository with `git clone https://github.com/andrewmcdonald27/technovation-book.git`.

1. Navigate to the newly-created `technovation-book` folder with `cd technovation-book`
and run `python -m venv venv` (Windows) or `python3 -m venv venv` (Mac)
to establish a clean Python virtual environment.

1. Activate the Python virtual environment by running `venv/Scripts/activate.bat` (Windows) or
`source venv/bin/activate` (Mac/Linux) in the same command prompt.
Note that you will need to do this *every time* you
open a new command prompt, as Python will try to use your global (non-virtual) environment
by default. If you are using the csh / tsch shell on Mac/Linux, you may need to run
`source venv/bin/activate.csh` instead. Once the virtual environment is successfully activated
and in use, the command prompt will be prepended with `(venv)`.

1. Install the required Python dependencies by running `pip install -r requirements.txt` in the same
command prompt.

1. Test that you can build the textbook by running `runestone build` in the same command prompt.
You should receive a message ending with `Done, build successful.` if everything works properly.

1. Test that you can serve the textbook by running `runestone serve` in the same command prompt.
Open a browser and navigate to [localhost:8000](http://localhost:8000/) to see the textbook.
Stop the server with `CTRL+C` in the command prompt when finished.

1. Make and save a small change to the `_sources/index.rst` file, then repeat the two previous steps.
You should see your change reflected in the homepage.

1. Start editing the `.rst` file you'd like to edit, and enjoy the journey! Documentation of
Runestone's custom markup language can be found [here](https://runestone.academy/runestone/static/authorguide/index.html).

1. To push your local changes to the `technovation-book` repository, reach out to Andrew
with your GitHub username; he will add your account as a collaborator to the 
repository to grant edit access. Once you've been added as a collaborator, run the
standard git commands
```
git add .
git commit -m "your commit message here"
git push
```
and enter your GitHub credentials if prompted. Double check that the changes have been pushed
by navigating to the [homepage of the repository](https://github.com/andrewmcdonald27/technovation-book),
and celebrate!
