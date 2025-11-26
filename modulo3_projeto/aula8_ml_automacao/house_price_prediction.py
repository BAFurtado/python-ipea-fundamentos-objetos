import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import generating_housing_data


# Prepare features and target
df = generating_housing_data.main()
X = df[['square_meters', 'bedrooms', 'bathrooms', 
        'year_built', 'distance_to_city_center']]
y = df['price']

# Split and scale the data (crucial for neural networks)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Build the model - notice this is regression, so 1 output neuron, no activation
model = tf.keras.Sequential([
        tf.keras.Input(shape=(5,)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(1)  # Single output for price, no activation
])

# For regression, we use different loss and metrics
model.compile(optimizer='adam',
              loss='mse',  # Mean Squared Error
              metrics=['mae'])  # Mean Absolute Error

# Train the model
print("Training house price predictor...")
history = model.fit(X_train_scaled, y_train, 
                    epochs=200, 
                    validation_split=0.2,
                    verbose=0)  # Set to 1 to see progress

# Evaluate
test_loss, test_mae = model.evaluate(X_test_scaled, y_test, verbose=0)
print(f"\nTest Mean Absolute Error: ${test_mae:,.2f}")

# Make a prediction for a new house
new_house = pd.DataFrame(
    [[180, 3, 2, 1995, 8]], 
    columns=['square_meters', 'bedrooms', 'bathrooms', 'year_built', 'distance_to_city_center']
)
new_house_scaled = scaler.transform(new_house)
predicted_price = model.predict(new_house_scaled, verbose=0)

print(f"\nPredicted price for new house: ${predicted_price[0][0]:,.2f}")

# Plot training history
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.ylabel('Loss (MSE)')
plt.xlabel('Epoch')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['mae'], label='Training MAE')
plt.plot(history.history['val_mae'], label='Validation MAE')
plt.title('Model Accuracy')
plt.ylabel('MAE ($)')
plt.xlabel('Epoch')
plt.legend()
plt.tight_layout()
plt.show()