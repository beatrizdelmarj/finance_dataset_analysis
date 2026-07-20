# finance_dataset_analysis

# Corporate Expense Analysis

A Python/Pandas data cleaning and reconciliation project using corporate 
invoice and payment records — built to demonstrate real-world financial 
data preparation skills.

## Project Overview

This project cleans, reconciles, and analyzes two raw and inconsistent financial datasets 
to answer a core accounts payable question: *What did we invoice, what did 
we actually pay, and what's still outstanding?*

## Dataset

| Dataset | Raw Rows | Clean Rows | Columns |
|---|---|---|---|
| `invoices_2025.csv` | 808 | 718 | invoice_id, date, vendor, category, amount, status |
| `payments_2025.csv` | 565 | 565 | payment_id, invoice_id, payment_date, amount_paid, method |

## Data Quality Issues Solved

- **161 corrupted rows recovered** — a CSV parsing error packed entire rows 
  into a single column. Recovered using Python's `io.StringIO` parser.
- **Mixed date formats standardized** — 4 different formats unified to ISO 8601.
- **Mixed amount formats parsed** — `$1.250.000`, `1,250,000 COP`, `1250000` 
  all converted to clean numeric values.
- **Inconsistent text normalized** — vendor names, status, and payment methods 
  standardized using `.str.upper()` and mapping dictionaries.
- **Null values handled** — rows missing critical fields dropped; remaining 
  nulls filled with meaningful defaults (`UNKNOWN`, `PENDING`).

## Key Findings

- **227 unpaid invoices** identified after reconciling invoices against payments
- **64 orphan payments** detected — payments referencing invoice IDs with no 
  matching invoice record (a red flag in any AP audit)
- **1 suspicious amount flagged** — a $1B COP entry from a cafeteria vendor, 
  likely a data entry error, marked with `audit_flag`
- **$4.8B COP invoiced vs $254M COP paid** — significant outstanding balance
- **$968M COP outstanding** across 227 unpaid invoices
- **$27.6M COP in orphan payments** — transfers with no matching invoice


## Tools & Technologies

- **Python 3.12 + Pandas 3.x** — data cleaning and reconciliation
- **Git / GitHub** — version control and portfolio traceability
- **SQL** *(coming soon)* — financial analysis queries
- **Power BI** *(coming soon)* — executive dashboard

## How to Run

```bash
# Activate virtual environment
source .venv/bin/activate

# Run any script
python 01_explore_data.py

