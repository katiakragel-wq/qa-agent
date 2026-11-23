**Acceptance criteria (from Ticket-1):**

- **AC1:** User can log in with a valid email and password
- **AC2:** After 5 failed attempts the account is locked for 15 minutes
- **AC3:** An error message is shown for invalid credentials, without revealing which field is wrong
- **AC4:** The "Remember me" checkbox keeps the user logged in for 30 days
- **AC5:** Password field masks input

**Test cases:**

| ID | Title | Preconditions | Steps | Expected result | Type | Covers |
|---|---|---|---|---|---|---|
| TC-01 | Login succeeds with valid email and password | A registered user account exists and is not locked | 1. Open the login page. 2. Enter the registered email. 3. Enter the correct password. 4. Click "Log in". | User is logged in and taken to their account page. | positive | AC1 |
| TC-02 | Account is not locked after 4 failed attempts | A registered user account exists and is not locked | 1. Open the login page. 2. Enter the registered email with a wrong password. 3. Repeat step 2 four times in total. 4. Enter the correct password and click "Log in". | Login succeeds. The account is not locked after 4 failed attempts. | boundary | AC2 |
| TC-03 | Account is locked after 5 failed attempts | A registered user account exists and is not locked | 1. Open the login page. 2. Enter the registered email with a wrong password. 3. Repeat step 2 five times in total. 4. Enter the correct password and click "Log in". | After the 5th failed attempt, an account-locked message is shown. The correct password is rejected while the account is locked. | boundary | AC2 |
| TC-04 | Lock expires after 15 minutes | Account was locked by 5 failed attempts at time T | 1. At T + 14 min 59 s, attempt login with the correct password. 2. At T + 15 min 1 s, attempt login with the correct password. | At T + 14 min 59 s login is rejected. At T + 15 min 1 s login succeeds. | boundary | AC2 |
| TC-05 | Invalid password shows generic error | A registered user account exists and is not locked | 1. Open the login page. 2. Enter the registered email. 3. Enter a wrong password. 4. Click "Log in". | An error message such as "Invalid email or password" is shown. The message does not indicate which field is wrong. User is not logged in. | negative | AC3 |
| TC-06 | Unregistered email shows the same generic error | No account exists for the email used | 1. Open the login page. 2. Enter an unregistered email. 3. Enter any password. 4. Click "Log in". | The same generic error as TC-05 is shown. The message does not reveal that the email is unregistered. | negative | AC3 |
| TC-07 | Remember me keeps user logged in for 30 days | A registered user account exists and is not locked | 1. Open the login page. 2. Enter valid credentials. 3. Check "Remember me". 4. Click "Log in". 5. Close and reopen the browser. 6. Set the clock to 29 days after login and reload the app. | User remains logged in at 29 days. | positive | AC4 |
| TC-08 | Remember me session expires after 30 days | Login was done with "Remember me" checked at time T | 1. Set the clock to T + 30 days + 1 minute. 2. Reload the app. | User is logged out and asked to log in again. | boundary | AC4 |
| TC-09 | Password input is masked | User is on the login page | 1. Click into the password field. 2. Type a password. | Characters appear as masked dots or asterisks, not as plain text. The input type is password. | positive | AC5 |
| TC-10 | Successful login resets the failed-attempt counter | A registered user account exists and is not locked | 1. Enter a wrong password 4 times. 2. Log in with the correct password. 3. Enter a wrong password 4 times. 4. Enter the correct password. | Account is not locked at any point. The counter resets after a successful login. | extra |  extra |
| TC-11 | Without "Remember me" the session does not persist for 30 days | A registered user account exists and is not locked | 1. Log in with valid credentials and leave "Remember me" unchecked. 2. Close and reopen the browser. | User is no longer logged in. (Behaviour is not specified in the ticket and should be confirmed with the product owner.) | extra | extra |