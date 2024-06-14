## Architecture Overview

The Loanapp is a monolithic app built using Django framework, the app is composed of the following components:

### 1. Accounts
This component is responsible for handling all account-related operations. It provides an interface for users to create their account, which can be either a Borrower or a Lender, and then to submit their personal and financial information

### 2. MoneyRequest
This component is responsible for handling all money-request operations. It provides an interface for Borrower to Create / Update / Cancel a MoneyRequest, for Lender to Read and Accept a MoneyRequest.

### 3. Contracts
Once a MoneyRequest is accepted, the Contracts component takes over. Contracts manages the lifecycle of the LoanContracts between the Borrower and the Lender, including the Creation of LoanContracts, disbursement of funds, creation of payment schedules, tracking repayments, and handling any changes to the loan terms.

Each app communicates with others via Django's internal mechanisms. The system uses a PostgreSQL database for persistent storage, with separate tables for each app to ensure data isolation. The entire application is containerized using Docker, which allows for easy deployment and scaling.