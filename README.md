This repository contains the implementation of a Three-Tier Architecture project. The project is divided into three distinct layers,
each handling a specific responsibility to ensure modularity, scalability, and maintainability.

Project Structure
three-tier-project/

├── DBAL/         # Database Access Layer

│   └── Handles interactions with the database

├── BLL/          # Business Logic Layer

│   └── Implements the core logic of the application

├── UI/           # User Interface Layer

│   └── Provides the front-end interface for users

└── README.md     # Project description and instructions


Features

Database Access Layer (DBAL):

Manages connections to the database.
Encapsulates SQL queries for data retrieval and manipulation.
Business Logic Layer (BLL):

Implements core application logic.
Acts as a bridge between the UI and DBAL.
User Interface (UI):

Provides a user-friendly interface for interaction.
Captures user input and displays data.


Technologies Used

Programming Language: Python
Database: SQL
IDE: IDLE (Integrated Development and Learning Environment)
