# Algorand Lock-In — Day 2 Step 1

### 07/05/2026

# Topic: What Blockchain “State” Actually Means

## Core Idea

Blockchain state refers to:

```text
Persistent data stored on the blockchain that can change over time.
```

State is one of the most important concepts in smart contracts and blockchain applications.

---

# Traditional Backend Analogy

Traditional application architecture:

```text
Frontend
   ↓
Backend
   ↓
Database
```

Example:
A voting application stores votes inside a database.

Example database state:

| User | Candidate |
| ---- | --------- |
| A    | John      |
| B    | Sarah     |

This stored information is:

```text
application state
```

---

# Blockchain Version

Blockchain applications also need persistent data.

But instead of:

```text
PostgreSQL / MySQL
```

The blockchain itself stores the application state.

Examples:

* balances
* vote counts
* counters
* ownership records
* voting status
* smart contract data

---

# Example — Counter App

Suppose blockchain state contains:

```text
counter = 5
```

A user presses:

```text
increment
```

Now blockchain state becomes:

```text
counter = 6
```

This update is a:

```text
blockchain state change
```

---

# Important Concept

Transactions are fundamentally:

```text
Requests to change blockchain state.
```

Examples:

## Yesterday

Sending ALGO changed:

* account balances

---

## Today

Smart contract calls will change:

* application state

Same fundamental concept.

---

# Smart Contracts + State

Traditional applications:

```text
Backend controls database
```

Blockchain applications:

```text
Smart contract controls blockchain state
```

Smart contracts define the rules for valid state changes.

---

# Voting dApp Example

Possible blockchain state:

## Vote counts

```text
Candidate A → 62
Candidate B → 31
```

---

## Wallet voting status

```text
Wallet XYZ → voted = true
```

Used to prevent duplicate voting.

---

## Candidate list

```text
["Alice", "Bob"]
```

---

## Voting deadline

```text
end_time = ...
```

---

# User Understanding (Refined)

Initial understanding:

```text
Candidate 1 : 62
Candidate 2 : 31
```

This is correct.

Reason:

* vote counts persist over time
* values change through transactions
* future behavior depends on them
* data must be trusted and publicly verifiable

This is exactly what blockchain state is designed for.

---

# What Makes Something “State”?

Data becomes blockchain state if it:

* persists over time
* changes through transactions
* must be remembered
* affects future behavior
* requires trust/shared visibility

---

# Important Distinction

Not everything belongs on-chain.

Blockchain storage:

* costs fees
* is public
* is replicated across nodes

So only important trusted shared data should become blockchain state.

---

# Good Blockchain State Examples

* balances
* vote counts
* ownership records
* voting status
* smart contract configuration

---

# Bad Blockchain State Examples

* UI theme
* animations
* temporary frontend state
* local app preferences

Those belong in frontend/backend systems.

---

# Huge Mental Model

Blockchain is essentially:

```text
A distributed state machine.
```

Transactions:

* read state
* validate rules
* modify state

Smart contracts control how state transitions happen.

---

# Step 1 Outcome

Completed:

* Understood blockchain state
* Connected blockchain state with traditional databases
* Understood transactions as state changes
* Understood smart contracts as rule engines for state transitions
* Identified valid blockchain state in voting application example
