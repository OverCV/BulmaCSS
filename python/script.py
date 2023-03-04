from pyodide.http import pyfetch
import pyodide
import asyncio

# Global variable
I = 0


def toggle_menu(e):
    navbar_menu = document.querySelector('#navbarMenu')
    navbar_menu.classList.toggle('is-active')


def open_modal(e):
    modal = document.querySelector('.modal')
    modal.classList.add('is-active')


def close_modal(e):
    modal = document.querySelector('.modal')
    modal.classList.remove('is-active')


async def make_request(url, method, headers=None):
    if not headers:
        headers = {
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/json'
        }

    response = await pyfetch(
        url=url,
        method=method,
        headers=headers
    )
    return await response.json()


async def load_contact_us(e):
    data = await make_request(url='https://randomuser.me/api', method='GET')

    image_data = data['results'][0]['picture']['large']
    user_image = document.getElementById('user-image')
    user_image.src = image_data

    f_name = document.getElementById('f-name')
    l_name = document.getElementById('l-name')
    age = document.getElementById('age')
    email = document.getElementById('email')
    cell = document.getElementById('cell')
    country = document.getElementById('country')
    city = document.getElementById('city')

    f_name_data = data['results'][0]['name']['first']
    l_name_data = data['results'][0]['name']['last']
    age_data = data['results'][0]['dob']['age']
    email_data = data['results'][0]['email']
    cell_data = data['results'][0]['cell']
    country_data = data['results'][0]['location']['country']
    city_data = data['results'][0]['location']['city']

    f_name.value = f_name_data
    l_name.value = l_name_data
    age.value = age_data
    email.value = email_data
    cell.value = cell_data
    country.value = country_data
    city.value = city_data


def add_cart(e):
    global I
    I += 1
    txt = f'Mis compras ({str(I)})'
    pyscript.write(f'my-cart {txt}')


def main():
    # Funcionalidad Menú
    navbar_burguer = document.querySelector('#navbarBurger')
    navbar_burguer.addEventListener(
        'click', pyodide.create_proxy(toggle_menu)
    )

    # Funcionalidad modal
    join = document.getElementById('join')
    modal_bg = document.querySelector('.modal-background')

    # Al clickear sobre el botón aparece el modal
    join.addEventListener(
        'click', pyodide.create_proxy(open_modal)
    )
    # Al clickear fuera del modal (parte oscura) desaparece
    modal_bg.addEventListener(
        'click', pyodide.create_proxy(close_modal)
    )

    # Funcionalidad fetch
    join.addEventListener(
        'click', pyodide.create_proxy(load_contact_us)
    )

    # Funcionalidad comprar
    buy = document.querySelector('#buy')
    buy.addEventListener(
        'click', pyodide.create_proxy(add_cart)
    )


main()
