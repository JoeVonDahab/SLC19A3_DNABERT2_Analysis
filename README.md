# SLC19A3 DNA-BERT

A Python project for DNA sequence analysis using BERT models for variant pathogenicity prediction.

## Overview

This repository leverages the pretrained DNABERT-2 model to generate embeddings for the SLC19A3 gene (Thiamine Transporter 2), which is approximately 32K nucleotides long. The project implements a neural network approach to classify DNA sequence variants based on their clinical significance, predicting whether variants are likely to cause pathological or non-pathological effects.

![8XV9_model-1](https://github.com/user-attachments/assets/07f8f358-2393-413a-9777-5f2c4259c952)




## Features

- Pre-processing of DNA sequence data from NCBI dbSNP
- Utilization of DNABERT-2 for generating sequence embeddings
- Hyperparameter optimization with grid search
- Early stopping to prevent overfitting
- Performance evaluation with validation metrics

## Dataset

- 1,069 labeled variants from NCBI dbSNP database
- Variants classified by clinical significance
- Focus on SLC19A3 gene variants

## Results

The model achieves excellent performance with:
- Test accuracy: 86.70%
- Macro average F1-score: 0.82

### Performance by Class
- Wild type: 98.53% F1-score (highest performance)
- Benign Variants: 77.23% F1-score
- Unknown Significance: 85.14% F1-score
- Pathological Variants: 66.67% F1-score (most challenging class)
![output_2](https://github.com/user-attachments/assets/bf47d066-fc34-40b8-b0d1-adf5c13a63bc)
![output_1](https://github.com/user-attachments/assets/f5ccf6a5-d5f6-4f80-9885-1f97995dd4de)

## Model Characteristics

The neural network demonstrates:
- Good recall (0.93) for Wild type class
- Balanced performance across most classes
- Some challenges with the Pathological Variants class, likely due to limited training examples

## Future Work

- Improve classification of underrepresented pathological variants
- Explore data augmentation techniques for imbalanced classes
- Implement additional transformer architectures
- Incorporate additional genomic features
- Enhance model interpretability for clinical applications
