<div align="center">
  <h1 align="center">
    <strong>Freddy Fazbear’s Pizza</strong>
    <br>
    <sub><strong>W H E R E &nbsp; C O D E &nbsp; M E E T S &nbsp; A N I M A T R O N I C S</strong></sub>
  </h1>
</div>


<p align="center">
  <img src="https://github.com/user-attachments/assets/4d55fff3-7604-4a02-9125-83fbbb6c6092" width="350">
</p>

<p align="center"><i>"Technology becomes powerful when it tells a story."</i></p>

---

# 🎙️ **El Mundo Detrás de los Animatrónicos**

Este proyecto abre una ventana al centro de control de Freddy Fazbear’s Pizza, donde todo lo que ocurre entre bastidores cobra vida.
Aquí, los animatrónicos no son simples personajes:
son entidades que se administran, se organizan y evolucionan dentro de un sistema web creado desde cero.

La aplicación recrea cómo sería gestionar el restaurante desde dentro, combinando estructura, diseño y una narrativa que captura la esencia del universo FNAF.
Una plataforma donde cada decisión cuenta, cada acción tiene impacto y cada animatrónico tiene una historia que se mueve contigo.

>Un espacio digital pensado para sentirse real.<br>
>Tu acceso directo al corazón del restaurante.

---

# 🍕 **La Misión: Crear un Sistema Vivo**

Este proyecto construye una aplicación web completa usando **Django 5**, diseñada para funcionar como el verdadero panel de administración de Freddy’s:

* CRUD avanzado
* Roles y permisos
* Registro/Login
* Tema oscuro con cookies
* Vistas basadas en clases y funciones
* Plantillas profesionales

---

# 🖥️ **Funciones Que Dan Vida al Restaurante**

A continuación se muestran todas las funcionalidades principales del sistema, acompañadas de capturas reales de la web.

## 🟣 **Animatronics Showcase (Lista)**

Ruta: `/freddyapp/list`

<p align="center">
  <img src="https://github.com/user-attachments/assets/75327b8e-64b9-469e-8423-96d6ee90df3c" width="800">
</p>



## 🔍 **Inside the Animatronic (Detalles)**

Ruta: `/freddyapp/<id>/view`

<p align="center">
  <img src="https://github.com/user-attachments/assets/3d709ac0-6685-480d-be12-fc8ad235225b" width="800">
</p>



## ✨ **Bring a New Animatronic to Life (Crear)**

Ruta: `/freddyapp/new`

<p align="center">
  <img src="https://github.com/user-attachments/assets/3b6a57d8-5732-4741-acdd-de3741b772fe" width="800">
</p>



## 🛠️ **Modify Their Destiny (Editar)**

Ruta: `/freddyapp/<id>/edit`

<p align="center">
  <img src="https://github.com/user-attachments/assets/2febaf9a-648f-4d42-b854-734369071cb5" width="800">
</p>



## 🗑️ **Retire an Animatronic (Borrar)**

Ruta: `/freddyapp/<id>/delete`

<p align="center">
  <img src="https://github.com/user-attachments/assets/537a2c4d-dacf-46bd-af08-941ae4f23d0f" width="800">
</p>

---

# 🔐 **Control de Acceso: Quién Entra y Quién No**

## 📝 **Registro**

Ruta: `/freddyapp/newuser`

<p align="center">
  <img src="https://github.com/user-attachments/assets/b5ffa1f7-4cd0-4832-86cb-afddf3fe815d" width="600">
</p>



## 🔑 **Inicio de Sesión**

Ruta: `/freddyapp/login`

<p align="center">
  <img src="https://github.com/user-attachments/assets/953aee7c-5079-4904-9c4b-fd3864b6fc17" width="600">
</p>



## 🚪 **Cierre de Sesión**

Ruta: `/freddyapp/logout`
Botón disponible en la barra superior.

---

# 🌓 **El Poder de las Cookies: Cambiar la Experiencia Visual**

El sistema permite cambiar entre modo claro y oscuro:

* Activar modo oscuro → `/freddyapp/theme`
* Volver al modo claro → `/freddyapp/clearcookies`

<p align="center">
  <img src="https://github.com/user-attachments/assets/b5f215a8-4fd1-4abc-80a4-3f27c420a840" width="800">
</p>

---

# 🔑 **Quién Manda Aquí: Roles y Permisos**

| Grupo  | Permisos                |
| ------ | ----------------------- |
| Client | Puede ver animatrónicos |
| Staff  | Crear, editar y borrar  |

Los usuarios registrados reciben automáticamente el rol **Client**.

---

# 🧠 **Anatomía del Proyecto**

```
django-freddy/
├── freddyproject/
├── freddyapp/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│── templates/
│       ├── base.html
│       ├── animatronic_list.html
│       ├── animatronic_view.html
│       ├── animatronic_form.html
│       ├── animatronic_confirm_delete.html
│       ├── login.html
│       └── register.html
└── manage.py
```

---

# ⚙️ **Arranca el Sistema: Guía Rápida**

```bash
python -m venv venv
venv\Scripts\activate
pip install django
python manage.py runserver
```

Luego abre:
➡ [http://127.0.0.1:8000/freddyapp/list](http://127.0.0.1:8000/freddyapp/list)

---

# 👩‍💻 **Quién Está Detrás del Código**

<p align="center">
  <img src="https://github.com/user-attachments/assets/d549c019-35bb-4af8-8e61-8d6885c6cd9b" width="200">
</p>

**Oumniya — Developer & Designer**<br>
GitHub: [https://github.com/Oumniya17](https://github.com/Oumniya17)

---

# 🎤 **Ideas Para Llevarse a Casa**

> “Good code solves problems.
> Great code tells a story.”

Este proyecto combina:

* técnica
* diseño
* creatividad
* narrativa

Un sistema **vivo**, construido con estilo, propósito y visión.
<div align="center"> <strong>Gracias por llegar hasta aquí.<br> El escenario se apaga… pero el sistema sigue vivo.</strong> </div>

---
