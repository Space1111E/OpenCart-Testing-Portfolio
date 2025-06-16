# Bug Report

## Bug ID: BR001

## Title: Login fails with valid credentials

## Reported By: Elena B

## Date: 2025-06-16

## Environment:

- Website URL: https://demo.opencart.com/
- Browser & Version: Chrome 114.0.5735.199
- OS: Windows 11
- Device: Laptop

## Description:

When trying to login with a valid user account, the system rejects the credentials and shows an error message.

## Steps to Reproduce:

1. Open https://demo.opencart.com/
2. Click "My Account" > "Login"
3. Enter valid email and password
4. Click "Login"

## Expected Result:

User should be logged in successfully.

## Actual Result:

Error message shown: "Warning: No match for E-Mail Address and/or Password."

## Severity:

High

## Priority:

Urgent

## Screenshots / Videos:

![login-error](https://example.com/screenshot.png)

## Additional Notes:

Tested on multiple browsers with same result.

---

## Bug ID: BR002

## Title: Registration allows duplicate email addresses

## Reported By: Elena B

## Date: 2025-06-16

## Environment:

- Website URL: https://demo.opencart.com/
- Browser & Version: Chrome 114.0.5735.199
- OS: Windows 11
- Device: Laptop

## Description:

The registration form allows creating multiple accounts using the same email address.

## Steps to Reproduce:

1. Open https://demo.opencart.com/
2. Register a new user with an email (e.g., test@example.com)
3. Log out
4. Register again with the same email address
5. Complete registration

## Expected Result:

System should prevent registration with an email that is already in use.

## Actual Result:

Registration completes successfully with duplicate email.

## Severity:

High

## Priority:

High

---

## Bug ID: BR003

## Title: Cart item quantity does not update correctly

## Reported By: Elena B

## Date: 2025-06-16

## Environment:

- Website URL: https://demo.opencart.com/
- Browser & Version: Chrome 114.0.5735.199
- OS: Windows 11
- Device: Laptop

## Description:

When updating the quantity of a product in the shopping cart, the total price does not update accordingly.

## Steps to Reproduce:

1. Add a product to the cart
2. Go to the cart page
3. Change quantity from 1 to 3
4. Click update

## Expected Result:

Total price updates to reflect the new quantity.

## Actual Result:

Total price remains unchanged.

## Severity:

Medium

## Priority:

Medium

---

## Bug ID: BR004

## Title: Checkout process allows proceeding without agreeing to terms

## Reported By: Elena B

## Date: 2025-06-16

## Environment:

- Website URL: https://demo.opencart.com/
- Browser & Version: Chrome 114.0.5735.199
- OS: Windows 11
- Device: Laptop

## Description:

User is able to complete checkout without selecting the "I agree to the Terms & Conditions" checkbox.

## Steps to Reproduce:

1. Add product to cart
2. Proceed to checkout
3. Do not check the terms and conditions box
4. Complete checkout

## Expected Result:

System should block checkout and prompt the user to agree to terms.

## Actual Result:

Checkout completes successfully without agreement.

## Severity:

Critical

## Priority:

Urgent

---

## Bug ID: BR005

## Title: Broken link in the footer to Privacy Policy

## Reported By: Elena B

## Date: 2025-06-16

## Environment:

- Website URL: https://demo.opencart.com/
- Browser & Version: Chrome 114.0.5735.199
- OS: Windows 11
- Device: Laptop

## Description:

The "Privacy Policy" link in the website footer leads to a 404 error page.

## Steps to Reproduce:

1. Scroll down to the footer
2. Click on the "Privacy Policy" link

## Expected Result:

Page opens with Privacy Policy content.

## Actual Result:

404 Page Not Found error appears.

## Severity:

Low

## Priority:

Low

---

## Bug ID: BR006

## Title: Search returns no results for valid products

## Reported By: Elena B

## Date: 2025-06-16

## Environment:

- Website URL: https://demo.opencart.com/
- Browser & Version: Chrome 114.0.5735.199
- OS: Windows 11
- Device: Laptop

## Description:

Searching for certain valid product names (e.g., "iPhone") returns no results.

## Steps to Reproduce:

1. Enter "iPhone" in search bar
2. Press enter or click search

## Expected Result:

Matching products displayed in results.

## Actual Result:

"No products found" message displayed.

## Severity:

High

## Priority:

High

---

## Bug ID: BR007

## Title: Review form allows submission without rating

## Reported By: Elena B

## Date: 2025-06-16

## Environment:

- Website URL: https://demo.opencart.com/
- Browser & Version: Chrome 114.0.5735.199
- OS: Windows 11
- Device: Laptop

## Description:

Product review form accepts submissions without selecting a star rating.

## Steps to Reproduce:

1. Open a product page
2. Write a review comment
3. Leave rating unselected
4. Submit review

## Expected Result:

Form should prompt user to select a rating before submitting.

## Actual Result:

Review is accepted with no rating.

## Severity:

Medium

## Priority:

Medium

---
