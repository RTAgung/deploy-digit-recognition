# Handwritten Digit Recognition [_open link_](https://deploy-digit-recognition.herokuapp.com)
Tugas proyek akhir dari mata kuliah Machine Learning

### Branch
- [master](https://github.com/RTAgung/digit-recognition/tree/master) = hasil model yang di deploy
- [modelling](https://github.com/RTAgung/digit-recognition/tree/modelling) = proses membangun model 

### Data
Data Handwrotten Digit Recognition diambil dari dataset Kaggle yang berisi data tabel 42000 baris dan 785 kolom ([_open_](https://www.kaggle.com/animatronbot/mnist-digit-recognizer)). 

Jumlah sampel tiap digit :

| digit | jumlah |
| ----- | ------ |
| 1     | 4684   |
| 7     | 4401   |
| 3     | 4351   |
| 9     | 4188   |
| 2     | 4177   |
| 6     | 4137   |
| 0     | 4132   |
| 4     | 4072   |
| 8     | 4063   |
| 5     | 3795   |

### Preprocessing
- Cek null data
- Cek duplikasi data
- Resize gambar menjadi 22x22 piksel
- Feature scaling menggunakan Standardization
- Splitting data
  - Data training (80%) : 33600
  - Data testing (20%) : 8400

### Modelling
- Menggunakan SVM kernel RBF
- Tuning parameter menggunakan GridSearchCV
  - C : [0.6, 1, 3, 6, 10]
  - gamma : ['scale', 'auto', 0.0009, 0.003, 0.006]
  - cv : 4
- Hasil training model
  - best estimator = SVC(C=6, gamma='auto')
  - best score = 0.9650

### Evaluating
Confusion Matrix :
| Digit      |   | Predicted |     |     |     |     |     |     |     |     |      |
|------------|---|-----------|-----|-----|-----|-----|-----|-----|-----|-----|------|
|            |   | 0         | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9    |
| **Actual** | 0 | 802       | 0   | 3   | 0   | 0   | 1   | 9   | 0   | 0   | 1    |
|            | 1 | 0         | 894 | 8   | 1   | 1   | 1   | 1   | 1   | 1   | 1    |
|            | 2 | 2         | 4   | 824 | 4   | 1   | 0   | 4   | 2   | 4   | 1    |
|            | 3 | 0         | 0   | 11  | 895 | 0   | 10  | 0   | 7   | 9   | 5    |
|            | 4 | 1         | 0   | 7   | 0   | 810 | 1   | 5   | 3   | 0   | 12   |
|            | 5 | 1         | 0   | 4   | 9   | 2   | 675 | 9   | 0   | 2   | 0    |
|            | 6 | 3         | 1   | 9   | 0   | 0   | 2   | 767 | 0   | 3   | 0    |
|            | 7 | 0         | 1   | 9   | 3   | 5   | 2   | 0   | 865 | 0   | 8    |
|            | 8 | 1         | 2   | 6   | 7   | 4   | 6   | 2   | 1   | 804 | 2    |
|            | 9 | 1         | 1   | 5   | 7   | 6   | 3   | 0   | 9   | 3   | 803  |

Classification Report :
| digit        | precision | recall | f1-score | support |
|--------------|-----------|--------|----------|---------|
| 0            | 0.99      | 0.98   | 0.99     | 816     |
| 1            | 0.99      | 0.98   | 0.99     | 909     |
| 2            | 0.93      | 0.97   | 0.95     | 846     |
| 3            | 0.97      | 0.96   | 0.96     | 937     |
| 4            | 0.98      | 0.97   | 0.97     | 839     |
| 5            | 0.96      | 0.96   | 0.96     | 702     |
| 6            | 0.96      | 0.98   | 0.97     | 785     |
| 7            | 0.97      | 0.97   | 0.97     | 893     |
| 8            | 0.97      | 0.96   | 0.97     | 835     |
| 9            | 0.96      | 0.96   | 0.96     | 838     |
| accuracy     |           |        | 0.97     | 8400    |
| macro avg    | 0.97      | 0.97   | 0.97     | 8400    |
| weighted avg | 0.97      | 0.97   | 0.97     | 8400    |

Accuracy :
| Label | Accuracy (%) |
|-------|--------------|
| 0     | 98.28        |
| 1     | 98.35        |
| 2     | 97.4         |
| 3     | 95.52        |
| 4     | 96.54        |
| 5     | 96.15        |
| 6     | 97.71        |
| 7     | 96.86        |
| 8     | 96.29        |
| 9     | 95.82        |
| Total | 97.00        |
