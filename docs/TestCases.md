# Test Cases for OpenCart Demo

## Test Case 1: New User Registration

**ID:** TC001  
**Description:** Verify registration with valid data.  
**Steps:**

1. Open https://demo.opencart.com/
2. Click "My Account" > "Register"
3. Fill all required fields with valid data (name, email, password, etc.)
4. Accept terms and conditions
5. Click the "Continue" button  
   **Expected Result:** Registration completes successfully and user is redirected to the welcome page.

---

## Test Case 2: Login with Valid Credentials

**ID:** TC002  
**Description:** Verify login using valid email and password.  
**Steps:**

1. Open https://demo.opencart.com/
2. Click "My Account" > "Login"
3. Enter registered email and password
4. Click "Login"  
   **Expected Result:** User logs into their account successfully.

---

## Test Case 3: Search Product and Display Results

**ID:** TC003  
**Description:** Search for the product “MacBook” and verify results.  
**Steps:**

1. Open https://demo.opencart.com/
2. Type “MacBook” into the search field
3. Add one of the displayed products to the cart  
   **Expected Result:** Product appears in search results and can be added to the cart.

---

## Test Case 4: Add Product to Cart

**ID:** TC004  
**Description:** Add the product “iPhone” to the shopping cart.  
**Steps:**

1. Open https://demo.opencart.com/
2. Search for the product “iPhone”
3. Click "Add to Cart" for the iPhone product  
   **Expected Result:** Product is added to the cart and the cart item count updates accordingly.

---

## Test Case 5: Checkout Process as Registered User

**ID:** TC005  
**Description:** Complete the purchase of a product as a registered user.  
**Steps:**

1. Log in to an existing account
2. Add a product to the cart
3. Click on the cart then “Checkout”
4. Fill in the required shipping and payment information
5. Complete the purchase  
   **Expected Result:** Order is confirmed and the order confirmation page is displayed.

---

## Test Case 6: Login with Invalid Credentials (Negative Test)

**ID:** TC006  
**Description:** Test login with incorrect email or password.  
**Steps:**

1. Open https://demo.opencart.com/
2. Click "My Account" > "Login"
3. Enter invalid email or password
4. Click "Login"  
   **Expected Result:** An error message is displayed and the user cannot log in.

---

## Test Case 7: Registration with Missing Mandatory Fields

**ID:** TC007  
**Description:** Test registration by leaving required fields empty.  
**Steps:**

1. Open https://demo.opencart.com/
2. Click "My Account" > "Register"
3. Leave mandatory fields (e.g., email, password) empty
4. Click "Continue"  
   **Expected Result:** Error messages appear for the empty fields and registration is blocked.

---

## Test Case 8: Password Reset Functionality

**ID:** TC008  
**Description:** Test the "Forgot Password" feature.  
**Steps:**

1. Open https://demo.opencart.com/
2. Click "My Account" > "Login"
3. Click the "Forgotten Password" link
4. Enter the registered email and submit the request  
   **Expected Result:** Confirmation that an email has been sent, and the user receives instructions via email.

---

## Test Case 9: Verify Elements on Product Page

**ID:** TC009  
**Description:** Check that all key elements are present on the product page.  
**Steps:**

1. Open https://demo.opencart.com/
2. Click on a product (e.g., "MacBook")
3. Verify that product name, price, description, "Add to Cart" button, and product image are displayed  
   **Expected Result:** All elements are visible and functional.

---

## Test Case 10: Add Product to Wishlist

**ID:** TC010  
**Description:** Test adding a product to the wishlist.  
**Steps:**

1. Log in to an account
2. Open a product page (e.g., "iPhone")
3. Click the "Add to Wish List" button  
   **Expected Result:** Product is added to the wishlist and a confirmation message is shown.

---

## Test Case 11: Display Message When Cart is Empty

**ID:** TC011  
**Description:** Verify that the cart shows a proper message when empty.  
**Steps:**

1. Open https://demo.opencart.com/
2. Click on the cart icon without adding any products  
   **Expected Result:** A message indicating that the cart is empty is displayed.

---

## Test Case 12: Product Filtering in Category

**ID:** TC012  
**Description:** Verify filter functionality within a product category.  
**Steps:**

1. Open https://demo.opencart.com/
2. Navigate to a product category (e.g., "Laptops & Notebooks")
3. Use filters by price or brand  
   **Expected Result:** Products are displayed according to selected filters.

---

## Test Case 13: Logout Functionality

**ID:** TC013  
**Description:** Verify that the user can successfully log out.  
**Steps:**

1. Log in to an existing account
2. Click "My Account" > "Logout"  
   **Expected Result:** User is logged out and redirected to the homepage.

---

## Test Case 14: Add Comment/Feedback on Product

**ID:** TC014  
**Description:** Test adding a comment on a product page.  
**Steps:**

1. Open a product page
2. Write a comment and provide a rating in the review section
3. Submit the comment  
   **Expected Result:** Comment is added and displayed in the reviews section.

---

## Test Case 15: Navigation Through Main Pages

**ID:** TC015  
**Description:** Verify that main navigation links work correctly.  
**Steps:**

1. Open the homepage
2. Click links such as "Desktops," "Laptops & Notebooks," "Components"  
   **Expected Result:** Each link opens the correct category page.
