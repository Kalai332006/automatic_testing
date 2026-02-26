import json
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_full_flow(driver):

    data = json.load(open("fixtures/data.json"))

    # Login
    login = LoginPage(driver)
    login.login(data["valid_user"]["username"], data["valid_user"]["password"])

    # Add product
    inventory = InventoryPage(driver)
    inventory.add_product()
    inventory.go_to_cart()

    # Checkout
    cart = CartPage(driver)
    cart.click_checkout()

    checkout = CheckoutPage(driver)
    checkout.enter_details(
        data["checkout_details"]["first_name"],
        data["checkout_details"]["last_name"],
        data["checkout_details"]["zip_code"]
    )

    checkout.finish_order()

    # Verify success
    assert "checkout-complete" in driver.current_url