import streamlit as st
questions_dic = {
    'q1': {
        'question':'What is git?',
        'option1': 'Foolish or boorish person.',
        'option2': 'A way to get and publish software packages ',
        'option3': 'A common unix command used to visualize code.',
        'option4': 'A source control tool.',
        'answer': 'A source control tool.'
    },
    'q2': {
        'question':'What is a public repository?',
        'option1': 'One in which developers by default have full edit privileges.',
        'option2': 'A repository globally accessible within the organization.',
        'option3': 'A repository that has been made publicly viewable, meaning it can be forked and viewed by anyone, but maintainers control the commits.',
        'option4': 'An open source repository.',
        'answer': 'A repository that has been made publicly viewable, meaning it can be forked and viewed by anyone, but maintainers control the commits.'
    },
    'q3': {
        'question':'How can main branches be used?',
        'option1': 'As the location for every commit to the repository of code by developers.',
        'option2': 'As the branch where only stable tested code is committed and released from.',
        'option3': 'To be used a honeypot to misdirect bad actors and bots.',
        'option4': 'The default first branch for any repository, but it can be removed or renamed per developer preferences. ',
        'answer' : 'As the location for every commit to the repository of code by developers.\nTo be used a honeypot to misdirect bad actors and bots.\n\nThe default first branch for any repository, but it can be removed or renamed per developer preferences. ',
        'Reason' : ' There’s no programmatic reason to have a branch named main, it’s just a default–you can change this default and rename it at any time. The usage of it can be customized to any workflow a developer or organization desires. The correct answers here outline the most common usage patterns.'
    },
    'q4': {
        'question':'How would you resolve a merge conflict?',
        'option1': 'By deleting your repository and pulling down a new version.',
        'option2': 'Hard reset your local files to HEAD.',
        'option3': 'Visually review the diffs and select which is correct via an IDE or GUI or command line interactive prompt.',
        'option4': 'By setting default behavior for merge conflicts. ',
        'option5': 'By creating a Pull Request and giving it to a senior resource to review.',
        'option6': 'Revert changes, rebase, and merge again.',
        'answer' : 'Visually review the diffs and select which is correct via an IDE or GUI or command line interactive prompt.\nBy creating a Pull Request and giving it to a senior resource to review.\n\nRevert changes, rebase, and merge again.'
    },
    'q5': {
        'question':'What is git stash?',
        'option1': 'A helpful collection of shortcuts to navigate git.',
        'option2': 'Shorthand for a foundation created to fund the git project.',
        'option3': 'Hidden Easter Eggs in the git code.',
        'option4': 'How you get rid of commits you don’t want.',
        'option5': 'Git stash command bundles the unpushed local changes to the working branch and stores them in a local stash folder so that you can perform other git operations against commits.',
        'answer' : 'Git stash command bundles the unpushed local changes to the working branch and stores them in a local stash folder so that you can perform other git operations against commits.'
    },
    'q6': {
        'question':'How do you view an index of all your stashes?',
        'option1': 'git show –v ',
        'option2': 'ls .git/refs/stash',
        'option3': 'git stash pop',
        'option4': 'git stash apply',
        'option5': 'git stash show',
        'option6': 'git stash list',
        'answer' : 'git stash list'
    },
    'q7': {
        'question':'What should you expect from ‘git stash show’?',
        'option1': 'Unless other arguments are passed the content of your most recent stash.',
        'option2': 'Unless other arguments are passed the content of your oldest stash.',
        'option3': 'An interactive command prompt to create stashes.',
        'option4': 'A diff of all currently stashed working directory states.',
        'answer' : 'Unless other arguments are passed the content of your most recent stash.'
    },
    'q8': {
        'question':'How do you use stashed changes?',
        'option1': 'Don’t these are effectively trash.',
        'option2': 'To keep track of secrets without formally committing them.',
        'option3': 'git stash apply to add your changes into the working tree.',
        'option4': 'git stash return to bring back stashed changes. ',
        'option5': 'git stash drop to cherry pick a stash into your working tree.',
        'answer' : 'git stash apply to add your changes into the working tree.'
    },
    'q9': {
        'question':'How do you list git commits from the command line?',
        'option1': 'git status',
        'option2': 'git grep',
        'option3': 'git log',
        'option4': 'git show',
        'answer' : 'git log'
    },
    'q10': {
        'question':'What does rebase mean?',
        'option1': 'Change sides in a capture the flag game.',
        'option2': 'To resolve merge conflicts in between a target and source branch.',
        'option3': 'To incorporate commits from another branch to your working branch in sequence with local commits to maintain a consistent history across branches.',
        'option4': 'Realigning a downstream branch with upstream remote while preserving uncommitted changes.',
        'answer' : 'To incorporate commits from another branch to your working branch in sequence with local commits to maintain a consistent history across branches.'
    },
    'q11': {
        'question':'When would you rebase?',
        'option1': 'When a feature branch has gone stale and needs to be reconciled with the newer codebase.',
        'option2': 'When you want to hide mistakes in your code. ',
        'option3': 'When you want to squash commit history.',
        'option4': 'To purge old commits from the history of a repository.',
        'answer' : 'When a feature branch has gone stale and needs to be reconciled with the newer codebase.'
    },
    'q12': {
        'question':'What is cherry picking?',
        'option1': 'Picking Cherries from fruit trees.',
        'option2': 'Selectively applying commits between branches and leaving others behind.',
        'option3': 'Creating a feature branch.',
        'option4': 'Creating a release.',
        'answer' : 'Selectively applying commits between branches and leaving others behind.'
    },
    'q13': {
        'question':'What is revert?',
        'option1': 'A way to respond to pull request comments',
        'option2': 'A way to add a commit reversing the changes of one or more previous commits',
        'option3': 'A way to switch from the current branch to the next-most current',
        'option4': 'A way to reindex the intersection of two branches',
        'option5': 'A way to excise commits from the current branch, as used to mitigate zero-day and other security vulnerabilities',
        'answer' : 'A way to add a commit reversing the changes of one or more previous commits'
    },
    'q14': {
        'question':'How would you change from one upstream to another?',
        'option1': 'Checkout a new repo from the desired location.',
        'option2': 'Change the HEAD of the local repository',
        'option3': 'Add the upstream reference locally and change your working tree’s fetch or push defaults.',
        'answer' : 'Add the upstream reference locally and change your working tree’s fetch or push defaults.'
    },
    'q15': {
        'question':'What’s the difference between a fork and a branch?',
        'option1': 'A fork is a separate repo created as a copy and a branch is a copy within the current repo.',
        'option2': 'A fork is a release and a branch is an unversioned commit in the code.',
        'option3': 'A fork is a competing version of a repository; a branch is an ordered series of commits.',
        'option4': 'A fork is a point is a decision tree in a repositories history; a branch is a specific path through the decision tree.',
        'answer' : 'A fork is a separate repo created as a copy and a branch is a copy within the current repo.'
    },
    'q16': {
        'question':'Why would you squash commit history?',
        'option1': 'To suppress local commits related to debugging on local branches for a cleaner commit history to the upstream repository.',
        'option2': 'To remove any history that might show secrets or keys or authentication tokens.',
        'option3': 'To hide bugs.',
        'option4': 'To annoy your coworkers.',
        'answer' : 'To suppress local commits related to debugging on local branches for a cleaner commit history to the upstream repository.\nTo remove any history that might show secrets or keys or authentication tokens.'
    },
    'q17': {
        'question':'What is the .gitignore file for?',
        'option1': 'A configuration file designed to tell git how to behave when it encounters merge conflicts.',
        'option2': 'A file that defines git users banned from contributing to a repository.',
        'option3': 'A file containing all blockchain related code committed to a repository.',
        'option4': 'A set of instructions defining which files git should not attempt to manage.',
        'option5': 'A list of repositories that git should not pull files from.',
        'answer' : 'A set of instructions defining which files git should not attempt to manage.'
    },


    

}

