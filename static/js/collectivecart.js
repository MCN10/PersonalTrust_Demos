var updateBtns = document.getElementsByClassName('update-cart')

for(i = 0; i < updateBtns.length; i++){
  updateBtns[i].addEventListener('click', function(){
    var productId = this.dataset.product
    var action = this.dataset.action
    var color = this.dataset.color
    var size = this.dataset.size
    console.log('productId:', productId, 'action:', action, 'color:', color, 'size:', size)

    if (request.user == 'AnonymousUser'){
      addCookieItem(productId, action, color, size)
    }else{
      updateUserOrder(productId,action, color, size)
      }
  })
}

function addCookieItem(productId, action){
  console.log('User is not authenticated....')
  if (action == 'add'){
    if (cart[productId] == undefined){
      cart[productId] = {'quantity':1}
    }else{
      cart[productId]['quantity'] += 1
    }
  }

  if (action == 'remove'){
    cart[productId]['quantity'] -= 1

    if (cart[productId]['quantity'] <= 0){
      console.log('Item should be deleted')
      delete cart[productId];
    }
  }

  console.log('Cart: ', cart)
  document.cookie = 'cart=' + JSON.stringify(cart) + ";domain;path=/"
  location.reload() 

}


function updateUserOrder(productId, action, color, size){
  console.log('User is authenticated, sending data')

  var url = '/TheCollective/update_item/'
  fetch(url, {
      method:'POST',
      headers:{
        'Content-Type':'application/json',
        'X-CSRFToken': csrftoken,
      },
      body:JSON.stringify({'productId': productId, 'action': action, 'color': color, 'size': size,})
  })

  .then((response) => {
      return response.json()
  })

  .then((data) => {
    console.log('data:' , data)
    location.reload()
  })
}
