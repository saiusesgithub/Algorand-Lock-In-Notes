# Algorand Lock-In — Day 1 Step 1

### 06/05/2026

# Topic: Wallet + Account Mental Model

## Core Idea

A blockchain wallet does NOT store coins.

The blockchain itself stores:

* balances
* transaction history
* account state
* smart contract state

The wallet only manages:

* private keys
* public addresses
* transaction signing

---

# Mental Model

```text
Blockchain = actual ledger/database
Wallet = authorization + signing tool
Address = public account identifier
Private key = ownership proof
```

---

# Important Concepts

## Public Address

Safe to share.

Used to:

* receive ALGO
* identify account on blockchain
* view transactions on explorer

Example:

```text
W7ENAOYKDGCPLZWRWFMKWXVXZR27CY3HMS7NGU45DQLIAB447TFGLPUMEY
```

---

## Private Key / Mnemonic Phrase

This is FULL ownership of the wallet.

If leaked:

* anyone can control the account
* anyone can transfer funds
* account is compromised

Mnemonic phrase is a human-readable backup that regenerates the private key.

Never share it.

---

# What Happened Today

## Network Used

TestNet

TestNet is a development blockchain network using fake ALGO for testing and learning.

---

## Wallet Funding

10 TestNet ALGO received from faucet.

Meaning:

* blockchain account is active
* can now send transactions
* can interact with smart contracts later

---

# Important Realization

No:

* bank account
* centralized signup
* company approval

was required to:

* create account
* receive assets
* interact with blockchain

This is one of the core ideas behind decentralized systems.

---

# Step 1 Outcome

Completed:

* Wallet created
* Mnemonic backed up
* TestNet selected
* Wallet funded with 10 ALGO
* Understood wallet vs blockchain difference
