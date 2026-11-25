**Acceptance criteria (from Ticket-1)**

- **AC1:** User can log in with a valid email and password
- **AC2:** After 5 failed attempts the account is locked for 15 minutes
- **AC3:** An error message is shown for invalid credentials, without revealing which field is wrong
- **AC4:** The "Remember me" checkbox keeps the user logged in for 30 days
- **AC5:** Password field masks input

**Test cases**

| ID | Title | Preconditions | Steps | Expected result | Type | Covers |
|---|---|---|---|---|---|---|
| TC-01 | Log in with valid email and password | A registered account exists; user is logged out | 1. Open the login page. 2. Enter the registered email. 3. Enter the correct password. 4. Click "Log in". | User is logged in and redirected to their account page. | positive | AC1 |
| TC-02 | Log in to a second registered account | Two registered accounts (A and B) exist; user is logged out | 1. Log in as account B with its email and password. | User is logged in as account B and sees B's account data, not A's. | positive | AC1 |
| TC-03 | Four failed attempts do not lock the account | A registered account exists; user is logged out | 1. Submit a wrong password for the account 4 times. 2. Submit the correct password. | The fifth attempt (correct password) succeeds and the user is logged in. | boundary | AC2 |
| TC-04 | Fifth failed attempt locks the account | A registered account exists; user is logged out | 1. Submit a wrong password 5 times. 2. Submit the correct password. | After the 5th failure the account is locked; the correct password is rejected with a lockout message. | negative | AC2 |
| TC-05 | Account unlocks after 15 minutes | Account was locked by 5 failed attempts at time T | 1. Attempt login with the correct password at T+14 min. 2. Attempt login with the correct password at T+15 min. | Attempt at T+14 is rejected as locked. Attempt at T+15 succeeds. | boundary | AC2 |
| TC-06 | Wrong password shows generic error | A registered account exists; user is logged out | 1. Enter the registered email. 2. Enter a wrong password. 3. Click "Log in". | An error such as "Invalid email or password" is shown. The message does not say which field is wrong. | negative | AC3 |
| TC-07 | Unregistered email shows the same generic error | User is logged out; the email is not registered | 1. Enter an unregistered email. 2. Enter any password. 3. Click "Log in". | The same generic error as TC-06 is shown. It does not reveal that the email is unknown. | negative | AC3 |
| TC-08 | "Remember me" keeps user logged in after browser restart | A registered account exists; user is logged out | 1. Log in with "Remember me" checked. 2. Close and reopen the browser on day 1. | User is still logged in without re-entering credentials. | positive | AC4 |
| TC-09 | "Remember me" session expires after 30 days | User logged in with "Remember me" checked at day 0 | 1. Reopen the app on day 29. 2. Reopen the app on day 30 (after 30 days). | Session is still active on day 29. Session has expired on day 30 and the user must log in again. | boundary | AC4 |
| TC-10 | Session is not kept when "Remember me" is unchecked | A registered account exists; user is logged out | 1. Log in with "Remember me" unchecked. 2. Close and reopen the browser. | User is logged out and must log in again. | negative | AC4 |
| TC-11 | Password characters are masked while typing | User is on the login page | 1. Click into the password field. 2. Type "Secret123". | Each typed character is shown as a mask symbol (e.g., dots), not as plain text. | positive | AC5 |
| TC-12 | Password stays masked after a failed login | A registered account exists; user is on the login page | 1. Type a wrong password. 2. Click "Log in" and wait for the error. 3. Check the password field. | The error appears and the password field still masks the input. The password is not displayed in plain text. | negative | AC5 |
| TC-13 | Email with leading/trailing spaces | A registered account exists; user is logged out | 1. Enter the email with a space before and after it. 2. Enter the correct password. 3. Click "Log in". | Login succeeds, or a clear validation message is shown. The behavior is consistent and does not crash. | boundary | extra |
| TC-14 | Email is case-insensitive | A registered account exists with a lowercase email; user is logged out | 1. Enter the email in uppercase or mixed case. 2. Enter the correct password. 3. Click "Log in". | User is logged in to the same account. | positive | extra |
| TC-15 | Successful login resets the failed-attempt counter | A registered account exists; user is logged out | 1. Submit 4 wrong passwords. 2. Log in with the correct password. 3. Submit 4 more wrong passwords. | The account is not locked after the second set of 4 failures. | boundary | extra |
| TC-16 | Empty email or password is rejected without a login attempt | User is on the login page | 1. Leave the email empty and enter a password. 2. Click "Log in". 3. Enter an email and leave the password empty. 4. Click "Log in". | A validation message is shown for each empty field. No authentication request is made and no failed attempt is counted. | negative | extra |