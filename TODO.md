# TODO: Implementar Soft Deletes y Auto-incremental ID

## Pasos a completar:

1. **Editar models.py**: Añadir campo `deleted_at` de tipo `datetime` nullable a los modelos `Categoria` y `Producto`. Importar `datetime`.

2. **Editar crud.py**:
   - Actualizar consultas de obtener para filtrar `deleted_at == None`.
   - Modificar `eliminar_categoria` y `eliminar_producto` para set `deleted_at = datetime.now()` en lugar de `session.delete()`.
   - Añadir funciones `obtener_categorias_eliminadas()` y `obtener_productos_eliminados()`.

3. **Editar main.py**:
   - Cambiar endpoints `@app.delete("/categorias/{id}")` y `@app.delete("/productos/{id}")` para usar soft delete.
   - Añadir nuevos endpoints `@app.get("/categorias/eliminadas")` y `@app.get("/productos/eliminados")` para ver eliminados.

4. **Editar schemas.py** (si necesario): Añadir esquemas de respuesta para eliminados si se requieren campos adicionales.

5. **Probar cambios**: Ejecutar la aplicación y verificar que los soft deletes funcionen y los endpoints nuevos devuelvan los eliminados.

## Progreso:
- [x] Paso 1 completado
- [x] Paso 2 completado
- [x] Paso 3 completado
- [x] Paso 4 completado (si aplicable)
- [x] Paso 5 completado
