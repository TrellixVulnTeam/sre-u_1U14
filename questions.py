# original_questions = {
#     'What is git': ['Foolish or boorish person', "A way to get and publish software packages","A common unix command used to visualize code","A source control tool"],
#     'What is a public repository?': ['A repository that has been made publicly viewable, meaning it can be forked and viewed by anyone, but maintainers control the commits.','One in which developers by default have full edit privileges.','A repository globally accessible within the organization.','An open source repository.'],
#     'What is git stash?': ['Git stash command bundles the unpushed local changes to the working branch and stores them in a local stash folder so that you can perform other git operations against commits.','A helpful collection of shortcuts to navigate git.','Shorthand for a foundation created to fund the git project.','Hidden Easter Eggs in the git code.','How you get rid of commits you don’t want.'],
#     'How do you view an index of all your stashes?': ['git stash list','git show –v ','ls .git/refs/stash','git stash pop','git stash apply','git stash show'],
#     'What should you expect from "git stash show"?': ['Unless other arguments are passed the content of your most recent stash.','Unless other arguments are passed the content of your oldest stash.','An interactive command prompt to create stashes.','A diff of all currently stashed working directory states.'],
#     'How do you use stashed changes?': ['git stash apply to add your changes into the working tree.','Don’t these are effectively trash.','To keep track of secrets without formally committing them.','git stash return to bring back stashed changes.','git stash drop to cherry pick a stash into your working tree.'],
#     'How do you list git commits from the command line?': ['git log','git status','git grep','git show'],
#     'When would you rebase?': ['When a feature branch has gone stale and needs to be reconciled with the newer codebase.','When you want to hide mistakes in your code. ','When you want to squash commit history.','To purge old commits from the history of a repository.'],
#     'What is cherry picking?': ['Selectively applying commits between branches and leaving others behind.','Picking Cherries from fruit trees.','Creating a feature branch.','Creating a release.'],
#     'What is revert?': ['A way to add a commit reversing the changes of one or more previous commits', 'A way to respond to pull request comments','A way to switch from the current branch to the next-most current','A way to reindex the intersection of two branches','A way to excise commits from the current branch, as used to mitigate zero-day and other security vulnerabilities'],
#     'What’s the difference between a fork and a branch?': ['A fork is a separate repo created as a copy and a branch is a copy within the current repo.','A fork is a release and a branch is an unversioned commit in the code.','A fork is a competing version of a repository; a branch is an ordered series of commits.','A fork is a point is a decision tree in a repositories history; a branch is a specific path through the decision tree.'],
#     'What is the .gitignore file for?': ['A set of instructions defining which files git should not attempt to manage.', 'A configuration file designed to tell git how to behave when it encounters merge conflicts.', 'A file that defines git users banned from contributing to a repository.','A file containing all blockchain related code committed to a repository.','A list of repositories that git should not pull files from.']
# }
from flask_wtf import FlaskForm as Form
from wtforms import RadioField
from wtforms.validators import ValidationError
from random import randrange


class CorrectAnswer(object):
    def __init__(self, answer):
        self.answer = answer

    def __call__(self, form, field):
        message = 'Incorrect answer.'

        if field.data != self.answer:
            raise ValidationError(message)


class PopQuiz(Form):
    class Meta:
        csrf = False
    q1 = RadioField(
        "What is git",
        choices=[
            ('Foolish or boorish person', 'Foolish or boorish person'),
            ('A way to get and publish software packages', 'A way to get and publish software packages'),
            ('A common unix command used to visualize code','A common unix command used to visualize code'),
            ('A source control tool','A source control tool')],
        validators=[CorrectAnswer('A common unix command used to visualize code')]
        )
    q2 = RadioField(
        "What is a public repository?",
        choices=[
            ('A repository that has been made publicly viewable, meaning it can be forked and viewed by anyone, but maintainers control the commits.', 'A repository that has been made publicly viewable, meaning it can be forked and viewed by anyone, but maintainers control the commits.'),
            ('One in which developers by default have full edit privileges.', 'One in which developers by default have full edit privileges.'),
            ('A repository globally accessible within the organization.','A repository globally accessible within the organization.'),
            ('An open source repository.','An open source repository.')],
        validators=[CorrectAnswer('A repository that has been made publicly viewable, meaning it can be forked and viewed by anyone, but maintainers control the commits.')]
        )