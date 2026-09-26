# Informe de monitoreo NEBIOT — guía de diligenciamiento

**Plantilla de monitoreo edición 1.3 · NEBIOT Standard 0.8.2**

## Propósito y relación documental

El Informe de monitoreo (MR) es la presentación principal específica del período. Explica qué se ejecutó, qué se observó, cómo se aplicó el plan aprobado, qué cambió y cómo la evidencia sustenta la cuenta ambiental. Acompaña a la Descripción del Proyecto (PD), la Estimación ex ante fechada (EA) y el Informe de resultados ex post (EP).

Usar el PD como referencia de diseño y conservar el pronóstico ex ante fechado. Adjuntar el informe ex post controlado como anexo cuantitativo, o integrar el informe equivalente e identificar su ubicación. El MR resume la misma cuenta: sus valores no se suman a los del informe ex post. El MR sustenta G2. La verificación independiente G3 y la decisión del programa G4 siguen separadas.

El estándar rector conserva versión 0.8.2. Los archivos PD, ex ante, ex post, Conciliación de migración y Cuentas Ambientales conservan edición 1.2. Esta edición incorpora el Informe de monitoreo; no modifica aquellos documentos, las fórmulas del libro ni el estándar.

## Archivos y versión maestra

- `Word/NEBIOT_Monitoring_Report_ES_Template_v1_3.docx` es directamente editable.
- `Word_Templates/NEBIOT_Monitoring_Report_ES_Template_v1_3.dotx` es una plantilla maestra reutilizable de Word.
- `Overleaf/NEBIOT_Monitoring_Report_ES.tex` es la entrada LaTeX en español; la entrada inglesa termina en `_EN.tex`.
- Los PDF son vistas de lectura, no formularios interactivos. El documento inicial no impone extensión máxima.

Seleccionar Word o LaTeX como versión maestra controlada. No hay sincronización automática entre Word, LaTeX y Excel. Conservar versión, huella, hoja, celda y vínculo con tabla del informe al transferir resultados.

## Diligenciamiento

Comenzar con portada y control documental: identidad, número y versión del informe, intervalo de monitoreo, convención temporal, corte de evidencia, fecha de presentación, elaborador, revisor y distribución. Distinguir estas fechas de la vida del proyecto y del período de un cálculo adjunto.

La Sección 02 establece las referencias exactas a PD, EA, EP, perfil y decisiones previas. Las Secciones 03–10 registran responsabilidades, ejecución, cobertura de monitoreo, evidencia espacial/material, calidad, sustituciones y cambios. Las Secciones 11–19 concilian contrafactual, emisiones del proyecto, fugas, cohortes, cuenta neta con signo, incertidumbre, riesgo, obligaciones y pronóstico. Las Secciones 20–26 cubren adicionalidad continua, traslapes, participación, salvaguardas, resultados ambientales/sociales separados, migración, alcance NVEU, hallazgos y entrega de evidencia.

Ampliar tablas para todos los elementos aplicables. Identificar datos faltantes o pendientes, no fabricar ceros. La no aplicabilidad requiere motivo y disposición del revisor. Completar cada fila aplicable del perfil FRM-05 aprobado o remitir al registro exacto sin cambios. No importar porcentajes, confianza, horizontes, umbrales ni denominaciones de ejemplos.

## Notación y registros de cálculo

Las tablas relacionadas con cálculos reproducen notación del catálogo matemático edición 1.2, con disposiciones rectoras y ubicación en el libro. Identificadores como `MR-15-T01` localizan registros del informe; no son requisitos nuevos.

Separar observaciones originales, conversiones modeladas, supuestos, proyecciones ex ante, cantidades reportadas ex post, alcance verificado y NVEU autorizadas. Conservar unidades, reservorios, caracterización de gases, soporte espacial e intervalo. Definir cada subtotal; no importar un subtotal ya neto de emisiones del proyecto como línea base bruta y deducir esas emisiones otra vez.

CALC proporciona un registro repetible de trazabilidad. Vincular cada cifra con datos originales, expresión exacta, entradas, unidades, transformaciones, ecuación receptora, resultado sin redondear, celda, fila del informe y comparación del revisor. Las tolerancias son ajustes de comparación numérica, no materialidad. Explicar diferencias por cambios justificados de método o alcance, sin forzar igualdad.

Las referencias usan la estructura sin cambios de Cuentas Ambientales edición 1.2. `ExPost!F:I` contiene línea base, proyecto, fugas y cuenta neta; `ExPost!J:L`, la interfaz de incertidumbre; `Comparison!D:J`, la comparación con el pronóstico; `Settlement`, `CarryForward` y `Results` mantienen distinciones entre candidato/ejecutado y denominación condicional. Registrar fila real y versión del archivo. Respetar capacidades del libro o usar ampliación controlada y probada; el informe no extiende sus fórmulas.

Conservar resultados negativos y obligaciones continuas. Aplicar arrastre de cota completa solo si se adopta expresamente. Liquidación real y cancelación de reserva necesitan evidencia de ejecución. Una asignación candidata no cambia una obligación registrada. Una cota negativa por incertidumbre no equivale automáticamente a reversión física.

## Correspondencia PD–monitoreo

XREF vincula cada sección sustantiva MR con identificadores reales de las plantillas PD, EA y EP edición 1.2. Los documentos diligenciados pueden tener distinta paginación o numeración: registrar ubicaciones exactas en Sección 02. Citar el PD no sustituye observaciones ni registros de ejecución del intervalo.

Los registros CSV repiten la correspondencia e identifican notación y ubicación de cada tabla de cálculo. Los identificadores de requisitos, ecuaciones, AP y FRM remiten al estándar rector, no a secciones ausentes del MR.

## Edición en Word

Pulsar campos entre corchetes para introducir información. Son controles nativos de contenido de texto; las expresiones son ecuaciones Office Math editables, no imágenes. Las tablas no están bloqueadas. Añadir filas y repetir encabezados. Las respuestas extensas fluyen a páginas siguientes. Actualizar campos y revisar numeración, tablas, ecuaciones y encabezados tras editar.

El contenido enlazado y las entradas XREF llevan a secciones del informe. Conservar sus marcadores al modificar títulos. Usar nueva versión del informe cuando cambie un registro de evaluación y conservar la versión sustituida.

## Edición en Overleaf

Cargar el ZIP exclusivo Overleaf, seleccionar XeLaTeX y elegir `NEBIOT_Monitoring_Report_EN.tex` o `NEBIOT_Monitoring_Report_ES.tex`. Los campos de portada están en la entrada elegida; el cuerpo en `content/` y el estilo compartido en `style/nebiot-monitoring.sty`.

Diligenciar `\MonitoringStart`, `\MonitoringEnd` y `\MonitoringReportID`, junto con identidad del proyecto. Registrar convención temporal en control documental. Reemplazar espacio de mapa por cartografía debidamente referenciada. Conservar bibliografía y referencias normativas al diligenciar.

## Logotipos e identidad

Cada idioma incluye imagen NEBIOT original y licencia. Conservar proporción de la imagen. Tres espacios opcionales identifican ejecutor, proponente y titulares o partes interesadas.

En Word, insertar imagen autorizada en línea dentro de la celda correspondiente y conservar rol de la organización. En LaTeX, cargar imagen en `assets/` y definir `\ImplementerLogo`, `\ProponentLogo` o `\StakeholderLogo` con ruta exacta. Una ruta vacía conserva el espacio reservado. Eliminar espacios sin uso del informe diligenciado. Un logotipo no acredita propiedad, consentimiento, respaldo, validación ni admisión.

## Presentación, evaluación y confidencialidad

El proponente presenta el informe con registro de elaboración técnica y revisión interna aplicable. El OVV independiente controla evaluación y dictamen. El MR cita dictamen o decisión emitidos por separado cuando existan; el elaborador no prellena conclusiones ni firma en nombre de otra función.

El informe público puede resumir datos personales, culturales o ubicaciones protegidas. Mantener índice controlado con acceso del revisor autorizado al registro completo. Incluir referencias, no material confidencial ajeno al proyecto. Conciliar resumen, anexo cuantitativo, archivos originales, afirmaciones previas y saldos iniciales/finales antes de presentar.
