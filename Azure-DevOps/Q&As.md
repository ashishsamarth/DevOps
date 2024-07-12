--------------------------------------------------------------------------------------------------------------------------
**Azure DevOps Quiz**
--------------------------------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------------------------------------
Q-0001: which of these best describe why companies are moving towards DevOps deployment?
--------------------------------------------------------------------------------------------------------------------------
a. Increase Deployment Frequency
b. Reduce the lead time between logging a bug and deploying a fix
c. Reduced Failure of new software features
d. None of these
e. All of these

Answer: e. All of these

--------------------------------------------------------------------------------------------------------------------------
Q-002: Which statement best describes the goal of DevOps?
--------------------------------------------------------------------------------------------------------------------------
a. Create a system where change management does not control application releases - it is built into the process of 
    software development
b. Create an environment where application developers perform all operation tasks
c. Create an environment to release more reliable applications faster
d. Create an environment that aligns with Agile, where in small, rapid application releases are values more than 
    application reliability

Answer: c. Create an environment to release more reliable applications faster

--------------------------------------------------------------------------------------------------------------------------
Q-003: Which of the following is an accurate description of a sprint?
--------------------------------------------------------------------------------------------------------------------------
a. A time estimate associated with a product feature being worked on by a development team
b. A deadline assigned to a project that is developed using the Agile methodology
c. A specific kind of project planning board avaialble when using the Agile work process in Azure DevOps
d. A fixed iteration of time that during which teams commit to creating a work deliverable

Answer: d. A fixed iteration of time that during which teams commit to creating a work deliverable

Explanation: Sprints are a 'time box' that, ideally, defines specific work items that can be completed in a relatively 
short amount of time - usually 2 or 3 weeks. Sprints facilitate concrete work product while also allowing teams to adapt 
quickly to change.

--------------------------------------------------------------------------------------------------------------------------
Q-004: Which of the following is not a work process teams can use to define work items in an Azure Board?
--------------------------------------------------------------------------------------------------------------------------
a. Scrum
b. CMMI
c. Lean / XP
d. Basic
e. Agile

Answer: c. Lean / XP

--------------------------------------------------------------------------------------------------------------------------
Q-005: As a product owner in an Agile development team, want to quickly add items to your team's portfolio backlog and 
also begin planning the next sprint. Which is likely going to be the best Azure Boards node for your objectives.
--------------------------------------------------------------------------------------------------------------------------
a. Backlogs
b. Queries
c. Sprints

Answer: a. Backlogs

Explanation: DevOps backlogs let you quickly add and prioritize your product and portfolio backlogs, which list work items 
either as a flat or hierarchical list. Backlogs also let you easily assign work from your backlog to a sprint.

--------------------------------------------------------------------------------------------------------------------------
Q-006: You are part of a development team that has an existing project stored in GitHub. You want to change migrate this 
code to use Azure DevOps Repo. Which of the following will help you quickly clone the Repo to Azure DevOps?
--------------------------------------------------------------------------------------------------------------------------
a. Implement a new pull request from an empty Azure Repo, then delete the existing Readme file
b. Perform a push request of the GitHub repo.
c. Configure a service hook in GitHub to sync the Github repo with DevOps.
d. Import a Git repo using Azure DevOps repos.

Answer: d. Import a Git repo using Azure DevOps repos.
Explanation: Import from the Azure Git Repo - migration from GitHub is very straightforward using the Import Git repo 
procedure.

--------------------------------------------------------------------------------------------------------------------------
Q-007: Which file can you configure to ensure that certain file types are not committed to the local Git repository?
--------------------------------------------------------------------------------------------------------------------------
a. .gitignore
b. ignore.git
c. git.ignore
d. gitignore.md

Answer: a. .gitignore

Explanation: Entries in the .gitignore file tell GIt not to include these files and file types when performing a pull 
request that would sync a local repo branch with a remote branch

--------------------------------------------------------------------------------------------------------------------------
Q-008: You have a local repository, but the team members have pushed some changes into the remote repository. Which Git 
operation would you use to download those changes into your working copy?
--------------------------------------------------------------------------------------------------------------------------
a. checkout
b. commit
c. export
d. pull

Answer: d. pull

Explanation: Straight from the Git documentation, a pull request "incorporates changes from a remote repository into the 
current branch."

--------------------------------------------------------------------------------------------------------------------------
Q-009: When a team adopts a Continuous Delivery mindset by using DevOps, what objectives will this help them accomplish?
--------------------------------------------------------------------------------------------------------------------------
a. A narrow focus on cycle time reduction - new features are released every two weeks, if not more frequently
b. Comples releases with fully tested and stable features, but also a fewer number of releases
c. That the team will be largely self0managed and responsive to changing requirements from customers and product owners
d. A way to understand a team's resource-based velocity - that is, how many stable features can be added to the value 
    stream given a certain number of team members.

Answer: c. That the team will be largely self0managed and responsive to changing requirements from customers and product 
owners

--------------------------------------------------------------------------------------------------------------------------
Q-010: You are new to a team developing an app written using .Net Core. This app connects to a SQL database. Currently, the
     app is developed using on-prem servers. For prod, the app will be moved and hosted on an Azure Web App. Where should 
     you store the SQL database connection settings?
--------------------------------------------------------------------------------------------------------------------------
a. By Configuring a connection string in Azure App Service
b. In a web config file
c. In the identity section in the App service
d. In Authentication / Authorization in App service

Answer: a. By Configuring a connection string in Azure App Service

--------------------------------------------------------------------------------------------------------------------------
Q-011: Your team is using an Azure Pipeline for CI/CD. The pipeline contains a secret (authentication credentials) that 
needs to be shared in the pipeline. How would you define the secret?
--------------------------------------------------------------------------------------------------------------------------
a. In the YAML File of the repo, add the "Secret" variable
b. In the YAML file of the repo, add a normal variable - all YAML files are encrypted in Azure Repos
c. Set the secret using the Azure DevOps pipeline editor
d. Set the secret with in the app itself - Azure will encrypt and store the secret using kerberos.

Answer: c. Set the secret using the Azure DevOps pipeline editor

--------------------------------------------------------------------------------------------------------------------------
