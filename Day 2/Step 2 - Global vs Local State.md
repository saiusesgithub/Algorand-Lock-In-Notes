# Algorand Lock-In — Day 2 Step 2

### 07/05/2026

# Topic: Global State vs Local State

## Core Question

Blockchain applications store different types of state.

Important design question:

```text
Who owns this state?
```

This determines whether data becomes:

* global state
* local state

---

# Global State

Global state = application-wide shared state.

Shared across:

* all users
* all wallets
* entire smart contract

There is one shared copy for the whole application.

---

# Examples Of Global State

## Voting dApp

```text
Alice → 62 votes
Bob → 31 votes
```

---

## Counter App

```text
counter = 10
```

---

## Voting Deadline

```text
end_time = ...
```

---

# Mental Model

```text
Global state = shared application database fields
```

---

# Local State

Local state = wallet/account-specific state.

Each account can have its own values.

Different users may have different local state.

---

# Examples Of Local State

```text
Wallet A → voted = true
Wallet B → voted = false
```

---

# Important Distinction

## Global State

```text
ONE shared copy
```

---

## Local State

```text
Separate copy per account
```

---

# Visual Mental Model

## Global State

```text
Voting App
    ├── Alice votes = 62
    ├── Bob votes = 31
    └── deadline = tomorrow
```

Shared by everybody.

---

## Local State

```text
Wallet A
    └── voted = true

Wallet B
    └── voted = false
```

Different per wallet.

---

# Traditional Backend Analogy

## Global State ≈ Shared Database Tables

| Candidate | Votes |
| --------- | ----- |
| Alice     | 62    |
| Bob       | 31    |

---

## Local State ≈ Per-User Data

| User Wallet | Already Voted |
| ----------- | ------------- |
| Wallet A    | true          |
| Wallet B    | false         |

---

# Classification Exercise

## 1. Total votes for Alice

Classification:

```text
Global State
```

Reason:

* shared across all users
* entire app depends on same value

---

## 2. Whether wallet XYZ already voted

Classification:

```text
Local State
```

Reason:

* tied to individual wallet/account
* differs per user

---

## 3. Voting deadline

Classification:

```text
Global State
```

Reason:

* one shared application rule
* same for everyone

---

## 4. Theme preference (dark/light mode)

Classification:

```text
Local State
```

But importantly:

This should usually NOT be blockchain state at all.

Reason:

* UI-only preference
* unnecessary on-chain storage
* wastes blockchain storage/resources

Better stored:

* frontend
* browser local storage
* backend database

---

## 5. Wallet-specific reputation score

Classification:

```text
Local State
```

Reason:

* tied to specific wallet/account
* differs between users

---

# Important Architecture Mistake Example

Suppose:

```text
already_voted = true
```

was stored globally.

Problem:

* one user votes
* entire app becomes blocked

Wrong design.

Correct design:

```text
Wallet A → voted = true
```

stored separately per wallet.

---

# HUGE DOUBT — Is Local State Stored On Every Node?

Question:

```text
If Wallet A has:

voted = true

Does every node know/store this?
```

Answer:

YES.

This is one of the BIGGEST concepts in blockchain.

---

# Important Realization

Blockchain nodes replicate blockchain state.

That includes:

* balances
* smart contract state
* global state
* local state

Meaning:

```text
Every full node stores all blockchain state.
```

---

# Then What Happens With Thousands Of Users?

Yes.

Nodes may store:

* thousands
* millions
* potentially billions

of account-specific local state entries.

Example:

```text
Wallet A → voted = true
Wallet B → voted = false
Wallet C → reputation = 54
```

All replicated across nodes.

---

# Why Is This Important?

Because blockchain systems prioritize:

```text
Consistency + trust + replication
```

over:

```text
storage efficiency
```

Every node needs enough state to:

* verify transactions
* validate smart contract logic
* independently confirm blockchain correctness

---

# HUGE Tradeoff

Blockchain storage is:

* replicated
* public
* expensive
* persistent

Which is why developers must carefully choose:

* what belongs on-chain
* what should remain off-chain

---

# Another Important Realization

Blockchain is essentially:

```text
A distributed replicated state machine.
```

Every node maintains a synchronized copy of blockchain state.

---

# Step 2 Outcome

Completed:

* Understood global state
* Understood local state
* Classified voting dApp data correctly
* Understood shared vs per-wallet storage
* Understood that nodes replicate both global and local state
* Understood why blockchain storage is expensive and carefully designed
