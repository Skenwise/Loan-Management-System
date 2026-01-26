# Loan Management System - Backend Module Structure

This document describes the backend structure for the Loan Management System (LMS), designed to maximize modularity, maintainability, and reusability across financial projects.

## Goals

- **Clear separation** between core primitives, data access, and business logic.
- **Pluggable backend modules**: swap business logic without touching core data.
- **Reusability**: shared models, tenants, identity modules.
- **Support LLM integrations**: clean adapter/port separation for AI-based enhancements.

---

## Backend Directory Overview

### core/  🔹 Shared primitives & domain logic
- `time.py` - ValueDate, PostingDateTime
- `money.py` - Money primitive, rounding rules
- `ids.py` - AccountID, LoanID, TransactionID, CustomerID
- `errors.py` - Domain exceptions

### tenants/ 🔹 Multi-tenant isolation
- `tenant.py` - TenantService, business logic
- `context.py` - Tenant context manager for scoped operations

### identity/ 🔹 Security & users
- `user.py` - User management port & adapter
- `role.py` - Roles, assignments
- `permission.py` - Permission handling
- `auth.py` - Authentication/authorization

### loans/ 🔹 Loan product logic
- `loan.py` - Loan entity and lifecycle
- `schedule.py` - Amortization & repayment schedules
- `interest.py` - Interest computation logic
- `disbursement.py` - Funding loans
- `repayment.py` - Payment handling

### accounts/ 🔹 Ledger accounts
- `account.py` - Account entity
- `chart_of_accounts.py` - Ledger structure
- `journal.py` - Journal entries
- `posting.py` - Posting logic

### payments/ 🔹 Money movement
- `inbound.py` - Incoming funds
- `outbound.py` - Outgoing funds
- `providers/` - Integration adapters (e.g., payment gateways)
- `settlement.py` - Finalizing transactions

### currency/ 🔹 Multi-currency support
- `currency.py` - Currency entities
- `exchange_rate.py` - FX rates
- `fx_revaluation.py` - FX revaluation logic

### audit/ 🔹 Logging & reconciliation
- `audit_log.py` - Audit trails
- `reconciliation.py` - Transaction matching
- `controls.py` - Internal controls

### reporting/ 🔹 Read-only projections
- `loan_reports.py` - Loan performance & repayment reports
- `ledger_views.py` - Accounting views
- `compliance.py` - Regulatory compliance reports

### app/ 🔹 Application entry
- `__init__.py`
- `main.py` - FastAPI app instance
- `routes/` - API endpoints
    - `loans.py`
    - `accounts.py`
    - `payments.py`
- `dependencies.py` - DI & shared dependencies (DB, Auth)

---

## Design Principles

1. **Port & Adapter Pattern**
   - Each module exposing external interactions (e.g., User, Loan, Payment) implements a **Port interface**.
   - The
