import pandas as pd
import numpy as np

def main(samples=1000, random_state=42):
    # Create synthetic housing data (in real life, you'd load from CSV)
    np.random.seed(random_state)
    n_samples = samples

    # Features that actually make sense for house prices
    data = {
        'square_meters': np.random.normal(80, 250, n_samples),
        'bedrooms': np.random.randint(1, 6, n_samples),
        'bathrooms': np.random.randint(1, 4, n_samples),
        'year_built': np.random.randint(1950, 2020, n_samples),
        'distance_to_city_center': np.random.exponential(10, n_samples)  # miles
    }

    # Create realistic price based on features + some noise
    df = pd.DataFrame(data)
    base_price = (
        df['square_meters'] * 150 + 
        df['bedrooms'] * 50000 + 
        df['bathrooms'] * 30000 +
        (df['year_built'] - 1950) * 1000 -
        df['distance_to_city_center'] * 10000
    )
    noise = np.random.normal(0, 50000, n_samples)
    df['price'] = base_price + noise
    return df


if __name__ == '__main__':
    main()
    