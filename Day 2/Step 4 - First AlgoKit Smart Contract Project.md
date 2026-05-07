# Algorand Lock-In — Day 2 Step 4

### 07/05/2026

# Topic: Creating First AlgoKit Smart Contract Project

## Core Milestone

This step marks the transition from:

```text
learning blockchain concepts
```

to:

```text
working inside a real blockchain application project
```

This is the beginning of actual smart contract development workflow.

---

# Creating The Project

Command used:

```bash
algokit init
```

Selections:

* Smart Contracts 📜
* Python 🐍
* Project name: Counter
* Starter template
* Python deployment code

---

# What AlgoKit Did Automatically

AlgoKit scaffolded:

* project structure
* Python virtual environment
* dependency management
* smart contract tooling
* deployment tooling
* testing setup
* configuration files

This is similar to:

```text
create-next-app
flutter create
django-admin startproject
```

but for Algorand applications.

---

# Important Realization

Blockchain applications are NOT just:

```text
single smart contract files
```

Real blockchain applications usually contain:

* contracts
* deployment scripts
* testing setup
* config files
* local blockchain integration
* environment management

---

# Poetry

During setup, AlgoKit used:

```text
Poetry
```

Poetry is a modern Python project/dependency manager.

Mental model:

| Ecosystem          | Tool       |
| ------------------ | ---------- |
| JavaScript         | npm        |
| Traditional Python | pip + venv |
| Modern Python      | Poetry     |

---

# Important Installed Packages

Observed packages:

* py-algorand-sdk
* algokit-utils
* algorand-python
* algorand-python-testing

This indicates entry into the:

```text
Algorand Python smart contract ecosystem
```

---

# Project Structure Overview

Observed structure:

```text
Counter/
 ├── .algokit/
 ├── .vscode/
 ├── projects/
 │    └── Counter/
 │         ├── smart_contracts/
 │         ├── tours/
 │         ├── .venv/
 │         ├── .algokit/
 │         ├── .vscode/
 │         ├── poetry.toml
 │         ├── poetry.lock
 │         ├── pyproject.toml
 │         └── README.md
```

---

# IMPORTANT DOUBT — Why Are There Two “Counter” Folders?

Observed:

```text
Code/Counter/projects/Counter
```

This initially feels confusing.

---

# Explanation

The OUTER:

```text
Counter/
```

is basically:

```text
workspace/container folder
```

It contains:

* workspace configuration
* top-level AlgoKit setup
* shared tooling/config
* potentially multiple projects later

---

# INNER:

```text
projects/Counter/
```

is the ACTUAL smart contract application project.

This is where:

* contract code
* deployment code
* Python environment
* app logic
* testing setup

actually live.

---

# Mental Model

Think of it like:

```text
Workspace
    └── Actual Application Project
```

Similar to:

```text
company_workspace/
    └── backend_service/
```

or:

```text
monorepo/
    └── actual_app/
```

---

# Most Important Folder Right Now

## smart_contracts/

This is currently the MOST important folder.

Mental model:

```text
smart_contracts/ = backend business logic
```

This is where:

* blockchain state
* contract methods
* validation logic
* smart contract behavior

will be implemented.

---

# Other Important Folders/Files

## .venv/

Contains isolated Python environment.

Equivalent mental model:

```text
node_modules for Python-ish understanding
```

---

## .algokit/

AlgoKit internal tooling/configuration.

Mostly ignored initially.

---

## .vscode/

VSCode editor settings.

---

## pyproject.toml

## poetry.toml

## poetry.lock

Python project + dependency configuration.

Equivalent mental model:

| Python         | JavaScript        |
| -------------- | ----------------- |
| pyproject.toml | package.json      |
| poetry.lock    | package-lock.json |

---

## README.md

Project documentation/instructions.

Very common in professional repositories.

---

# Huge Realization

The blockchain project structure already resembles:

* backend frameworks
* infrastructure projects
* DevOps-heavy systems
* professional software repositories

This is because blockchain engineering overlaps heavily with:

* backend engineering
* infrastructure
* APIs
* networking
* distributed systems

---

# Important Mindset

Developers are NOT expected to instantly understand every file/folder.

Professional workflow usually involves:

* gradual architecture understanding
* layer-by-layer exploration
* learning through implementation

---

# Step 4 Outcome

Completed:

* Created first AlgoKit project
* Understood project scaffolding
* Understood role of Poetry
* Understood workspace vs actual app structure
* Understood important folders/files
* Identified smart_contracts as primary development area
* Connected blockchain projects with real software architecture workflows






------------------------
------------------------
------------------------

# Additional Step 4 Notes — AlgoKit Project Scaffolding

# Step 4 — Create Your First AlgoKit Smart Contract Project

## Core Milestone

This is the:

```text
first REAL blockchain application project
```

Until now:

* concepts
* mental models
* infrastructure understanding

Now:

```text
actual development workflow begins
```

---

# What Does AlgoKit Actually Generate?

When a project is created, AlgoKit scaffolds:

* smart contract structure
* deployment workflow
* testing setup
* frontend/backend integration structure
* development environment

Mental model:

```text
AlgoKit = project scaffolding + developer workflow toolkit
```

---

# Ecosystem Analogy

Similar to:

```text
create-next-app
flutter create
django-admin startproject
```

but for:

```text
Algorand applications
```

---


# Today's Project — Counter App

The learning project created is:

```text
Counter App
```

---

# Why Counter App?

Because it teaches:

* blockchain state
* state updates
* transactions
* smart contract calls
* deployment flow

without overwhelming complexity.

---

# Counter App Behavior

```text
Initial value = 0

User presses increment
↓
Blockchain state updates
↓
Counter = 1
```

Simple but extremely important foundational project.

---

# Important Connection

## Yesterday

```text
transactions changed balances
```

---

## Today

```text
transactions change application state
```

Same architecture.
Different type of state.

---

# Important Mindset

After generation, many files/folders may initially feel overwhelming.

This is normal.

Professional developers ALSO:

* gradually explore architecture
* learn folder purposes over time
* understand systems layer-by-layer

Instant mastery is NOT expected.

---

# Initial Observation Goals

Important things to notice initially:

* where smart contract code probably lives
* deployment-related files
* configuration files
* tooling structure

Only intuition is needed initially.