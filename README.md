# Sistema de Gestión, Inventario y Pedidos para Supermercados (PWA)

**Integrantes:**
- Antonio Fernández (C.I: 30.506.712)

**Subproyecto:** Desarrollo de Aplicaciones I  
**Profesor:** Rafael Barrios  

---

## 1. Descripción General
El sistema es una Aplicación Web Progresiva (PWA) orientada a la gestión centralizada de inventarios, control de stock en tiempo real y recepción de pedidos para supermercados y abastos locales.

---

## 2. Metodología de Desarrollo en V (Fase Descendente)

### A. Análisis de Requisitos (Requirement Gathering)
- **Necesidades del Usuario:** Control automatizado de inventarios, erradicación de errores en conteo manual y rapidez en la captura de pedidos y ventas en caja.
- **Funcionalidades:**
  - Gestión de productos por categorías, precios y niveles de existencia.
  - Carrito de compras virtual para pedidos de clientes y registro directo de ventas físicas en caja.
  - Generación de reportes de rotación de productos y métricas del negocio.
  - Funcionalidades PWA (manifest, instalabilidad y caché offline básico vía Service Worker).

### B. Análisis del Sistema (System Analysis)
- **Comportamiento General:** Sistema cliente-servidor web interactivo.
- **Arquitectura Funcional:** 
  - **Frontend:** HTML5, CSS3, JS y Service Worker para PWA.
  - **Backend:** Django Framework (Python).
  - **Persistencia:** Base de datos relacional SQLite gestionada vía ORM de Django.

### C. Diseño de Software / Arquitectura (Software Design)
- **Patrón Arquitectónico:** Modelo-Vista-Template (MVT).
- **Módulos:**
  - `accounts`: Autenticación, usuarios y roles.
  - `inventory`: Control de productos y categorías.
  - `orders`: Carrito y procesamiento de compras.
- **Stack Tecnológico:** Python 3.12, Django, SQLite, HTML/CSS, Virtualenv (`venv`).

### D. Diseño de Módulos (Module Design)
- **Modelos de Datos Principales:**
  - `User`: Extendiendo `AbstractUser` con campo `role` (`ADMIN`, `GESTOR`, `USUARIO`, `VISITANTE`).
  - `Category`: `name`, `description`.
  - `Product`: `name`, `barcode`, `price`, `stock`, `category`.
  - `Order`: `user`, `status`, `total`, `created_at`.
  - `OrderItem`: `order`, `product`, `quantity`, `subtotal`.

---

## 3. Guía de Instalación y Ejecución
> **Nota de Hardware:** Se utiliza `venv` de Python como alternativa ligera a contenedores Docker.

1. Activar entorno virtual:
   ```bash
   venv\Scripts\activate
