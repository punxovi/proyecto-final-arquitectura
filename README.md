# Proyecto final — Arquitectura de software

Caso de estudio: **PedidoFácil**, plataforma web de gestión de pedidos para pequeños comercios.

## Contenido

- `documento-arquitectura.md`: Documento de Arquitectura de Software con las 12 secciones solicitadas.
- `diagrams/`: código Mermaid independiente para todos los diagramas.
- `diagrams/diagramas-completos.md`: todos los diagramas reunidos en un único archivo Markdown.
- `app/`: componente funcional mínimo de gestión de pedidos.
- `tests/`: pruebas automatizadas.
- `.github/workflows/ci.yml`: pipeline de integración continua.
- `requirements.txt`: dependencias de ejecución y pruebas.

## Ejecución local

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

La API queda disponible en `http://localhost:8000` y su documentación en `http://localhost:8000/docs`.
La interfaz web local queda disponible en `http://localhost:8000/`.

## Pruebas

```bash
pytest -q
```

## Ejecución con Docker

```bash
docker build -t pedidofacil .
docker run --rm -p 8000:8000 pedidofacil
```

## Diagramas

Los archivos `.mmd` pueden pegarse en [Mermaid Live Editor](https://mermaid.live/) o convertirse con Mermaid CLI:

```bash
npx @mermaid-js/mermaid-cli -i diagrams/01-contexto.mmd -o contexto.svg
```

