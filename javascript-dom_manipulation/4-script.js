const click = document.querySelector('#add_item');
const add_item = document.querySelector('.my_list');

click.addEventListener('click', function () {
  const create_li = document.createElement('li');
  const create_item = document.createTextNode('Item');
  create_li.appendChild(create_item);
  add_item.appendChild(create_li);
});
