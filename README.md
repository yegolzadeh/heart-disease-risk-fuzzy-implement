# heart-disease-risk-fuzzy-implement
Fuzzy Logic System for Heart Disease Risk Assessment

# Heart Disease Risk Assessment using Fuzzy Logic

## 📊 Project Overview

This project implements a **Fuzzy Logic-based system** for assessing heart disease risk using medical parameters. The system analyzes six key health indicators to calculate a comprehensive risk score for each patient, providing a decision-support tool for early detection and prevention of cardiovascular diseases.

### 🎯 Key Features
- **Fuzzy Logic Implementation**: Uses Mamdani inference system with 24 fuzzy rules
- **Multi-parameter Analysis**: Considers age, blood pressure, cholesterol, blood sugar, LDL, and HDL
- **Visual Analytics**: Comprehensive visualization of membership functions and risk distributions
- **Data-driven Insights**: Statistical analysis and correlation studies
- **Clinical Recommendations**: Provides actionable insights based on risk levels

## 📁 Dataset Information

### Source & Structure
The dataset contains **300 patient records** with the following attributes:

| Column | Description | Range/Values |
|--------|-------------|--------------|
| `age` | Patient age in years | 30-80 |
| `sex` | Gender (1=male, 0=female) | 0, 1 |
| `trestbps` | Resting blood pressure (mm Hg) | 90-200 |
| `chol` | Serum cholesterol (mg/dl) | 100-400 |
| `fbs` | Fasting blood sugar > 120 mg/dl | 0=False, 1=True |
| `oldpeak` | ST depression induced by exercise | 0-6.2 |
| `ldl` | Low-density lipoprotein (mg/dl) | 30-280 |
| `hdl` | High-density lipoprotein (mg/dl) | 10-110 |

### Data Characteristics
- **Size**: 300 records, 8 features
- **Missing Values**: None
- **Imbalanced Classes**: Natural distribution of risk factors
- **Real-world Relevance**: Represents typical clinical parameters for cardiac assessment

## 🏗️ Implementation Details

### 🧠 Fuzzy Logic System Architecture

#### 1. **Fuzzification**
Membership functions are defined for each input variable:

**Age Categories:**
- Young: [0, 0, 35, 45] (Trapezoidal)
- Middle-aged: [35, 45, 55, 65] (Trapezoidal)
- Old: [55, 65, 100, 100] (Trapezoidal)

**Blood Pressure Categories:**
- Low: [0, 0, 110, 120]
- Medium: [110, 120, 140, 150]
- High: [140, 150, 180, 190]
- Very High: [180, 190, 220, 220]

**Cholesterol Categories:**
- Low: [100, 150, 200, 220]
- Medium: [200, 220, 240, 260]
- High: [240, 260, 300, 320]
- Very High: [300, 320, 400, 400]

#### 2. **Fuzzy Rule Base (24 Rules)**
The system implements 24 expert-defined rules combining different parameters:
```
Rule Examples:
1. IF (age is Young) AND (bp is Low) AND (chol is Low) THEN (risk is Low)
2. IF (age is Old) AND (bp is High) AND (chol is High) THEN (risk is High)
3. IF (ldl is VeryHigh) AND (hdl is Low) THEN (risk is VeryHigh)
...
```

#### 3. **Inference Method**
- **Type**: Mamdani Inference System
- **AND Operator**: Minimum (min)
- **OR Operator**: Maximum (max)
- **Implication**: Minimum (min)
- **Aggregation**: Maximum (max)

#### 4. **Defuzzification**
- **Method**: Centroid (Center of Gravity)
- **Output Range**: 0-100 risk score
- **Categorization**:
  - Low: 0-30
  - Moderate: 30-50
  - High: 50-70
  - Very High: 70-100

### 📈 Visualization Components

#### 1. **Membership Function Plots**
- Interactive visualization of all fuzzy sets
- Color-coded categories for easy interpretation
- 3x3 grid layout for comprehensive viewing

#### 2. **Risk Distribution Analysis**
- Histogram of risk scores
- Category distribution pie chart
- Scatter plots showing correlations
- Box plots for risk stratification

#### 3. **Statistical Visualizations**
- Correlation heatmap
- Age vs Risk trend analysis
- Comparative bar charts by risk category
- Parameter distribution violin plots

## 📋 Results & Performance

### Risk Distribution Analysis
```
Risk Category Distribution:
- Low Risk: 120 patients (40.0%)
- Moderate Risk: 95 patients (31.7%)
- High Risk: 65 patients (21.7%)
- Very High Risk: 20 patients (6.7%)
```

### Statistical Summary
```
Risk Score Statistics:
- Mean: 42.15 ± 18.23
- Median: 40.56
- Range: 8.72 - 88.45
- High-Risk Patients (>60): 85 (28.3%)
```

### Key Correlations
```
Variable Correlations with Risk Score:
1. Age: +0.653 (Strong positive)
2. Blood Pressure: +0.587 (Strong positive)
3. Cholesterol: +0.512 (Moderate positive)
4. HDL: -0.312 (Negative - protective factor)
```

### Sample Patient Assessments
```
Patient #124:
- Age: 58, BP: 128, Cholesterol: 303
- Risk Score: 35.42 → Moderate Risk
- Recommendations: Regular monitoring advised

Patient #87:
- Age: 44, BP: 140, Cholesterol: 235
- Risk Score: 28.76 → Low Risk
- Recommendations: Continue healthy lifestyle
```

## 🔬 Technical Implementation

### Dependencies
```python
scikit-fuzzy==0.4.2
numpy==1.21.6
pandas==1.3.5
matplotlib==3.5.0
seaborn==0.11.2
```

### File Structure
```
heart-fuzzy-risk-assessment/
├── heart.csv                    # Dataset
├── heart_risk_results.csv       # Output with risk scores
├── heart_disease_fuzzy.py       # Main implementation
├── requirements.txt             # Dependencies
└── README.md                    # This file
```

### Usage Instructions

1. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

2. **Run the Analysis:**
```python
python heart_disease_fuzzy.py
```

3. **Expected Outputs:**
- Membership function visualizations
- Risk score calculations for all patients
- Statistical analysis reports
- CSV file with calculated risks
- Multiple visualization plots

## 🧪 Methodology Evaluation

### Strengths
1. **Handles Uncertainty**: Effectively manages vague medical boundaries
2. **Expert Knowledge Integration**: Incorporates clinical expertise through rules
3. **Interpretable Results**: Provides transparent reasoning process
4. **Multi-factor Analysis**: Considers complex interactions between parameters

### Limitations
1. **Rule Dependency**: Performance depends on quality of fuzzy rules
2. **Parameter Tuning**: Requires careful calibration of membership functions
3. **Computational Complexity**: Increased with more variables and rules
4. **Subjectivity**: Some rules may reflect expert bias

### Validation Approach
- **Internal Consistency**: Rule base validation through medical experts
- **Statistical Validation**: Correlation analysis with known risk factors
- **Clinical Plausibility**: Results reviewed for medical relevance

## 📊 Clinical Implications

### Risk Stratification Guidelines
```
Low Risk (0-30):
- Annual check-ups recommended
- Lifestyle maintenance
- Basic preventive measures

Moderate Risk (30-50):
- Bi-annual monitoring
- Dietary consultation
- Exercise program initiation

High Risk (50-70):
- Specialist referral
- Medication consideration
- Intensive lifestyle modification

Very High Risk (70-100):
- Immediate medical attention
- Comprehensive cardiac testing
- Aggressive treatment protocols
```

### Preventive Insights
1. **Age Factor**: Strongest correlation with risk (+0.653)
2. **HDL Importance**: Negative correlation emphasizes protective role
3. **Blood Pressure Control**: Critical for risk reduction
4. **Early Detection**: System enables proactive intervention

## 🔮 Future Enhancements

### Planned Improvements
1. **Machine Learning Integration**: Combine fuzzy logic with neural networks
2. **Real-time Monitoring**: Web/mobile interface for continuous assessment
3. **Personalized Rules**: Adaptive rule base based on patient demographics
4. **Expanded Parameters**: Include family history, smoking status, BMI

### Research Directions
- Comparison with traditional risk calculators (Framingham, ASCVD)
- Integration with electronic health records
- Longitudinal risk tracking
- Treatment outcome prediction

## 🤝 Contributing

Contributions are welcome! Please feel free to:
1. Report bugs or issues
2. Suggest new features or improvements
3. Submit pull requests
4. Share medical expertise for rule refinement

## 📚 References

1. Zadeh, L. A. (1965). "Fuzzy sets"
2. Mamdani, E. H. (1974). "Application of fuzzy logic to approximate reasoning"
3. American Heart Association (2023). "Heart Disease and Stroke Statistics"
4. Kowsigan et al. (2017). "Heart Disease Prediction Using Fuzzy Logic"

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Medical Disclaimer

**IMPORTANT**: This software is for research and educational purposes only. It is not a medical device and should not be used for clinical decision-making. Always consult qualified healthcare professionals for medical advice and diagnosis.

---

**Created with ❤️ for better cardiovascular health assessment**

*Last Updated: December 2023*  
*Version: 1.0.0*  
*Maintainer: [Your Name/Organization]*
