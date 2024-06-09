# loanapp-prototype

## Introduction

A prototype for a p2p loan app that allows different users to borrow and lend money between each others

## Design

### User Roles

#### Borrower
A Borrower wants to borrow money and choose a way to repay
- Create Account: Borrower needs to create account and provide info
- Create Money Request: Borrower can then create money request and specify the needs
- Sign Contract: Borrower signs the contract (TO-DO feature)
- Receive Funds: Borrower receives money from Lender
- Payment Schedule: Borrower receives a payment schedule based on contract
- Repayment: Borrower repays based on payment schedule
- Missed Payment: Penalty for missing payments

#### Lender
A Lender wants to lend money and get return
- Create Account: Lender needs to create account
- Deposit Funds: lender needs to desposit funds
- Accept Money Request: Lender can accept money request
- Sign Contract: Lender signs the contract (TO-DO feature)
- Send Funds: Lender sends the fund
- Receive Repayment: Lender receives repayment from Borrower

### User Journey

#### Account Creation
- Borrower applies by submitting personal info
- Lender creates account by submitting personal info

#### Lender Deposit
- Lender deposits funds to the account

#### MoneyRequest Creation
- Borrower creates the request including amount, tenor, monthly repayment % (the remainder will be asked to pay back at the end)
- Underwriting decision based on the info and mock bureau (TO-DO feature)
- Price given to Borrower based on Underwriting decision
- Borrower chooses to accept, and confirms the creation of MoneyRequest

#### MoneyRequest Confirm
- Lender accepts the MoneyRequest (if deposit is higher than Deposit Balance)
- Borrower is notified with the acceptance, and receives a repayment schedule

#### Monthly Repayment
- Lender repays on monthly basis based on repayment schedule
- Miss payment handling (TO-DO feature)

#### MoneyRequest Cancel
- Borrow can cancel the request if not been accepted by Lender

#### MoneyRequest Close
- A MoneyRequest will be closed if it is cancelled, or fully paid

## Installation

.

## Usage

.

## Testing

.
