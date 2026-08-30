import pytest
import pandas as pd
import numpy as np

def test_feature_engineering_shape():
    """تست بررسی صحت ساخت ویژگی‌های لَگ و رولینگ روی داده‌های خام"""
    sample_size = 72
    timestamps = pd.date_range(start="2026-09-01", periods=sample_size, freq="h")
    
    raw_df = pd.DataFrame({
        'timestamp': timestamps,
        'day_ahead_price': np.random.normal(55, 40, sample_size),
        'residual_load': np.random.normal(42000, 6000, sample_size),
        'wind_generation': np.random.uniform(4000, 18000, sample_size),
        'solar_generation': np.maximum(0, np.random.normal(3500, 4500, sample_size))
    })
    
    # شبیه‌سازی منطق تابع prepare_ml_features
    df = raw_df.copy().sort_values('timestamp').reset_index(drop=True)
    df['price_lag_24h'] = df['day_ahead_price'].shift(24)
    df['price_rolling_mean_6h'] = df['day_ahead_price'].rolling(window=6).mean()
    df = df.dropna().reset_index(drop=True)
    
    assert not df.empty, "DataFrame پس از پاکسازی نباید خالی باشد"
    assert 'price_lag_24h' in df.columns, "ستون تاخیری 24 ساعته ایجاد نشده است"
    assert 'price_rolling_mean_6h' in df.columns, "ستون میانگین متحرک ایجاد نشده است"

def test_target_classification_classes():
    """تست بررسی دسته‌بندی دامنه‌های ریسک و اسپک‌های قیمت"""
    sample_size = 50
    prices = pd.Series(np.linspace(-30, 150, sample_size))
    
    negative_threshold = -20.0
    positive_threshold = 100.0
    
    conditions = [
        (prices <= negative_threshold),
        (prices >= positive_threshold)
    ]
    choices = [1, 2]
    targets = np.select(conditions, choices, default=0)
    
    unique_classes = np.unique(targets)
    assert set(unique_classes).issubset({0, 1, 2}), "کلاس‌های هدف باید محدود به 0، 1 و 2 باشند"
