# Algorand Lock-In — Day 1 Step 2

### 06/05/2026

# Topic: TestNet + Faucets + Blockchain Explorers

## Algorand Networks

Algorand has multiple blockchain networks.

---

## MainNet

Production blockchain.

Uses:

* real ALGO
* real applications
* real users
* real value

Mistakes on MainNet can cost real money.

---

## TestNet

Developer/testing blockchain.

Behaves similarly to MainNet:

* real transactions
* real blocks
* real confirmations
* real smart contracts

But uses:

* fake ALGO
* faucet funding

Purpose:

* learning
* testing
* debugging
* development

---

# Faucet

A faucet provides free TestNet ALGO to developers.

Purpose:

* allow testing without real money
* activate accounts
* test transactions and smart contracts

Today:

* 10 TestNet ALGO received through faucet

---

# Blockchain Explorer

A blockchain explorer is a public interface used to inspect blockchain data.

Can inspect:

* wallet balances
* transactions
* blocks
* smart contracts
* account activity

Mental model:

```text
Blockchain explorer = search engine for blockchain data
```

---

# Important Observation

Initially used:

* Pera Explorer
* Lora Explorer

Issue observed:

* showing MainNet data instead of TestNet

This demonstrates an important concept:

```text
Blockchain networks are separate.
MainNet data ≠ TestNet data
```

An explorer must explicitly support/select TestNet.

Same wallet address can exist on:

MainNet
TestNet
LocalNet

with entirely different balances/state.

That’s a VERY important mental model.

---

# Key Concept Learned

Wallet apps are NOT storing balances internally.

Instead:

```text
Wallet app → reads blockchain state
Explorer → reads blockchain state
```

Both are simply interfaces over blockchain data.

---

# Step 2 Outcome

Completed:

* Understood MainNet vs TestNet
* Understood faucet purpose
* Understood explorer purpose
* Observed network separation behavior
* Learned that blockchain data is public and network-specific
