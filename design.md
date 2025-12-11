# Loan Management System (Desktop App) — Architecture Design

**Platform:** Electron + React + FastAPI + SQLite
**Target OS:** Windows (can extend to Linux/macOS)
**Purpose:** Manage loans, borrowers, repayments, wallets, and reports efficiently with role-based access and offline-first capability.

---

## 1. **System Overview**

The Loan Management System (LMS) is a **desktop application** built to manage all aspects of loan operations for small-to-medium enterprises or financial institutions. It combines a modern **React UI** with a **FastAPI backend** and **SQLite database** for offline-first operation. Electron wraps the web application as a desktop executable.

**Core Principles:**

* Modular design: each module can be developed and tested independently.
* Offline-first: SQLite database ensures all data is stored locally.
* Scalable: backend architecture allows future migration to server-based database if needed.
* Role-based access: secure and flexible user permission management.
* Extensible: modules for payments, wallets, integrations, and reports are designed for easy extension.

---

## 2. **High-Level Architecture Diagram**

```
+---------------------------------------------------+
|                    Electron                      |
|  (Desktop wrapper for React + FastAPI backend)   |
|                                                   |
|  +------------------+    +-------------------+  |
|  |   React Frontend |<-->| FastAPI Backend    |  |
|  |  (Renderer)      |    |  (Business Logic) |  |
|  +------------------+    +-------------------+  |
|           |                       |              |
|           |                       |              |
|           v                       v              |
|      SQLite Database <-------------+              |
|  (loan_management.db)                             |
+---------------------------------------------------+
```

---

## 3. **Frontend (React + Electron Renderer)**

### Responsibilities:

* User interface (UI) and user experience (UX)
* Role-specific dashboards: admin, clerk, auditor
* Forms for borrowers, loans, payments, wallets
* Tables, charts, and reports (Excel/PDF export)
* Notifications and alerts (desktop & email)

### Key Technologies:

* **React** for UI components
* **Tailwind CSS / Material UI** for styling
* **Electron Renderer Process** to interact with OS-level APIs (file system, notifications)
* **Axios / Fetch** for API calls to FastAPI backend

### Main Modules:

1. **Auth & User Management:** login, logout, role-based access, user profile
2. **Borrower Module:** list, add, update, upload documents
3. **Loan Module:** create loans, view active/denied/defaulted loans, approval workflow
4. **Payment Module:** track repayments, update payments, mark defaults
5. **Wallet & Transactions:** transfer funds, expense management, transaction history
6. **Reports & Analytics:** dashboards, charts, Excel/PDF exports
7. **Notifications:** reminders, email alerts, loan agreement emails

---

## 4. **Backend (FastAPI)**

### Responsibilities:

* Business logic and API endpoints
* Loan approval workflows
* Interest and repayment calculations
* Wallet and transaction processing
* Notifications (email or local alerts)
* User authentication and role management
* Database CRUD operations

### Key Technologies:

* **FastAPI** (Python) — high-performance backend framework
* **SQLite** — lightweight relational database
* **SQLAlchemy** — ORM for database operations
* **Pydantic** — request/response validation
* **SMTP / Email Libraries** — email notifications

### Main Modules:

1. **Authentication & Authorization:** JWT tokens, RBAC, session management
2. **Borrower Management:** CRUD, document storage references
3. **Loan Management:** create, approve, deny, schedule, status update
4. **Payment Management:** repayment tracking, late fee calculations, default flagging
5. **Wallet & Transaction Management:** fund transfers, ledger maintenance
6. **Reports & Analytics:** portfolio summary, active/pending/denied loans
7. **Notification Engine:** emails for loan agreements, reminders, settlements
8. **Integration Layer (Optional):** payment gateways, credit scoring APIs

---

## 5. **Database Design (SQLite)**

### Core Tables:

1. **users**
   | Field          | Type    | Description                     |
   |----------------|---------|---------------------------------|
   | id             | int PK  | Unique user ID                  |
   | name           | string  | Full name                        |
   | email          | string  | Login email                     |
   | password_hash  | string  | Hashed password                  |
   | role_id        | int FK  | Role of user                     |
   | created_at     | datetime | Account creation timestamp      |

2. **roles**
   | Field       | Type     | Description                  |
   |-------------|---------|-------------------------------|
   | id          | int PK  | Role ID                        |
   | name        | string  | Role name (Admin, Clerk, etc.)|
   | permissions | JSON    | List of permissions            |

3. **borrowers**
   | Field          | Type     | Description                       |
   |----------------|---------|-----------------------------------|
   | id             | int PK  | Borrower ID                       |
   | name           | string  | Full name                          |
   | contact        | string  | Phone / Email                     |
   | dob            | date    | Date of birth                      |
   | documents_json | JSON    | List of uploaded documents         |
   | created_at     | datetime | Record creation timestamp         |

4. **loans**
   | Field          | Type     | Description                       |
   |----------------|---------|-----------------------------------|
   | id             | int PK  | Loan ID                            |
   | borrower_id    | int FK  | Linked borrower                    |
   | type           | string  | Loan type (Personal/Business)      |
   | principal      | float   | Loan principal amount              |
   | interest_rate  | float   | Interest %                         |
   | interest_cycle | string  | Monthly/Weekly/Custom              |
   | status         | string  | Pending / Approved / Denied / Defaulted |
   | created_at     | datetime | Loan creation timestamp           |
   | approved_at    | datetime | Approval timestamp (nullable)     |

5. **wallets**
   | Field       | Type     | Description             |
   |-------------|---------|-------------------------|
   | id          | int PK  | Wallet ID               |
   | type        | string  | Loan / Expense          |
   | balance     | float   | Current balance         |
   | owner_id    | int FK  | User or organization    |

6. **transactions**
   | Field         | Type     | Description           |
   |---------------|---------|-----------------------|
   | id            | int PK  | Transaction ID        |
   | wallet_from   | int FK  | Source wallet         |
   | wallet_to     | int FK  | Destination wallet    |
   | amount        | float   | Amount transferred    |
   | type          | string  | Transfer / Payment    |
   | date          | datetime| Transaction date      |

7. **payments**
   | Field       | Type     | Description             |
   |-------------|---------|-------------------------|
   | id          | int PK  | Payment ID              |
   | loan_id     | int FK  | Linked loan             |
   | amount_paid | float   | Payment amount          |
   | due_date    | date    | Scheduled payment date  |
   | payment_date| date    | Actual payment date     |
   | status      | string  | Paid / Pending / Default|

8. **loan_approval_workflows**
   | Field       | Type     | Description             |
   |-------------|---------|-------------------------|
   | id          | int PK  | Workflow step ID        |
   | loan_id     | int FK  | Loan linked             |
   | step        | string  | Step name               |
   | status      | string  | Pending / Approved / Denied|
   | assigned_to | int FK  | User responsible        |
   | timestamp   | datetime| Step timestamp          |

---

## 6. **Module Interaction**

```
[React UI] <--API--> [FastAPI Backend] <--ORM--> [SQLite Database]

- Frontend calls backend API for CRUD operations
- Backend validates, applies business logic, updates DB
- Backend triggers notifications when necessary
- Frontend updates dashboards & tables in real-time
```

---

## 7. **Additional Considerations**

* **Backup & Restore:** SQLite file can be backed up periodically
* **Security:** Password hashing, JWT authentication, role-based access
* **Exporting:** Use `xlsxwriter` or `openpyxl` for Excel, PDF libraries for reports
* **Offline-first:** Full app works without internet; optional sync for integrations
* **Notifications:** Desktop notifications via Electron + optional email via SMTP

---

## 8. **Development Roadmap**

1. Backend API setup (FastAPI + SQLite + SQLAlchemy)
2. User authentication & roles
3. Borrower module
4. Loan module + approval workflow
5. Wallet & transactions module
6. Payments module + reminders
7. Reports & analytics module
8. Notifications & email integration
9. Frontend React UI (module-by-module)
10. Electron packaging & deployment
