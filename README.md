Description in English and Ukrainian 
# VPN service in the form of a website.
The user can create a "client site" (the actual name/url of the site that the client wants to visit). It will act as a proxy server. Relatively speaking, this "client site" becomes an intermediary between the original site and the client. The user can freely navigate between the pages of the external site without leaving the "client site". 
The routing looks like localhos/{user_site_name}/{routes_on_original_site}...
The user can see the following statistics:
1.	The number of clicks between the pages of the client's website
2.	The amount of data that was sent and downloaded through the "client site"
## Project Launch and Annotation:
docker-compose up --build
1.	Tested on https://espreso.tv/. When using other resources for testing, there may be nuances in the display of shapes and images.
2.	The system already has a ready-made User: email=1234567899@admin.com / password=1234567899@admin.com and UserSite: site_url=https://espreso.tv/ / name=espreso 
3.	Authentication is performed using Knox TokenAuthentication, so after Login, you need to take from the response (example / "token": "513e6ddd3ba93064620839ef8f5f5493540d0d11c8451df15269db29fbe644c3"), and add to the headers (example /Authorisation: Token "513e6ddd3ba93064620839ef8f5f5493540d0d11c8451df15269db29fbe644c3")

## Endpoints
### http://localhost:8000/registration/  User registration
### http://localhost:8000/login/  Login
### http://localhost:8000/user/   View User
### http://localhost:8000/user/<int:id>/  Editing User data. Full or partial changes to all of their data.
### http://localhost:8000/site/new/  Creation of a website. The number is not limited. Links and site names must be unique
### http://localhost:8000/espreso/  Going to the site. Only the GET method. 
### http://localhost:8000/espreso/{routes_on_original_site}  Moving around the site. Supports all available methods.
### http://localhost:8000/statistics/espreso/  View statistics. Website URL / number of visits / amount of data 
### http://127.0.0.1:8081/  Access to the database. Login and password in .env

# VPN сервіс у вигляді веб сайту.
Користувач може створити «клієнтський сайт» (власна назва / url сайту який клієнт хоче відвідувати). Він буде виступати як проксі сервер. Умовно кажучи цей  «клієнтський сайт» стає посередником між оригінальним сайтом і клієнтом. Користувач може вільно переміщатись між сторінками зовнішнього сайту не полишаючи «клієнтський сайт». 
Роутинг виглядає як localhos/{user_site_name}/{routes_on_original_site}…
Користувач може бачити наступну статистику: 
1.	Кількість переходів між сторінками  «клієнтського сайту»
2.	Об'єм даних який було відправлено і завантажено через «клієнтський сайт»
## Запуск проекту та Анотація:
docker-compose up --build
1.	Відтестовано на сайті https://espreso.tv/. При використанні інших ресурсів для перевірки можуть виникнути нюанси з відображенням форм та зображень.
2.	В системі вже є готовий User: email=1234567899@admin.com / password=1234567899@admin.com та UserSite: site_url=https://espreso.tv/ / name=espreso 
3.	Authentication виконано за допомогою Knox TokenAuthentication тому після Login необхідно з відповіді взяти (приклад / "token": "513e6ddd3ba93064620839ef8f5f5493540d0d11c8451df15269db29fbe644c3"), та додати до заголовків (приклад / Authorization: Token "513e6ddd3ba93064620839ef8f5f5493540d0d11c8451df15269db29fbe644c3")

## Endpoints
### http://localhost:8000/registration/  Реєстрація User
### http://localhost:8000/login/  Логін
### http://localhost:8000/user/   Перегляд User
### http://localhost:8000/user/<int:id>/  Редагування даних User. Повні чи часткові зміни всіх його даних.
### http://localhost:8000/site/new/  Створення сайту. Кількість не обмежена. Посилання і назви сайту мають бути унікальні
### http://localhost:8000/espreso/  Перехід на сайт. Тільки метод GET. 
### http://localhost:8000/espreso/{routes_on_original_site}  Переміщення по сайту. Підтримує всі доступні методи.
### http://localhost:8000/statistics/espreso/  Перегляд статистики. URL сайту / кількість переходів / Об'єм даних 
### http://127.0.0.1:8081/  Доступ до бази даних. Логін та пароль в .env

