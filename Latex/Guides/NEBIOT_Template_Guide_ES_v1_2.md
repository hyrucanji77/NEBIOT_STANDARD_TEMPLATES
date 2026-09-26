# Plantillas de proyectos y resultados NEBIOT — edición 1.2

Estándar rector: Estándar NEBIOT 0.8.2. Esta edición de plantillas no modifica el estándar.

## Contenido
Cuatro etapas (NIP, prefactibilidad, factibilidad y PD) y tres productos contables (ExAnte, ExPost y Migration_Reconciliation), cada uno en inglés estadounidense y español. Cada producto tiene DOCX, DOTX, código completo Overleaf y vista previa PDF compilada. Dos libros de cálculo tienen instrucciones equivalentes y fórmulas idénticas. Use un idioma y un formato de edición controlado; no diligencie copias paralelas innecesarias.

## ¿Dónde corresponde cada producto?
- **NIP:** identifique estimaciones disponibles y vacíos; no se requiere una cuenta futura completa de monitoreo para evaluar el concepto.
- **Prefactibilidad:** adjunte una cuenta ExAnte indicativa sustentada y el plan de estudios. Los vacíos no cuantificados permanecen explícitos.
- **Factibilidad y PD:** adjunte el informe ExAnte controlado, libro, evidencia y perfil aplicable. Conserve la estimación y sus supuestos originales como copia fechada.
- **Presentación de monitoreo:** diligencie ExPost para el período real, con contrafactual conservado, evidencia medida o calificada, resultado con signo, incertidumbre, obligaciones y registros separados de evaluación. El cálculo ex post no es automáticamente un resultado verificado.
- **Migración:** use Migration_Reconciliation con ExAnte y/o ExPost según corresponda. Conserve el cálculo original, registre la armonización y muestre aparte el efecto del método NEBIOT. Conserve otras unidades de carbono externas y su estado original en los registros de migración; no las renombre como NVEU.

El nuevo anexo A de cada plantilla de etapa identifica sus productos contables. Son identificadores de plantilla, no requisitos ni etapas nuevos del estándar. Todas las referencias a cláusulas y ecuaciones corresponden al Estándar NEBIOT 0.8.2.

## Word
Abra un DOCX para editar una copia del proyecto o un DOTX para generar un documento nuevo. Diligencie controles entre corchetes. Tablas y áreas narrativas se expanden; la cantidad inicial de filas y páginas no limita la presentación. Añada tablas y anexos según necesidad. Reemplace los tres campos de logotipo de portada con imágenes autorizadas del ejecutor, proponente y partes interesadas, conservando proporción y funciones reales. No altere el logotipo NEBIOT. Actualice campos Word antes de exportar el PDF y revise las páginas completas.

## Overleaf
Cargue la carpeta Overleaf como ZIP/proyecto propio, seleccione XeLaTeX y uno de los archivos raíz:

NEBIOT_NIP_EN.tex / NEBIOT_NIP_ES.tex
NEBIOT_Prefeasibility_EN.tex / NEBIOT_Prefeasibility_ES.tex
NEBIOT_Feasibility_EN.tex / NEBIOT_Feasibility_ES.tex
NEBIOT_PD_EN.tex / NEBIOT_PD_ES.tex
NEBIOT_ExAnte_EN.tex / NEBIOT_ExAnte_ES.tex
NEBIOT_ExPost_EN.tex / NEBIOT_ExPost_ES.tex
NEBIOT_Migration_Reconciliation_EN.tex / NEBIOT_Migration_Reconciliation_ES.tex

Los campos de portada y rutas de logos están en el archivo raíz; las respuestas completas están en su archivo content. El formato compartido está en style/nebiot-template.sty. Los comandos opcionales son ImplementerLogo, ProponentLogo y StakeholderLogo. Cargue la imagen en assets e indique la ruta. Una ruta vacía conserva un campo identificado. No sobrescriba los logos NEBIOT. Los PDF son copias de lectura, no formularios interactivos.

## Libros de cálculo
Use NEBIOT_Environmental_Accounts_ES_v1_2.xlsx o su equivalente EN. Son libros independientes; no vinculan libros privados de origen ni la otra edición. Los nombres de hojas y códigos de entrada son estables en ambos idiomas.

1. **Profile:** registre proyecto, categoría, perfil FRM-05 y evidencia. d_u queda vacío hasta aprobar categoría de carbono compatible. FULL_BOUND opera solo con adopción registrada de F-R05; OTHER_PROFILE requiere cálculo separado documentado.
2. **Evidence / Spatial / Factors:** identifique objetos, fechas, reservorios, unidades y soporte espacial exactos. Las conversiones opcionales píxel-área y biomasa-carbono no establecen exactitud de clasificación, calibración de carbono ni mitigación anual.
3. **Components:** registre contribuciones disjuntas con signo para EA o EP y clave de período. BL son emisiones netas de línea base; PJ del proyecto; LK fugas atribuibles. Una cantidad que ya descuenta emisiones del proyecto no es línea base bruta. Para masa precalculada t CO2e, use factor 1 y registre rutina y evidencia completas. Incluya al menos una fila sustentada por cada BL/PJ/LK, incluso cero justificado. NO significa exclusión deliberada; documéntela en el informe.
4. **ExAnte / ExPost:** asigne claves coincidentes, alcance real y estado de evidencia. Q_hat = BL − PJ − LK. DEDUCTION usa una deducción no negativa justificada; BOUND una cota suministrada no mayor que la estimación puntual. Ninguna ruta estima incertidumbre ni sustituye su evaluación independiente. Reservas y obligaciones ExAnte son escenarios de planificación, no asientos ejecutados.
5. **Settlement:** calcula masa elegible y liquidación/base de reserva candidatas F-R03. La liquidación ejecutada es entrada separada, limitada a la asignación candidata compatible y con evidencia si es positiva. La reserva requerida que supera la base conserva el faltante; no se limita artificialmente ni se considera financiada.
6. **CarryForward:** FULL_BOUND calcula magnitud negativa, descuenta solo reconocimiento previo sustentado y cancelación compatible ejecutada, y añade la obligación nueva a la pendiente. El enlace al período anterior prueba el saldo inicial. El primer saldo requiere registro inicial identificado. El libro no autentica ni ejecuta asientos.
7. **Results:** informa cantidades candidatas. No calcula cantidad NVEU si fallan los controles previos o faltan denominación/perfil. La cantidad calculada nunca es emisión. La precisión y redondeo a enteros, cuando procedan, deben implementarse en la cuenta específica aprobada y conservar su residuo.
8. **Comparison:** compara ex ante fijo con ex post en soporte igual. El puente es ΔQ = ΔBL − ΔPJ − ΔLK antes de incertidumbre/reserva. Una diferencia no demuestra por sí sola adicionalidad ni error material.
9. **Migration:** conserva cantidades originales, armonizadas con método anterior y con método NEBIOT. El ajuste de base más diferencia de método debe ser igual a diferencia total. La tabla no crea unidades de reemplazo, borra obligaciones ni aprueba períodos históricos.
10. **Allocation:** distribuye resultado neto matriz mediante pesos explícitos. Los pesos por matriz/base suman uno. La asignación no es observación mensual nueva; no cuente un resultado anual otra vez como mitigación mensual adicional.
11. **Checks / Examples / Formula_Map:** revise filas detenidas, casos sintéticos y alcance computacional. El libro vacío se marca EMPTY, no aprobado.

Texto azul identifica entradas; fondo verde claro identifica cálculos. Códigos: EA/EP, BL/PJ/LK, YES/NO, DEDUCTION/BOUND, FULL_BOUND/OTHER_PROFILE, OBSERVED/MODELED/ASSUMED/REPORTED/OVV_ASSESSED. COMPLETE y CALCULATED solo se refieren a controles limitados de entrada/aritmética; no son decisiones de conformidad, verificación ni autorización.

Hay 50 filas de períodos, 300 de componentes y 150 de asignaciones. No son límites del programa ni horizontes de acreditación. Antes de ampliar, extienda todos los rangos dependientes, validaciones y controles y vuelva a probar el libro. Conserve el archivo original de cada presentación formal y registre correcciones aparte. No hay macros ni contraseñas; proteja la copia controlada mediante las disposiciones reales de gestión documental.

## Lo que los libros no calculan
No ajustan clasificadores de vegetación, reconstruyen árboles, estiman probabilidades de impulsores, eligen contrafactuales, estiman covarianzas o confianza, efectúan verificación independiente, autentican firmas, financian/cancelan reservas ni autorizan NVEU. Esos cálculos y decisiones permanecen en sus métodos y registros calificados. Components recibe sus resultados trazables. La evidencia faltante nunca se convierte en cero.

## Referencias de fuentes y evidencia
[1] NEBIOT. Estándar NEBIOT, versión controlada 0.8.2, edición integrada NEB-DOC-000 y sus documentos asociados. La tabla de correspondencias conserva los identificadores exactos de cláusulas, fórmulas y registros. Cada proyecto diligenciado debe añadir las fuentes, datos, licencias, observaciones, cálculos y decisiones aplicables. Las plantillas vacías no contienen resultados de proyectos.


## Notación matemática y revisión de cálculos — edición 1.2

Las tablas relacionadas con cálculos identifican cantidad, notación matemática, unidad, expresión aplicable y ubicación en el libro receptor. EA designa el pronóstico fechado y EP la cuenta del período reportado. Cada índice o símbolo se define en su ámbito; no sustituye la definición de la variable específica del proyecto.

Cada informe incorpora el anexo CALC. Repetir el registro por resultado: archivo fuente, versión y huella; hoja y celda/rango; identificador de observación original; unidad de entrada; fórmula fuente exacta; valores sustituidos; fórmula receptora; valores intermedios; resultado sin redondear; tabla y celda del informe; recálculo independiente; tolerancia numérica; y decisión del revisor. Distinguir una entrada faltante de cero.

### Secuencia de revisión

1. Congelar el original e identificar cuenta, intervalo, soporte espacial, reservorios y unidades. No convertir un subtotal fuente ya neto de emisiones del proyecto en una entrada bruta de línea base.
2. Reproducir la fórmula original desde sus entradas. Registrar diferencia exacta y tolerancias numéricas absoluta y relativa, cuando se utilicen. Una tolerancia informática no es un umbral de materialidad aprobado.
3. Registrar en Source_Map cualquier armonización de unidades, límites, períodos, exclusiones o descuentos. Conservar la cuenta original. Distinguir conversión de unidades y cambio metodológico.
4. Diligenciar Components, ExAnte o ExPost comparables. Consultar Symbol_Map y Math_Notation antes de trasladar valores al informe. Un factor uno solo corresponde a una cantidad ya compatible; no reemplaza la caracterización de gases.
5. Registrar en Reviewer_Match valor de referencia, recálculo por el mismo método, unidad común y tolerancia aritmética absoluta explícita. La columna receptora separada documenta un cambio metodológico justificado; su diferencia no es error automático.
6. Trasladar al informe el resultado aprobado sin redondeo intermedio. Word y LaTeX son registros de presentación, no motores de hoja de cálculo; los campos no se sincronizan automáticamente. Conservar celda exacta y versión congelada del libro con el informe.

### Capacidad del libro y continuidad de períodos

El libro heredado dispone de 50 filas de períodos (6–55), 300 filas de componentes (6–305) y 150 filas de asignación subperiódica (6–155). Son capacidades de la plantilla, no horizontes de proyecto aprobados. No ingresar datos fuera de esos rangos y suponer que se incluyen. Para proyectos mayores, usar segmentos de cuenta identificados con traslado de saldos iniciales, o ampliar todos los rangos dependientes mediante control de cambios y repetir las pruebas. La concordancia fuente separada cubre todas las filas anuales fuente, independientemente de esta capacidad. No omitir períodos, obligaciones o registros para hacerlos caber.

### Herramientas de revisión

Tools/source_audit.py evalúa recursivamente el vocabulario de fórmulas de los dos libros fuente y compara cada celda con el resultado almacenado. Usa la biblioteca estándar de Python y no modifica el archivo. Las expresiones no soportadas se registran NOT_EVALUATED, nunca como aprobadas. Tools/formula_notation.py convierte el registro en matemáticas literales por dirección de celda. Son herramientas aritméticas, no validación de evidencia ni autorización de NVEU.

Ejemplo con las rutas propias:

```text
python Tools/source_audit.py --source EA="/ruta/original.xlsx" --output "/ruta/revision_privada"
python Tools/formula_notation.py --alias EA --replay-ledger "/ruta/revision_privada/EA_formula_cells.csv.gz" --output "/ruta/revision_privada"
```

El paquete reutilizable no contiene entradas de clientes. El archivo restringido de revisión fuente contiene datos confidenciales y no debe distribuirse con las plantillas vacías.
