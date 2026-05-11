# Algorand Lock-In — Day 3 Step 4

### 11/05/2026 (supposed to do on 8th , but stuff came up , so doing this in college on 11th as i have free time)

# Topic: How Frontends Fetch Blockchain State

## Core Goal

Understand:

* how frontend fetches blockchain data
* how UI updates happen
* how SDKs/nodes/APIs fit together
* why blockchain apps constantly refetch state
* practical frontend ↔ blockchain interaction flow

---

# Important Realization

Smart contracts do NOT automatically:

```text
push UI updates magically
```

Frontend applications must:

```text
manually fetch blockchain state
```

This is similar to:

* REST API fetching
* backend querying
* database reads

---

# Traditional App Flow

Example:

```text
Frontend requests posts
        ↓
Backend returns JSON
        ↓
UI renders posts
```

---

# Blockchain App Version

Blockchain applications work similarly:

```text
Frontend requests blockchain state
        ↓
Node/API returns contract state
        ↓
UI renders latest blockchain data
```

---

# Practical Blockchain Fetch Flow

```text
Frontend/App
        ↓
Algorand SDK / API
        ↓
Node API
        ↓
Blockchain State Returned
```

---

# Example Voting App

Suppose blockchain global state contains:

```text
Alice = 62
Bob = 31
```

stored inside smart contract global state.

---

# Frontend State Request

Frontend asks:

```text
Give me global state for App ID 5001
```

Node/API may return:

```json
{
  "Alice": 62,
  "Bob": 31
}
```

Frontend then updates UI.

---

# Huge Practical Realization

Blockchain frontends are heavily:

```text
state-fetch-driven
```

Because frontend constantly needs latest:

* balances
* vote counts
* NFT ownership
* app state
* transaction status

---

# Important Distinction

Blockchain state is usually:

```text
publicly readable
```

Meaning frontend can usually fetch:

* balances
* app state
* transactions
* global state

WITHOUT wallet authentication.

---

# Important Wallet Distinction

| Action                  | Wallet Needed? |
| ----------------------- | -------------- |
| Read blockchain state   | ❌ No           |
| Modify blockchain state | ✅ Yes          |

---

# Example

Fetching vote count:

```text
No signing needed
```

Voting transaction:

```text
Wallet signing REQUIRED
```

---

# Frontend State Lifecycle

Real dApps constantly follow this loop:

```text
Fetch blockchain state
        ↓
Render UI
        ↓
User interacts
        ↓
Wallet signs transaction
        ↓
Blockchain state changes
        ↓
Frontend fetches latest state again
        ↓
UI refreshes
```

This is the practical dApp lifecycle.

---

# SDK Role

SDKs simplify:

* fetching blockchain state
* contract interaction
* transaction creation
* app interaction
* node communication

Without SDKs:

```text
raw blockchain interaction would be extremely painful
```

---

# Example SDK Mental Model

Instead of manually constructing blockchain packets:

```python
client.get_global_state()
```

SDK abstracts complexity.

---

# Connection To Generated Clients

Generated files like:

```text
counter_client.py
```

exist specifically to simplify:

* contract calls
* state fetching
* blockchain interaction

---

# User Understanding (Refined)

Question:

```text
Why would UI become outdated if frontend fetched blockchain state only once?
```

Initial understanding:

```text
Because blockchain state changed.
```

Correct.

More specifically:

* blockchain state updates after transactions
* frontend still holds old cached state
* UI no longer reflects latest blockchain data

---

# How Real dApps Solve This

Initial understanding:

```text
After interactions or every few seconds,
frontend fetches latest blockchain data again using SDKs.
```

Correct.

Real dApps commonly:

* refetch after transactions
* poll periodically
* subscribe to blockchain updates/events
* synchronize frontend with latest blockchain state

---

# IMPORTANT DOUBT — Does Frontend Directly Call Individual Nodes?

Question:

```text
Does frontend manually interact with individual blockchain nodes?
```

Answer:

```text
Usually NO.
```

Frontend typically interacts through:

* SDKs
* APIs
* service providers

The SDK/API layer manages:

* node communication
* request formatting
* state fetching
* transaction handling

---

# Important Mental Model

Frontend usually does:

```text
Frontend
    ↓
SDK/API
    ↓
Node infrastructure
    ↓
Blockchain
```

NOT:

```text
Frontend manually controlling individual nodes
```

---

# Huge Realization

Modern blockchain development is heavily:

```text
SDK-driven + frontend-driven
```

NOT primarily:

* low-level blockchain packet engineering
* raw node communication
* manual blockchain protocol handling

This is why:

* frontend development
* product architecture
* integration understanding

matter heavily in practical Web3 development.

---

# Major Conceptual Shift

Blockchain apps stopped feeling like:

```text
magic decentralized systems
```

and started feeling like:

```text
frontend applications connected to distributed blockchain-backed state
```

---

# Step 4 Outcome

Completed:

* Understood blockchain state fetching
* Understood frontend ↔ SDK ↔ node flow
* Understood why UI becomes outdated
* Understood frontend synchronization patterns
* Understood read vs write blockchain actions
* Understood practical SDK role in dApps
* Understood why modern Web3 is frontend-heavy
