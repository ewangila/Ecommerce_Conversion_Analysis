# GreenCart E-commerce Conversion Analysis

Statistical A/B test analysis evaluating whether a new website design significantly improves conversion rates for GreenCart.

## Business Objective
Determine if **Version B** (simplified navigation + larger images) produces a statistically significant increase in conversion rate compared to the current design (**Version A**).

## Dataset Summary
| Design     | Visitors | Conversions | Conversion Rate |
|------------|----------|-------------|-----------------|
| Version A  | 1,000    | 150         | 15.0%           |
| Version B  | 1,200    | 210         | 17.5%           |

Observed absolute difference: **+2.5 percentage points**

## Methods
1. **Point estimate + 95% Confidence Interval** for the current (Version A) conversion rate
2. **Two-proportion Z-test** to assess whether the difference between Version A and Version B is statistically significant
3. Business-friendly interpretation of the statistical results

## Key Results
- Current conversion rate (Version A): **15.0%**  
  95% CI: **(12.8%, 17.2%)**
- Observed lift with Version B: **+2.5 pp**
- Two-proportion Z-test p-value: **0.1145**
- Conclusion: The observed difference is **not statistically significant** at α = 0.05

**Recommendation:** Do not switch to the new design yet. Continue testing to gather more data.

## Project Structure
```
├── greencart.ipynb      # Full analysis notebook (recommended starting point)
├── analysis.py          # Same analysis as a plain Python script
├── requirements.txt
├── .gitignore
└── LICENSE
```
## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/ewangila/Ecommerce_Conversion_Analysis.git
cd Ecommerce_Conversion_Analysis

# 2. Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the analysis
python analysis.py

# or open the notebook
jupyter notebook greencart.ipynb
```
## Requirements

- Python 3.8+
- numpy
- scipy
- jupyter / ipykernel (for the notebook)

## License
This project is licensed under the [MIT License](LICENSE).
