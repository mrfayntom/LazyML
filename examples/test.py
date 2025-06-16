from lazyml.trainer import LazyTrainer

trainer = LazyTrainer(
    data_path= r"C:\Users\Mr. Phantom\Documents\Lazy Ml\house_prices.csv",
    target_col="Price (Lakhs)",
    features=["Area (sq ft)", "Bedrooms", "Location"],
    categorical_cols=["Location"]
)

trainer.train()
trainer.evaluate()
trainer.plot_summary()
trainer.save()
trainer.save_scaler()
trainer.save_encoders()
