window.onload = fetchData;

function fetchData() {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const productCode = urlParams.get('productCode');

    document.getElementById('product-code').innerText = productCode;

    getProductStatus(productCode);
}

function getProductStatus(productCode) {

    const orderStatus = "Доставлен";
    document.getElementById('order-status').innerText = orderStatus;
}

