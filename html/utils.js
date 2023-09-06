const USER_TOKEN_KEY = 'USER_TOKEN_KEY'
const LOGGED_IN_USER_KEY = 'LOGGED_IN_USER'
const LOGIN_NAV_ITEM_KEY = 'login-nav-item'
const PRODUCTS_NAV_ITEM_KEY = 'products-nav-item'
const LOGOUT_NAV_ITEM_KEY = 'logout-nav-item'
const ORDERS_NAV_ITEM_KEY = 'orders-nav-item'
const USER_DETAILS_NAV_ITEM_KEY = 'user-details-nav-item'
const USER_ROLE = 'role'
const EDIT_PRODUCT = 'EDIT_PRODUCT'

const setValueInLocalStorage = (key, value) => {
    localStorage.setItem(key, value)
}

const getValueFromLocalStorage = (key) => {
    return localStorage.getItem(key)
}

const clearValueInLocalStorage = (key) => {
    localStorage.removeItem(key)
}


const getQueryStringParam = (key) => {
    const urlParams = new URLSearchParams(window.location.search)
    return urlParams.get(key)
}
