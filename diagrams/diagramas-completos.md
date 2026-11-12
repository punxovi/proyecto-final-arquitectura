# Diagramas completos — PedidoFácil

Este archivo reúne todos los diagramas del proyecto. Cada sección contiene un diagrama Mermaid independiente.

## 1. Diagrama de contexto

```mermaid
flowchart LR
    Cliente[Cliente] -->|HTTPS/REST| PF((PedidoFácil))
    Operador[Operador] -->|HTTPS/REST| PF
    Admin[Administrador] -->|HTTPS/REST| PF
    PF -->|consulta/autorización| Identidad[Proveedor de identidad]
    PF -->|persistencia| DB[(PostgreSQL)]
    PF -->|pago opcional| Pago[Servicio de pagos]
    PF -->|notificaciones| Notif[Correo / mensajería]
```

## 2. Diagrama de casos de uso

```mermaid
flowchart LR
    C[Cliente] --> UC1((Registrar pedido))
    C --> UC2((Consultar pedido))
    C --> UC3((Recibir notificación))
    O[Operador] --> UC2
    O --> UC4((Confirmar pedido))
    O --> UC5((Actualizar estado))
    A[Administrador] --> UC6((Gestionar productos))
    A --> UC7((Gestionar usuarios))
    UC4 -. incluye .-> UC5
    UC5 -. dispara .-> UC3
```

## 3. Diagrama de componentes

```mermaid
flowchart TB
    UI[Web UI] --> API[API REST / FastAPI]
    API --> APP[Order Application Service]
    APP --> DOMAIN[Dominio: Order, Product, Customer]
    APP --> REPO[OrderRepository]
    REPO --> DB[(PostgreSQL)]
    APP --> AUTH[Identity Adapter]
    APP --> PAY[Payment Adapter]
    APP --> NOTIF[Notification Adapter]
    NOTIF --> EMAIL[Proveedor de mensajería]
```

## 4. Diagrama de clases

```mermaid
classDiagram
    class Order {
      +UUID id
      +OrderStatus status
      +Money total
      +confirm()
      +changeStatus()
    }
    class OrderItem {
      +int quantity
      +Money unitPrice
      +subtotal()
    }
    class Product { +UUID id +String name +Money price }
    class Customer { +UUID id +String name +String email }
    class OrderService { +createOrder() +updateStatus() }
    class OrderRepository { +save(order) +findById(id) +findAll() }
    class NotificationAdapter { +notifyStatusChanged(event) }
    class PricingStrategy { <<interface>> +calculate(items) }
    Order "1" *-- "1..*" OrderItem
    OrderItem --> Product
    Order --> Customer
    OrderService --> OrderRepository
    OrderService --> NotificationAdapter
    OrderService --> PricingStrategy
```

## 5. Diagrama de secuencia: crear pedido

```mermaid
sequenceDiagram
    actor Cliente
    participant API as API REST
    participant Service as OrderService
    participant Repo as OrderRepository
    participant DB as PostgreSQL
    Cliente->>API: POST /api/orders
    API->>API: Validar contrato
    API->>Service: createOrder(data)
    Service->>Service: Calcular total y estado inicial
    Service->>Repo: save(order)
    Repo->>DB: INSERT pedido
    DB-->>Repo: id creado
    Repo-->>Service: pedido persistido
    Service-->>API: pedido
    API-->>Cliente: 201 Created
```

## 6. Diagrama de secuencia: cambio de estado

```mermaid
sequenceDiagram
    actor Operador
    participant API as API REST
    participant Service as OrderService
    participant Repo as OrderRepository
    participant Events as Event Bus
    participant Notif as Notification Adapter
    Operador->>API: PATCH /orders/{id}/status
    API->>Service: updateStatus(id, status)
    Service->>Repo: findById(id)
    Repo-->>Service: pedido
    Service->>Service: Validar transición
    Service->>Repo: save(pedido actualizado)
    Service->>Events: OrderStatusChanged
    Events-->>Notif: entregar evento
    Notif-->>Operador: notificación al cliente
    Service-->>API: pedido actualizado
    API-->>Operador: 200 OK
```

## 7. Diagrama de despliegue

```mermaid
flowchart TB
    Browser[Navegador] --> CDN[CDN / Reverse Proxy]
    CDN --> API1[Contenedor API 1]
    CDN --> API2[Contenedor API 2]
    API1 --> DB[(PostgreSQL administrado)]
    API2 --> DB
    API1 --> Queue[Cola opcional]
    API2 --> Queue
    Queue --> Worker[Worker de notificaciones]
    Worker --> External[Proveedor externo]
    CI[GitHub Actions] --> Registry[Container Registry]
    Registry --> API1
    Registry --> API2
```

## 8. Diagrama de actividad: proceso de pedido

```mermaid
flowchart TD
    A([Inicio]) --> B[Cliente ingresa productos]
    B --> C{¿Datos válidos?}
    C -- No --> D[Mostrar errores]
    D --> B
    C -- Sí --> E[Calcular total]
    E --> F[Crear pedido PENDIENTE]
    F --> G{¿Pago requerido?}
    G -- Sí --> H[Solicitar autorización de pago]
    H --> I{¿Pago aprobado?}
    I -- No --> J[Cancelar pedido]
    I -- Sí --> K[Confirmar pedido]
    G -- No --> K
    K --> L[Preparar y entregar]
    L --> M([Fin])
    J --> M
```

## 9. Diagrama del pipeline CI/CD

```mermaid
flowchart LR
    Commit[Push / Pull Request] --> Checkout[Checkout]
    Checkout --> Install[Instalar dependencias]
    Install --> Test[pytest]
    Test --> Build[Construir imagen Docker]
    Build --> Security[Escaneo de dependencias]
    Security --> Deploy[Entrega a staging]
    Deploy --> Evidence[Reporte y evidencia]
```

