# 🍄 Taller de Aprendizaje Automático No Supervisado con el Dataset de Setas

Este repositorio contiene un taller práctico orientado al aprendizaje automático **no supervisado**, usando técnicas de **PCA** y **Clustering (KMeans)**, junto con una comparativa con un modelo supervisado (Random Forest).

Usaremos el **Mushroom Dataset**, un conjunto de datos muy conocido en el ámbito educativo que contiene información sobre diferentes tipos de hongos, incluyendo su clasificación como **comestibles o venenosos**.

---

## 📂 Dataset

Puedes obtener el dataset desde el siguiente enlace:

🔗 [Mushroom Dataset - UCI Repository](https://archive.ics.uci.edu/ml/datasets/Mushroom)

- **Instancia:** Cada fila representa un hongo.
- **Variables:** Todas son **categóricas** (forma, color, olor, etc.).
- **Variable objetivo (`class`)**: Binaria — `e` (edible/comestible) o `p` (poisonous/venenoso).

---

## 🧠 Objetivos del taller

- Cargar y explorar un dataset categórico complejo.
- Tratar valores nulos y eliminar columnas no informativas.
- Codificar variables categóricas usando **One-Hot Encoding**.
- Reducir dimensionalidad con **PCA (Análisis de Componentes Principales)**.
- Aplicar **K-Means Clustering** para detectar estructuras ocultas en los datos.
- Comparar el rendimiento del modelo no supervisado con un modelo supervisado (**Random Forest**).

---

## 🔧 Tecnologías utilizadas

- Python
- Pandas / NumPy
- Seaborn / Matplotlib
- Scikit-learn (`PCA`, `KMeans`, `RandomForestClassifier`)

---

## 🗂️ Contenido del notebook

### 1. 📥 Carga y exploración de datos
- Visualización general del dataset.
- Conteo de valores nulos y valores únicos por variable.
- Eliminación de columnas constantes o poco informativas.

### 2. 🧼 Preprocesamiento
- Imputación o eliminación de valores faltantes.
- Conversión de variables categóricas con **OneHotEncoder**.
- Separación entre `X` (features) e `y` (class).

### 3. 🧪 PCA (Análisis de Componentes Principales)
- Reducción de dimensionalidad a 2 componentes.
- Visualización de los datos en 2D.
- Evaluación visual de separabilidad.

### 4. 🌳 Clasificación supervisada (Random Forest)
- Entrenamiento de un modelo de clasificación.
- Evaluación con métricas de precisión.
- Estudio del impacto del número de componentes en el rendimiento del modelo.

### 5. 🔍 Clustering con K-Means
- Determinación del número óptimo de clusters (método del codo).
- Entrenamiento y visualización de clusters.
- Evaluación de la correspondencia entre clusters y clases reales (sin usar las etiquetas).


---

## ✅ Resultados clave del taller

- **One‑Hot Encoding (OHE)**: 117 variables tras codificación; 8124 instancias.
- **PCA**: para explicar el 90% de varianza se requieren ≈ **50 componentes**. Las 10 primeras explican ≈ 51%.
- **KMeans** sobre PCA(90%): mejor k por silhouette = **8**.
  - Precisión por mapeo mayoritario `class↔cluster`: **≈ 0.898**
  - ARI: **0.274**, NMI: **0.433**
  - La mayoría de clusters son muy “puros”; el cluster 2 es el más mixto.
- **Random Forest (supervisado)**:
  - Con OHE (sin PCA): **accuracy = 1.00** en test.
  - Con PCA (≥5 componentes): **≈ 0.999** (no mejora, pero reduce dimensionalidad si fuera necesario).

Conclusión: PCA es útil para visualizar y estabilizar el clustering; para clasificación supervisada, el OHE directo con Random Forest ya alcanza rendimiento perfecto en este dataset educativo.

Archivos generados:
- `data/mushrooms.csv`: dataset original consolidado.
- `data/mushrooms_with_clusters.csv`: dataset con columna `cluster` desde el pipeline OHE→Scaler→PCA(90%)→KMeans(k=8).
- `EDA.ipynb`: notebook con todos los pasos reproducibles.

Siguientes extensiones opcionales:
- Probar **DBSCAN** para detectar formas no esféricas y ruido.
- Analizar **importancias de características** de RF y explicar reglas.
- Persistir modelos con `joblib` y añadir una pequeña guía de inferencia.

---

## 🌳 ¿Qué es Random Forest y por qué lo usamos?

**Random Forest** es un modelo de **aprendizaje supervisado** que usamos como **comparativa de referencia** en nuestro taller. Aquí te explico de forma sencilla:

### 🤔 ¿Qué es Random Forest?

Imagina que tienes que decidir si un hongo es comestible o venenoso. En lugar de preguntarle a una sola persona experta, le preguntas a **300 expertos diferentes**, cada uno con su propia forma de pensar. Luego, **votas**: si la mayoría dice "comestible", decides que es comestible. Eso es básicamente Random Forest:

- **"Forest"** = "bosque" → No es UN árbol de decisión, son **MUCHOS árboles** trabajando juntos.
- **"Random"** = "aleatorio" → Cada árbol ve una **muestra diferente** de los datos y se enfoca en **variables diferentes**.
- **Votación final**: Cada árbol da su predicción, y la respuesta final es la **más votada**.

### 💡 ¿Por qué lo usamos aquí?

En este taller comparamos dos enfoques:

1. **🔄 NO SUPERVISADO (KMeans + PCA)**:
   - **No sabe** si los hongos son comestibles o venenosos (no le damos esa etiqueta).
   - Intenta **agrupar** los hongos según sus características (olor, forma, color, etc.).
   - **Objetivo**: Descubrir patrones ocultos sin "ayuda".

2. **✅ SUPERVISADO (Random Forest)**:
   - **SÍ sabe** qué hongos son comestibles y cuáles venenosos (le damos las etiquetas).
   - Aprende las **reglas** que distinguen ambos grupos.
   - **Objetivo**: Clasificar correctamente hongos nuevos.

### 📊 ¿Qué resultados obtuvimos?

- **Random Forest sin PCA**: Accuracy del **100%** (perfecto).
  - Con las 117 variables codificadas (One-Hot Encoding) directamente, el modelo encuentra las reglas perfectas.

- **Random Forest con PCA**: Accuracy del **99.9%** (casi perfecto).
  - Aunque PCA reduce de 117 a 50 variables (manteniendo el 90% de la información), el rendimiento apenas baja.
  - Esto muestra que **PCA es útil** para simplificar sin perder mucho poder predictivo.

### 🎯 Conclusión práctica

- **KMeans (no supervisado)** logró ≈ **90% de precisión** agrupando hongos **sin saber** si eran comestibles o venenosos.

- **Random Forest (supervisado)** logró **100%** porque **sí sabía** las respuestas correctas durante el entrenamiento.

**La lección**: Cuando tienes datos etiquetados (supervisado), puedes alcanzar mejores resultados, pero el no supervisado es increíblemente útil cuando **no tienes etiquetas** o quieres **descubrir grupos** que no conocías.

---

## 📊 Evaluación  

Se considerarán los siguientes criterios:  

Competencia:  Evaluar conjuntos de datos utilizando herramientas de análisis y de visualización de datos
  
✅ Uso y gestión de formato .csv  
✅ Limpieza y preprocesado de datos  
✅ Visualización de datos (seaborn, matplotlib, plotly)  
✅ Análisis exploratorio detallado (EDA)  
✅ Uso de técnicas de preprocesado (normalización, escalado, label encoder, one hot encoder)    
✅ Uso de técnicas avanzadas de limpieza de datos (eliminación de valores atípicos, imputación de valores faltantes)  
✅ Uso de técnicas de reducción de dimensionalidad (PCA, t-SNE)   
  

Competencia:  Aplicar algoritmos de aprendizaje automático según el problema, identificando y resolviendo problemas clásicos de inteligencia artificial:

✅ Seleccionar las variables que son útiles y las que no lo son  
✅ Reconocer un caso de aprendizaje no supervisado   
✅ Aplicar modelos de clustering  
✅ Reconocer si es un problema de regresión o de clasificación      
✅ Separación de datos en train/test  
✅ Uso modelos de ensemble (RandomForest, GradientBoosting, AdaBoost, XGBoost, LightGBM)  
  
Más detalles en: [roadmap-mad-ai-p4.coderf5.es](https://roadmap-mad-ai-p4.coderf5.es/)  






