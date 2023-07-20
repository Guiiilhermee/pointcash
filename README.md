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
0. Exit

Between 1 and 3 enter with the desired amount to make what you wish

Option 4 will show up your balance and option 0 will finish your operation.

## Features 

### Existing Features

- Firstly the program shows to enter the Account Number
- Secondly to enter with a PIN number

![Account number](https://user-images.githubusercontent.com/127660583/254709726-a7e44e9d-e1c0-4859-a7bd-270360c919f6.png)


![PIN number](https://user-images.githubusercontent.com/127660583/254709727-84865923-a48b-477f-a92b-b40df2653de0.png)


- After add Account number and pin the display will show options and the user can choose one.

![options](https://user-images.githubusercontent.com/127660583/254740291-a2faf02b-724d-4290-948d-04b66e48bd47.png)

- If the user enter with a different number the program prints "Invalid option. Please try again."

![Invalid option](https://user-images.githubusercontent.com/127660583/254733837-f16a0dcd-740e-4ec2-8e0f-2c92abadf506.png)

- If the user enter with a high amount the program prints "Insufficient balance."

![ins. balance](https://user-images.githubusercontent.com/127660583/254709731-56884122-611d-4daa-a9c6-929773ea0022.png)

- When the user enter with option 1 "deposit" and just set the amount.

![deposit](https://user-images.githubusercontent.com/127660583/254709721-c064f288-1ac8-491d-aa16-3344fc7bfb3a.png)

- When the user enter with option 4 "check balance" the display prints the current balance on the screen.

![balance](https://user-images.githubusercontent.com/127660583/254739554-6e05813d-f036-4997-ad71-5e9f2fea8612.png)

- When the user enter with option 0 "Exit" the program stops showing a message "Thanks for using Cash Point."

![exit](https://user-images.githubusercontent.com/127660583/254740291-a2faf02b-724d-4290-948d-04b66e48bd47.png)

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
