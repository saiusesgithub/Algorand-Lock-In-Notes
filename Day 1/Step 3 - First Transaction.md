# Algorand Lock-In — Day 1 Step 3

### 06/05/2026

# Topic: First Blockchain Transaction

## Core Idea

A blockchain transaction is NOT just a money transfer.

More accurate mental model:

```text
Transaction = signed blockchain state update
```

Examples of blockchain transactions:

* sending ALGO
* calling smart contracts
* voting
* updating application state
* storing data

---

# What Happened Today

A self-transfer transaction was executed.

Transaction:

* sender = same wallet
* receiver = same wallet
* amount = 0.1 ALGO

Purpose:

* understand signing
* observe confirmation flow
* inspect blockchain transaction lifecycle

---

# Transaction Lifecycle

## 1. Transaction Created

Transaction object contains:

* sender
* receiver
* amount
* fee
* network parameters

---

## 2. Transaction Signed

Wallet signs transaction using:

* private key

This proves ownership and authorization.

---

## 3. Transaction Broadcast

Transaction sent to Algorand network nodes.

---

## 4. Network Validation

Nodes verify:

* valid signature
* sufficient balance
* correct transaction format

---

## 5. Included In Block

Once validated:

* transaction enters blockchain block
* blockchain state updates

---

# Network Fee

Observed fee:

```text
0.001 ALGO
```

Important concept:

Blockchain operations are not free.

Fees help:

* prevent spam
* incentivize network operation
* prioritize transactions

Smart contract interactions later will also require fees.

---

# Important Realization

Even a self-transfer still:

* requires signing
* gets validated
* gets recorded permanently
* consumes network fee

because blockchain tracks state transitions, not just transfers between different people.

---

# Step 3 Outcome

Completed:

* First blockchain transaction
* Observed transaction ID
* Observed confirmation flow
* Observed network fee
* Understood transaction lifecycle
* Understood blockchain state update concept
