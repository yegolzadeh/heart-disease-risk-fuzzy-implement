# -*- coding: utf-8 -*-

# First, install required packages

import numpy as np
import pandas as pd
import skfuzzy as fuzz
import skfuzzy.membership as mf
import matplotlib.pyplot as plt
import warnings
import os
warnings.filterwarnings('ignore')

# Create directory for saving plots
if not os.path.exists('plots'):
    os.makedirs('plots')

# Read data from CSV file
print("Reading heart data from CSV file...")
data = pd.read_csv('heart.csv')

# Display initial information about the data
print(f"\nNumber of samples: {len(data)}")
print(f"Available columns: {list(data.columns)}")
print("\nSample of data:")
print(data.head())

# Define fuzzy variables
x_age = np.arange(0, 101, 1)
x_bloodPressure = np.arange(0, 221, 1)
x_cholesterol = np.arange(100, 401, 1)
x_bloodSugar = np.arange(0, 201, 1)
x_hdl = np.arange(0, 101, 1)
x_ldl = np.arange(0, 301, 1)
y_risk = np.arange(0, 101, 1)

print("\n\n" + "="*80)
print("Fuzzy System for Heart Disease Risk Detection")
print("="*80)

# Membership functions
age_young = mf.trapmf(x_age, [0, 0, 35, 45])
age_mid = mf.trapmf(x_age, [35, 45, 55, 65])
age_old = mf.trapmf(x_age, [55, 65, 100, 100])

bloodPressure_low = mf.trapmf(x_bloodPressure, [0, 0, 110, 120])
bloodPressure_mid = mf.trapmf(x_bloodPressure, [110, 120, 140, 150])
bloodPressure_high = mf.trapmf(x_bloodPressure, [140, 150, 180, 190])
bloodPressure_veryHigh = mf.trapmf(x_bloodPressure, [180, 190, 220, 220])

cholesterol_low = mf.trapmf(x_cholesterol, [100, 150, 200, 220])
cholesterol_mid = mf.trapmf(x_cholesterol, [200, 220, 240, 260])
cholesterol_high = mf.trapmf(x_cholesterol, [240, 260, 300, 320])
cholesterol_veryHigh = mf.trapmf(x_cholesterol, [300, 320, 400, 400])

x_bloodSugar_fbs = np.arange(0, 2, 1)
bloodSugar_normal = mf.trimf(x_bloodSugar_fbs, [-0.5, 0, 0.5])
bloodSugar_high = mf.trimf(x_bloodSugar_fbs, [0.5, 1, 1.5])

ldl_normal = mf.trimf(x_ldl, [0, 0, 130])
ldl_limit = mf.trimf(x_ldl, [100, 130, 160])
ldl_high = mf.trimf(x_ldl, [130, 160, 190])
ldl_veryHigh = mf.trapmf(x_ldl, [160, 190, 300, 300])

hdl_low = mf.trapmf(x_hdl, [0, 0, 40, 50])
hdl_mid = mf.trapmf(x_hdl, [40, 50, 60, 70])
hdl_high = mf.trapmf(x_hdl, [60, 70, 100, 100])

risk_low = mf.trapmf(y_risk, [0, 0, 25, 35])
risk_moderate = mf.trapmf(y_risk, [25, 35, 50, 60])
risk_high = mf.trapmf(y_risk, [50, 60, 75, 85])
risk_veryHigh = mf.trapmf(y_risk, [75, 85, 100, 100])

# Plot and save membership functions
print("\nCreating membership functions plot...")
fig, axes = plt.subplots(3, 3, figsize=(15, 12))
axes = axes.flatten()

axes[0].plot(x_age, age_young, 'r', linewidth=2, label='Young')
axes[0].plot(x_age, age_mid, 'g', linewidth=2, label='Middle-aged')
axes[0].plot(x_age, age_old, 'b', linewidth=2, label='Old')
axes[0].set_title('Age')
axes[0].legend()
axes[0].set_xlabel('Age')
axes[0].set_ylabel('Membership Degree')

axes[1].plot(x_bloodPressure, bloodPressure_low, 'r', linewidth=2, label='Low')
axes[1].plot(x_bloodPressure, bloodPressure_mid, 'g', linewidth=2, label='Medium')
axes[1].plot(x_bloodPressure, bloodPressure_high, 'b', linewidth=2, label='High')
axes[1].plot(x_bloodPressure, bloodPressure_veryHigh, 'm', linewidth=2, label='Very High')
axes[1].set_title('Blood Pressure')
axes[1].legend()

axes[2].plot(x_cholesterol, cholesterol_low, 'r', linewidth=2, label='Low')
axes[2].plot(x_cholesterol, cholesterol_mid, 'g', linewidth=2, label='Medium')
axes[2].plot(x_cholesterol, cholesterol_high, 'b', linewidth=2, label='High')
axes[2].plot(x_cholesterol, cholesterol_veryHigh, 'm', linewidth=2, label='Very High')
axes[2].set_title('Cholesterol')
axes[2].legend()

axes[3].plot(x_bloodSugar_fbs, bloodSugar_normal, 'g', linewidth=2, label='Normal')
axes[3].plot(x_bloodSugar_fbs, bloodSugar_high, 'r', linewidth=2, label='High')
axes[3].set_title('Fasting Blood Sugar')
axes[3].legend()

axes[4].plot(x_ldl, ldl_normal, 'g', linewidth=2, label='Normal')
axes[4].plot(x_ldl, ldl_limit, 'y', linewidth=2, label='Borderline')
axes[4].plot(x_ldl, ldl_high, 'r', linewidth=2, label='High')
axes[4].plot(x_ldl, ldl_veryHigh, 'm', linewidth=2, label='Very High')
axes[4].set_title('LDL (Bad Cholesterol)')
axes[4].legend()

axes[5].plot(x_hdl, hdl_low, 'r', linewidth=2, label='Low')
axes[5].plot(x_hdl, hdl_mid, 'y', linewidth=2, label='Medium')
axes[5].plot(x_hdl, hdl_high, 'g', linewidth=2, label='High')
axes[5].set_title('HDL (Good Cholesterol)')
axes[5].legend()

axes[6].plot(y_risk, risk_low, 'g', linewidth=2, label='Low')
axes[6].plot(y_risk, risk_moderate, 'y', linewidth=2, label='Moderate')
axes[6].plot(y_risk, risk_high, 'r', linewidth=2, label='High')
axes[6].plot(y_risk, risk_veryHigh, 'm', linewidth=2, label='Very High')
axes[6].set_title('Heart Disease Risk Level')
axes[6].legend()

axes[7].axis('off')
axes[8].axis('off')

plt.tight_layout()
# Save the plot BEFORE showing it
plt.savefig('plots/membership_functions.png', dpi=300, bbox_inches='tight')
print("✓ Membership functions plot saved as 'plots/membership_functions.png'")
plt.show()

# Function to calculate risk for a patient
def calculate_heart_risk(age, trestbps, chol, fbs, ldl, hdl):
    """Calculate heart disease risk using fuzzy logic"""
    
    # Fuzzification
    age_fit_young = fuzz.interp_membership(x_age, age_young, age)
    age_fit_mid = fuzz.interp_membership(x_age, age_mid, age)
    age_fit_old = fuzz.interp_membership(x_age, age_old, age)
    
    bp_fit_low = fuzz.interp_membership(x_bloodPressure, bloodPressure_low, trestbps)
    bp_fit_mid = fuzz.interp_membership(x_bloodPressure, bloodPressure_mid, trestbps)
    bp_fit_high = fuzz.interp_membership(x_bloodPressure, bloodPressure_high, trestbps)
    bp_fit_veryHigh = fuzz.interp_membership(x_bloodPressure, bloodPressure_veryHigh, trestbps)
    
    chol_fit_low = fuzz.interp_membership(x_cholesterol, cholesterol_low, chol)
    chol_fit_mid = fuzz.interp_membership(x_cholesterol, cholesterol_mid, chol)
    chol_fit_high = fuzz.interp_membership(x_cholesterol, cholesterol_high, chol)
    chol_fit_veryHigh = fuzz.interp_membership(x_cholesterol, cholesterol_veryHigh, chol)
    
    fbs_fit_normal = fuzz.interp_membership(x_bloodSugar_fbs, bloodSugar_normal, fbs)
    fbs_fit_high = fuzz.interp_membership(x_bloodSugar_fbs, bloodSugar_high, fbs)
    
    ldl_fit_normal = fuzz.interp_membership(x_ldl, ldl_normal, ldl)
    ldl_fit_limit = fuzz.interp_membership(x_ldl, ldl_limit, ldl)
    ldl_fit_high = fuzz.interp_membership(x_ldl, ldl_high, ldl)
    ldl_fit_veryHigh = fuzz.interp_membership(x_ldl, ldl_veryHigh, ldl)
    
    hdl_fit_low = fuzz.interp_membership(x_hdl, hdl_low, hdl)
    hdl_fit_mid = fuzz.interp_membership(x_hdl, hdl_mid, hdl)
    hdl_fit_high = fuzz.interp_membership(x_hdl, hdl_high, hdl)
    
    # Fuzzy rules
    rule1 = np.fmin(np.fmin(np.fmin(age_fit_young, bp_fit_low), chol_fit_low), risk_low)
    rule2 = np.fmin(np.fmin(np.fmin(age_fit_mid, bp_fit_mid), chol_fit_mid), risk_moderate)
    rule3 = np.fmin(np.fmin(np.fmin(age_fit_old, bp_fit_high), chol_fit_high), risk_high)
    rule4 = np.fmin(np.fmin(np.fmin(age_fit_old, bp_fit_veryHigh), chol_fit_veryHigh), risk_veryHigh)
    
    rule5 = np.fmin(np.fmin(ldl_fit_veryHigh, hdl_fit_low), risk_veryHigh)
    rule6 = np.fmin(np.fmin(ldl_fit_high, hdl_fit_low), risk_high)
    rule7 = np.fmin(np.fmin(ldl_fit_normal, hdl_fit_high), risk_low)
    
    rule8 = np.fmin(fbs_fit_high, risk_high)
    rule9 = np.fmin(fbs_fit_normal, risk_moderate)
    
    # Combine rules
    out_low = np.fmax(rule1, rule7)
    out_moderate = np.fmax(rule2, rule9)
    out_high = np.fmax(np.fmax(rule3, rule6), rule8)
    out_veryHigh = np.fmax(rule4, rule5)
    
    aggregated = np.fmax(np.fmax(out_low, out_moderate), np.fmax(out_high, out_veryHigh))
    
    risk_score = fuzz.defuzz(y_risk, aggregated, 'centroid')
    
    return risk_score, aggregated

# Calculate risk for all patients
print("\nCalculating heart disease risk for all patients...")
risk_scores = []
risk_categories = []

for idx, row in data.iterrows():
    risk_score, _ = calculate_heart_risk(
        age=row['age'],
        trestbps=row['trestbps'],
        chol=row['chol'],
        fbs=row['fbs'],
        ldl=row['ldl'],
        hdl=row['hdl']
    )
    
    risk_scores.append(risk_score)
    
    if risk_score < 30:
        category = "Low"
    elif risk_score < 50:
        category = "Moderate"
    elif risk_score < 70:
        category = "High"
    else:
        category = "Very High"
    
    risk_categories.append(category)

# Add new columns to data
data['risk_score'] = risk_scores
data['risk_category'] = risk_categories

# Display results
print("\n\n" + "="*80)
print("Heart Disease Risk Calculation Results")
print("="*80)

print(f"\nTotal number of patients: {len(data)}")
print("\nRisk distribution:")
print(data['risk_category'].value_counts())

print("\n\nDescriptive statistics of risk scores:")
print(f"Mean: {data['risk_score'].mean():.2f}")
print(f"Standard deviation: {data['risk_score'].std():.2f}")
print(f"Minimum: {data['risk_score'].min():.2f}")
print(f"Maximum: {data['risk_score'].max():.2f}")
print(f"Median: {data['risk_score'].median():.2f}")

print("\n\nTop 10 patients with highest risk:")
print(data.nlargest(10, 'risk_score')[['age', 'trestbps', 'chol', 'fbs', 'ldl', 'hdl', 'risk_score', 'risk_category']])

print("\n\nTop 10 patients with lowest risk:")
print(data.nsmallest(10, 'risk_score')[['age', 'trestbps', 'chol', 'fbs', 'ldl', 'hdl', 'risk_score', 'risk_category']])

# Create and save risk analysis charts
print("\nCreating risk analysis charts...")
fig, axes = plt.subplots(2, 3, figsize=(18, 12))

# 1. Risk scores histogram
axes[0, 0].hist(data['risk_score'], bins=20, color='skyblue', edgecolor='black')
axes[0, 0].set_title('Distribution of Heart Disease Risk Scores')
axes[0, 0].set_xlabel('Risk Score')
axes[0, 0].set_ylabel('Number of Patients')
axes[0, 0].grid(True, alpha=0.3)

# 2. Bar chart of risk categories
category_counts = data['risk_category'].value_counts()
colors = ['green', 'yellow', 'orange', 'red']
axes[0, 1].bar(category_counts.index, category_counts.values, color=colors)
axes[0, 1].set_title('Distribution of Risk Categories')
axes[0, 1].set_xlabel('Risk Category')
axes[0, 1].set_ylabel('Number of Patients')
axes[0, 1].grid(True, alpha=0.3)

# 3. Scatter plot: Age vs Risk
scatter = axes[0, 2].scatter(data['age'], data['risk_score'], 
                             c=data['risk_score'], cmap='RdYlGn_r', alpha=0.6)
axes[0, 2].set_title('Relationship between Age and Risk')
axes[0, 2].set_xlabel('Age')
axes[0, 2].set_ylabel('Risk Score')
plt.colorbar(scatter, ax=axes[0, 2])

# 4. Scatter plot: Blood Pressure vs Risk
scatter = axes[1, 0].scatter(data['trestbps'], data['risk_score'], 
                             c=data['risk_score'], cmap='RdYlGn_r', alpha=0.6)
axes[1, 0].set_title('Relationship between Blood Pressure and Risk')
axes[1, 0].set_xlabel('Blood Pressure (trestbps)')
axes[1, 0].set_ylabel('Risk Score')
plt.colorbar(scatter, ax=axes[1, 0])

# 5. Scatter plot: Cholesterol vs Risk
scatter = axes[1, 1].scatter(data['chol'], data['risk_score'], 
                             c=data['risk_score'], cmap='RdYlGn_r', alpha=0.6)
axes[1, 1].set_title('Relationship between Cholesterol and Risk')
axes[1, 1].set_xlabel('Cholesterol')
axes[1, 1].set_ylabel('Risk Score')
plt.colorbar(scatter, ax=axes[1, 1])

# 6. Box plot: Risk based on fbs
box_data = [data[data['fbs'] == 0]['risk_score'], data[data['fbs'] == 1]['risk_score']]
axes[1, 2].boxplot(box_data, labels=['Normal Blood Sugar', 'High Blood Sugar'])
axes[1, 2].set_title('Risk Distribution Based on Fasting Blood Sugar Level')
axes[1, 2].set_ylabel('Risk Score')
axes[1, 2].grid(True, alpha=0.3)

plt.tight_layout()
# Save the plot BEFORE showing it
plt.savefig('plots/risk_analysis_charts.png', dpi=300, bbox_inches='tight')
print("✓ Risk analysis charts saved as 'plots/risk_analysis_charts.png'")
plt.show()

# Correlation analysis
print("\n\n" + "="*80)
print("Correlation Analysis Between Variables and Risk Score")
print("="*80)

correlation_matrix = data[['age', 'trestbps', 'chol', 'fbs', 'ldl', 'hdl', 'risk_score']].corr()
print("\nCorrelation matrix:")
print(correlation_matrix['risk_score'].sort_values(ascending=False))

# Create and save correlation matrix chart
print("\nCreating correlation matrix plot...")
fig, ax = plt.subplots(figsize=(10, 8))
im = ax.imshow(correlation_matrix, cmap='coolwarm', vmin=-1, vmax=1)

for i in range(len(correlation_matrix.columns)):
    for j in range(len(correlation_matrix.columns)):
        text = ax.text(j, i, f'{correlation_matrix.iloc[i, j]:.2f}',
                       ha="center", va="center", color="black", fontsize=9)

ax.set_xticks(range(len(correlation_matrix.columns)))
ax.set_yticks(range(len(correlation_matrix.columns)))
ax.set_xticklabels(correlation_matrix.columns, rotation=45)
ax.set_yticklabels(correlation_matrix.columns)
ax.set_title('Correlation Matrix Between Variables')
plt.colorbar(im)
plt.tight_layout()
# Save the plot BEFORE showing it
plt.savefig('plots/correlation_matrix.png', dpi=300, bbox_inches='tight')
print("✓ Correlation matrix plot saved as 'plots/correlation_matrix.png'")
plt.show()

# Display results for sample patients
print("\n\n" + "="*80)
print("Sample Calculations for Several Patients")
print("="*80)

sample_patients = data.sample(5)
for idx, row in sample_patients.iterrows():
    print(f"\nPatient #{idx}:")
    print(f"  Age: {row['age']}, Blood Pressure: {row['trestbps']}, Cholesterol: {row['chol']}")
    print(f"  FBS: {row['fbs']}, LDL: {row['ldl']}, HDL: {row['hdl']}")
    print(f"  Risk Score: {row['risk_score']:.2f} - Category: {row['risk_category']}")

# Save results to CSV file
output_filename = 'heart_risk_results.csv'
data.to_csv(output_filename, index=False, encoding='utf-8-sig')
print(f"\n\nResults saved in file '{output_filename}'.")

print("\n\n" + "="*80)
print("Overall Results Analysis:")
print("="*80)

high_risk_count = len(data[data['risk_score'] > 60])
high_risk_percentage = (high_risk_count / len(data)) * 100

print(f"\n• {high_risk_count} patients ({high_risk_percentage:.1f}%) are at high or very high risk.")
print(f"• Average age of high-risk patients: {data[data['risk_score'] > 60]['age'].mean():.1f} years")
print(f"• Average cholesterol of high-risk patients: {data[data['risk_score'] > 60]['chol'].mean():.1f}")
print(f"• Average blood pressure of high-risk patients: {data[data['risk_score'] > 60]['trestbps'].mean():.1f}")

# General recommendations
print("\n\nGeneral Recommendations:")
print("1. Patients with high risk (score > 60) should be referred for cardiac examination.")
print("2. Patients with moderate risk (score 30-60) should be under regular monitoring.")
print("3. Patients with low risk (score < 30) should continue a healthy lifestyle.")

print("\n\n" + "="*80)
print("Summary of Saved Plots:")
print("="*80)
print("1. membership_functions.png - Fuzzy membership functions")
print("2. risk_analysis_charts.png - Risk analysis charts (6 subplots)")
print("3. correlation_matrix.png - Correlation matrix")
print(f"\nAll plots saved in 'plots' directory with high quality (300 DPI)")
