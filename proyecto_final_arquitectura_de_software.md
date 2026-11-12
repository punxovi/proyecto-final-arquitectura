# Proyecto Final

* **Asignatura:** Arquitectura de Software
* **Título:** Diseño, documentación y evaluación de la arquitectura de una solución de software empresarial.
* **Modalidad propuesta:** Trabajo en equipos de 3 a 4 estudiantes.
* **Producto final:** Documento de Arquitectura de Software, acompañado de modelos arquitectónicos, diagramas UML y evidencias técnicas de integración continua.

---

## 1. Contexto del proyecto

En la actualidad, las organizaciones de diversos sectores requieren soluciones de software que permitan optimizar sus procesos, gestionar información, automatizar operaciones y responder eficientemente a las necesidades de sus usuarios.

El desarrollo de estas soluciones demanda una arquitectura de software que garantice una adecuada organización de sus componentes, facilite su integración y mantenimiento, y considere atributos de calidad como rendimiento, escalabilidad, disponibilidad y seguridad.

En este contexto, el diseño y la documentación de arquitecturas de software constituyen actividades fundamentales para establecer las bases técnicas de una solución tecnológica, facilitar la comunicación entre los equipos de desarrollo y orientar las decisiones relacionadas con su construcción, implementación y evolución.

Por ello, resulta necesario aplicar principios y estilos arquitectónicos, frameworks de documentación, patrones de diseño y prácticas contemporáneas de desarrollo, como la integración y entrega continuas (CI/CD) y DevOps.

Para el desarrollo de este proyecto, cada equipo de estudiantes deberá seleccionar libremente un sistema de software o aplicación, existente o propuesto, perteneciente a cualquier ámbito de aplicación, como educación, salud, comercio electrónico, servicios, logística, administración pública, gestión empresarial, entre otros.

El sistema seleccionado constituirá el caso de estudio sobre el cual se desarrollará el análisis, diseño, documentación y evaluación de su arquitectura de software, integrando los conocimientos adquiridos durante las tres unidades de la asignatura.

---

## 2. Enunciado del proyecto

Los estudiantes, organizados en equipos de trabajo, deberán asumir el rol de arquitectos de software y seleccionar un sistema o aplicación informática que permita abordar los principales aspectos relacionados con el diseño, documentación y evaluación de una arquitectura de software.

La solución seleccionada podrá corresponder a un sistema existente, cuya arquitectura será analizada y documentada a partir de la información disponible, o a una propuesta de desarrollo de software, para la cual se definirá una arquitectura que responda a sus requerimientos funcionales y no funcionales.

A partir del sistema seleccionado, cada equipo deberá elaborar un **Documento de Arquitectura de Software (DAS)** que contemple la identificación y justificación de estilos arquitectónicos, la aplicación de patrones de diseño, la especificación de requerimientos, el modelado mediante diagramas UML y la documentación de las diferentes vistas arquitectónicas.

Asimismo, deberán identificar y evaluar los principales atributos de calidad de la arquitectura propuesta, incorporar prácticas de integración y entrega continuas (CI/CD) y aplicar principios de DevOps y mejora continua.

Como parte del proyecto, los estudiantes deberán implementar y demostrar un proceso básico de integración continua mediante una herramienta apropiada, utilizando un componente funcional mínimo del sistema seleccionado.

El proyecto finalizará con la entrega del Documento de Arquitectura de Software y una presentación en la que cada equipo deberá explicar y justificar las principales decisiones arquitectónicas adoptadas, así como demostrar las evidencias técnicas correspondientes.

---

## 3. Objetivo general

Documentar una arquitectura de software del diseño de una solución empresarial, aplicando principios y estilos arquitectónicos, frameworks de documentación, patrones de diseño, atributos de calidad y prácticas de integración continua y DevOps.

---

## 4. Condiciones para seleccionar el sistema o aplicación

El sistema seleccionado deberá cumplir las siguientes condiciones:

1. Contar con funcionalidades que permitan identificar y documentar requerimientos funcionales y no funcionales.
2. Presentar una estructura que permita definir componentes, módulos, relaciones e interacciones.
3. Permitir la aplicación y justificación de estilos arquitectónicos y patrones de diseño.
4. Tener suficiente complejidad para representar diferentes vistas arquitectónicas mediante diagramas UML.
5. Permitir la identificación y evaluación de atributos de calidad.
6. Posibilitar la implementación de un pipeline básico de integración continua sobre un componente de software.

> **Importante:** No será necesario desarrollar completamente el sistema seleccionado. El proyecto estará centrado en su arquitectura, documentación y evaluación, junto con una implementación técnica mínima que permita evidenciar las prácticas de CI/CD.

Cuando se seleccione un sistema existente y no se disponga de su documentación interna, los estudiantes deberán diferenciar claramente los aspectos conocidos de las decisiones arquitectónicas propuestas por el equipo.

Los requerimientos no funcionales deberán ser definidos por los estudiantes, considerando al menos rendimiento, escalabilidad, disponibilidad, seguridad y mantenibilidad. Cada requerimiento deberá expresarse mediante condiciones verificables.

---

## 5. Estructura del Documento de Arquitectura de Software

Se propone la siguiente estructura de 12 secciones, agrupadas según los resultados de aprendizaje de la asignatura.

### Parte I. Fundamentos y definición arquitectónica

| Sección | Contenido y evidencias solicitadas |
| :--- | :--- |
| **1. Introducción y contexto** | Descripción de la organización, problemática, objetivos, alcance, actores y restricciones del proyecto. |
| **2. Análisis de estilos arquitectónicos** | Comparación de al menos tres estilos arquitectónicos aplicables. Ventajas, desventajas y justificación de la selección. |
| **3. Arquitectura de solución** | Descripción de la arquitectura propuesta, componentes principales, tecnologías y mecanismos de comunicación. Identificación de antipatrones y estrategias para evitarlos. |

### Parte II. Diseño y documentación

| Sección | Contenido y evidencias solicitadas |
| :--- | :--- |
| **4. Especificación de requerimientos** | Identificación y priorización de requerimientos funcionales y no funcionales. Matriz de trazabilidad entre requerimientos y decisiones arquitectónicas. |
| **5. Framework de documentación** | Aplicación del modelo de vistas arquitectónicas $4+1$ de Kruchten para documentar la solución. |
| **6. Modelado arquitectónico y UML** | Diagramas de casos de uso, componentes, clases, secuencia y despliegue, organizados según las vistas pertinentes. |
| **7. Patrones de diseño** | Selección y aplicación justificada de al menos tres patrones de diseño, explicando el problema que resuelven y representando su aplicación mediante UML. |
| **8. Decisiones arquitectónicas** | Registro de decisiones arquitectónicas (ADR), alternativas consideradas, justificaciones y consecuencias. |

### Parte III. Calidad, CI/CD y DevOps

| Sección | Contenido y evidencias solicitadas |
| :--- | :--- |
| **9. Evaluación de atributos de calidad** | Análisis de rendimiento, escalabilidad, disponibilidad, seguridad y mantenibilidad mediante escenarios de calidad y una evaluación basada en riesgos y compromisos arquitectónicos. |
| **10. Integración y entrega continuas** | Diseño e implementación básica de un pipeline CI/CD que incluya integración del código, construcción y ejecución automatizada de pruebas. |
| **11. DevOps y mejora continua** | Propuesta de colaboración desarrollo-operaciones, monitoreo, retroalimentación, métricas, automatización y mecanismos de mejora continua. |
| **12. Conclusiones y recomendaciones** | Evaluación global de la arquitectura, cumplimiento de requerimientos, limitaciones, riesgos y propuestas de evolución futura. |

---

## 6. Modelos y diagramas mínimos

Para mantener el alcance del proyecto dentro de una asignatura de arquitectura, se solicita incluir los siguientes artefactos:

| Artefacto | Propósito |
| :--- | :--- |
| **Diagrama de contexto** | Representar el sistema y su interacción con actores y sistemas externos. |
| **Diagrama de casos de uso** | Identificar funcionalidades y actores principales. |
| **Diagrama de componentes** | Representar los módulos y sus dependencias. |
| **Diagrama de clases** | Mostrar la estructura lógica y la aplicación de patrones de diseño. |
| **Diagrama de secuencia** | Representar al menos dos interacciones relevantes. |
| **Diagrama de despliegue** | Describir la distribución física de los componentes. |
| **Diagrama de actividad** | Representar un proceso de negocio relevante. |
| **Diagrama del pipeline CI/CD** | Mostrar las etapas de integración, pruebas y entrega. |

> *Nota:* Los diagramas deberán mantener coherencia entre sí y con los requerimientos y decisiones arquitectónicas.

---

## 7. Entregables

1. **Documento de Arquitectura de Software:** Archivo PDF con las 12 secciones desarrolladas, tablas, diagramas, decisiones y justificaciones.
2. **Repositorio técnico:** Código de un componente mínimo, pruebas automatizadas y configuración del pipeline CI/CD.
3. **Evidencias de ejecución:** Capturas o registros verificables del funcionamiento del pipeline y resultados de las pruebas.
4. **Presentación y defensa:** Exposición de la arquitectura propuesta, sus decisiones fundamentales, evaluación de calidad y demostración de CI/CD.

---

## 8. Rúbrica

### Unidad I - Principios de Arquitectura de Software (Máximo: 30 pts.)

| Criterio de evaluación | Destacado (100%) | Logrado (75%) | En desarrollo (50%) | Insuficiente (25%) | Máximo |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **1. Reconoce los principales estilos arquitectónicos de software.** | Identifica y compara correctamente al menos tres estilos, justificando ventajas y limitaciones. *(7 pts.)* | Identifica y compara tres estilos con justificaciones parcialmente desarrolladas. *(5,25 pts.)* | Identifica estilos, pero presenta comparaciones incompletas. *(3,5 pts.)* | Identifica estilos con errores o sin comparación pertinente. *(1,75 pts.)* | **7** |
| **2. Evalúa las tendencias y tecnologías actuales, como las arquitecturas orientadas a modelos y orientadas a servicios.** | Analiza tendencias, justificando su pertinencia para el proyecto. *(7 pts.)* | Analiza tecnologías actuales con justificación suficiente, aunque limitada. *(5,25 pts.)* | Describe tecnologías sin analizar adecuadamente su pertinencia. *(3,5 pts.)* | Presenta tecnologías sin análisis o con errores conceptuales. *(1,75 pts.)* | **7** |
| **3. Integra estilos arquitectónicos de software apropiados para definir una arquitectura de solución.** | Integra estilos coherentes con los requerimientos y justifica técnicamente su selección. *(9 pts.)* | Integra estilos adecuados, con algunas debilidades en su justificación. *(6,75 pts.)* | Integra estilos parcialmente apropiados, con inconsistencias. *(4,5 pts.)* | Propone estilos inadecuados o sin integración coherente. *(2,25 pts.)* | **9** |
| **4. Integra patrones de diseño de software apropiados para definir una arquitectura de solución.** | Incorpora patrones pertinentes, justificando su aplicación y contribución arquitectónica. *(7 pts.)* | Incorpora patrones adecuados con justificación limitada. *(5,25 pts.)* | Incorpora patrones con errores o escasa relación con la solución. *(3,5 pts.)* | Presenta patrones incorrectos o sin aplicación pertinente. *(1,75 pts.)* | **7** |

### Unidad II - Diseño y Documentación de Arquitecturas de Software (Máximo: 40 pts.)

| Criterio de evaluación | Destacado (100%) | Logrado (75%) | En desarrollo (50%) | Insuficiente (25%) | Máximo |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **5. Reconoce los principales patrones de diseño y frameworks.** | Identifica y justifica correctamente los patrones y el framework de documentación seleccionados. *(8 pts.)* | Identifica patrones y frameworks adecuados, con justificaciones parcialmente desarrolladas. *(6 pts.)* | Identifica algunos patrones y frameworks, pero presenta confusiones. *(4 pts.)* | Presenta identificaciones incorrectas o sin fundamentación. *(2 pts.)* | **8** |
| **6. Identifica los requisitos clave de un sistema de software, establece prioridades y relaciones entre ellos, para traducirlos en decisiones arquitectónicas sólidas.** | Especifica y prioriza RF/RNF, establece trazabilidad y justifica decisiones arquitectónicas. *(12 pts.)* | Especifica y prioriza requisitos, con algunas debilidades en trazabilidad o justificación. *(9 pts.)* | Presenta requisitos incompletos y relaciones arquitectónicas poco claras. *(6 pts.)* | Presenta requisitos deficientes, sin priorización ni trazabilidad adecuada. *(3 pts.)* | **12** |
| **7. Describe una arquitectura de software utilizando diversos enfoques de documentación y lenguajes de descripción arquitectónica.** | Documenta integralmente la arquitectura mediante $4+1$ y diagramas UML correctos, completos y coherentes. *(14 pts.)* | Documenta la arquitectura con diagramas adecuados, aunque presenta omisiones menores. *(10,5 pts.)* | Presenta documentación parcial, con diagramas incompletos o inconsistentes. *(7 pts.)* | Documentación deficiente, diagramas incorrectos o sin coherencia arquitectónica. *(3,5 pts.)* | **14** |
| **8. Identifica los atributos de calidad de un sistema a nivel arquitectónico.** | Identifica y especifica atributos de calidad mediante escenarios medibles y verificables. *(6 pts.)* | Identifica atributos pertinentes, aunque algunos escenarios carecen de precisión. *(4,5 pts.)* | Identifica atributos sin establecer criterios verificables suficientes. *(3 pts.)* | Identifica atributos incorrectamente o sin relación con el sistema. *(1,5 pts.)* | **6** |

### Unidad III - Evaluación de Atributos y Prácticas Contemporáneas en Desarrollo de Software (Máximo: 30 pts.)

| Criterio de evaluación | Destacado (100%) | Logrado (75%) | En desarrollo (50%) | Insuficiente (25%) | Máximo |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **9. Implementa prácticas efectivas de integración y entrega continuas (CI/CD), aplicando herramientas y mejores prácticas para automatizar el proceso de desarrollo y entrega de software.** | Implementa y demuestra un pipeline CI/CD funcional, con construcción, pruebas automatizadas y evidencias. *(10 pts.)* | Implementa un pipeline funcional con algunas limitaciones en automatización o evidencias. *(7,5 pts.)* | Implementa parcialmente el pipeline, con errores o etapas incompletas. *(5 pts.)* | Presenta una configuración deficiente o sin ejecución funcional demostrable. *(2,5 pts.)* | **10** |
| **10. Aplica principios de DevOps para optimizar la colaboración entre equipos de desarrollo y operaciones, mejorando la eficiencia y calidad del ciclo de vida del software.** | Aplica principios DevOps mediante roles, colaboración, automatización y flujo de trabajo claramente definidos. *(7 pts.)* | Aplica principios DevOps adecuados, con algunas debilidades en colaboración o automatización. *(5,25 pts.)* | Describe prácticas DevOps con aplicación parcial o poco fundamentada. *(3,5 pts.)* | Presenta prácticas incorrectas o sin aplicación efectiva. *(1,75 pts.)* | **7** |
| **11. Incorpora mecanismos de mejora continua en el flujo de desarrollo, mediante métricas, retroalimentación y herramientas de monitoreo.** | Incorpora métricas, monitoreo, retroalimentación y acciones de mejora claramente definidas. *(7 pts.)* | Incorpora mecanismos pertinentes, aunque algunas métricas o acciones están poco desarrolladas. *(5,25 pts.)* | Presenta mecanismos parciales, con métricas o acciones poco claras. *(3,5 pts.)* | Presenta mecanismos deficientes o sin relación con la mejora continua. *(1,75 pts.)* | **7** |
| **12. Evalúa el impacto de la automatización y la cultura colaborativa en la mejora continua del producto y del proceso.** | Evalúa fundamentadamente el impacto de CI/CD y DevOps mediante evidencias, indicadores y conclusiones. *(6 pts.)* | Evalúa el impacto con argumentos pertinentes, aunque con evidencias limitadas. *(4,5 pts.)* | Presenta una evaluación superficial, con escaso sustento técnico. *(3 pts.)* | Presenta afirmaciones sin evidencias o análisis pertinente. *(1,5 pts.)* | **6** |

> **Puntuación Total Máxima:** **100 puntos**

### Consideraciones para la calificación

* La rúbrica utiliza cuatro niveles de desempeño: **Destacado**, **Logrado**, **En desarrollo** e **Insuficiente**.
* Cuando un criterio no presente ninguna evidencia evaluable, se asignarán **1 punto**, independientemente de los niveles descritos.
* La distribución es de **30 puntos** para la Unidad I, **40 puntos** para la Unidad II y **30 puntos** para la Unidad III.
* **Nota:** La puntuación total se obtiene sumando los puntos alcanzados en los 12 criterios, hasta un máximo de **100 puntos**.