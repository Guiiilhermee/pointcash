# Point Cash

Point Cash is a Python terminal program which runs in the Code Institute mock terminal on Heroku.

Users can manage money through the Python terminal choosing deposit, withdraw, transfer and check balance.

Here is the live version of my project. - https://cash-point-2ee1f9c68969.herokuapp.com/

![mock responsive](https://user-images.githubusercontent.com/127660583/254711225-2e2b3b58-0a3d-49d5-96e3-c9391e1961c1.png)

## How to use it

Point Cash is based on ATM machine program.

In this version, the user can add any number on account number and PIN and set the option that you wish.

In options the user can choose number 1, 2, 3, 4 or 5.

1. Deposit
2. Withdraw
3. Transfer
4. Check Balance
5. Exit

Between 1 and 3 enter with the desired amount to make what you wish

Option 4 will show up your balance and option 5 will finish your operation.

## Features 

### Existing Features



### Future Features

- The Google sheet is already synchronized with the program and I would like to set up account number and PIN to start the program, like a real ATM machine.
- Allow more options
- Allow aditional languages

### Data Model

### Testing

- I have tested this program by doing:

    - Passed the code through a PEP8 Linter, fixed and confirmed that there are no problems.
    - Tested in my own terminal and the CI Heroku terminal.
    - Given invalid inputs: when the number does not match the option and different amounts.

### Bugs

- Solved bugs

    - When I wrote my project and ran it with python3 run.py sometimes showed up this message
    
    “File "run.py", line 30
     else:
     ^
    SyntaxError: invalid syntax”

    - which now I know it is in line 30, the problem would be with "else" and I have to investigate.

### Remaining Bugs

- No bugs remaining

### Validator Testing

- PEP8
    - No errors were returned form PEP8online.com

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

- Steps for deployment:
  - Create an new Heroku app
  - Set the buildbacks to Python and NodeJS in that order
  - Link the Heroku app to the repository
  - Click on Deploy
  - Run program

## Credits

  - Unacademy for the details of the ATM machine
  - Deployment terminal from Code Institute.
