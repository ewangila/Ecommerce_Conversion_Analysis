import numpy as np
from scipy import stats

# Set up our data for the current website (Version A)
conversions_a = 150    # Number of users who added items to cart
visitors_a = 1000      # Total visitors to current design

def analyze_conversion_rate(conversions, visitors, confidence_level=0.95):
    """
    Analyze conversion rate with confidence interval.
    """
    # Step 1: Calculate sample proportion
    p_hat = conversions / visitors
    print(f"Current conversion rate: {p_hat:.1%}")

    # Step 2: Verify we can use normal approximation
    successes = visitors * p_hat
    failures = visitors * (1 - p_hat)
    
    print("\nChecking requirements:")
    print(f"Number of conversions: {successes:.1f} (need ≥ 10)")
    print(f"Number of non-conversions: {failures:.1f} (need ≥ 10)")
    
    if successes >= 10 and failures >= 10:
        print("Requirements met for reliable analysis")
    else:
        print("Warning: Need more data for reliable analysis")
        return

    # Step 3: Calculate standard error
    std_error = np.sqrt((p_hat * (1 - p_hat)) / visitors)
    print(f"\nStandard Error: {std_error:.4f}")

    # Step 4: Find critical value and margin of error
    z_critical = stats.norm.ppf((1 + confidence_level) / 2)
    margin_error = z_critical * std_error
    print(f"Margin of Error: {margin_error:.1%}")

    # Step 5: Construct confidence interval
    ci_lower = max(0, p_hat - margin_error) 
    ci_upper = min(1, p_hat + margin_error) 
    
    print(f"\n{confidence_level*100}% Confidence Interval:")
    print(f"({ci_lower:.1%}, {ci_upper:.1%})")
    
    return {
        'point_estimate': p_hat,
        'confidence_interval': (ci_lower, ci_upper),
        'margin_error': margin_error
    }

# Analyze current website performance
current_performance = analyze_conversion_rate(conversions_a, visitors_a)

def compare_designs(conversions_a, visitors_a, conversions_b, visitors_b, alpha=0.05):
    """
    Compare two website designs using hypothesis testing.
    """
    # Step 1: Calculate observed proportions
    p_a = conversions_a / visitors_a
    p_b = conversions_b / visitors_b
    
    print("Observed Conversion Rates:")
    print(f"Current Design: {p_a:.1%}")
    print(f"New Design: {p_b:.1%}")
    print(f"Absolute Difference: {(p_b - p_a):.1%}")
    
    # Step 2: Calculate pooled proportion
    p_pooled = (conversions_a + conversions_b) / (visitors_a + visitors_b)
    
    # Step 3: Calculate standard error for difference in proportions
    se_diff = np.sqrt(p_pooled * (1 - p_pooled) * (1/visitors_a + 1/visitors_b))
    
    # Step 4: Calculate test statistic
    z_stat = (p_b - p_a) / se_diff
    
    # Step 5: Calculate p-value (two-sided test)
    p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
    
    print(f"\nTest Statistics:")
    print(f"Z-statistic: {z_stat:.3f}")
    print(f"P-value: {p_value:.4f}")
    
    # Step 6: Make decision
    print("\nDecision:")
    if p_value < alpha:
        print(f" Statistically significant (p < {alpha})")
        print("The difference between designs is unlikely to be due to chance.")
    else:
        print(f"× Not statistically significant (p > {alpha})")
        print("We don't have enough evidence to conclude the designs are different.")
    
    return {
        'difference': p_b - p_a,
        'p_value': p_value,
        'z_statistic': z_stat
    }

# Compare the two designs
visitors_b = 1200
conversions_b = 210

comparison_results = compare_designs(conversions_a, visitors_a, conversions_b, visitors_b)

def prepare_business_summary(current_perf, comparison):
    """
    Create a business-friendly summary of our analysis.
    """
    print("\nSummary for Sarah:")
    print(f"Current Website Performance:")
    print(f"• Conversion rate is between "
          f"{current_perf['confidence_interval'][0]:.1%} and "
          f"{current_perf['confidence_interval'][1]:.1%} "
          f"(95% confidence)")
    
    if comparison['p_value'] < 0.05:
        print("\nNew Design Impact:")
        print(f"• The new design shows a {abs(comparison['difference']):.1%} "
              f"{'increase' if comparison['difference'] > 0 else 'decrease'} "
              f"in conversion rate")
        print("• This difference is statistically significant")
    else:
        print("\nNew Design Impact:")
        print("• While we observe some differences, we need more data to be "
              "confident they're not due to chance")
    
    print("\nRecommendations:")
    if comparison['p_value'] < 0.05 and comparison['difference'] > 0:
        print("• Consider implementing the new design")
        print("• Continue monitoring to ensure performance remains stable")
    else:
        print("• Continue testing to gather more data")
        print("• Consider analyzing specific user segments where the new "
              "design might be more effective")

# Run the summary (relies on current_performance from Part 1)
prepare_business_summary(current_performance, comparison_results)