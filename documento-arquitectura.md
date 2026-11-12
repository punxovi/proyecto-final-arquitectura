# Documento de Arquitectura de Software (DAS)

## PedidoFácil: plataforma web de gestión de pedidos

**Versión:** 1.0  
**Fecha:** 12 de noviembre de 2026  
**Tipo de solución:** propuesta académica  
**Equipo:** completar con nombres de los integrantes

> Este documento distingue entre decisiones propuestas por el equipo y hechos implementados en el prototipo. La implementación mínima disponible en este repositorio cubre la API de salud y la gestión básica de pedidos; no pretende ser el producto completo.

## 1. Introducción y contexto

### 1.1 Problema

Los pequeños comercios suelen recibir pedidos por teléfono, mensajería o redes sociales. Esto provoca registros duplicados, errores de cálculo, poca trazabilidad del estado del pedido y dificultad para conocer la carga operativa. PedidoFácil centraliza el registro, consulta y actualización de pedidos en una API web que puede ser consumida por una interfaz de escritorio o móvil.

### 1.2 Objetivo

Diseñar y documentar una solución empresarial sencilla, segura y mantenible que permita registrar pedidos, calcular su total, consultar su estado y avanzar el pedido durante el proceso de atención.

### 1.3 Alcance

Incluye clientes, catálogo básico, creación de pedidos, consulta de pedidos, actualización de estados, autenticación conceptual, auditoría, notificaciones y pipeline CI/CD. El prototipo implementado contiene creación, consulta, cambio de estado y health check, usando almacenamiento en memoria para mantener el alcance académico.

Fuera de alcance para esta entrega: pagos reales, despacho georreferenciado, aplicación móvil nativa, multiempresa avanzada y operación productiva 24/7.

### 1.4 Actores

| Actor | Responsabilidad |
|---|---|
| Cliente | Consulta productos y registra o revisa sus pedidos. |
| Operador | Confirma pedidos y cambia estados operativos. |
| Administrador | Gestiona productos, usuarios y configuración. |
| Servicio de pagos | Confirma pagos, si se habilita el módulo. |
| Servicio de notificaciones | Envía correo o mensajes de cambios de estado. |
| CI/CD | Construye, prueba y valida cada cambio. |

### 1.5 Restricciones y supuestos

- El sistema se implementa inicialmente como una aplicación web modular.
- La primera versión se despliega en contenedores sobre una nube pública.
- La base de datos relacional es la fuente de verdad para producción.
- El prototipo usa memoria únicamente para facilitar la demostración.
- Se considera una escala inicial de 100 pedidos por minuto y 500 usuarios concurrentes.
- Las decisiones son propuestas académicas y deben validarse con pruebas de carga y seguridad antes de producción.

## 2. Análisis de estilos arquitectónicos

| Estilo | Ventajas | Limitaciones | Pertinencia |
|---|---|---|---|
| Monolito modular | Simple de construir y desplegar; transacciones directas; bajo costo operativo. | Escalamiento conjunto; un error puede afectar toda la aplicación si no hay aislamiento. | Alta para el alcance inicial. |
| Microservicios | Escalamiento independiente; equipos autónomos; aislamiento de fallas. | Mayor complejidad operacional, observabilidad, red y consistencia distribuida. | Media; sobredimensionado para el MVP. |
| Arquitectura hexagonal | Separa dominio de infraestructura; facilita pruebas y reemplazo de adaptadores. | Requiere más interfaces y disciplina de diseño. | Alta como estructura interna. |
| Orientada a eventos | Desacopla notificaciones, auditoría y procesos asíncronos. | Consistencia eventual y mayor complejidad de depuración. | Media para evolución futura. |

### 2.1 Selección

Se adopta un **monolito modular con organización hexagonal y eventos internos**. La decisión equilibra simplicidad y calidad: el despliegue inicial es único, pero los módulos de pedidos, catálogo, identidad y notificaciones tienen límites claros. Si el volumen lo justifica, notificaciones puede extraerse posteriormente como servicio independiente.

### 2.2 Tendencias consideradas

- **API-first:** el contrato HTTP permite que distintas interfaces consuman la solución.
- **Contenedores:** Docker hace reproducible el entorno.
- **Infraestructura como código y CI/CD:** automatizan validaciones y reducen errores manuales.
- **Arquitectura orientada a modelos:** las entidades Pedido, Cliente y Producto expresan el dominio y sus reglas.
- **Servicios desacoplados:** las notificaciones y pagos se integran mediante adaptadores, sin contaminar el dominio.

## 3. Arquitectura de solución

### 3.1 Vista general

La solución tiene un cliente web, un API Gateway/reverse proxy, una API PedidoFácil, una base de datos PostgreSQL y adaptadores para pagos y notificaciones. Internamente, la API se divide en presentación, aplicación, dominio e infraestructura.

### 3.2 Componentes principales

| Componente | Responsabilidad | Tecnología propuesta |
|---|---|---|
| Web UI | Formularios, consulta y seguimiento. | React o HTML/TypeScript |
| API REST | Expone casos de uso y valida contratos. | Python/FastAPI |
| Dominio | Reglas de pedidos, estados y totales. | Python puro |
| Persistencia | Repositorios y transacciones. | SQLAlchemy + PostgreSQL |
| Identidad | Usuarios, roles y tokens. | JWT/OAuth2 |
| Notificaciones | Publica cambios de estado. | SMTP/servicio externo |
| Observabilidad | Logs, métricas y trazas. | OpenTelemetry + Prometheus |
| CI/CD | Calidad automatizada. | GitHub Actions |

### 3.3 Mecanismos de comunicación

- Cliente a API: HTTPS y JSON mediante REST.
- API a base de datos: conexión privada y pool de conexiones.
- API a servicios externos: HTTPS con timeouts, reintentos limitados e idempotencia.
- Eventos internos: publicación de `OrderStatusChanged` para notificaciones y auditoría.

### 3.4 Antipatrones y prevención

| Antipatrón | Riesgo | Prevención |
|---|---|---|
| God Object | Una clase concentra reglas y dependencias. | Módulos por dominio y servicios pequeños. |
| Big Ball of Mud | Dependencias circulares y límites difusos. | Capas, contratos e inspección de dependencias. |
| Distributed Monolith | Microservicios demasiado acoplados. | Mantener monolito hasta que exista una razón medible para separar. |
| Shared Database sin reglas | Cambios de un módulo rompen otros. | Repositorios y dueño explícito de cada agregado. |
| Secretos en código | Exposición de credenciales. | Secret Manager/variables protegidas y escaneo en CI. |

## 4. Especificación de requerimientos

### 4.1 Requerimientos funcionales

| ID | Requerimiento | Prioridad |
|---|---|---|
| RF-01 | El cliente podrá crear un pedido con uno o más productos. | Must |
| RF-02 | El sistema calculará el total automáticamente. | Must |
| RF-03 | El cliente y operador podrán consultar pedidos autorizados. | Must |
| RF-04 | El operador podrá actualizar el estado del pedido. | Must |
| RF-05 | El sistema registrará fecha, usuario y cambio de estado. | Should |
| RF-06 | El sistema enviará notificación al cambiar de estado. | Should |
| RF-07 | El administrador gestionará productos y precios. | Should |
| RF-08 | El sistema integrará un proveedor de pagos opcional. | Could |

### 4.2 Requerimientos no funcionales verificables

| ID | Atributo | Escenario medible |
|---|---|---|
| RNF-01 | Rendimiento | El 95% de las consultas de pedidos responderá en menos de 500 ms con 500 usuarios concurrentes. |
| RNF-02 | Escalabilidad | La API podrá aumentar a 1.000 pedidos por minuto agregando instancias sin modificar el dominio. |
| RNF-03 | Disponibilidad | La API tendrá objetivo mensual de 99,5%, excluyendo mantenimiento anunciado. |
| RNF-04 | Seguridad | Las operaciones privadas requerirán token válido y rol autorizado; ningún secreto estará en el repositorio. |
| RNF-05 | Mantenibilidad | El pipeline deberá aprobar pruebas y revisión antes de fusionar cambios; cobertura objetivo inicial: 80%. |
| RNF-06 | Recuperabilidad | La base de datos tendrá respaldo diario y RPO de 24 h/RTO de 4 h en la primera versión. |
| RNF-07 | Observabilidad | Cada petición tendrá ID de correlación y los errores 5xx se medirán por minuto. |

### 4.3 Matriz de trazabilidad

| Requerimiento | Decisión/Componente | Evidencia |
|---|---|---|
| RF-01, RF-02 | Módulo Order y servicio de aplicación | `app/main.py`, prueba de total |
| RF-03, RF-04 | API REST y estados enumerados | endpoints GET/PATCH |
| RF-05 | Auditoría/evento de dominio | diseño futuro y ADR-004 |
| RNF-01 | API stateless, pool y caché futura | escenario de rendimiento |
| RNF-02 | Monolito replicable detrás de proxy | diagrama de despliegue |
| RNF-04 | HTTPS, JWT, RBAC y gestión de secretos | ADR-003 |
| RNF-05 | Pytest y GitHub Actions | `.github/workflows/ci.yml` |

## 5. Framework de documentación 4+1

| Vista | Qué documenta | Artefacto |
|---|---|---|
| Lógica | Entidades y reglas del dominio. | Diagrama de clases |
| Desarrollo | Módulos y dependencias del código. | Diagrama de componentes |
| Procesos | Interacciones y concurrencia. | Diagramas de secuencia y actividad |
| Física | Nodos y despliegue. | Diagrama de despliegue |
| Escenarios (+1) | Casos de uso que validan las vistas. | Casos de uso y flujos principales |

## 6. Modelado arquitectónico y UML

Los códigos fuente de los diagramas están en `diagrams/`:

1. `01-contexto.mmd`: contexto del sistema.
2. `02-casos-uso.mmd`: actores y funcionalidades.
3. `03-componentes.mmd`: módulos y dependencias.
4. `04-clases.mmd`: entidades y patrones.
5. `05-secuencia-crear-pedido.mmd`: creación de pedido.
6. `06-secuencia-cambio-estado.mmd`: actualización y notificación.
7. `07-despliegue.mmd`: distribución física.
8. `08-actividad-pedido.mmd`: proceso de negocio.
9. `09-pipeline-cicd.mmd`: integración continua.

También se encuentran todos reunidos en `diagrams/diagramas-completos.md`, separados por nombre y listos para copiar en el documento final.

La coherencia entre diagramas se basa en el mismo vocabulario: Cliente, Operador, Pedido, Producto, OrderService, OrderRepository y NotificationAdapter.

## 7. Patrones de diseño

### 7.1 Repository

`OrderRepository` abstrae el almacenamiento. El dominio no depende de PostgreSQL, lo que permite probar con un repositorio en memoria y cambiar la infraestructura sin modificar reglas de negocio.

### 7.2 Service Layer

`OrderService` coordina el caso de uso de creación: valida, calcula el total, persiste y publica el cambio. Evita colocar lógica de negocio en los controladores HTTP.

### 7.3 Adapter

`NotificationAdapter` y `PaymentAdapter` convierten contratos internos a APIs externas. El dominio depende de interfaces propias, no de un proveedor específico.

### 7.4 Strategy

Las estrategias de cálculo de envío o descuento pueden variar según tipo de cliente o zona. La regla se selecciona mediante una interfaz, evitando condicionales extensos.

## 8. Decisiones arquitectónicas (ADR)

### ADR-001 — Monolito modular como primera versión

- **Estado:** aceptada.
- **Contexto:** el equipo necesita entregar una solución demostrable con bajo costo operativo.
- **Alternativas:** microservicios desde el inicio; monolito sin módulos.
- **Decisión:** monolito modular con límites explícitos.
- **Consecuencias:** despliegue simple y menor latencia; el escalamiento es conjunto.

### ADR-002 — API REST sobre HTTPS

- **Estado:** aceptada.
- **Contexto:** se requiere interoperabilidad con web, móvil y servicios externos.
- **Alternativas:** GraphQL; comunicación directa entre clientes y base de datos.
- **Decisión:** REST/JSON con versionado `/api`.
- **Consecuencias:** contrato claro y fácil de probar; algunas consultas pueden requerir más de una llamada.

### ADR-003 — Autenticación JWT y autorización RBAC

- **Estado:** propuesta para producción.
- **Contexto:** clientes y operadores requieren permisos diferentes.
- **Alternativas:** sesiones de servidor; API sin autenticación.
- **Decisión:** OAuth2/JWT, roles `CLIENTE`, `OPERADOR`, `ADMIN`.
- **Consecuencias:** API stateless y escalable; se debe gestionar expiración, revocación y almacenamiento seguro de tokens.

### ADR-004 — Eventos para notificaciones

- **Estado:** aceptada como evolución.
- **Contexto:** enviar notificaciones no debe bloquear la confirmación del pedido.
- **Alternativas:** llamada síncrona; cola/evento.
- **Decisión:** publicar `OrderStatusChanged` y procesar con adaptador asíncrono.
- **Consecuencias:** mejor desacoplamiento; consistencia eventual y necesidad de reintentos/idempotencia.

## 9. Evaluación de atributos de calidad

### 9.1 Escenarios de calidad

| Atributo | Estímulo | Respuesta esperada | Medida |
|---|---|---|---|
| Rendimiento | 500 usuarios consultan pedidos. | API procesa sin degradación crítica. | P95 < 500 ms. |
| Escalabilidad | Aumenta el tráfico 5x. | Se agregan réplicas de API. | 1.000 pedidos/minuto. |
| Disponibilidad | Se detiene una instancia. | Proxy deriva tráfico a otra instancia. | 99,5% mensual. |
| Seguridad | Usuario intenta actualizar pedido ajeno. | API rechaza operación y registra evento. | 401/403 y log auditable. |
| Mantenibilidad | Se cambia el proveedor de correo. | Se modifica un adaptador. | Sin cambios en dominio. |

### 9.2 Riesgos y compromisos

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---:|---:|---|
| Pérdida de datos en memoria | Alta en prototipo | Alto | PostgreSQL y respaldos antes de producción. |
| Dependencia de proveedor externo | Media | Medio | Adapter, timeout, retry y fallback. |
| Complejidad prematura | Media | Alto | Mantener monolito hasta observar métricas. |
| Acceso no autorizado | Media | Alto | JWT, RBAC, validación y auditoría. |

El principal compromiso es priorizar simplicidad y mantenibilidad sobre independencia total de despliegue. La separación modular permite evolucionar cuando existan métricas que justifiquen el costo.

## 10. Integración y entrega continuas

El pipeline de GitHub Actions ejecuta:

1. checkout del repositorio;
2. configuración de Python 3.12;
3. instalación reproducible de dependencias;
4. ejecución de cuatro pruebas automatizadas;
5. validación de importación y arranque lógico de la API.

La evidencia se obtiene desde la pestaña **Actions** del repositorio: ejecución verde, resumen de pasos y salida de `pytest`. Para completar una demostración, se recomienda adjuntar una captura de una ejecución exitosa y otra ejecución fallida corregida.

### 10.1 Estrategia de ramas

- `main`: versión estable.
- `feature/*`: trabajo individual.
- Pull request obligatorio hacia `main`.
- CI obligatorio antes de fusionar.
- Etiquetas `vX.Y.Z` para entregas.

## 11. DevOps y mejora continua

### 11.1 Flujo y responsabilidades

Desarrollo implementa y prueba; revisión técnica valida diseño; operaciones administra configuración, despliegue y alertas; el equipo completo revisa métricas y retrospectivas. La responsabilidad es compartida: quien modifica un módulo también aporta pruebas, documentación y observabilidad.

### 11.2 Métricas

| Métrica | Objetivo inicial | Frecuencia |
|---|---:|---|
| Tasa de éxito del pipeline | >= 95% | Por semana |
| Tiempo medio de recuperación | < 4 h | Por incidente |
| Tiempo de ciclo de PR | < 24 h | Por sprint |
| P95 de API | < 500 ms | Diario |
| Errores 5xx | < 1% | Diario |
| Cobertura de pruebas | >= 80% | Cada build |

### 11.3 Mejora continua

Cada sprint se revisan fallos del pipeline, latencia, errores y comentarios de usuarios. Se selecciona al menos una acción de mejora priorizada. Ejemplos: agregar prueba de autorización, incorporar base de datos de prueba, crear dashboard de latencia y automatizar despliegue a entorno de staging.

## 12. Conclusiones y recomendaciones

La arquitectura propuesta satisface el alcance académico porque relaciona requerimientos, estilos, patrones, vistas 4+1, atributos de calidad y CI/CD. El monolito modular resulta suficiente para comenzar y evita la complejidad de operar microservicios prematuramente. La organización hexagonal mantiene el dominio independiente de HTTP y de la persistencia.

La principal limitación del prototipo es el almacenamiento en memoria y la ausencia de autenticación real, pagos y despliegue productivo. Antes de publicar el sistema se recomienda incorporar PostgreSQL, migraciones, JWT/RBAC, pruebas de carga, escaneo de dependencias, logs estructurados, métricas, respaldos y despliegue en staging.

Como evolución futura se propone extraer notificaciones cuando las métricas demuestren necesidad, incorporar una cola de mensajes, habilitar pagos idempotentes y añadir un panel de indicadores operativos.

## Anexo A. Evidencias sugeridas

- Captura del repositorio con estructura de carpetas.
- Captura de `pytest -q` con pruebas exitosas.
- Captura de una ejecución verde de GitHub Actions.
- Captura de `/docs` o una llamada a `/health`.
- Exportación de los nueve diagramas como SVG o PNG.
- Registro de decisiones ADR y revisión por los integrantes.

