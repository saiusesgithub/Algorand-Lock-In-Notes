# Algorand Lock-In — Day 2 Step 3

### 07/05/2026

# Topic: Smart Contract Mental Model

## Core Idea

Smart contracts are NOT:

* magical
* intelligent
* AI systems
* always-running servers

Best mental model:

```text
Smart contracts = deterministic backend logic running on blockchain
```

---

# Traditional Backend Analogy

Traditional voting app:

```text
Frontend
   ↓
Backend
   ↓
Database
```

Backend logic might look like:

```python
if already_voted:
    reject_vote()

votes[candidate] += 1
```

Responsibilities:

* validate rules
* update database
* control application behavior

---

# Blockchain Version

Blockchain applications replace:

```text
Backend + Database
```

with:

```text
Smart Contract + Blockchain State
```

The smart contract now controls:

* validation rules
* state transitions
* application behavior

---

# What A Smart Contract Actually Does

A smart contract:

* receives transactions
* validates rules
* reads blockchain state
* modifies blockchain state

---

# Voting Contract Flow Example

Suppose Wallet A votes for Alice.

---

## 1. Transaction Sent

Wallet submits transaction:

```text
Vote for Alice
```

This transaction acts as a request to modify blockchain state.

---

## 2. Smart Contract Checks Rules

The smart contract validates:

```text
Did Wallet A already vote?
```

If yes:

* reject transaction

If no:

* continue execution

---

## 3. State Changes

Blockchain state updates:

```text
Alice votes += 1
Wallet A → voted = true
```

Both global and local state may change.

---

# User Understanding (Refined)

Initial understanding:

## What transaction gets sent?

```text
Vote for Alice
```

Correct.

The transaction acts as an instruction/request to the smart contract.

---

## What does the smart contract check?

```text
Whether Wallet A already voted
```

Correct.

This prevents duplicate voting.

---

## What state changes?

```text
Alice vote count
```

Correct.

Additionally:

```text
Wallet A → voted = true
```

may also be updated.

---

## Why must nodes agree on result?

Initial understanding:

```text
Consensus shouldn't break.
Every node should agree for blockchain state to update.
```

Correct.

Reason:

* blockchain is replicated across nodes
* all nodes must maintain identical state
* every node must compute same result from same transaction

Otherwise:

* blockchain forks/conflicts occur
* consensus breaks
* state becomes inconsistent

---

# Important Concept — Smart Contracts Are NOT Always Running

Smart contracts execute ONLY when triggered by transactions.

They are NOT:

```text
background servers continuously running
```

Instead:

```text
transaction-triggered execution
```

---

# Deterministic Execution

Every node must compute identical results.

Therefore smart contracts must behave deterministically.

---

# Good Example

```python
counter += 1
```

Every node gets same result.

---

# Bad Example

```python
counter += random.randint(1, 100)
```

Different nodes may compute different values.

Consensus breaks.

---

# Huge Realization

When a smart contract executes:

```text
Every node executes/verifies the same logic.
```

This is why blockchain computation:

* must be deterministic
* is more restricted than normal backend code
* becomes computationally expensive

---

# Another Important Insight

Traditional backend systems:

* company controls rules
* database admins can manipulate data
* logic can secretly change

Blockchain smart contracts:

* rules become public
* execution becomes verifiable
* state transitions become transparent

---

# Final Mental Model

Smart contracts are essentially:

```text
Shared trusted backend logic.
```

---

# Step 3 Outcome

Completed:

* Understood smart contract purpose
* Connected smart contracts with backend logic
* Understood transaction-triggered execution
* Understood deterministic execution
* Understood why node agreement is necessary
* Walked through complete voting transaction lifecycle
